# H3FaceTrackCrop

## 节点类型

`H3FaceTrackCrop`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 3 个 workflow 中。

## 输入

- `images:IMAGE`（3 次）
- `identity_reference:IMAGE`（3 次）
- `identity_clip_vision:CLIP_VISION`（3 次）
- `face_pick:H3FACEPICK`（3 次）
- `detector:COMBO`（3 次）
- `confidence:FLOAT`（3 次）
- `crop_factor:FLOAT`（3 次）
- `canvas_width:INT`（3 次）
- `canvas_height:INT`（3 次）
- `canvas_mode:COMBO`（3 次）

## 输出

- `crops:IMAGE`（3 次）
- `transform:H3FACEXFORM`（3 次）
- `preview:IMAGE`（3 次）
- `report:STRING`（3 次）
- `canvas_w:INT`（3 次）
- `canvas_h:INT`（3 次）
- `frame_count:INT`（3 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["face_yolov8n.pt", 0.35, 2.5, 768, 768, "manual", 21, 51, "gaussian", "per_frame", true, 0.28, "largest_face", "none", `（3 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
