from flask import Blueprint, render_template, request, jsonify, current_app
from flask_mail import Mail, Message
import json
from datetime import datetime

# Initialize Mail
mail = Mail()

# Define the blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    """Renders the high-performance PEKIMdev Home Page."""
    return render_template('home.html', title="Uncompromising Quality")

@main.route('/about')
def about():
    """Renders the Engineering Mindset / About Page."""
    return render_template('about.html', title="The Mindset Behind the Code")

@main.route('/services')
def services():
    return render_template('services.html', title="Precision Engineering | Services")

@main.route('/projects')
def project_archive():
    return render_template('projects.html', title="Showcasing Excellence | Project Archive")

@main.route('/contact')
def contact():
    return render_template('contact.html', title="Connect with PEKIMdev | Contact Us")

# Form Handlers
@main.route('/submit-services-quote', methods=['POST'])
def submit_services_quote():
    """Handle the services page quote form submission."""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'service', 'description']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'success': False, 'message': f'{field.capitalize()} is required'}), 400
        
        # Basic email validation
        if '@' not in data.get('email', ''):
            return jsonify({'success': False, 'message': 'Please provide a valid email address'}), 400
        
        # Store form data
        quote_data = {
            'timestamp': datetime.now().isoformat(),
            'name': data.get('name'),
            'email': data.get('email'),
            'phone': data.get('phone', ''),
            'company': data.get('company', ''),
            'service': data.get('service'),
            'budget': data.get('budget', ''),
            'description': data.get('description'),
            'source': 'services'
        }
        
        # Log to console
        print(f"Services Quote Submission: {json.dumps(quote_data, indent=2)}")
        
        # Send email notification to admin
        try:
            send_quote_email(quote_data)
        except Exception as e:
            print(f"Email sending failed: {str(e)}")
            # Don't fail the request if email fails
        
        return jsonify({
            'success': True,
            'message': 'Quote request submitted successfully! We\'ll get back to you within 24 hours.'
        }), 200
    
    except Exception as e:
        print(f"Error in services quote submission: {str(e)}")
        return jsonify({'success': False, 'message': 'An error occurred. Please try again.'}), 500

@main.route('/submit-contact', methods=['POST'])
def submit_contact():
    """Handle the contact page form submission."""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'service', 'description']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'success': False, 'message': f'{field.capitalize()} is required'}), 400
        
        # Basic email validation
        if '@' not in data.get('email', ''):
            return jsonify({'success': False, 'message': 'Please provide a valid email address'}), 400
        
        # Store form data
        contact_data = {
            'timestamp': datetime.now().isoformat(),
            'name': data.get('name'),
            'email': data.get('email'),
            'phone': data.get('phone', ''),
            'company': data.get('company', ''),
            'service': data.get('service'),
            'budget': data.get('budget', ''),
            'description': data.get('description'),
            'source': 'contact'
        }
        
        # Log to console
        print(f"Contact Submission: {json.dumps(contact_data, indent=2)}")
        
        # Send email notification to admin
        try:
            send_contact_email(contact_data)
        except Exception as e:
            print(f"Email sending failed: {str(e)}")
            # Don't fail the request if email fails
        
        return jsonify({
            'success': True,
            'message': 'Thank you for reaching out! We\'ll contact you within 1-6 business hours.'
        }), 200
    
    except Exception as e:
        print(f"Error in contact submission: {str(e)}")
        return jsonify({'success': False, 'message': 'An error occurred. Please try again.'}), 500

def send_quote_email(quote_data):
    """Send quote request email to admin."""
    recipient = current_app.config.get('RECIPIENT_EMAIL')
    if not recipient:
        print("No recipient email configured")
        return
    
    subject = f"New Quote Request from {quote_data['name']}"
    
    body = f"""
New Quote Request Received:

Name: {quote_data['name']}
Email: {quote_data['email']}
Phone: {quote_data['phone']}
Company: {quote_data['company']}
Service: {quote_data['service']}
Budget: {quote_data['budget']}

Description:
{quote_data['description']}

Submitted at: {quote_data['timestamp']}
Source: Services Page
---
Please respond to: {quote_data['email']}
    """
    
    msg = Message(subject=subject, recipients=[recipient], body=body)
    mail.send(msg)
    print(f"Email sent to {recipient}")

def send_contact_email(contact_data):
    """Send contact form email to admin."""
    recipient = current_app.config.get('RECIPIENT_EMAIL')
    if not recipient:
        print("No recipient email configured")
        return
    
    subject = f"New Contact Form Submission from {contact_data['name']}"
    
    body = f"""
New Contact Form Submission:

Name: {contact_data['name']}
Email: {contact_data['email']}
Phone: {contact_data['phone']}
Company: {contact_data['company']}
Service: {contact_data['service']}
Budget: {contact_data['budget']}

Message:
{contact_data['description']}

Submitted at: {contact_data['timestamp']}
Source: Contact Page
---
Please respond to: {contact_data['email']}
    """
    
    msg = Message(subject=subject, recipients=[recipient], body=body)
    mail.send(msg)
    print(f"Email sent to {recipient}")