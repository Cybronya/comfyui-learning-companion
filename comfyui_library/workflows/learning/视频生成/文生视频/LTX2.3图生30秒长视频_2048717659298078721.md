---
key: 视频生成/文生视频/LTX2.3图生30秒长视频_2048717659298078721.json
name: LTX2.3图生30秒长视频_2048717659298078721
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3图生30秒长视频_2048717659298078721.json
hash: 54e7ce5e2b991e7a
coverage: 0.557604
learned_at: 2026-10-15 22:45:06
nodes: [SetNode, SetNode, GetNode, PreviewImage, PreviewImage, ConditioningZeroOut, easy showAnything, SetNode, SetNode, SetNode, ImpactInt, SetNode, PreviewImage, ConditioningZeroOut, easy showAnything, GetNode, GetNode, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, GetNode, easy showAnything, ConditioningZeroOut, GetNode, TextEncodeQwenImageEditPlus, VAEEncode, easy showAnything, VAELoader, SetNode, SetNode, GetNode, GetNode, ManualSigmas, KSamplerSelect, CFGGuider, SamplerCustomAdvanced, GetNode, KSamplerSelect, LTXVScheduler, CFGGuider, RandomNoise, ComfyMathExpression, ComfyMathExpression, CLIPTextEncode, CLIPTextEncode, SetNode, GetNode, LTXVConcatAVLatent, SetNode, LTXVSeparateAVLatent, LTXVSeparateAVLatent, SamplerCustomAdvanced, ComfyMathExpression, SetNode, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, GetNode, easy showAnything, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, TrimAudioDuration, SetLatentNoiseMask, SolidMask, GetNode, VAEDecode, GetNode, VAEDecode, GetNode, LTXVConditioning, SetNode, EmptyLTXVLatentVideo, GetNode, VAEDecode, PrimitiveFloat, LTX2_NAG, GetNode, GetNode, GetNode, GetNode, LTXVChunkFeedForward, GetNode, SetNode, MathExpression|pysssss, LTXVEmptyLatentAudio, VHS_VideoCombine, GetNode, CLIPLoader, LatentUpscaleModelLoader, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, RandomNoise, ImpactInt, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecodeTiled, RTXVideoSuperResolution, easy promptLine, easy promptLine, easy promptLine, llama_cpp_model_loader, KSampler, KSampler, KSampler, KSampler, String Replace (mtb), SomethingToString, GetNode, String Replace (mtb), String Replace (mtb), GetNode, PrimitiveStringMultiline, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LTXVConcatAVLatent, GetNode, GetNode, GetNode, GetNode, LTXVLatentUpsampler, LTXVCropGuides, llama_cpp_model_loader, easy showAnything, llama_cpp_instruct_adv, VRAM_Debug, SetNode, String Replace (mtb), VRAM_Debug, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, LTXVImgToVideoInplaceKJ, LTXVAddGuideMulti, LTXVAudioVAEEncode, PrimitiveStringMultiline, UNETLoader, CLIPTextEncode, CLIPTextEncode, ReferenceLatent, ReferenceLatent, SamplerCustomAdvanced, CFGGuider, KSamplerSelect, Switch any [Crystools], CLIPLoader, VAELoader, VAEEncode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Switch any [Crystools], Switch any [Crystools], Switch any [Crystools], SetNode, SetNode, SetNode, SetNode, ConditioningZeroOut, easy promptLine, UNETLoader, Flux2Scheduler, LayerColor: ColorAdapter, SetNode, LayerColor: ColorAdapter, SetNode, LayerColor: ColorAdapter, SetNode, PreviewImage, PreviewImage, PreviewImage, SetNode, PreviewImage, RandomNoise, GetImageSize, PrimitiveBoolean, Switch any [Crystools], ImageScaleToTotalPixels, VAEDecode, VAEDecode, LayerColor: ColorAdapter, PreviewImage, UNETLoader, LoraLoaderModelOnly, Switch any [Crystools], VRAM_Debug, PrimitiveBoolean, MarkdownNote, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, llama_cpp_instruct_adv, LoadAudio, easy showAnything, PrimitiveStringMultiline, LoadImage, ImpactInt]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 24, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 65454653, "steps": 5, "width": 97}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/LTX2.3图生30秒长视频_2048717659298078721.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3图生30秒长视频_2048717659298078721.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（217 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `ConditioningZeroOut`
- `easy showAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImpactInt`
- `SetNode`
- `PreviewImage`
- `ConditioningZeroOut`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `GetNode`
- `easy showAnything`
- `ConditioningZeroOut`
- `GetNode`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `easy showAnything`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `CFGGuider`
- `RandomNoise`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `ComfyMathExpression`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `TrimAudioDuration`
- `SetLatentNoiseMask`
- `SolidMask`
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `VAEDecode` ★核心
- `GetNode`
- `LTXVConditioning`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `VAEDecode` ★核心
- `PrimitiveFloat`
- `LTX2_NAG`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVChunkFeedForward`
- `GetNode`
- `SetNode`
- `MathExpression|pysssss`
- `LTXVEmptyLatentAudio` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `CLIPLoader`
- `LatentUpscaleModelLoader`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `RandomNoise`
- `ImpactInt`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `RTXVideoSuperResolution`
- `easy promptLine`
- `easy promptLine`
- `easy promptLine`
- `llama_cpp_model_loader`
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `String Replace (mtb)`
- `SomethingToString`
- `GetNode`
- `String Replace (mtb)`
- `String Replace (mtb)`
- `GetNode`
- `PrimitiveStringMultiline`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `llama_cpp_model_loader`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `VRAM_Debug`
- `SetNode`
- `String Replace (mtb)`
- `VRAM_Debug`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEEncode` ★核心
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `KSamplerSelect` ★核心
- `Switch any [Crystools]`
- `CLIPLoader`
- `VAELoader`
- `VAEEncode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Switch any [Crystools]`
- `Switch any [Crystools]`
- `Switch any [Crystools]`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ConditioningZeroOut`
- `easy promptLine`
- `UNETLoader` ★核心
- `Flux2Scheduler`
- `LayerColor: ColorAdapter`
- `SetNode`
- `LayerColor: ColorAdapter`
- `SetNode`
- `LayerColor: ColorAdapter`
- `SetNode`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `SetNode`
- `PreviewImage`
- `RandomNoise`
- `GetImageSize`
- `PrimitiveBoolean`
- `Switch any [Crystools]`
- `ImageScaleToTotalPixels`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `LayerColor: ColorAdapter`
- `PreviewImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `Switch any [Crystools]`
- `VRAM_Debug`
- `PrimitiveBoolean`
- `MarkdownNote`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `llama_cpp_instruct_adv`
- `LoadAudio`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `LoadImage`
- `ImpactInt`

**识别到的模式**：image_to_image

## 关键参数

- `width` = `97`
- `height` = `24`
- `batch_size` = `1`
- `seed` = `65454653`
- `steps` = `5`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **56%**（121/217）

**有卡**：`ConditioningZeroOut`、`ImpactInt`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`VAELoader`、`ManualSigmas`、`KSamplerSelect`、`CFGGuider`、`SamplerCustomAdvanced`、`LTXVScheduler`、`RandomNoise`、`ComfyMathExpression`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTXVAudioVAEDecode`、`TrimAudioDuration`、`SetLatentNoiseMask`、`SolidMask`、`VAEDecode`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`LTX2_NAG`、`LTXVChunkFeedForward`、`MathExpression|pysssss`、`LTXVEmptyLatentAudio`、`VHS_VideoCombine`、`CLIPLoader`、`LatentUpscaleModelLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`、`VAEDecodeTiled`、`RTXVideoSuperResolution`、`easy promptLine`、`llama_cpp_model_loader`、`KSampler`、`String Replace (mtb)`、`SomethingToString`、`LayerUtility: ImageScaleByAspectRatio V2`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`llama_cpp_instruct_adv`、`VRAM_Debug`、`LTXVImgToVideoInplaceKJ`、`LTXVAddGuideMulti`、`LTXVAudioVAEEncode`、`UNETLoader`、`ReferenceLatent`、`Switch any [Crystools]`、`Flux2Scheduler`、`LayerColor: ColorAdapter`、`GetImageSize`、`PrimitiveBoolean`、`ImageScaleToTotalPixels`、`LoadAudio`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 4 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
