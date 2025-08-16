# BMSCE Campus Path Finder

A Python-based GUI application that helps students, staff, and visitors navigate through the BMS College of Engineering campus by finding the shortest path between different locations.

## 🎯 Project Overview

The BMSCE Campus Path Finder is an interactive desktop application built with Python and Tkinter that provides turn-by-turn navigation directions within the BMS College of Engineering campus. The application uses a graph-based algorithm to calculate the optimal route between any two campus locations.

## ✨ Features

- **Interactive GUI**: User-friendly interface with dropdown menus for easy location selection
- **Shortest Path Algorithm**: Uses Dijkstra's algorithm to find the optimal route
- **Turn-by-Turn Directions**: Provides specific navigation instructions (e.g., "Take right", "Go straight")
- **Campus Map Integration**: Background image of the campus for visual reference
- **Real-time Path Display**: Shows detailed path information in a popup window
- **Error Handling**: Validates user inputs and provides helpful error messages
- **Responsive Design**: Adapts to window resizing with dynamic background scaling

## 🏛️ Campus Locations

The application includes navigation for the following campus locations:

- **Entrance** - Main campus entrance
- **Trust Office** - Administrative offices
- **Sports Complex** - Sports and recreation facilities
- **Hostel** - Student accommodation
- **Canteen** - Food and dining area
- **Boys Hostel** - Male student accommodation
- **Bank** - Banking facilities
- **B S Narayan Platinum Jubilee Block** - Main academic building
- **PG Block** - Postgraduate studies building
- **LAW Canteen** - Law school dining area
- **Mechanical Block** - Mechanical engineering department
- **Science Block** - Science and research facilities
- **Administrative Block** - Administrative offices
- **BMS College Architecture** - Architecture department
- **BMS College of LAW** - Law school

## 🛠️ Installation

### Prerequisites

- Python 3.6 or higher
- Tkinter (usually comes with Python)
- PIL (Pillow) library

### Setup Instructions

1. **Clone or download the project files**
   ```bash
   git clone <repository-url>
   cd BMSCE_path_finder
   ```

2. **Install required dependencies**
   ```bash
   pip install Pillow
   ```

3. **Add campus map image**
   - Place your campus map image file (e.g., `4df980e3-d950-4c1f-b402-f4fadc9bba6f.jpg`) in the project directory
   - Update the image path in the code if needed

## 🚀 Usage

1. **Run the application**
   ```bash
   python "final aalAAT (3).ipynb"
   ```
   *Note: You may need to convert the Jupyter notebook to a Python script first*

2. **Using the interface**
   - Select your starting point from the dropdown menu
   - Select your destination point from the dropdown menu
   - Click "Find Path" to get navigation directions
   - Use "Clear" to reset the form

3. **Understanding the output**
   - The application will show a popup with the complete path
   - Each step includes the current location and the direction to take
   - The final destination is shown at the end

## 🔧 Technical Details

### Architecture

- **Frontend**: Tkinter GUI framework
- **Backend**: Python with custom graph algorithms
- **Algorithm**: Dijkstra's shortest path algorithm using heapq
- **Data Structure**: Adjacency list representation of campus graph

### Key Components

- `campus_graph`: Dictionary containing campus locations and their connections
- `find_shortest_path()`: Core algorithm function for pathfinding
- `display_path_and_directions()`: Formats path output with directions
- `show_output_popup()`: Creates result display window
- `update_background_image()`: Handles responsive background scaling

### File Structure

```
BMSCE_path_finder/
├── README.md
├── final aalAAT (3).ipynb
└── 4df980e3-d950-4c1f-b402-f4fadc9bba6f.jpg (campus map)
```

## 🎨 Customization

### Adding New Locations

To add new campus locations, update the `campus_graph` dictionary:

```python
campus_graph["New Location"] = [
    ("Connected Location 1", "Direction instruction"),
    ("Connected Location 2", "Direction instruction")
]
```

### Modifying the Interface

- Change colors by modifying the `bg` and `fg` parameters
- Adjust fonts by changing the `font` parameters
- Modify window size and layout in the main GUI setup

## 🐛 Troubleshooting

### Common Issues

1. **Image not found**: Ensure the campus map image file is in the correct location
2. **Tkinter not available**: Install Python with Tkinter support
3. **PIL import error**: Install Pillow library using `pip install Pillow`

### Error Messages

- "Please select both start and end points" - Select both dropdown options
- "Invalid start or end point" - Choose locations from the provided list
- "No path found" - The selected locations may not be connected

## 🤝 Contributing

Contributions are welcome! Here are some ways to contribute:

- Add new campus locations and connections
- Improve the user interface design
- Add new features like path visualization
- Optimize the pathfinding algorithm
- Add support for different campus maps

## 📝 License

This project is created for educational purposes at BMS College of Engineering.

## 👥 Authors

- Developed for BMSCE campus navigation
- Created as part of academic project work

## 📞 Support

For questions or issues related to this project, please contact the development team or refer to the BMSCE IT department.

---

**Note**: This application is designed specifically for the BMS College of Engineering campus layout. For use at other institutions, the campus graph and map image would need to be updated accordingly.
