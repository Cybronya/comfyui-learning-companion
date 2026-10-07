# ApplyEcomIDAdvanced

## 节点类型

`ApplyEcomIDAdvanced`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `instantid_ipa:INSTANTID`（1 次）
- `pulid:PULID`（1 次）
- `eva_clip:EVA_CLIP`（1 次）
- `insightface:FACEANALYSIS`（1 次）
- `control_net:CONTROL_NET`（1 次）
- `image:IMAGE`（1 次）
- `model:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）
- `image_kps:IMAGE`（1 次）

## 输出

- `MODEL:MODEL`（1 次）
- `positive:CONDITIONING`（1 次）
- `negative:CONDITIONING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["fidelity", 0, 1, 0.8, 0.8, 0, "average"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
