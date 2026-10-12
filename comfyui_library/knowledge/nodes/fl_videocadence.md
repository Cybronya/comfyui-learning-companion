# FL_VideoCadence

## 节点类型

`FL_VideoCadence`

## 分类

Video

## 作用

视频处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `images:IMAGE`（1 次）
- `fps:INT`（1 次）
- `threshold:FLOAT`（1 次）
- `min_scene_length:INT`（1 次）
- `detection_method:COMBO`（1 次）
- `downsample_detection:BOOLEAN`（1 次）
- `use_gpu_acceleration:BOOLEAN`（1 次）

## 输出

- `scene_lengths_str:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[24, 30, 12, "hybrid", false, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
