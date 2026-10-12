# load_SD35

## 节点类型

`load_SD35`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `preset:COMBO`（9 次）
- `unet_name:COMBO`（9 次）
- `unet_Weight_Dtype:COMBO`（9 次）
- `clip1:COMBO`（9 次）
- `clip2:COMBO`（9 次）
- `clip3:COMBO`（9 次）
- `vae:COMBO`（9 次）
- `lora:COMBO`（9 次）
- `lora_strength:FLOAT`（9 次）
- `width:INT`（9 次）

## 输出

- `context:RUN_CONTEXT`（9 次）
- `model:MODEL`（9 次）
- `preset_save:PDATA`（9 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[null, "None", "fp8_e4m3fn", "clip_l.safetensors", "clip_g.safetensors", "t5xxl_fp8_e4m3fn.safetensors", "SD3.5vae.safet`（9 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
