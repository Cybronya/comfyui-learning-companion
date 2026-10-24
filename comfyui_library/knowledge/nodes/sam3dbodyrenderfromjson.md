# SAM3DBodyRenderFromJson

## 节点类型

`SAM3DBodyRenderFromJson`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `model:SAM3D_MODEL`（2 次）
- `background_image:IMAGE`（2 次）
- `pose_json:STRING`（2 次）
- `preset:COMBO`（2 次）
- `offset_x:FLOAT`（2 次）
- `offset_y:FLOAT`（2 次）
- `scale_offset:FLOAT`（2 次）
- `width:INT`（2 次）
- `height:INT`（2 次）
- `body_fat:FLOAT`（2 次）

## 输出

- `image:IMAGE`（2 次）
- `settings_json:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["{}", "female", 0, 0, 1, 0, 0, -0.5, 0, 0, 0.30000000000000004, 0, 0.4000000000000001, 0, 0, -0.4000000000000001, 0.900`（1 次）
- `["{}", "female", 0, -0.1, 1, 0, 0, -0.5, 0, 0, 0, 0, 0, 0, 0, 0, 0.9, 1.2, 1, 1, 0, 0, 0, 1, 0, 0, 0.5, 0.3, 0.3, 0, 0.4`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
