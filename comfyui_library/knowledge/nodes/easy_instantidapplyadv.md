# easy instantIDApplyADV

## 节点类型

`easy instantIDApplyADV`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 6 个 workflow 中。

## 输入

- `pipe:PIPE_LINE`（6 次）
- `image:IMAGE`（6 次）
- `image_kps:IMAGE`（6 次）
- `mask:MASK`（6 次）
- `control_net:CONTROL_NET`（6 次）
- `positive:CONDITIONING`（6 次）
- `negative:CONDITIONING`（6 次）
- `instantid_file:COMBO`（6 次）
- `insightface:COMBO`（6 次）
- `control_net_name:COMBO`（6 次）

## 输出

- `pipe:PIPE_LINE`（6 次）
- `model:MODEL`（6 次）
- `positive:CONDITIONING`（6 次）
- `negative:CONDITIONING`（6 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["ip-adapter.bin", "CPU", "instantid/diffusion_pytorch_model.safetensors", 1, 1, 0.9500000000000001, 0, 1, 0.35]`（6 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
