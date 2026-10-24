---
key: 图片生成/图生图/flux-fill-dev-OneReward-扩图-按比例_2082040121574117378.json
name: flux-fill-dev-OneReward-扩图-按比例_2082040121574117378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/flux-fill-dev-OneReward-扩图-按比例_2082040121574117378.json
hash: 7ce18a616af52a0d
coverage: 0.853659
learned_at: 2026-10-23 11:35:38
nodes: [Image Comparer (rgthree), ConditioningZeroOut, SimpleMath+, SimpleMath+, SimpleMath+, SimpleMath+, ImageScale, LayerMask: MaskGrow, ImageUpscaleWithModel, UpscaleModelLoader, GetImageSize, Florence2ModelLoader, Florence2Run, LayerUtility: ImageMaskScaleAsV2, ImageScaleToTotalPixelsX, CLIPTextEncodeFlux, InpaintModelConditioning, KSampler, VAEDecode, UNETLoader, VAELoader, DualCLIPLoader, GetImageSize, ImagePadForOutpaint, easy imageSizeBySide, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, PreviewImage, Reroute, SeedVR2LoadVAEModel, PreviewImage, Fast Groups Bypasser (rgthree), Note, SimpleMathFloat+, SimpleMathFloat+, SimpleMathFloat+, SimpleMathFloat+, Seed (rgthree), LayerUtility: ImageBlend, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "beta", "seed": 13305, "steps": 20}
---

# 图片生成/图生图/flux-fill-dev-OneReward-扩图-按比例_2082040121574117378.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/flux-fill-dev-OneReward-扩图-按比例_2082040121574117378.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（41 个）：
- `Image Comparer (rgthree)`
- `ConditioningZeroOut`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `ImageScale`
- `LayerMask: MaskGrow`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `GetImageSize`
- `Florence2ModelLoader`
- `Florence2Run`
- `LayerUtility: ImageMaskScaleAsV2`
- `ImageScaleToTotalPixelsX`
- `CLIPTextEncodeFlux` ★核心
- `InpaintModelConditioning`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `GetImageSize`
- `ImagePadForOutpaint`
- `easy imageSizeBySide`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `PreviewImage`
- `Reroute`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `SimpleMathFloat+`
- `SimpleMathFloat+`
- `SimpleMathFloat+`
- `SimpleMathFloat+`
- `Seed (rgthree)`
- `LayerUtility: ImageBlend`
- `SaveImage`
- `LoadImage`

## 关键参数

- `seed` = `13305`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `res_multistep`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **85%**（35/41）

**有卡**：`ConditioningZeroOut`、`SimpleMath+`、`ImageScale`、`LayerMask: MaskGrow`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`GetImageSize`、`Florence2ModelLoader`、`Florence2Run`、`LayerUtility: ImageMaskScaleAsV2`、`ImageScaleToTotalPixelsX`、`CLIPTextEncodeFlux`、`InpaintModelConditioning`、`KSampler`、`VAEDecode`、`UNETLoader`、`VAELoader`、`DualCLIPLoader`、`ImagePadForOutpaint`、`easy imageSizeBySide`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`SimpleMathFloat+`、`Seed (rgthree)`、`LayerUtility: ImageBlend`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、ConditioningZeroOut、LoadImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel
