---
key: 图片生成/反推提示词/（Qwen3.8本地版）最强MiniMax H3提示词增强器_2099379334015442946.json
name: （Qwen3.8本地版）最强MiniMax H3提示词增强器_2099379334015442946
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/（Qwen3.8本地版）最强MiniMax H3提示词增强器_2099379334015442946.json
hash: f55f72add18dc3c0
coverage: 0.85
learned_at: 2026-10-26 01:49:00
nodes: [LoadImage, PreviewImage, 忽略多组孤海, LoadImage, LoadImage, LoadImage, T8PerformanceDirectorConfig, CR Prompt Text, VRAM_Debug, CR Prompt Text, LoadImage, LoadImage, easy showAnything, Note, CR Prompt Text, MiniMaxH3PromptEnhancerT8, CM_FloatToInt, ShellAgentPluginOutputText, ImageFlip+, SaveImage]
patterns: []
missing: []
---

# 图片生成/反推提示词/（Qwen3.8本地版）最强MiniMax H3提示词增强器_2099379334015442946.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/（Qwen3.8本地版）最强MiniMax H3提示词增强器_2099379334015442946.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（20 个）：
- `LoadImage`
- `PreviewImage`
- `忽略多组孤海`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `T8PerformanceDirectorConfig`
- `CR Prompt Text`
- `VRAM_Debug`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
- `Note`
- `CR Prompt Text`
- `MiniMaxH3PromptEnhancerT8`
- `CM_FloatToInt`
- `ShellAgentPluginOutputText`
- `ImageFlip+`
- `SaveImage`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`LoadImage`、`忽略多组孤海`、`T8PerformanceDirectorConfig`、`CR Prompt Text`、`VRAM_Debug`、`MiniMaxH3PromptEnhancerT8`、`CM_FloatToInt`、`ShellAgentPluginOutputText`、`ImageFlip+`、`SaveImage`

**用到的条目**：SaveImage、LoadImage、MiniMaxH3PromptEnhancerT8、CR Prompt Text、ShellAgentPluginOutputText、CM_FloatToInt、VRAM_Debug、T8PerformanceDirectorConfig
