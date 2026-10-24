---
key: 图片生成/图生图/Gemini 3 Pro图片反推+自定义定向修改提示词+全能图片image2.0生图工作流_2067816340215394305.json
name: Gemini 3 Pro图片反推+自定义定向修改提示词+全能图片image2.0生图工作流_2067816340215394305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Gemini 3 Pro图片反推+自定义定向修改提示词+全能图片image2.0生图工作流_2067816340215394305.json
hash: 9d826a1d552e2b9d
coverage: 0.555556
learned_at: 2026-10-23 11:02:45
nodes: [LoadImage, PrimitiveNode, PrimitiveNode, RH_RhartImageG2TextToImage, SaveImage, Image Comparer (rgthree), easy showAnything, Text, RH_Captioner_Pro]
patterns: []
missing: []
---

# 图片生成/图生图/Gemini 3 Pro图片反推+自定义定向修改提示词+全能图片image2.0生图工作流_2067816340215394305.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Gemini 3 Pro图片反推+自定义定向修改提示词+全能图片image2.0生图工作流_2067816340215394305.json`

## 结构

**生成流程**：Output → Other

**节点**（9 个）：
- `LoadImage`
- `PrimitiveNode`
- `PrimitiveNode`
- `RH_RhartImageG2TextToImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `easy showAnything`
- `Text`
- `RH_Captioner_Pro`

## 知识

覆盖率 **56%**（5/9）

**有卡**：`LoadImage`、`RH_RhartImageG2TextToImage`、`SaveImage`、`Text`、`RH_Captioner_Pro`

**用到的条目**：LoadImage、SaveImage、RH_RhartImageG2TextToImage、Text、RH_Captioner_Pro、sd15-t2i-basic、sd15-t2i-lora、sd1_5_text2image_sampler_clip_checkpoint
