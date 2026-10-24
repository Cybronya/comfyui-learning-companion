# Load Image Sequence (mtb)

## 节点类型

`Load Image Sequence (mtb)`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输出

- `image:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `current_frame:INT`（1 次）
- `total_frames:INT`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["videos/####.png", 0, ""]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
