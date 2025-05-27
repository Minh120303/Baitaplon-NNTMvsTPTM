import google.generativeai as genai
import os
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import markdown

class GeminiService:
    def __init__(self):
        self.api_key = ""
        genai.configure(api_key=self.api_key)
        
        generation_config = {
            "temperature": 0.5,
            "top_p": 0.8,
            "top_k": 40,
            "max_output_tokens": 1024,
        }

        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_NONE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_NONE"
            },
        ]

        self.model = genai.GenerativeModel(
            model_name="gemini-2.0-flash",
            generation_config=generation_config,
        )
        
        self.system_prompt = """
        Bạn là một chuyên gia bệnh học thực vật. Hãy đưa ra lời khuyên điều trị cho:
        Cây: {plant_name}
        Tình trạng: {disease}
        

        Yêu cầu trả về HTML với cấu trúc sau:

        <div class="treatment-content">
          <h2>Điều trị</h2>
          <ul>
            <li>Điểm 1 ngắn gọn</li>
            <li>Điểm 2 ngắn gọn</li>
            <li>Điểm 3 ngắn gọn</li>
          </ul>
          
          <h2>Phòng ngừa</h2>
          <ul>
            <li>Điểm 1 ngắn gọn</li>
            <li>Điểm 2 ngắn gọn</li>
            <li>Điểm 3 ngắn gọn</li>
          </ul>
        </div>

        Yêu cầu nội dung:
        - Mỗi điểm chỉ 1 câu ngắn gọn
        - Không thêm dấu chấm cuối câu
        - Không dùng "..." hoặc các ký tự đặc biệt
        - Nếu là thuốc, ghi rõ tên thuốc trong ngoặc đơn
        """

    def get_treatment_recommendation(self, plant_name, disease):
        try:
            prompt = self.system_prompt.format(
                plant_name=plant_name,
                disease=disease
            )

            response = self.model.generate_content(
                prompt,
                stream=False
            )
            
            if response and response.text:
                treatment_html = response.text.strip()
                if treatment_html.startswith('```html'):
                    treatment_html = treatment_html[7:]
                if treatment_html.endswith('```'):
                    treatment_html = treatment_html[:-3]
                treatment_html = treatment_html.strip()
                
                if not treatment_html.startswith('<div class="treatment-content">'):
                    treatment_html = f'<div class="treatment-content">{treatment_html}</div>'
                
                return {
                    'success': True,
                    'treatment': treatment_html
                }
            else:
                return {
                    'success': False,
                    'error': 'Không thể tạo khuyến nghị điều trị'
                }
                
        except Exception as e:
            print(f"Error getting treatment recommendation: {str(e)}")
            return {
                'success': False,
                'error': f'Lỗi khi tạo khuyến nghị điều trị: {str(e)}'
            } 