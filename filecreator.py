import os

def create_project_structure():
    # Define the root project directory
    project_root = 'photographer_finder_app'

    # Define the file structure
    structure = {
        'backend': {
            'app.py': '',
            'models': {
                'user.py': '',
                'booking.py': '',
                'review.py': '',
            },
            'routes': {
                'auth.py': '',
                'bookings.py': '',
                'photographers.py': '',
                'clients.py': '',
            },
            'services': {
                'payment.py': '',
                'geolocation.py': '',
            },
            'utils': {
                'validators.py': '',
            }
        },
        'frontend': {
            'public': {},
            'src': {
                'components': {
                    'Navbar.js': '',
                    'SearchBar.js': '',
                },
                'pages': {
                    'Home.js': '',
                    'Profile.js': '',
                    'Booking.js': '',
                },
                'utils': {
                    'api.js': '',
                }
            }
        },
        'config': {
            'settings.py': '',
        },
        'database': {
            'migrations': {},
            'seed_data.py': '',
        },
        'tests': {
            'test_auth.py': '',
            'test_booking.py': '',
        },
        'requirements.txt': '',
        'package.json': '',
        'README.md': '',
    }

    def create_files(base_path, structure):
        for name, value in structure.items():
            # Create directories
            if isinstance(value, dict):
                new_dir = os.path.join(base_path, name)
                os.makedirs(new_dir, exist_ok=True)
                create_files(new_dir, value)
            # Create files with empty content
            else:
                file_path = os.path.join(base_path, name)
                with open(file_path, 'w') as f:
                    f.write(value)

    # Create the root project directory
    os.makedirs(project_root, exist_ok=True)

    # Create the file structure inside the project directory
    create_files(project_root, structure)

    print(f"Project structure for '{project_root}' has been created successfully!")

if __name__ == '__main__':
    create_project_structure()
