# Cartify Backend

Follow these steps to set it up on Windows.

---

## Prerequisites
- Python 3.x installed (`py --version`)
- Git installed (`git --version`)
- (Optional) VS Code or any editor you like

---

## Setup Steps

```powershell
# 1. Clone the repository
git clone https://github.com/LemarkSumalpong/cartify-backend.git
cd cartifybackend

# 2. Create & activate a virtual environment
py -3 -m venv venv
.\venv\Scripts\Activate.ps1

# If PowerShell blocks scripts, run this one-time fix:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py migrate

# 5. Create a superuser
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver

http://127.0.0.1:8000/
Admin panel → http://127.0.0.1:8000/admin/
