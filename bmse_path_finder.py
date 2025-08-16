#!/usr/bin/env python3
"""
BMSCE Campus Path Finder
A Python GUI application for navigating the BMS College of Engineering campus.

Author: BMSCE Development Team
Date: 2024
"""

import tkinter as tk
from tkinter import messagebox, StringVar
from PIL import Image, ImageTk
import heapq

# Campus graph representing locations and their connections with directions
campus_graph = {
    "Entrance": [("Trust Office", "Take right"), ("Sports complex", "Take left"), ("B S Narayan Platinum Jubilee Block", "Go straight")],
    "Trust Office": [("Entrance", "Take left"), ("Administrative Block", "Go straight"), ("Sports complex", "Take right")],
    "Sports complex": [("Entrance", "Take left"), ("Hostel", "Go straight & Take Left"), ("Trust Office", "Take left")],
    "Hostel": [("Sports complex", "Go straight"), ("Canteen", "Go straight"), ("Entrance", "Take right")],
    "Canteen": [("Hostel", "Go straight"), ("Boys Hostel", "Take left"), ("Sports complex", "Take right")],
    "Boys Hostel": [("Canteen", "Take right"), ("Bank", "Take left"), ("Hostel", "Take right")],
    "Bank": [("Boys Hostel", "Take right"), ("Canteen", "Take left")],
    "B S Narayan Platinum Jubilee Block": [("Entrance", "Go straight"), ("PG Block", "Take right"), ("Science Block", "Go straight"), ("Mechanical Block", "Take left")],
    "PG Block": [("B S Narayan Platinum Jubilee Block", "Take left"), ("LAW", "Take right"), ("Entrance", "Take right")],
    "LAW Canteen": [("PG Block", "Take left"), ("Mechanical Block", "Go straight"), ("Canteen", "Take left"), ("BMS College Architecture", "Take right")],
    "Mechanical Block": [("B S Narayan Platinum Jubilee Block", "Take left"), ("LAW Canteen", "Go straight"), ("Science Block", "Take right")],
    "Science Block": [("B S Narayan Platinum Jubilee Block", "Go straight"), ("Mechanical Block", "Take left"), ("PG Block", "Take right")],
    "Administrative Block": [("Trust Office", "Go straight"), ("Entrance", "Take left")],
    "BMS College Architecture": [("LAW Canteen", "Take left"), ("BMS College of LAW", "Take right"), ("PG Block", "Take left")],
    "BMS College of LAW": [("BMS College Architecture", "Take left"), ("LAW Canteen", "Take right")]
}

def find_shortest_path(graph, start, end):
    """
    Find the shortest path between two locations using Dijkstra's algorithm.
    
    Args:
        graph (dict): The campus graph with locations and connections
        start (str): Starting location
        end (str): Destination location
    
    Returns:
        list: List of locations forming the shortest path, or None if no path exists
    """
    queue = [(0, start, [])]
    visited = set()
    
    while queue:
        (cost, current, path) = heapq.heappop(queue)
        
        if current in visited:
            continue
            
        path = path + [current]
        
        if current == end:
            return path
            
        visited.add(current)
        
        for (next_node, direction) in graph.get(current, []):
            heapq.heappush(queue, (cost + 1, next_node, path))
    
    return None

def display_path_and_directions(path, directions):
    """
    Format the path and directions for display.
    
    Args:
        path (list): List of locations in the path
        directions (list): List of direction instructions
    
    Returns:
        str: Formatted string with path and directions
    """
    steps = []
    for i in range(len(path) - 1):
        steps.append(f"{path[i]} -> {directions[i]} -> {path[i + 1]}")
    steps.append(path[-1])
    return "\n".join(steps)

def update_background_image(event=None):
    """
    Update the background image when the window is resized.
    """
    new_width = root.winfo_width()
    new_height = root.winfo_height() - 150
    
    if new_width > 0 and new_height > 0:
        resized_image = background_image.resize((new_width, new_height), Image.LANCZOS)
        global background_photo
        background_photo = ImageTk.PhotoImage(resized_image)
        canvas.delete("all")
        canvas.create_image(0, 0, anchor="nw", image=background_photo)
        canvas.image = background_photo

def show_output_popup(path, directions):
    """
    Display the path results in a popup window.
    
    Args:
        path (list): List of locations in the path
        directions (list): List of direction instructions
    """
    # Create a new window
    popup = tk.Toplevel(root)
    popup.title("Path Details")
    popup.geometry("400x300")
    
    # Display the path and directions in the popup
    output_text = display_path_and_directions(path, directions)
    output_label = tk.Label(popup, text="Path found:\n" + output_text, 
                           font=('Arial', 12), padx=10, pady=10)
    output_label.pack(expand=True, fill='both')
    
    # Add a button to close the popup
    close_button = tk.Button(popup, text="Close", command=popup.destroy, 
                            bg='#f44336', fg='white', font=('Arial', 10, 'bold'))
    close_button.pack(pady=10)

def find_path_gui():
    """
    Main function to handle path finding from the GUI.
    """
    start = start_var.get().strip()
    end = end_var.get().strip()
    
    if not start or not end:
        messagebox.showerror("Error", "Please select both start and end points.")
        return
        
    if start not in campus_graph or end not in campus_graph:
        messagebox.showerror("Error", "Invalid start or end point. Please check the input and try again.")
        return
        
    path = find_shortest_path(campus_graph, start, end)
    
    if path:
        directions = []
        for i in range(len(path) - 1):
            for (next_node, direction) in campus_graph[path[i]]:
                if next_node == path[i + 1]:
                    directions.append(direction)
                    break
        show_output_popup(path, directions)
    else:
        result_label.config(text="No path found. The start and end points might not be connected.")

def clear_fields():
    """
    Clear all input fields and results.
    """
    start_var.set('')
    end_var.set('')
    result_label.config(text="")

def main():
    """
    Main function to initialize and run the GUI application.
    """
    global root, canvas, background_image, background_photo, start_var, end_var, result_label
    
    # Initialize the main window
    root = tk.Tk()
    root.title("BMSCE Campus Path Finder")
    
    # Load background image
    try:
        background_image = Image.open("4df980e3-d950-4c1f-b402-f4fadc9bba6f.jpg")
    except FileNotFoundError:
        print("Warning: Campus map image not found. Please ensure the image file is in the same directory.")
        background_image = None
    
    # Create canvas for background
    canvas = tk.Canvas(root)
    canvas.pack(fill="both", expand=True)
    
    # Bind resize event
    root.bind("<Configure>", update_background_image)
    
    # Create heading frame
    heading_frame = tk.Frame(root, bg='#f0f0f0', padx=10, pady=20, borderwidth=2, relief='solid')
    heading_frame.pack(side='top', fill='x')
    
    heading_label = tk.Label(
        heading_frame,
        text="B. M. S. COLLEGE OF ENGINEERING (Autonomous Institute, Affiliated to VTU, Belagavi)\nPost Box No.: 1908, Bull Temple Road, Bengaluru – 560 019\n\nCampus Path Finder",
        font=('Arial', 18, 'bold'),
        bg='#f0f0f0',
        fg='#003366',
        justify='center'
    )
    heading_label.pack()
    
    # Create main control frame
    frame = tk.Frame(root, bg='#e0e0e0', padx=10, pady=10, borderwidth=2, relief='raised')
    frame.place(relx=0.6, rely=0.4, anchor='center')
    frame.config(width=250, height=300)
    
    # Initialize variables
    start_var = StringVar()
    end_var = StringVar()
    
    # Create GUI elements
    tk.Label(frame, text="Select the starting point:", 
             bg='#e0e0e0', font=('Arial', 12, 'bold')).grid(row=0, column=0, padx=5, pady=5, sticky='e')
    
    start_menu = tk.OptionMenu(frame, start_var, *campus_graph.keys())
    start_menu.grid(row=0, column=1, padx=5, pady=5)
    start_menu.config(font=('Arial', 10), width=25)
    
    tk.Label(frame, text="Select the destination point:", 
             bg='#e0e0e0', font=('Arial', 12, 'bold')).grid(row=1, column=0, padx=5, pady=5, sticky='e')
    
    end_menu = tk.OptionMenu(frame, end_var, *campus_graph.keys())
    end_menu.grid(row=1, column=1, padx=5, pady=5)
    end_menu.config(font=('Arial', 10), width=25)
    
    # Create buttons
    find_button = tk.Button(frame, text="Find Path", command=find_path_gui, 
                           bg='#4CAF50', fg='white', font=('Arial', 10, 'bold'), 
                           relief='raised', padx=5, pady=3)
    find_button.grid(row=2, column=0, pady=5, columnspan=2)
    
    clear_button = tk.Button(frame, text="Clear", command=clear_fields, 
                            bg='#f44336', fg='white', font=('Arial', 10, 'bold'), 
                            relief='raised', padx=5, pady=3)
    clear_button.grid(row=3, column=0, pady=5, columnspan=2)
    
    # Create result label
    result_label = tk.Label(frame, text="", bg='#e0e0e0', 
                           font=('Arial', 10, 'italic'), wraplength=200)
    result_label.grid(row=4, column=0, columnspan=2, pady=5)
    
    # Initialize background image
    if background_image:
        update_background_image()
    
    # Start the main event loop
    root.mainloop()

if __name__ == "__main__":
    main()
