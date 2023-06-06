import nltk
import time
import random

greeting_responses = ['Hello! How can I assist you today?', 'Hi there! How can I assist you today?',
                     'Hey! How can I help you today?', 'Greetings! How can I assist you today?']
course_enquiry_responses = ['The course covers a range of topics related to focus and productivity, including Secret Sutras, Focus by Arjuna Way and Frequency track which will make this happen effectively.']
course_fee_responses = ["The course fee is only Rs.999 and it offers a cost-effective solution for improving concentration and productivity."]
included_course_responses = ["The course includes 11 main modules, which cover topics such as understanding the science of attention, improving focus through mindfulness, and developing better concentration through exercise."]
course_duration_responses = ["The Focus course is designed to be self-paced, so learners can take as much time as they need to complete the material. On average, it takes around 4-5 hours to complete the course."]
course_support_responses = ["Yes, the Focus course includes access to a private online community where you can ask questions and connect with other learners. In addition, the course instructor is available to provide support and answer questions via email."]
refund_policy_responses = ["Because somewhere around 80% is offered as a discount, we can’t issue refunds. It’s a valuable course."]
goodbye_responses = ['Goodbye!', 'Have a nice day!', 'Bye!', 'See you later!']
default_responses = ["I'm sorry, I didn't understand your question.",
                    'Can you please provide more information?',
                    "I'm not sure I can help you with that."]


def get_bot_response(user_message):
    tokens = nltk.word_tokenize(user_message)
    pos_tags = nltk.pos_tag(tokens)

    if any(tag[0].lower() in ['hello', 'hi', 'hey', 'greetings'] for tag in pos_tags):
        return random.choice(greeting_responses)
    elif any(tag[0].lower() == 'course' and 'topics' or 'about' in user_message.lower() for tag in pos_tags):
        return random.choice(course_enquiry_responses)
    elif any(tag[0].lower() in ['fee', 'fees', 'cost', 'price'] for tag in pos_tags):
        return random.choice(course_fee_responses)
    elif 'included' in user_message.lower() and 'course' in user_message.lower():
        return random.choice(included_course_responses)
    elif any(tag[0].lower() in ['how', 'long'] and 'course' in user_message.lower() and 'take' in user_message.lower() for tag in pos_tags):
        return random.choice(course_duration_responses)
    elif any(tag[0].lower() in ['ask', 'questions', 'support', 'while', 'taking'] for tag in pos_tags):
        return random.choice(course_support_responses)
    elif any(tag[0].lower() in ['refund', 'refunds', 'satisfied'] for tag in pos_tags):
        return random.choice(refund_policy_responses)
    elif any(tag[0].lower() in ['goodbye', 'bye', 'see', 'later'] for tag in pos_tags):
        return random.choice(goodbye_responses)
    else:
        return random.choice(default_responses)
