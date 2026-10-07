# WanVideoVACEStartToEndFrame

## 节点类型

`WanVideoVACEStartToEndFrame`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `start_image:IMAGE`（1 次）
- `end_image:IMAGE`（1 次）
- `control_images:IMAGE`（1 次）
- `inpaint_mask:MASK`（1 次）
- `num_frames:INT`（1 次）
- `empty_frame_level:FLOAT`（1 次）
- `start_index:INT`（1 次）
- `end_index:INT`（1 次）

## 输出

- `images:IMAGE`（1 次）
- `masks:MASK`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[65, 0.5, 0, -1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
