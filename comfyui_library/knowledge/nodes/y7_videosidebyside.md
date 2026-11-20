# Y7_VideoSideBySide

## 节点类型

`Y7_VideoSideBySide`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `frames:IMAGE`（1 次）
- `depth_maps:IMAGE`（1 次）
- `method:COMBO`（1 次）
- `depth_scale:INT`（1 次）
- `mode:COMBO`（1 次）
- `output_type:COMBO`（1 次）
- `depth_blur_strength:INT`（1 次）
- `temporal_smoothing:FLOAT`（1 次）
- `batch_size:INT`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["mesh_warping", 60, "parallel", "sbs", 7, 0.2, 8]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
