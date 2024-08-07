# SouthWest Store

Welcome to the SouthWest Store, an e-commerce platform built with Django.

## Features
- **Product Catalog**: Browse extensive product descriptions, prices, and images.
- **Shopping Cart**: Add, adjust, or remove items with ease.
- **Checkout Process**: Streamlined checkout supporting multiple payment methods.
- **Responsive Design**: Fully responsive for all devices.

## Getting Started
### Prerequisites
- Python 3.8+
- pip

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/afrocoder16/southwest-store.git
    ```

2. Navigate to the project directory:
    ```sh
    cd southwest-store
    ```

3. you can create a virtual environment:
    ```sh
    python -m venv venv(name of your virtual environment)
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

6. Start the development server:
    ```sh
    python manage.py runserver
    ```

7. Open your browser and navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see the application in action.

## Usage
- **Browse Products**: Visit the home page to see the product catalog.
- **Manage Cart**: Add, remove, or adjust items in your cart.
- **User Accounts**: Register for an account for a personalized experience.

## Contributing
for contributions 

1. Fork the repository.
2. Create a feature branch:
    ```sh
    git checkout -b feature/YourFeatureName
    ```
3. Commit your changes:
    ```sh
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```sh
    git push origin feature/YourFeatureName
    ```
5. Open a Pull Request.

## Development Workflow
1. **Branching**: Use feature branches for all new features or fixes.
2. **Commits**: Write clear, concise commit messages.
3. **Pull Requests**: Ensure PRs are reviewed by at least one other team member.

## Code Style
- Follow PEP 8 guidelines for Python code.
- Use descriptive variable and function names.
- Keep functions and methods short and focused on a single task.

## Testing
1. Write unit tests for new features and bug fixes.
2. Run tests before pushing code:
    ```sh
    python manage.py test
    ```

## Environment Variables
Create a `.env` file in the root directory and add the necessary environment variables.
