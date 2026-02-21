import os
import random

def handler(request):
    uid = request.args.get("uid")

    if not uid:
        return {
            "statusCode": 400,
            "body": '{"error": "UID required"}',
            "headers": {"Content-Type": "application/json"}
        }

    avatar_folder = os.path.join(os.getcwd(), "avatars")

    try:
        files = os.listdir(avatar_folder)
        images = [f for f in files if f.lower().endswith(".png")]

        if not images:
            return {
                "statusCode": 500,
                "body": '{"error": "No avatars found"}',
                "headers": {"Content-Type": "application/json"}
            }

        image = random.choice(images)
        file_path = os.path.join(avatar_folder, image)

        with open(file_path, "rb") as f:
            image_data = f.read()

        return {
            "statusCode": 200,
            "body": image_data,
            "headers": {
                "Content-Type": "image/png"
            },
            "isBase64Encoded": False
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": f'{{"error": "{str(e)}"}}',
            "headers": {"Content-Type": "application/json"}
        }