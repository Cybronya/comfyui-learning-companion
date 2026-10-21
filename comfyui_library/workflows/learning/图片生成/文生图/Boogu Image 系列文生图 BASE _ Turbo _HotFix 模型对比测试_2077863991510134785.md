---
key: 图片生成/文生图/Boogu Image 系列文生图 BASE _ Turbo _HotFix 模型对比测试_2077863991510134785.json
name: Boogu Image 系列文生图 BASE _ Turbo _HotFix 模型对比测试_2077863991510134785
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Boogu Image 系列文生图 BASE _ Turbo _HotFix 模型对比测试_2077863991510134785.json
hash: 85ddbd798d9e77aa
coverage: 0.937799
learned_at: 2026-10-20 00:18:52
nodes: [KSampler, KSampler, KSampler, SamplerCustomAdvanced, ReferenceLatent, ReferenceLatent, RandomNoise, VAEEncode, CLIPTextEncode, CLIPTextEncode, easy int, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, EmptyFlux2LatentImage, SamplerCustomAdvanced, ReferenceLatent, ReferenceLatent, RandomNoise, VAEEncode, CLIPTextEncode, CLIPTextEncode, easy int, Flux2Scheduler, KSamplerSelect, EmptyFlux2LatentImage, SamplerCustomAdvanced, ReferenceLatent, ReferenceLatent, VAEEncode, CLIPTextEncode, CLIPTextEncode, easy int, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, EmptyFlux2LatentImage, SamplerCustomAdvanced, ReferenceLatent, ReferenceLatent, RandomNoise, VAEEncode, CLIPTextEncode, CLIPTextEncode, easy int, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, EmptyFlux2LatentImage, RandomNoise, VAEDecode, VAEDecode, VAEDecode, SaveImage, SaveImage, CR Prompt Text, SaveImage, PreviewImage, CR Prompt Text, SaveImage, PreviewImage, SaveImage, SamplerCustomAdvanced, ReferenceLatent, ReferenceLatent, RandomNoise, VAEEncode, CLIPTextEncode, CLIPTextEncode, easy int, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, EmptyFlux2LatentImage, VAEDecode, CR Prompt Text, SaveImage, SaveImage, PreviewImage, PreviewImage, CR Prompt Text, CR Prompt Text, VAEDecode, VAEDecode, VAEDecode, ImageColorMatch+, ImageColorMatch+, ImageColorMatch+, LayerColor: Brightness & Contrast, ImageColorMatch+, ImageColorMatch+, PreviewImage, SaveImage, SaveImage, SaveImage, KSampler, CLIPTextEncode, KSampler, CLIPTextEncode, ConditioningZeroOut, CLIPTextEncode, KSampler, SaveImage, SamplerCustomAdvanced, ReferenceLatent, ReferenceLatent, RandomNoise, VAEEncode, CLIPTextEncode, CLIPTextEncode, easy int, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, EmptyFlux2LatentImage, VAEDecode, CR Prompt Text, SaveImage, PreviewImage, SamplerCustomAdvanced, ReferenceLatent, ReferenceLatent, RandomNoise, VAEEncode, CLIPTextEncode, CLIPTextEncode, easy int, Flux2Scheduler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, EmptyFlux2LatentImage, VAEDecode, SaveImage, PreviewImage, SaveImage, ImageColorMatch+, ImageColorMatch+, PreviewImage, VAEDecode, VAEDecode, PreviewImage, LayerUtility: ImageReel, LayerUtility: ImageReel, MarkdownNote, EmptyLatentImage, LoadImage, LoadImage, MarkdownNote, PixaromaLabel, PixaromaLabel, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, UNETLoader, CR Prompt Text, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, UNETLoader, VAELoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAEDecode, VAELoader, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, JanusModelLoader, PreviewImage, ShowText|pysssss, CFGGuider, CFGGuider, CFGGuider, CFGGuider, CFGGuider, CFGGuider, CFGGuider, KSampler, HFEPostProcessor (lrzjason), LayerUtility: ImageReel, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageReelComposit, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, VAEDecode, KSampler, LoadImage, JanusImageUnderstanding, UNETLoader]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "lcm", "scheduler": "sgm_uniform", "seed": 48887194592853, "steps": 4, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Boogu Image 系列文生图 BASE _ Turbo _HotFix 模型对比测试_2077863991510134785.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Boogu Image 系列文生图 BASE _ Turbo _HotFix 模型对比测试_2077863991510134785.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（209 个）：
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `RandomNoise`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy int`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `RandomNoise`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy int`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy int`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `RandomNoise`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy int`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyFlux2LatentImage`
- `RandomNoise`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `CR Prompt Text`
- `SaveImage`
- `PreviewImage`
- `CR Prompt Text`
- `SaveImage`
- `PreviewImage`
- `SaveImage`
- `SamplerCustomAdvanced` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `RandomNoise`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy int`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyFlux2LatentImage`
- `VAEDecode` ★核心
- `CR Prompt Text`
- `SaveImage`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `CR Prompt Text`
- `CR Prompt Text`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `ImageColorMatch+`
- `ImageColorMatch+`
- `ImageColorMatch+`
- `LayerColor: Brightness & Contrast`
- `ImageColorMatch+`
- `ImageColorMatch+`
- `PreviewImage`
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `SamplerCustomAdvanced` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `RandomNoise`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy int`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyFlux2LatentImage`
- `VAEDecode` ★核心
- `CR Prompt Text`
- `SaveImage`
- `PreviewImage`
- `SamplerCustomAdvanced` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `RandomNoise`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy int`
- `Flux2Scheduler`
- `KSamplerSelect` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `EmptyFlux2LatentImage`
- `VAEDecode` ★核心
- `SaveImage`
- `PreviewImage`
- `SaveImage`
- `ImageColorMatch+`
- `ImageColorMatch+`
- `PreviewImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReel`
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `PixaromaLabel`
- `PixaromaLabel`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CR Prompt Text`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `JanusModelLoader`
- `PreviewImage`
- `ShowText|pysssss`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `CFGGuider`
- `KSampler` ★核心
- `HFEPostProcessor (lrzjason)`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReelComposit`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LoadImage`
- `JanusImageUnderstanding`
- `UNETLoader` ★核心

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `48887194592853`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `lcm`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（196/209）

**有卡**：`KSampler`、`SamplerCustomAdvanced`、`ReferenceLatent`、`RandomNoise`、`VAEEncode`、`CLIPTextEncode`、`easy int`、`Flux2Scheduler`、`KSamplerSelect`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyFlux2LatentImage`、`VAEDecode`、`SaveImage`、`CR Prompt Text`、`ImageColorMatch+`、`LayerColor: Brightness & Contrast`、`ConditioningZeroOut`、`LayerUtility: ImageReel`、`EmptyLatentImage`、`LoadImage`、`PixaromaLabel`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`JanusModelLoader`、`CFGGuider`、`HFEPostProcessor (lrzjason)`、`LayerUtility: ImageReelComposit`、`JanusImageUnderstanding`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 7 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
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
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
