# GrowingWell AI – Child Daily Routine Tracker

## Project Overview
GrowingWell AI is a web application designed to help parents track their child's daily routine, including food intake, sleep, outdoor activity, study time, and screen time. It generates AI-powered daily summaries to help parents understand their child's routine and identify areas that may need attention.

## Technologies Used
- **Frontend:** Angular
- **Backend:** Python, Django REST Framework
- **Database:** MySQL
- **AI Integration:** Google Gemini AI

## Key Features
- **Daily Routine Tracking:** Record and manage daily activities.
- **Food and Nutrition Tracking:** Record food intake and protein-rich foods.
- **Sleep Tracking:** Maintain daily sleep records.
- **Activity Tracking:** Track outdoor activity, study time, and screen time.
- **AI-Powered Summary:** Generate a concise daily summary using Google Gemini AI.
- **Data Management:** Create, view, update, and delete daily records.
- **Error Handling:** Retry AI requests when temporary failures occur and provide a fallback message if the service is unavailable.

## How It Works
1. Parents enter their child's daily routine details through the Angular interface.
2. The Django REST Framework backend processes the information.
3. MySQL stores the daily records.
4. Google Gemini AI generates a summary based on the recorded information.
5. The application displays the saved records and AI-generated summary.

## Installation and Setup

### Prerequisites
- Python
- Node.js and npm
- Angular CLI
- MySQL
- Google Gemini API key

### Backend Setup
1. Navigate to the Django backend directory.
2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure the MySQL database and Django database settings.
4. Create a `.env` file and add your Gemini API key:

   ```env
   GEMINI_API_KEY=your_gemini_api_key
   ```

5. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

6. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. Navigate to the Angular frontend directory.
2. Install dependencies:

   ```bash
   npm install
   ```

3. Start the Angular development server:

   ```bash
   ng serve
   ```

4. Open the local URL displayed in your terminal, usually `http://localhost:4200`.

**Note:** Configure the frontend API URL and backend database settings according to your local environment before running the application.

## AI Safety Disclaimer
AI-generated suggestions may not always be accurate. This application provides general guidance only and does not replace professional medical advice. Always follow your doctor's advice and prescription.

## Project Status
Developed as a personal project to practise full-stack web development, database integration, and generative AI integration.

## Technologies and Learning Outcomes
This project demonstrates practical experience with Angular, Django REST Framework, MySQL, REST APIs, environment-based API key management, and Google Gemini AI integration.
