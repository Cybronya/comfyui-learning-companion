# TextGenerateV2

## 节点类型

`TextGenerateV2`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 18 个 workflow 中。

## 输入

- `clip:CLIP`（19 次）
- `images.image1:IMAGE`（19 次）
- `videos.video1:IMAGE`（19 次）
- `audios.audio1:AUDIO`（19 次）
- `system_prompt:STRING`（19 次）
- `prompt:STRING`（19 次）
- `max_length:INT`（19 次）
- `sampling_mode:COMFY_DYNAMICCOMBO_V3`（19 次）
- `thinking:BOOLEAN`（19 次）
- `use_default_template:BOOLEAN`（19 次）

## 输出

- `generated_text:STRING`（19 次）
- `thinking:STRING`（19 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 8192, "on", 1, 20, 0.95, 0, 1, 0, 0, true, true, "auto"]`（11 次）
- `["", 8196, "on", 1, 20, 0.95, 0, 1, 0, 0, true, true, "auto"]`（3 次）
- `["", 3604, "on", 0.7, 64, 0.95, 0.05, 1.05, 0, 0, false, true, "off"]`（1 次）
- `["", 1536, "off", true, true, "auto"]`（1 次）
- `["", 1024, "on", 0.7, 64, 0.95, 0.05, 1.05, 0, 0, false, true, "auto"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
