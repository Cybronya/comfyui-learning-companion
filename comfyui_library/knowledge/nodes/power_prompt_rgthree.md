# Power Prompt (rgthree)

## 节点类型

`Power Prompt (rgthree)`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `opt_model:MODEL`（1 次）
- `opt_clip:CLIP`（1 次）
- `prompt:STRING`（1 次）
- `insert_embedding:COMBO`（1 次）

## 输出

- `CONDITIONING:CONDITIONING`（1 次）
- `MODEL:MODEL`（1 次）
- `CLIP:CLIP`（1 次）
- `TEXT:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["实拍照片，仅局部修改蒙版区域，替换鞋帮圆形徽章logo，logo位置、大小、比例、样式完全匹配参考图。圆形白色徽章，圈内文字CONUERLIUE，ALL HUMAN，黑色五角星。logo贴合黑色帆布鞋曲面透视，融入帆布纹理，匹配原图室内`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
