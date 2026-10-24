# workflow>参数设置

## 节点类型

`workflow>参数设置`

## 分类

Other

## 作用

作用未知，需人工补充（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 5 个 workflow 中。

## 输入

- `模型:MODEL`（5 次）
- `image:IMAGE`（3 次）
- `images:IMAGE`（3 次）
- `LoRA:PEFTLORA`（2 次）
- `图像:IMAGE`（2 次）
- `宽度:INT`（2 次）
- `高度:INT`（2 次）

## 输出

- `模型:MODEL`（5 次）
- `图像:IMAGE`（5 次）
- `显示帮助:STRING`（3 次）
- `CR Text Concatenate 显示帮助:STRING`（3 次）
- `output:*`（2 次）
- `宽度:INT`（2 次）
- `高度:INT`（2 次）
- `放大系数:FLOAT`（2 次）
- `批次大小:INT`（2 次）
- `show_help:STRING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["flux1-dev-fp8.safetensors", "fp8_e4m3fn_fast", "anime,Jojo's_style", "unsloth/Meta-Llama-3.1-8B-Instruct", "depth_anyt`（1 次）
- `["flux1-dev-fp8.safetensors", "fp8_e4m3fn_fast", "anime,Jojo's_style", "unsloth/Meta-Llama-3.1-8B-Instruct", "depth_anyt`（1 次）
- `["flux1-dev-fp8.safetensors", "fp8_e4m3fn_fast", "anime, ghibli style", "unsloth/Meta-Llama-3.1-8B-Instruct", "depth_any`（1 次）
- `["CogFlorence-2-Large-Freeze", "fp16", "sdpa", "flux1-dev.sft", "fp8_e4m3fn", "3D, Disney Style, ((Pierce Style)), Maste`（1 次）
- `["CogFlorence-2-Large-Freeze", "fp16", "sdpa", "flux1-dev.sft", "fp8_e4m3fn", "3D, Disney Style, ((Pierce Style)), Maste`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
