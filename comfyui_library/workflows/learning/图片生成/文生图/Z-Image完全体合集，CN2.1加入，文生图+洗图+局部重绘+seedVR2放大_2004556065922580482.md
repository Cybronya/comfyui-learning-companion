---
key: 图片生成/文生图/Z-Image完全体合集，CN2.1加入，文生图+洗图+局部重绘+seedVR2放大_2004556065922580482.json
name: Z-Image完全体合集，CN2.1加入，文生图+洗图+局部重绘+seedVR2放大_2004556065922580482
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-Image完全体合集，CN2.1加入，文生图+洗图+局部重绘+seedVR2放大_2004556065922580482.json
hash: ac40ba581188ec93
coverage: 0.80303
learned_at: 2026-10-19 22:01:02
nodes: [LayerUtility: ImageReelComposit, PreviewImage, Image Comparer (rgthree), LayerUtility: ImageReel, ModelPatchLoader, easy setNode, easy getNode, easy setNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), VAEDecode, Fast Groups Bypasser (rgthree), easy setNode, easy getNode, easy getNode, SaveImage, SaveImage, Image Comparer (rgthree), PreviewImage, Image Comparer (rgthree), GrowMask, Mask Fill Holes, MaskPreview+, easy getNode, AIO_Preprocessor, Qwen3_VQA, ShowText|pysssss, Anything Everywhere3, RH_LLMAPI_NODE, easy showAnything, UNETLoader, VAELoader, CLIPLoader, LayerUtility: ImageScaleByAspectRatio V2, EmptyLatentImage, LoadImage, Text Multiline, VAEDecode, CLIPTextEncode, ConditioningZeroOut, KSamplerAdvanced, ZImageFunControlnet, ConditioningZeroOut, CLIPTextEncode, ConditioningZeroOut, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, VAEEncode, KSamplerAdvanced, KSamplerAdvanced, easy setNode, ShowText|pysssss, easy clearCacheAll, Fast Groups Bypasser (rgthree), KSamplerAdvanced, SaveImage, MuyeTextEditOutput, VAEDecode, ModelPatchLoader, KSamplerAdvanced, CLIPTextEncode, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, ZImageFunControlnet, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 4, "cfg": 8, "denoise": "simple", "height": 1536, "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize", "width": 864}
---

# 图片生成/文生图/Z-Image完全体合集，CN2.1加入，文生图+洗图+局部重绘+seedVR2放大_2004556065922580482.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-Image完全体合集，CN2.1加入，文生图+洗图+局部重绘+seedVR2放大_2004556065922580482.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（66 个）：
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageReel`
- `ModelPatchLoader`
- `easy setNode`
- `easy getNode`
- `easy setNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `SaveImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `GrowMask`
- `Mask Fill Holes`
- `MaskPreview+`
- `easy getNode`
- `AIO_Preprocessor`
- `Qwen3_VQA`
- `ShowText|pysssss`
- `Anything Everywhere3`
- `RH_LLMAPI_NODE`
- `easy showAnything`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `Text Multiline`
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSamplerAdvanced` ★核心
- `ZImageFunControlnet`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `VAEEncode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `easy setNode`
- `ShowText|pysssss`
- `easy clearCacheAll`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerAdvanced` ★核心
- `SaveImage`
- `MuyeTextEditOutput`
- `VAEDecode` ★核心
- `ModelPatchLoader`
- `KSamplerAdvanced` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ZImageFunControlnet`
- `LoadImage`

## 关键参数

- `width` = `864`
- `height` = `1536`
- `batch_size` = `4`
- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `simple`

## 知识

覆盖率 **80%**（53/66）

**有卡**：`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`ModelPatchLoader`、`easy setNode`、`easy getNode`、`VAEDecode`、`SaveImage`、`GrowMask`、`Mask Fill Holes`、`MaskPreview+`、`AIO_Preprocessor`、`Qwen3_VQA`、`RH_LLMAPI_NODE`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLatentImage`、`LoadImage`、`Text Multiline`、`CLIPTextEncode`、`ConditioningZeroOut`、`KSamplerAdvanced`、`ZImageFunControlnet`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`VAEEncode`、`easy clearCacheAll`、`MuyeTextEditOutput`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、SaveImage、EmptyLatentImage、LoadImage
