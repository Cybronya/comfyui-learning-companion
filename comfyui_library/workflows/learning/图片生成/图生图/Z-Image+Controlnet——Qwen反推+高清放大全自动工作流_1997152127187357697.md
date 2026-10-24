---
key: 图片生成/图生图/Z-Image+Controlnet——Qwen反推+高清放大全自动工作流_1997152127187357697.json
name: Z-Image+Controlnet——Qwen反推+高清放大全自动工作流_1997152127187357697
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Z-Image+Controlnet——Qwen反推+高清放大全自动工作流_1997152127187357697.json
hash: a83d26124b8d8742
coverage: 0.851064
learned_at: 2026-10-23 11:29:27
nodes: [LayerUtility: ColorImage V2, DepthAnythingV2Preprocessor, PreviewImage, LayerUtility: ImageRemoveAlpha, LayerMask: BiRefNetUltraV2, LayerMask: LoadBiRefNetModelV2, SaveImage, SaveImage, CR Prompt Text, LayerUtility: ImageScaleByAspectRatio V2, TTP_Image_Tile_Batch, ImageScale, ImageCASharpening+, TTP_Image_Assy, ImageCASharpening+, SaveImage, EmptyLatentImage, CLIPTextEncode, ModelSamplingAuraFlow, ImageConcatMulti, SDPoseOODLoader, SDPoseOODProcessor, VAEDecode, ColorMatch, SeedVR2, easy cleanGpuUsed, ShowText|pysssss, AILab_QwenVL, LoadImage, GetImageSizeAndCount, ImageScaleToTotalPixels, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, Any Switch (rgthree), PreviewImage, ModelPatchLoader, Fast Groups Bypasser (rgthree), QwenImageDiffsynthControlnet, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, easy cleanGpuUsed, KSampler, Seed (rgthree), LayerUtility: ImageBlend, ConditioningZeroOut]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 750806643784704, "steps": 10, "width": 1024}
---

# 图片生成/图生图/Z-Image+Controlnet——Qwen反推+高清放大全自动工作流_1997152127187357697.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Z-Image+Controlnet——Qwen反推+高清放大全自动工作流_1997152127187357697.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（47 个）：
- `LayerUtility: ColorImage V2`
- `DepthAnythingV2Preprocessor`
- `PreviewImage`
- `LayerUtility: ImageRemoveAlpha`
- `LayerMask: BiRefNetUltraV2`
- `LayerMask: LoadBiRefNetModelV2`
- `SaveImage`
- `SaveImage`
- `CR Prompt Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TTP_Image_Tile_Batch`
- `ImageScale`
- `ImageCASharpening+`
- `TTP_Image_Assy`
- `ImageCASharpening+`
- `SaveImage`
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `ImageConcatMulti`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `VAEDecode` ★核心
- `ColorMatch`
- `SeedVR2`
- `easy cleanGpuUsed`
- `ShowText|pysssss`
- `AILab_QwenVL`
- `LoadImage`
- `GetImageSizeAndCount`
- `ImageScaleToTotalPixels`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `Any Switch (rgthree)`
- `PreviewImage`
- `ModelPatchLoader`
- `Fast Groups Bypasser (rgthree)`
- `QwenImageDiffsynthControlnet`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `Seed (rgthree)`
- `LayerUtility: ImageBlend`
- `ConditioningZeroOut`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `750806643784704`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（40/47）

**有卡**：`LayerUtility: ColorImage V2`、`DepthAnythingV2Preprocessor`、`LayerUtility: ImageRemoveAlpha`、`LayerMask: BiRefNetUltraV2`、`LayerMask: LoadBiRefNetModelV2`、`SaveImage`、`CR Prompt Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`TTP_Image_Tile_Batch`、`ImageScale`、`ImageCASharpening+`、`TTP_Image_Assy`、`EmptyLatentImage`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`ImageConcatMulti`、`SDPoseOODLoader`、`SDPoseOODProcessor`、`VAEDecode`、`ColorMatch`、`SeedVR2`、`easy cleanGpuUsed`、`AILab_QwenVL`、`LoadImage`、`GetImageSizeAndCount`、`ImageScaleToTotalPixels`、`ModelPatchLoader`、`QwenImageDiffsynthControlnet`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`KSampler`、`Seed (rgthree)`、`LayerUtility: ImageBlend`、`ConditioningZeroOut`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、LoadImage
