# GeminiNodeV3

## 节点类型

`GeminiNodeV3`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `model.images.image_1:IMAGE`（5 次）
- `model.audio.audio_1:AUDIO`（5 次）
- `model.video.video_1:VIDEO`（5 次）
- `model.files:GEMINI_INPUT_FILES`（5 次）
- `model.images.image_2:IMAGE`（3 次）

## 输出

- `STRING:STRING`（5 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Gemini 3.8 Flash", "Describe the image", "static", "MEDIUM", 32768, 42, "randomize", ""]`（1 次）
- `["Gemini 3.8 Flash", "TARGET IMAGE ASPECT RATIO: {{aspect_ratio}} (width:height).\nUser idea: {{original_prompt}}", "sta`（1 次）
- `["Gemini 3.8 Flash", "Follow the system instructions: The main subject is a rubberhose animation character from @image_1`（1 次）
- `["Gemini 3.8 Flash", "A ninja sprints across a rooftop beneath the moonlit night sky before launching high into the air.`（1 次）
- `["Gemini 3.8 Flash", "A ninja sprints across a rooftop beneath the moonlit night sky before launching high into the air.`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
