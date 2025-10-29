from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

# Load PEGASUS model - better for abstractive summarization
print("Loading model...")
summarizer = pipeline("summarization", model="google/pegasus-xsum")
print("Model loaded successfully!")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        # Count words
        word_count = len(text.split())
        
        # Check minimum length
        if word_count < 50:
            return jsonify({
                'error': f'Text too short! Please provide at least 50 words. You entered {word_count} words.'
            }), 400
        
        # Limit text length to prevent memory issues
        if word_count > 500:
            text = ' '.join(text.split()[:500])
            word_count = 500
        
        # PEGASUS parameters - optimized for quality
        max_length = 64   # PEGASUS produces concise summaries
        min_length = 32
        
        # Generate summary
        summary = summarizer(
            text, 
            max_length=max_length, 
            min_length=min_length,
            do_sample=False,
            num_beams=8,                    # Higher beams = better quality
            length_penalty=0.8,             # Encourages concise summaries
            early_stopping=True
        )
        
        summary_text = summary[0]['summary_text'].strip()
        
        return jsonify({
            'summary': summary_text,
            'original_length': word_count,
            'summary_length': len(summary_text.split())
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
