import os
from django.shortcuts import render

def firebase_config_script(request):
    """
    這個 view 會讀取環境變數中的 Firebase 設定，
    並將它們作為一個 JavaScript 檔案回傳。
    """
    firebase_config = {
        'apiKey': os.environ.get('FIREBASE_API_KEY'),
        'authDomain': os.environ.get('FIREBASE_AUTH_DOMAIN'),
        'databaseURL': os.environ.get('FIREBASE_DATABASE_URL'),
        'projectId': os.environ.get('FIREBASE_PROJECT_ID'),
        'storageBucket': os.environ.get('FIREBASE_STORAGE_BUCKET'),
        'messagingSenderId': os.environ.get('FIREBASE_MESSAGING_SENDER_ID'),
        'appId': os.environ.get('FIREBASE_APP_ID'),
    }
    
    return render(
        request,
        'webpush/firebase_config.js',
        {'firebase_config': firebase_config},
        content_type='application/javascript'
    )
