# FeiHouEasyH3RHFaceRefine

## 节点类型

`FeiHouEasyH3RHFaceRefine`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `images:IMAGE`（2 次）
- `model:MODEL`（2 次）
- `h3_context:MINIMAX_H3_CONTEXT`（2 次）
- `reference_face:IMAGE`（2 次）
- `reference_faces:IMAGE`（2 次）
- `audio:AUDIO`（2 次）
- `enabled:BOOLEAN`（2 次）
- `detector:COMBO`（2 次）
- `target:COMBO`（2 次）
- `denoise:FLOAT`（2 次）

## 输出

- `images:IMAGE`（2 次）
- `audio:AUDIO`（2 次）
- `fps:FLOAT`（2 次）
- `report:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, "face_yolov8m.pt", "largest_face", 0.25, 8, 636094094319744, "randomize", false, "768", 0.35, 2.5, "不分段", "euler"`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
