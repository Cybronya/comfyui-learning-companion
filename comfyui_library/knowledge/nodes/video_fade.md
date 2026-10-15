# Video_Fade

## 节点类型

`Video_Fade`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `video1:IMAGE`（2 次）
- `video2:IMAGE`（2 次）
- `mask:MASK`（2 次）
- `OverlappingFrame:INT`（2 次）
- `method:COMBO`（2 次）

## 输出

- `video:IMAGE`（2 次）
- `frames:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[8, "Cosine"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
