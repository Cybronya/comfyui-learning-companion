# Lynx_Model

## 节点类型

`Lynx_Model`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `diffusion_models:COMBO`（1 次）
- `gguf:COMBO`（1 次）
- `adapter_path:STRING`（1 次）
- `torch_dtype:COMBO`（1 次）

## 输出

- `model:Lynx_MODEL`（1 次）
- `info:Lynx_INFO`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["wan2.1_t2v_14B_bf16_Comfy-Org.safetensors", "none", "/root/ComfyUI/models/photomaker/lynx_full", "bf16"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
