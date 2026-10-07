# Gemini_Flash_200_Exp

## 节点类型

`Gemini_Flash_200_Exp`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `images:IMAGE`（8 次）
- `video:IMAGE`（8 次）
- `audio:AUDIO`（8 次）
- `prompt:STRING`（1 次）

## 输出

- `generated_content:STRING`（8 次）
- `generated_images:IMAGE`（8 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Analyze the situation in details.", "image", "gemini-2.0-flash-exp-image-generation", "generate_images", false, true, `（1 次）
- `["1. Transcribe the audio\n2. Who is speaking?", "audio", "gemini-2.0-flash-exp", "analysis", false, false, "", "", 8192`（1 次）
- `["图一女人穿上图2衣服", "image", "gemini-2.0-flash-exp-image-generation", "generate_images", false, false, "", "", 8192, 0.4, fal`（1 次）
- `["图1女人和图2男人拥抱，保持人物和服装的一致性", "image", "gemini-2.0-flash-exp-image-generation", "generate_images", false, false, "", "", 8`（1 次）
- `["请将女人衣服换位红色长裙，请保持人物一致性输出", "image", "gemini-2.0-flash-exp-image-generation", "generate_images", false, false, "", "", 8`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
