# T8LLaDAImageVQConditioning

## 节点类型

`T8LLaDAImageVQConditioning`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输入

- `clip:CLIP`（4 次）
- `prompt:STRING`（4 次）
- `negative_prompt:STRING`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）

## 输出

- `positive:CONDITIONING`（4 次）
- `negative:CONDITIONING`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "", 1024, 1024]`（2 次）
- `["A red fox sleeping beneath a glass tree.", "", 1024, 1024]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
