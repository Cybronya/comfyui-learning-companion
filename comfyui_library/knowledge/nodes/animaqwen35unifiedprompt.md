# AnimaQwen35UnifiedPrompt

## 节点类型

`AnimaQwen35UnifiedPrompt`

## 分类

Prompt

## 作用

提示词处理节点（按节点名关键词推断，TODO(待验证)）

## 实测使用

出现在本库 1 个 workflow 中。

## 输入

- `model:MODEL`（2 次）
- `native_clip:CLIP`（2 次）
- `qwen35_clip:CLIP`（2 次）
- `prompt:STRING`（1 次）

## 输出

- `expanded:CONDITIONING`（2 次）
- `native:CONDITIONING`（2 次）

## 参数（widgets_values 按位置，参数名未知）

常见取值：

- `["Anima-3.8B-expanded_adapter.safetensors", "masterpiece, best quality, score_9, score_9, very aesthetic, ultra detailed`（1 次）
- `["Anima-3.8B-expanded_adapter.safetensors", "worst quality, low quality, score_1, score_2, score_3, artist name, blurry,`（1 次）

## 可信度

Generated（自动起草：输入/输出/取值分布为 workflow 实测；作用为名称推断）TODO(待验证)
