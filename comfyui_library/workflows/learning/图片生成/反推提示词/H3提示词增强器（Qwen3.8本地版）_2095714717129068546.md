---
key: 图片生成/反推提示词/H3提示词增强器（Qwen3.8本地版）_2095714717129068546.json
name: H3提示词增强器（Qwen3.8本地版）_2095714717129068546
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/H3提示词增强器（Qwen3.8本地版）_2095714717129068546.json
hash: 8f50e65d16bcc68d
coverage: 0.818182
learned_at: 2026-10-26 01:45:15
nodes: [LoadImage, SaveImage, LoadImage, MiniMaxH3PromptEnhancerT8, CR Prompt Text, LoadImage, RH_Translator, easy showAnything, PreviewAny, easy saveText, easy saveText]
patterns: []
missing: []
---

# 图片生成/反推提示词/H3提示词增强器（Qwen3.8本地版）_2095714717129068546.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/H3提示词增强器（Qwen3.8本地版）_2095714717129068546.json`

## 结构

**生成流程**：Output → Other

**节点**（11 个）：
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `MiniMaxH3PromptEnhancerT8`
- `CR Prompt Text`
- `LoadImage`
- `RH_Translator`
- `easy showAnything`
- `PreviewAny`
- `easy saveText`
- `easy saveText`

## 知识

覆盖率 **82%**（9/11）

**有卡**：`LoadImage`、`SaveImage`、`MiniMaxH3PromptEnhancerT8`、`CR Prompt Text`、`RH_Translator`、`easy saveText`

**用到的条目**：LoadImage、MiniMaxH3PromptEnhancerT8、CR Prompt Text、SaveImage、easy saveText、RH_Translator、sd15-t2i-basic、sd15-t2i-lora
