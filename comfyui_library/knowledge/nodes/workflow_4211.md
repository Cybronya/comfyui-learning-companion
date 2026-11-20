# workflow>人像转卡通

## 节点类型

`workflow>人像转卡通`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（1 次）
- `image_kps:IMAGE`（1 次）
- `mask:MASK`（1 次）
- `width:INT`（1 次）
- `height:INT`（1 次）
- `batch_size:INT`（1 次）
- `provider:COMBO`（1 次）
- `instantid_file:COMBO`（1 次）
- `pulid_file:COMBO`（1 次）
- `control_net_name:COMBO`（1 次）

## 输出

- `IMAGE:IMAGE`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[768, 1024, 1, "CUDA", "ip-adapter.bin", "ip-adapter_pulid_sdxl_fp16.safetensors", "instantid/diffusion_pytorch_model.sa`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
