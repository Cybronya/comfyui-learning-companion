# BriaImageEditNode

## 节点类型

`BriaImageEditNode`

## 分类

Image Processing

## 作用

图像处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `mask:MASK`（2 次）

## 输出

- `IMAGE:IMAGE`（2 次）
- `structured_prompt:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["FIBO", "Modern architectural photography at night, blue hour. Anti-glare technology, crisp and clear lens, no lens fla`（1 次）
- `["FIBO", "A baby otter is held in a person's hand, with warm tones", "", "", 1, "randomize", 3, 50, "false"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
