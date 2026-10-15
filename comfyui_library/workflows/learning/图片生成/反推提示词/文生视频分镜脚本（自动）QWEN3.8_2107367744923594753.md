---
key: 图片生成/反推提示词/文生视频分镜脚本（自动）QWEN3.8_2107367744923594753.json
name: 文生视频分镜脚本（自动）QWEN3.8_2107367744923594753
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/文生视频分镜脚本（自动）QWEN3.8_2107367744923594753.json
hash: 8aff9bc5af4f8337
coverage: 0.888889
learned_at: 2026-10-15 22:25:03
nodes: [SaveImage, LoadImage, RH_Translator, LoadImage, easy saveText, CR Prompt Text, MiniMaxH3PromptEnhancerT8, CM_FloatToInt, PreviewAny]
patterns: []
missing: []
---

# 图片生成/反推提示词/文生视频分镜脚本（自动）QWEN3.8_2107367744923594753.json

> 来源文件 `comfyui_library/workflows/图片生成/反推提示词/文生视频分镜脚本（自动）QWEN3.8_2107367744923594753.json`

## 结构

**生成流程**：Output → Other

**节点**（9 个）：
- `SaveImage`
- `LoadImage`
- `RH_Translator`
- `LoadImage`
- `easy saveText`
- `CR Prompt Text`
- `MiniMaxH3PromptEnhancerT8`
- `CM_FloatToInt`
- `PreviewAny`

## 知识

覆盖率 **89%**（8/9）

**有卡**：`SaveImage`、`LoadImage`、`RH_Translator`、`easy saveText`、`CR Prompt Text`、`MiniMaxH3PromptEnhancerT8`、`CM_FloatToInt`

**用到的条目**：LoadImage、MiniMaxH3PromptEnhancerT8、CR Prompt Text、SaveImage、easy saveText、CM_FloatToInt、RH_Translator、sd15-t2i-basic
