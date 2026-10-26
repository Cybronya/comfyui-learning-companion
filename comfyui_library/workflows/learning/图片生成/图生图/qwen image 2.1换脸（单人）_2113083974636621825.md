---
key: 图片生成/图生图/qwen image 2.1换脸（单人）_2113083974636621825.json
name: qwen image 2.1换脸（单人）_2113083974636621825
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen image 2.1换脸（单人）_2113083974636621825.json
hash: 7376252343ca5704
coverage: 0.617647
learned_at: 2026-10-26 22:04:15
nodes: [GetImageSize, LayerUtility: ColorImage, GetNode, MaskPreview+, 取色器_孤海, PreviewImage, SetNode, GetNode, LayerUtility: ImageBlend, SetNode, LayerMask: MaskGrow, GetNode, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, CLIPLoader, CLIPLoader, VAELoader, KSampler, QwenImage21Cache, VAEDecode, SaveImage, PrimitiveStringMultiline, GetNode, Image Comparer (rgthree), SetNode, GetNode, BatchImagesNode, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LayerMask: SegmentAnythingUltra V2, LoadImage, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 68, "steps": 40}
---

# 图片生成/图生图/qwen image 2.1换脸（单人）_2113083974636621825.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen image 2.1换脸（单人）_2113083974636621825.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `GetImageSize`
- `LayerUtility: ColorImage`
- `GetNode`
- `MaskPreview+`
- `取色器_孤海`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageBlend`
- `SetNode`
- `LayerMask: MaskGrow`
- `GetNode`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `SaveImage`
- `PrimitiveStringMultiline`
- `GetNode`
- `Image Comparer (rgthree)`
- `SetNode`
- `GetNode`
- `BatchImagesNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LayerMask: SegmentAnythingUltra V2`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`

## 关键参数

- `seed` = `68`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **62%**（21/34）

**有卡**：`GetImageSize`、`LayerUtility: ColorImage`、`MaskPreview+`、`取色器_孤海`、`LayerUtility: ImageBlend`、`LayerMask: MaskGrow`、`TextEncodeQwenImage21`、`TextGenerateLTX2Prompt`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`QwenImage21Cache`、`VAEDecode`、`SaveImage`、`BatchImagesNode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerMask: SegmentAnythingUltra V2`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
