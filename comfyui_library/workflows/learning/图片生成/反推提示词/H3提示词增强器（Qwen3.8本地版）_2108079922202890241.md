---
key: 图片生成/反推提示词/H3提示词增强器（Qwen3.8本地版）_2108079922202890241.json
name: H3提示词增强器（Qwen3.8本地版）_2108079922202890241
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/H3提示词增强器（Qwen3.8本地版）_2108079922202890241.json
hash: c7df9486c1cb9aeb
coverage: 0.8
learned_at: 2026-10-26 01:45:15
nodes: [LoadImage, MiniMaxH3PromptEnhancerT8, LoadImage, RH_Translator, PreviewAny, easy saveText, easy saveText, easy showAnything, CR Prompt Text, easy imageSave]
patterns: []
missing: []
---

# 图片生成/反推提示词/H3提示词增强器（Qwen3.8本地版）_2108079922202890241.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/H3提示词增强器（Qwen3.8本地版）_2108079922202890241.json`

## 结构

**生成流程**：Output → Other

**节点**（10 个）：
- `LoadImage`
- `MiniMaxH3PromptEnhancerT8`
- `LoadImage`
- `RH_Translator`
- `PreviewAny`
- `easy saveText`
- `easy saveText`
- `easy showAnything`
- `CR Prompt Text`
- `easy imageSave`

## 知识

覆盖率 **80%**（8/10）

**有卡**：`LoadImage`、`MiniMaxH3PromptEnhancerT8`、`RH_Translator`、`easy saveText`、`CR Prompt Text`、`easy imageSave`

**用到的条目**：LoadImage、MiniMaxH3PromptEnhancerT8、CR Prompt Text、easy imageSave、easy saveText、RH_Translator、sd15-t2i-basic、sd15-t2i-lora
