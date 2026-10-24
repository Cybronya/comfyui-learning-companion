---
key: 图片生成/图生图/Gemini 3 Pro图片反推+自定义定向修改提示词+全能图片image2.0（洗图）_2068205383113592833.json
name: Gemini 3 Pro图片反推+自定义定向修改提示词+全能图片image2.0（洗图）_2068205383113592833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Gemini 3 Pro图片反推+自定义定向修改提示词+全能图片image2.0（洗图）_2068205383113592833.json
hash: eb5c429f095aee3a
coverage: 0.636364
learned_at: 2026-10-23 11:02:46
nodes: [RH_Captioner_Pro, easy showAnything, PrimitiveNode, PrimitiveNode, RH_RhartImageG2TextToImage, Image Comparer (rgthree), SaveImage, ImageReceiver, ImageSender, LoadImage, Text]
patterns: []
missing: []
---

# 图片生成/图生图/Gemini 3 Pro图片反推+自定义定向修改提示词+全能图片image2.0（洗图）_2068205383113592833.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Gemini 3 Pro图片反推+自定义定向修改提示词+全能图片image2.0（洗图）_2068205383113592833.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（11 个）：
- `RH_Captioner_Pro`
- `easy showAnything`
- `PrimitiveNode`
- `PrimitiveNode`
- `RH_RhartImageG2TextToImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `ImageReceiver`
- `ImageSender`
- `LoadImage`
- `Text`

## 知识

覆盖率 **64%**（7/11）

**有卡**：`RH_Captioner_Pro`、`RH_RhartImageG2TextToImage`、`SaveImage`、`ImageReceiver`、`ImageSender`、`LoadImage`、`Text`

**用到的条目**：LoadImage、SaveImage、RH_RhartImageG2TextToImage、Text、RH_Captioner_Pro、ImageReceiver、ImageSender、sd15-t2i-basic
