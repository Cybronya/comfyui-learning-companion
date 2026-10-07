# LoadQwenImageDiffSynthiPipe

## 节点类型

`LoadQwenImageDiffSynthiPipe`

## 分类

Input

## 作用

输入类节点：读入外部数据（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 2 个 workflow 中。

## 输入

- `offload:BOOLEAN`（2 次）
- `fp8_quantization:BOOLEAN`（1 次）
- `lora:COMBO`（1 次）
- `lora_alpha:FLOAT`（1 次）
- `lora:QwenImageLora`（1 次）
- `if_lighting_lora_name:COMBO`（1 次）
- `controlnet:COMBO`（1 次）

## 输出

- `pipe:QwenImageDiffSynthiPipe`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `[true, false, "Qwen-Image-EliGen.safetensors", 1]`（1 次）
- `[true, "Qwen-Image-Lightning-8steps-V1.1.safetensors", "None"]`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
