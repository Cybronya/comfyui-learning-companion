---
key: 图片生成/反推提示词/文生视频分镜脚本（自动）QWEN3.8_2107367744923594753.json
name: 文生视频分镜脚本（自动）QWEN3.8_2107367744923594753
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/反推提示词/文生视频分镜脚本（自动）QWEN3.8_2107367744923594753.json
hash: 8aff9bc5af4f8337
coverage: 0.666667
learned_at: 2026-10-07 02:41:12
nodes: [SaveImage, LoadImage, RH_Translator, LoadImage, easy saveText, CR Prompt Text, MiniMaxH3PromptEnhancerT8, CM_FloatToInt, PreviewAny]
patterns: []
missing: [CR Prompt Text, easy saveText]
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
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

覆盖率 **67%**（6/9）

**有卡**：`SaveImage`、`LoadImage`、`RH_Translator`、`MiniMaxH3PromptEnhancerT8`、`CM_FloatToInt`

**缺卡**（2）：`CR Prompt Text`、`easy saveText`

**用到的条目**：LoadImage、MiniMaxH3PromptEnhancerT8、SaveImage、CM_FloatToInt、RH_Translator、sd15-t2i-basic、sd15-t2i-lora、SaveText

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `easy saveText` 仅有 SaveImage 的通用知识，没有该节点自己的说明
