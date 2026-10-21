---
key: 图片生成/文生图/QwenImageEditt-RemixAIO图像编辑全功能｜局部重绘_2096308499755126785.json
name: QwenImageEditt-RemixAIO图像编辑全功能｜局部重绘_2096308499755126785
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QwenImageEditt-RemixAIO图像编辑全功能｜局部重绘_2096308499755126785.json
hash: 261f45486d788d55
coverage: 0.766871
learned_at: 2026-10-20 01:19:28
nodes: [LayerUtility: ImageReelComposit, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), LayerUtility: ImageReel, InpaintModelConditioning, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, Image Comparer (rgthree), ReferenceLatent, ConditioningZeroOut, ConditioningZeroOut, ReferenceLatent, VAEDecode, LayerUtility: ImageReel, ConditioningZeroOut, ControlNetInpaintingAliMamaApply, VAEDecode, KSampler, MaskPreview+, Seed (rgthree), KSampler, LayerUtility: ImageReel, easy setNode, easy setNode, easy setNode, easy setNode, easy setNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), VAEDecode, PreviewImage, easy setNode, VAEDecode, PreviewImage, VAEDecode, SaveImage, SaveImage, KSampler, LayerUtility: ImageReelComposit, Seed (rgthree), LayerUtility: ImageReelComposit, PreviewImage, SaveImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, Fast Groups Bypasser (rgthree), LayerUtility: ImageScaleByAspectRatio V2, Seed (rgthree), easy getNode, EmptyLatentImage, KSampler, Seed (rgthree), KSampler, TextEncodeQwenImageEditPlusAdvance_lrzjason, Seed (rgthree), Fast Groups Bypasser (rgthree), LoadImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, Fast Groups Bypasser (rgthree), LayerUtility: ImageScaleByAspectRatio V2, ImagePadForOutpaint, LoadImage, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, SDPoseKeypointExtractor, PreviewImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, Seed (rgthree), LayerUtility: ImageReelComposit, LayerUtility: ImageReel, SaveImage, SDPoseDrawKeypoints, Switch image [Crystools], Fast Groups Bypasser (rgthree), Image Comparer (rgthree), LoadImage, LoadImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), TextEncodeQwenImageEditPlusAdvance_lrzjason, ConditioningZeroOut, PreviewImage, ConditioningZeroOut, KSampler, SaveImage, ConditioningZeroOut, TextEncodeQwenImageEditPlusAdvance_lrzjason, Mask Fill Holes, LayerMask: MaskGrow, Fast Groups Bypasser (rgthree), ControlNetLoader, CheckpointLoaderSimple, AIO_Preprocessor, UNETLoader, Anything Everywhere3, Anything Everywhere3, Anything Everywhere3, Fast Groups Bypasser (rgthree), Any Switch (rgthree), Image Comparer (rgthree), SaveImage, SeedVR2VideoUpscaler, Fast Groups Bypasser (rgthree), CheckpointLoaderSimple, CheckpointLoaderSimple, LoraLoaderModelOnly, CLIPLoader, VAELoader, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, LoadImage, SaveImage, PreviewImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "Qwen-Image-Edit-Remix-AIO.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/QwenImageEditt-RemixAIO图像编辑全功能｜局部重绘_2096308499755126785.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QwenImageEditt-RemixAIO图像编辑全功能｜局部重绘_2096308499755126785.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（163 个）：
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageReel`
- `InpaintModelConditioning`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `Image Comparer (rgthree)`
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `ConditioningZeroOut`
- `ControlNetInpaintingAliMamaApply`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `MaskPreview+`
- `Seed (rgthree)`
- `KSampler` ★核心
- `LayerUtility: ImageReel`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `VAEDecode` ★核心
- `PreviewImage`
- `easy setNode`
- `VAEDecode` ★核心
- `PreviewImage`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `KSampler` ★核心
- `LayerUtility: ImageReelComposit`
- `Seed (rgthree)`
- `LayerUtility: ImageReelComposit`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Seed (rgthree)`
- `easy getNode`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `Seed (rgthree)`
- `KSampler` ★核心
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `Seed (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `Fast Groups Bypasser (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImagePadForOutpaint`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SDPoseKeypointExtractor`
- `PreviewImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `Seed (rgthree)`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `SaveImage`
- `SDPoseDrawKeypoints`
- `Switch image [Crystools]`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `ConditioningZeroOut`
- `PreviewImage`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `SaveImage`
- `ConditioningZeroOut`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `Mask Fill Holes`
- `LayerMask: MaskGrow`
- `Fast Groups Bypasser (rgthree)`
- `ControlNetLoader`
- `CheckpointLoaderSimple` ★核心
- `AIO_Preprocessor`
- `UNETLoader` ★核心
- `Anything Everywhere3`
- `Anything Everywhere3`
- `Anything Everywhere3`
- `Fast Groups Bypasser (rgthree)`
- `Any Switch (rgthree)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `Fast Groups Bypasser (rgthree)`
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `LoadImage`
- `SaveImage`
- `PreviewImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `checkpoint` = `Qwen-Image-Edit-Remix-AIO.safetensors`

## 知识

覆盖率 **77%**（125/163）

**有卡**：`LayerUtility: ImageReelComposit`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageReel`、`InpaintModelConditioning`、`ReferenceLatent`、`ConditioningZeroOut`、`VAEDecode`、`ControlNetInpaintingAliMamaApply`、`KSampler`、`MaskPreview+`、`Seed (rgthree)`、`easy setNode`、`easy getNode`、`SaveImage`、`EmptyLatentImage`、`TextEncodeQwenImageEditPlusAdvance_lrzjason`、`LoadImage`、`ImagePadForOutpaint`、`SDPoseKeypointExtractor`、`SDPoseDrawKeypoints`、`Switch image [Crystools]`、`Mask Fill Holes`、`LayerMask: MaskGrow`、`ControlNetLoader`、`CheckpointLoaderSimple`、`AIO_Preprocessor`、`UNETLoader`、`SeedVR2VideoUpscaler`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`SeedVR2LoadDiTModel`、`SeedVR2LoadVAEModel`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 6 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
