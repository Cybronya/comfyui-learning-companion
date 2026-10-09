# PoseAndFaceDetection

## 节点类型

`PoseAndFaceDetection`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:POSEMODEL`（1 次）
- `images:IMAGE`（1 次）
- `retarget_image:IMAGE`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）

## 输出

- `pose_data:POSEDATA`（1 次）
- `face_images:IMAGE`（1 次）
- `key_frame_body_points:STRING`（1 次）
- `bboxes:BBOX`（1 次）
- `face_bboxes:BBOX,`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[480, 832]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
