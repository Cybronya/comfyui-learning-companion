# ReActorFaceSwap

## 节点类型

`ReActorFaceSwap`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `input_image:IMAGE`（1 次）
- `source_image:IMAGE`（1 次）
- `face_model:FACE_MODEL`（1 次）
- `face_boost:FACE_BOOST`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）
- `FACE_MODEL:FACE_MODEL`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, "inswapper_128.onnx", "retinaface_resnet50", "none", 1, 0.5, "no", "no", "0", "0", 1]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
