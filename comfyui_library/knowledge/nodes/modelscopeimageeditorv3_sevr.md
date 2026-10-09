# ModelScopeImageEditorV3_Sevr

## 节点类型

`ModelScopeImageEditorV3_Sevr`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `manual_image_url:STRING`（1 次）
- `prompt:STRING`（1 次）
- `negative_prompt:STRING`（1 次）
- `batch_size:INT`（1 次）
- `size:COMBO`（1 次）
- `steps:INT`（1 次）
- `guidance:FLOAT`（1 次）
- `seed:INT`（1 次）
- `modelscope_api_key:STRING`（1 次）

## 输出

- `edited_image:IMAGE`（1 次）
- `usage_instruction:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "改写写实风格，提高画质，细节丰富，清晰", "偏黄，暗黄，模糊，欧美人，黑人，色调艳丽，过曝，细节模糊不清，整体发灰，最差质量，低质量，JPEG压缩残留，丑陋的，残缺的，多余的手指，杂乱的背景，三条腿", 8, "AutoSiz`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
