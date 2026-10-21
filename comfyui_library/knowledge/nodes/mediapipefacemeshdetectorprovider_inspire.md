# MediaPipeFaceMeshDetectorProvider //Inspire

## 节点类型

`MediaPipeFaceMeshDetectorProvider //Inspire`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `max_faces:INT`（2 次）
- `face:BOOLEAN`（2 次）
- `mouth:BOOLEAN`（2 次）
- `left_eyebrow:BOOLEAN`（2 次）
- `left_eye:BOOLEAN`（2 次）
- `left_pupil:BOOLEAN`（2 次）
- `right_eyebrow:BOOLEAN`（2 次）
- `right_eye:BOOLEAN`（2 次）
- `right_pupil:BOOLEAN`（2 次）

## 输出

- `BBOX_DETECTOR:BBOX_DETECTOR`（2 次）
- `SEGM_DETECTOR:SEGM_DETECTOR`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[10, true, false, false, false, false, false, false, false]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
