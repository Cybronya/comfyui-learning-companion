# TextGenerate

## 节点类型

`TextGenerate`

## 分类

Utility

## 作用

文本工具节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 47 个 workflow 中。

## 输入

- `clip:CLIP`（71 次）
- `image:IMAGE`（71 次）
- `video:IMAGE`（71 次）
- `audio:AUDIO`（71 次）
- `prompt:STRING`（71 次）
- `max_length:INT`（71 次）
- `sampling_mode:COMFY_DYNAMICCOMBO_V3`（71 次）
- `thinking:BOOLEAN`（71 次）
- `use_default_template:BOOLEAN`（71 次）
- `mtp:COMBO`（71 次）

## 输出

- `generated_text:STRING`（71 次）
- `thinking:STRING`（67 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", 512, "on", 0.7, 64, 0.95, 0.05, 1.05, 0, 0, false, true, "auto"]`（7 次）
- `["", 2048, "on", 0.7, 64, 0.95, 0.05, 1.05, 1, 0, false, true, "auto"]`（5 次）
- `["Are the person's feet or shoes in this picture? Answer yes or no.", 16, "off", true, true, "auto"]`（5 次）
- `["Are the person's legs in this picture? Answer yes or no.", 16, "off", true, true, "auto"]`（5 次）
- `["", 200, "off", true, true, "auto"]`（5 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
