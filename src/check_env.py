# Script para crear/verificar el archivo .env
def create_or_verify_env():
    """Create or verify .env file"""
    import os
    from pathlib import Path
    
    env_path = Path('.env')
    
    if env_path.exists():
        print(f"📁 .env file exists at: {env_path.absolute()}")
        with open(env_path, 'r') as f:
            content = f.read()
            print("Current content:")
            print(content)
            
        # Check if HF_TOKEN is present
        if 'HF_TOKEN=' in content:
            print("✅ HF_TOKEN found in .env")
            # Extract the token to verify format
            for line in content.split('\n'):
                if line.startswith('HF_TOKEN='):
                    token_value = line.split('=', 1)[1].strip()
                    if token_value.startswith('hf_') and len(token_value) > 10:
                        print("✅ Token format looks correct")
                    else:
                        print("⚠️  Token format might be incorrect")
                    break
        else:
            print("❌ HF_TOKEN not found in .env")
            
    else:
        print("❌ .env file does not exist")
        print("Creating template .env file...")
        template = """# Hugging Face Token
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Get your token from: https://huggingface.co/settings/tokens
# Replace the x's with your actual token
"""
        with open(env_path, 'w') as f:
            f.write(template)
        print("✅ Created .env template")
        print("💡 Please edit .env and replace with your actual token")

# Run the verification
create_or_verify_env()