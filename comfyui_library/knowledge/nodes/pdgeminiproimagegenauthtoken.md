# PDGeminiProImageGenAuthToken

## 节点类型

`PDGeminiProImageGenAuthToken`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（3 次）
- `auth_token:STRING`（3 次）
- `prompt:STRING`（3 次）
- `model:COMBO`（3 次）
- `aspect_ratio:COMBO`（3 次）
- `resolution:COMBO`（3 次）
- `response_modalities:COMBO`（3 次）
- `seed:INT`（3 次）
- `system_prompt:STRING`（3 次）

## 输出

- `image:IMAGE`（3 次）
- `text:STRING`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "为我生成图中角色的绘制Q版的，穿红色毛衣，背景干净纯白色，扁平化矢量风格，LINE 风格的半身像表情包，生成3×3照片网格（共9张）涵盖动作包含：每个表情下方都有一个文字标签区域，马年相关。\n马上有钱 (拿红包)\n\n马上暴`（1 次）
- `["", "为我生成图中角色的绘制Q版的，穿红色毛衣，背景干净纯白色，扁平化矢量风格，LINE 风格的半身像表情包，生成3×3照片网格（共9张）涵盖动作包含：每个表情下方都有一个文字标签区域，马年相关。\n马上有钱 (拿红包)\n\n马上暴`（1 次）
- `["", "A futuristic city with flying cars", "gemini-3-pro-image-preview", "auto", "1K", "IMAGE+TEXT", 863926653901401, "r`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
