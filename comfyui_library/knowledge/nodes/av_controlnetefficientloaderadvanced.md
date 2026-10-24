# AV_ControlNetEfficientLoaderAdvanced

## 节点类型

`AV_ControlNetEfficientLoaderAdvanced`

## 分类

Model Loading

## 作用

加载类节点：把磁盘上的资源装入图中（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）
- `image:IMAGE`（2 次）
- `timestep_keyframe:TIMESTEP_KEYFRAME`（2 次）

## 输出

- `positive:CONDITIONING`（2 次）
- `negative:CONDITIONING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["control_v11f1p_sd15_depth.pth", 0.7000000000000001, 0, 1, "depth_midas", "None", 512, true]`（1 次）
- `["control_v11p_sd15_scribble.pth", 0.8, 0, 1, "scribble", "None", 512, true]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
