# GPTImage2Generate

## 节点类型

`GPTImage2Generate`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `prompt:STRING`（1 次）
- `model:COMBO`（1 次）
- `size:COMBO`（1 次）
- `n:INT`（1 次）
- `api_key:STRING`（1 次）
- `api_base:STRING`（1 次）
- `timeout:INT`（1 次）

## 输出

- `图像:IMAGE`（1 次）
- `图片URL:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "gpt-image-2", "2160x3840（9:16｜4K竖版）", 1, "", "https://api.kegeai.top", 9999]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
