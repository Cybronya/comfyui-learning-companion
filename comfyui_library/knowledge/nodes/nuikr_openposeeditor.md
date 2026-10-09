# NuiKr.OpenPoseEditor

## 节点类型

`NuiKr.OpenPoseEditor`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `pose_image:IMAGE`（2 次）
- `pose_point:POSE_KEYPOINT`（2 次）
- `prev_image:IMAGE`（2 次）
- `bridge_anything:*`（2 次）
- `image:STRING`（2 次）
- `output_width_for_dwpose:INT`（2 次）
- `output_height_for_dwpose:INT`（2 次）
- `scale_for_xinsr_for_dwpose:BOOLEAN`（2 次）
- `stop_for_edit:BOOLEAN`（2 次）

## 输出

- `dw_pose_image:IMAGE`（2 次）
- `dw_comb_image:IMAGE`（2 次）
- `dw_pose_image_width:INT`（2 次）
- `dw_pose_image_height:INT`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["openpose_dw_bg_temp_1790583608761.png", 512, 704, true, false, "/data/ComfyUI/personal/input/openpose_ld_temp_17905836`（1 次）
- `["566daa07b941923f98a237f377d5f5f8a8025021fdaffffe13577a6ec87096f5.jpg", 1024, 1024, true, false, "/data/ComfyUI/persona`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
