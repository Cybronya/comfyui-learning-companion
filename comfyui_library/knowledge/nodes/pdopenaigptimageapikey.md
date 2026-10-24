# PDOpenAIGPTImageAPIKey

## 节点类型

`PDOpenAIGPTImageAPIKey`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）
- `api_key:STRING`（2 次）
- `prompt:STRING`（2 次）
- `seed:INT`（2 次）
- `quality:COMBO`（2 次）
- `background:COMBO`（2 次）
- `size:COMBO`（2 次）
- `n:INT`（2 次）
- `model:COMBO`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `info:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", 1436353604, "randomize", "low", "auto", "auto", 1, "gpt-image-1"]`（1 次）
- `["", "生成皮克斯风格", 1758374198, "randomize", "high", "auto", "auto", 1, "gpt-image-1"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
