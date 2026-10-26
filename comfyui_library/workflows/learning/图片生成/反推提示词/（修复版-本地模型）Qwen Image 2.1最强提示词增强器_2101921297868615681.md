---
key: 图片生成/反推提示词/（修复版-本地模型）Qwen Image 2.1最强提示词增强器_2101921297868615681.json
name: （修复版-本地模型）Qwen Image 2.1最强提示词增强器_2101921297868615681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/（修复版-本地模型）Qwen Image 2.1最强提示词增强器_2101921297868615681.json
hash: 14eb915fa5e93f02
coverage: 0.7
learned_at: 2026-10-26 01:49:01
nodes: [CR Prompt Text, LoadImage, SaveImage, Note, easy showAnything, ShellAgentPluginOutputText, LoadImage, LoadImage, easy showAnything, QwenImage21PromptEnhancerT8]
patterns: []
missing: []
---

# 图片生成/反推提示词/（修复版-本地模型）Qwen Image 2.1最强提示词增强器_2101921297868615681.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/（修复版-本地模型）Qwen Image 2.1最强提示词增强器_2101921297868615681.json`

## 结构

**生成流程**：Output → Other

**节点**（10 个）：
- `CR Prompt Text`
- `LoadImage`
- `SaveImage`
- `Note`
- `easy showAnything`
- `ShellAgentPluginOutputText`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
- `QwenImage21PromptEnhancerT8`

## 知识

覆盖率 **70%**（7/10）

**有卡**：`CR Prompt Text`、`LoadImage`、`SaveImage`、`ShellAgentPluginOutputText`、`QwenImage21PromptEnhancerT8`

**用到的条目**：SaveImage、LoadImage、QwenImage21PromptEnhancerT8、CR Prompt Text、ShellAgentPluginOutputText、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint
