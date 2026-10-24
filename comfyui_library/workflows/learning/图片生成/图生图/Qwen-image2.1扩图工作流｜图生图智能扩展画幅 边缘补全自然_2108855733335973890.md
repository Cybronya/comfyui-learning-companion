---
key: 图片生成/图生图/Qwen-image2.1扩图工作流｜图生图智能扩展画幅 边缘补全自然_2108855733335973890.json
name: Qwen-image2.1扩图工作流｜图生图智能扩展画幅 边缘补全自然_2108855733335973890
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1扩图工作流｜图生图智能扩展画幅 边缘补全自然_2108855733335973890.json
hash: 3caa62efcb6b39cc
coverage: 0.75
learned_at: 2026-10-23 11:18:30
nodes: [KSampler, UNETLoader, CLIPLoader, VAELoader, DrawMaskOnImage, LayerUtility: ImageScaleByAspectRatio V2, easy forLoopStart, PrimitiveInt, PrimitiveStringMultiline, TextEncodeQwenImage21, LoadImage, PreviewImage, SaveImage, easy forLoopEnd, VAEDecode, ImagePadForOutpaint, easy imageColorMatch, LoadImage, LoadImage, ImagePadForOutpaint, LayerColor: ColorAdapter, Image Comparer (rgthree), PreviewImage, Image Comparer (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 1054153900772662, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1扩图工作流｜图生图智能扩展画幅 边缘补全自然_2108855733335973890.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1扩图工作流｜图生图智能扩展画幅 边缘补全自然_2108855733335973890.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `DrawMaskOnImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy forLoopStart`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `TextEncodeQwenImage21`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `easy forLoopEnd`
- `VAEDecode` ★核心
- `ImagePadForOutpaint`
- `easy imageColorMatch`
- `LoadImage`
- `LoadImage`
- `ImagePadForOutpaint`
- `LayerColor: ColorAdapter`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `Image Comparer (rgthree)`

## 关键参数

- `seed` = `1054153900772662`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **75%**（18/24）

**有卡**：`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`DrawMaskOnImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy forLoopStart`、`TextEncodeQwenImage21`、`LoadImage`、`SaveImage`、`easy forLoopEnd`、`VAEDecode`、`ImagePadForOutpaint`、`easy imageColorMatch`、`LayerColor: ColorAdapter`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、LayerColor: ColorAdapter
