# Echo_LoadModel

## 节点类型

`Echo_LoadModel`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 4 个 workflow 中。

## 输出

- `model:MODEL_PIPE_E`（4 次）
- `face_detector:MODEL_FACE_E`（4 次）
- `visualizer:MODEL_VISUAL_E`（4 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["stabilityai/sd-vae-ft-mse", true, "audio_drived", false, false, false, "V1"]`（2 次）
- `["stabilityai/sd-vae-ft-mse", true, "audio_drived", false, false, false, "V2"]`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
