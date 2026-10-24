# workflow>文字抠图

## 节点类型

`workflow>文字抠图`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `image:IMAGE`（2 次）
- `LayerMask: SAM2UltraV2 image:IMAGE`（2 次）
- `model_name:COMBO`（2 次）
- `device:COMBO`（2 次）
- `precision:COMBO`（2 次）
- `sam2_model:COMBO`（2 次）
- `LayerMask: LoadSAM2Model precision:COMBO`（2 次）
- `LayerMask: LoadSAM2Model device:COMBO`（2 次）
- `target:STRING`（2 次）
- `bbox_selection:STRING`（2 次）

## 输出

- `text:JSON`（2 次）
- `mask:MASK`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Qwen/Qwen2.5-VL-7B-Instruct", "auto", "BF16", "sam2.1_hiera_large.safetensors", "fp16", "cuda", "文字", "all", 0, false,`（1 次）
- `["Qwen/Qwen2.5-VL-7B-Instruct", "auto", "BF16", "sam2.1_hiera_large.safetensors", "fp16", "cuda", "文字", "all", 0, true, `（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
