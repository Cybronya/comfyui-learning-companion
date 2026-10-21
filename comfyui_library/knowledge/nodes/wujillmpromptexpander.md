# WujiLLMPromptExpander

## 节点类型

`WujiLLMPromptExpander`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `图像1:IMAGE`（1 次）
- `图像2:IMAGE`（1 次）
- `图像3:IMAGE`（1 次）
- `图像4:IMAGE`（1 次）
- `视频:IMAGE`（1 次）
- `提示词:STRING`（1 次）
- `模型选择:COMBO`（1 次）
- `mmproj模型:COMBO`（1 次）
- `API_Key:STRING`（1 次）
- `扩写预设:COMBO`（1 次）

## 输出

- `扩写提示词:STRING`（1 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["", "Qwen3.5-9B-Q4_0.gguf", "Qwen3.5-9B-mmproj-BF16.gguf", "", "自定义", "", 0.7, 8192, false, false, "-------------------`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
