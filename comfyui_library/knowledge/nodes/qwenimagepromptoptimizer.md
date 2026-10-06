# QwenImagePromptOptimizer

## 节点类型

`QwenImagePromptOptimizer`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 17 个 workflow 中。

## 输入

- `图像_01:IMAGE`（17 次）
- `图像_02:IMAGE`（17 次）
- `图像_03:IMAGE`（17 次）
- `图像_04:IMAGE`（17 次）
- `图像_05:IMAGE`（17 次）
- `图像_06:IMAGE`（17 次）
- `图像_07:IMAGE`（17 次）
- `用户提示词:STRING`（17 次）
- `文生图模型:COMBO`（17 次）
- `图生图模型:COMBO`（17 次）

## 输出

- `prompt:STRING`（17 次）
- `json:STRING`（17 次）
- `是否反推:BOOLEAN`（17 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "Qwen-Image-2.1-PE-T2I.Q5_K_M.gguf", "Qwen-Image-2.1-PE-I2I.Q5_K_M.gguf", "Qwen-Image-2.1-PE-I2I.mmproj-bf16.gguf",`（5 次）
- `["", "Qwen-Image-2.1-PE-T2I.Q5_K_M.gguf", "Qwen-Image-2.1-PE-I2I.Q5_K_M.gguf", "Qwen-Image-2.1-PE-I2I.mmproj-bf16.gguf",`（4 次）
- `["", "Qwen-Image-2.1-PE-T2I.Q5_K_M.gguf", "Qwen-Image-2.1-PE-I2I.Q5_K_M.gguf", "Qwen-Image-2.1-PE-I2I.mmproj-bf16.gguf",`（3 次）
- `["", "Qwen-Image-2.1-PE-T2I.Q5_K_M.gguf", "Qwen-Image-2.1-PE-I2I.Q5_K_M.gguf", "Qwen-Image-2.1-PE-I2I.mmproj-bf16.gguf",`（2 次）
- `["", "Qwen-Image-2.1-PE-T2I.Q5_K_M.gguf", "Qwen-Image-2.1-PE-I2I.Q5_K_M.gguf", "Qwen-Image-2.1-PE-I2I.mmproj-bf16.gguf",`（2 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
