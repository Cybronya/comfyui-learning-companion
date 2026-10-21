---
key: 图片生成/文生图/图片生成_illustration_QwenEdit_ZImage_(动漫转真人)_2018682887188520962.json
name: 图片生成_illustration_QwenEdit_ZImage_(动漫转真人)_2018682887188520962
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/图片生成_illustration_QwenEdit_ZImage_(动漫转真人)_2018682887188520962.json
hash: 2e09f1e68e9e9a8a
coverage: 0.659341
learned_at: 2026-10-19 22:30:28
nodes: [ImageUpscaleWithModel, KSampler, SetNode, SetNode, SetNode, CLIPTextEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, PreviewAny, GetNode, CLIPTextEncode, SetNode, EmptyLatentImage, VAEDecode, Reroute, PreviewImage, VAEEncodeTiled, KSampler, Reroute, VAEDecodeTiled, CFGNorm, ModelSamplingAuraFlow, Image Comparer (rgthree), VAEDecode, VAEEncode, ModelSamplingAuraFlow, Note, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, Note, CFGNorm, MarkdownNote, VAEDecode, GetImageSizeAndCount, TextEncodeQwenImageEditPlus, GetImageSizeAndCount, ImageScaleToTotalPixels, ReferenceLatent, VAEDecode, ReferenceLatent, VAEEncode, SetNode, Image Comparer (rgthree), FluxKontextImageScale, Reroute, TextEncodeQwenImageEditPlus, ReferenceLatent, VAEEncode, ReferenceLatent, ConditioningZeroOut, KSampler, Reroute, FluxKontextImageScale, ImageScaleToTotalPixels, KSampler, Note, GetImageSizeAndCount, GetImageSizeAndCount, easy int, KSamplerAdvanced, VAEDecode, ImageScaleToTotalPixels, CLIPTextEncode, CLIPTextEncode, CLIPTextEncode, easy int, ImageScaleToTotalPixels, CLIPTextEncode, KSamplerAdvanced, easy seed, easy int, KSamplerAdvanced, KSamplerAdvanced, ReferenceLatent, ReferenceLatent, VAEEncode, KSamplerAdvanced, Image Comparer (rgthree), Image Comparer (rgthree), VAEDecode, VAEDecode, Reroute, easy int, easy seed, Reroute, VAEDecode, Image Comparer (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), KSamplerAdvanced, Reroute, Reroute, Reroute, Image Comparer (rgthree), CLIPTextEncode, Reroute, UpscaleModelLoader, Note, Reroute, Reroute, Reroute, Reroute, Reroute, ImageConcanate, ImageScaleToMaxDimension, Image Comparer (rgthree), Note, ImageConcanate, Reroute, ImageConcanate, Reroute, Image Comparer (rgthree), SaveImage, SeedVR2LoadVAEModel, Reroute, Reroute, Reroute, SaveImage, ImageBatchMulti, GetImageSizeAndCount, ImageScaleToMaxDimension, Image Comparer (rgthree), Image Comparer (rgthree), Image Comparer (rgthree), CheckpointLoaderSimple, LoadImage, StringConcatenate, WD14Tagger|pysssss, UpscaleModelLoader, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, Note, CLIPLoader, VAELoader, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, VAELoader, CLIPLoader, UNETLoader, VRAMReserver, KSamplerAdvanced, CLIPLoader, LoraLoaderModelOnly, VAELoader, LoraLoaderModelOnly, UnetLoaderGGUF, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, VAEEncode, CLIPTextEncode, TextEncodeQwenImageEditPlus, Reroute, Reroute, VAELoader, VRAMReserver, VRAMReserver, LoraLoaderModelOnly, CLIPLoader, UNETLoader, CLIPLoader, UNETLoader, VAELoader, Reroute, LoraLoaderModelOnly, Reroute, Reroute, AILab_ImagePreview, Reroute, TextEncodeQwenImageEditPlus, CLIPTextEncode, CLIPTextEncode, LoraLoaderModelOnly, UltimateSDUpscale]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "new_waiIllustriousSDXL_v160.safetensors", "denoise": "kl_optimal", "height": 1536, "sampler_name": 1, "scheduler": "euler_ancestral", "seed": "enable", "steps": "randomize", "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/图片生成_illustration_QwenEdit_ZImage_(动漫转真人)_2018682887188520962.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/图片生成_illustration_QwenEdit_ZImage_(动漫转真人)_2018682887188520962.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（182 个）：
- `ImageUpscaleWithModel`
- `KSampler` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewAny`
- `GetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `PreviewImage`
- `VAEEncodeTiled` ★核心
- `KSampler` ★核心
- `Reroute`
- `VAEDecodeTiled` ★核心
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `VAEEncode` ★核心
- `ModelSamplingAuraFlow`
- `Note`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `Note`
- `CFGNorm`
- `MarkdownNote`
- `VAEDecode` ★核心
- `GetImageSizeAndCount`
- `TextEncodeQwenImageEditPlus`
- `GetImageSizeAndCount`
- `ImageScaleToTotalPixels`
- `ReferenceLatent`
- `VAEDecode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `SetNode`
- `Image Comparer (rgthree)`
- `FluxKontextImageScale`
- `Reroute`
- `TextEncodeQwenImageEditPlus`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `KSampler` ★核心
- `Reroute`
- `FluxKontextImageScale`
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `Note`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `easy int`
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy int`
- `ImageScaleToTotalPixels`
- `CLIPTextEncode` ★核心
- `KSamplerAdvanced` ★核心
- `easy seed`
- `easy int`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `KSamplerAdvanced` ★核心
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `Reroute`
- `easy int`
- `easy seed`
- `Reroute`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `KSamplerAdvanced` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `Reroute`
- `UpscaleModelLoader`
- `Note`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageConcanate`
- `ImageScaleToMaxDimension`
- `Image Comparer (rgthree)`
- `Note`
- `ImageConcanate`
- `Reroute`
- `ImageConcanate`
- `Reroute`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SeedVR2LoadVAEModel`
- `Reroute`
- `Reroute`
- `Reroute`
- `SaveImage`
- `ImageBatchMulti`
- `GetImageSizeAndCount`
- `ImageScaleToMaxDimension`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `StringConcatenate`
- `WD14Tagger|pysssss`
- `UpscaleModelLoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VRAMReserver`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `Reroute`
- `Reroute`
- `VAELoader`
- `VRAMReserver`
- `VRAMReserver`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `Reroute`
- `Reroute`
- `AILab_ImagePreview`
- `Reroute`
- `TextEncodeQwenImageEditPlus`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `UltimateSDUpscale`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler_ancestral`
- `denoise` = `kl_optimal`
- `width` = `768`
- `height` = `1536`
- `batch_size` = `1`
- `checkpoint` = `new_waiIllustriousSDXL_v160.safetensors`

## 知识

覆盖率 **66%**（120/182）

**有卡**：`ImageUpscaleWithModel`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`VAEDecode`、`VAEEncodeTiled`、`VAEDecodeTiled`、`CFGNorm`、`ModelSamplingAuraFlow`、`VAEEncode`、`FluxKontextMultiReferenceLatentMethod`、`GetImageSizeAndCount`、`TextEncodeQwenImageEditPlus`、`ImageScaleToTotalPixels`、`ReferenceLatent`、`FluxKontextImageScale`、`ConditioningZeroOut`、`easy int`、`KSamplerAdvanced`、`easy seed`、`UpscaleModelLoader`、`ImageConcanate`、`ImageScaleToMaxDimension`、`SaveImage`、`SeedVR2LoadVAEModel`、`ImageBatchMulti`、`CheckpointLoaderSimple`、`LoadImage`、`StringConcatenate`、`WD14Tagger|pysssss`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`VRAMReserver`、`UnetLoaderGGUF`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`AILab_ImagePreview`、`UltimateSDUpscale`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
