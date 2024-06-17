# System Monitor

This project is a basic and functional script that can track disk, cpu and memory usage of the system. It uses tkinter for a basic interface and shows the values with colors and changes in real time. It can also send alerts when values exceeds a certain threshold.

## Modules Used

- **tkinter**: For the graphical user interface.
- **threading**: To handle real-time updates.
- **psutil**: To obtain usages values from cpu, hard disk and memory.
- **time**: To sleep the program in the loop.
- **plyer**: To generate alerts. 
- **queue**: To use queue object.

## Installation

To run this project, you need to have Python installed. Follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/LeonardoEnriqueVila/SystemMonitor
    ```
2. Navigate to the project directory:
    ```bash
    cd SystemMonitor
    ```
3. Install the required modules:

## Usage

To start the monitor, run the following command:
```bash
python main.py
