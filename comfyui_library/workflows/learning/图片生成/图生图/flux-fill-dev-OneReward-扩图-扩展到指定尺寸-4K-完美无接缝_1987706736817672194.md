---
key: 图片生成/图生图/flux-fill-dev-OneReward-扩图-扩展到指定尺寸-4K-完美无接缝_1987706736817672194.json
name: flux-fill-dev-OneReward-扩图-扩展到指定尺寸-4K-完美无接缝_1987706736817672194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux-fill-dev-OneReward-扩图-扩展到指定尺寸-4K-完美无接缝_1987706736817672194.json
hash: 184ca40bcfd39784
coverage: 0.820513
learned_at: 2026-10-23 11:35:37
nodes: [ImageUpscaleWithModel, VAELoader, ImageScale, DifferentialDiffusion, Anything Everywhere3, CLIPTextEncodeFlux, ConditioningZeroOut, InpaintModelConditioning, MaskPreview, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, DifferentialDiffusion, InpaintModelConditioning, easy imageSize, LayerColor: Brightness & Contrast, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, easy imageSize, KSampler, Reroute, PreviewImage, Note, ImagePadForOutpaintTargetSize, LayerMask: MaskGrow, KSampler, PreviewBridge, Florence2Run, ShowText|pysssss, Image Comparer (rgthree), LoadImage, Florence2ModelLoader, UNETLoader, DualCLIPLoader, UNETLoader, ResizeMask, Image Comparer (rgthree), UpscaleModelLoader, LayerUtility: ImageBlend, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 12756, "steps": 20}
---

# 图片生成/图生图/flux-fill-dev-OneReward-扩图-扩展到指定尺寸-4K-完美无接缝_1987706736817672194.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux-fill-dev-OneReward-扩图-扩展到指定尺寸-4K-完美无接缝_1987706736817672194.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（39 个）：
- `ImageUpscaleWithModel`
- `VAELoader`
- `ImageScale`
- `DifferentialDiffusion`
- `Anything Everywhere3`
- `CLIPTextEncodeFlux` ★核心
- `ConditioningZeroOut`
- `InpaintModelConditioning`
- `MaskPreview`
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DifferentialDiffusion`
- `InpaintModelConditioning`
- `easy imageSize`
- `LayerColor: Brightness & Contrast`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `easy imageSize`
- `KSampler` ★核心
- `Reroute`
- `PreviewImage`
- `Note`
- `ImagePadForOutpaintTargetSize`
- `LayerMask: MaskGrow`
- `KSampler` ★核心
- `PreviewBridge`
- `Florence2Run`
- `ShowText|pysssss`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Florence2ModelLoader`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `ResizeMask`
- `Image Comparer (rgthree)`
- `UpscaleModelLoader`
- `LayerUtility: ImageBlend`
- `SaveImage`

## 关键参数

- `seed` = `12756`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（32/39）

**有卡**：`ImageUpscaleWithModel`、`VAELoader`、`ImageScale`、`DifferentialDiffusion`、`CLIPTextEncodeFlux`、`ConditioningZeroOut`、`InpaintModelConditioning`、`MaskPreview`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy imageSize`、`LayerColor: Brightness & Contrast`、`KSampler`、`ImagePadForOutpaintTargetSize`、`LayerMask: MaskGrow`、`PreviewBridge`、`Florence2Run`、`LoadImage`、`Florence2ModelLoader`、`UNETLoader`、`DualCLIPLoader`、`ResizeMask`、`UpscaleModelLoader`、`LayerUtility: ImageBlend`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、ConditioningZeroOut、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、CLIPTextEncodeFlux
