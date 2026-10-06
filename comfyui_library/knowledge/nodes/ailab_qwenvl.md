# AILab_QwenVL

## 节点类型

`AILab_QwenVL`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 10 个 workflow 中。

## 输入

- `image:IMAGE`（14 次）
- `video:IMAGE`（14 次）
- `model_name:COMBO`（14 次）
- `quantization:COMBO`（14 次）
- `preset_prompt:COMBO`（14 次）
- `custom_prompt:STRING`（14 次）
- `max_tokens:INT`（14 次）
- `keep_model_loaded:BOOLEAN`（14 次）
- `seed:INT`（14 次）
- `attention_mode:COMBO`（14 次）

## 输出

- `RESPONSE:STRING`（14 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen3-VL-4B-Instruct", "None (FP16)", "🖼️ Detailed Description", "", 512, true, 666, "fixed", "auto"]`（9 次）
- `["Qwen3-VL-4B-Instruct", "None (FP16)", "Describe this image in detail.", "", 1024, true, 569979645047677, "randomize", `（3 次）
- `["Qwen3-VL-8B-Instruct", "8-bit (Balanced)", "Describe this image in detail.", "你需作为专业AI图像生成提示词设计师，针对给定图像，详细描述其主体、前景、中景、`（1 次）
- `["Qwen3-VL-4B-Instruct", "8-bit (Balanced)", "Create a detailed text-to-image prompt from this image.", "请详细描述这张图，只输出用于图`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
