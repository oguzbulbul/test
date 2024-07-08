from rplidar import RPLidar

# Set up the RPLidar
PORT_NAME = '/dev/ttyUSB0'  # Update this if your device is connected to a different port
BAUD_RATE = 115200
lidar = RPLidar(PORT_NAME, baudrate=BAUD_RATE)

# Function to print lidar scans
def print_scan():
    print("WELCOME TO LIDAR SCANNER")
    try:
        print('Recording measurements... Press Ctrl+C to stop.')
        for scan in lidar.iter_scans():
            for (_, angle, distance) in scan:
                print('Angle: {:.2f}, Distance: {:.2f}'.format(angle, distance))
    except KeyboardInterrupt:
        print('Stopping.')
    lidar.stop()
    lidar.disconnect()

if __name__ == '__main__':
    print_scan()
