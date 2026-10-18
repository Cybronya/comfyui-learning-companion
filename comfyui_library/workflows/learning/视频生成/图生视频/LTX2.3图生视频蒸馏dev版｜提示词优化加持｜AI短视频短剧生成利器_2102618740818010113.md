---
key: 视频生成/图生视频/LTX2.3图生视频蒸馏dev版｜提示词优化加持｜AI短视频短剧生成利器_2102618740818010113.json
name: LTX2.3图生视频蒸馏dev版｜提示词优化加持｜AI短视频短剧生成利器_2102618740818010113
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3图生视频蒸馏dev版｜提示词优化加持｜AI短视频短剧生成利器_2102618740818010113.json
hash: d608a0332361907c
coverage: 0.615385
learned_at: 2026-10-17 02:28:51
nodes: [SetNode, SetNode, SetNode, CR Text, GetNode, GetNode, GetNode, EmptyImage, LTXVConcatAVLatent, GetNode, GetNode, easy cleanGpuUsed, LTXVConditioning, SetNode, SetNode, GetNode, easy cleanGpuUsed, SetNode, GetNode, SetNode, LTXVPreprocess, LayerUtility: ImageScaleByAspectRatio V2, GetNode, LayerUtility: ImageScaleByAspectRatio V2, CR Text, CR Text, SetNode, GetNode, EmptyLTXVLatentVideo, GetNode, GetNode, ImageScaleBy, SetNode, SetNode, LTXVImgToVideoInplace, Int, SetNode, CR Text, easy cleanGpuUsed, easy cleanGpuUsed, CR Text, CR Text, SetNode, VAELoaderKJ, VAELoaderKJ, SetNode, CLIPTextEncode, GetNode, LTXVCropGuides, CFGGuider, RandomNoise, easy cleanGpuUsed, GetNode, KSamplerSelect, LTXVConcatAVLatent, LTXVImgToVideoInplace, LTXVLatentUpsampler, SamplerCustomAdvanced, CR Text, SetNode, easy cleanGpuUsed, Any To String (mtb), GetNode, llama_cpp_instruct_adv, SetNode, GetNode, GetNode, GetNode, GetNode, CR Text, CR Text, Any To String (mtb), CR Text, Any To String (mtb), Any To String (mtb), SetNode, GetNode, easy convertAnything, ttN concat, CR Text Concatenate, SetNode, CR Text, LoraLoaderModelOnly, ResizeImagesByLongerEdge, DualCLIPLoader, SetNode, PrimitiveInt, Int, GetNode, MathExpression|pysssss, LTXVEmptyLatentAudio, GetNode, GetNode, GetNode, CFGGuider, GetNode, GetNode, GetNode, RandomNoise, SamplerCustomAdvanced, LTXVSeparateAVLatent, KSamplerSelect, GetNode, LTXVScheduler, GetNode, CR Value, easy convertAnything, SetNode, SetNode, SetNode, SetNode, SetNode, LTXVChunkFeedForward, VRAMReserver, CR Text, easy cleanGpuUsed, LTXVSeparateAVLatent, GetNode, LTXVAudioVAEDecode, GetNode, GetNode, VAEDecodeTiled, SaveVideo, LatentUpscaleModelLoader, SetNode, SetNode, SetNode, CR Text, EmptyImage, GetImageSize, LTXVConcatAVLatent, easy cleanGpuUsed, LTXVConditioning, SetNode, SetNode, GetNode, easy cleanGpuUsed, CR Text, CR Text, GetNode, GetNode, ImageScaleBy, SetNode, LTXVImgToVideoInplace, GetNode, SetNode, CR Text, easy cleanGpuUsed, easy cleanGpuUsed, CLIPTextEncode, CR Text, CLIPTextEncode, GetNode, LTXVCropGuides, CFGGuider, RandomNoise, easy cleanGpuUsed, KSamplerSelect, LTXVConcatAVLatent, LTXVLatentUpsampler, CR Text, LoraLoaderModelOnly, SetNode, PrimitiveInt, GetNode, MathExpression|pysssss, LTXVEmptyLatentAudio, GetNode, GetNode, RandomNoise, LTXVSeparateAVLatent, KSamplerSelect, CR Text, easy cleanGpuUsed, LTXVSeparateAVLatent, LTXVAudioVAEDecode, GetNode, VAEDecodeTiled, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Any To String (mtb), SetNode, GetNode, SaveVideo, GetImageSize, CR Text, LTXVAudioVAELoader, LTXAVTextEncoderLoader, SetNode, GetNode, LoraLoaderModelOnly, SetNode, SetNode, CR Text, CR String To Combo, SetNode, CR String To Combo, SetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, CreateVideo, CreateVideo, UNETLoader, CheckpointLoaderSimple, GetNode, CFGGuider, GetNode, GetNode, CLIPTextEncode, EmptyLTXVLatentVideo, LatentUpscaleModelLoader, GetNode, SetNode, CR Text, LTXVImgToVideoInplace, SamplerCustomAdvanced, SamplerCustomAdvanced, ManualSigmas, GetNode, LTXVChunkFeedForward, VRAMReserver, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, CheckpointLoaderSimple, LTXVAudioVAELoader, LTXAVTextEncoderLoader, ShowText|pysssss, llama_cpp_model_loader, LTXVScheduler, ManualSigmas, ManualSigmas, Fast Groups Muter (rgthree), ImpactSwitch, ImpactSwitch, ImpactSwitch, CR Text, CR Text, ImpactSwitch, easy int, Display Any (rgthree), LoadImage, CR Text, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3图生视频蒸馏dev版｜提示词优化加持｜AI短视频短剧生成利器_2102618740818010113.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3图生视频蒸馏dev版｜提示词优化加持｜AI短视频短剧生成利器_2102618740818010113.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（299 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `CR Text`
- `GetNode`
- `GetNode`
- `GetNode`
- `EmptyImage`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `SetNode`
- `LTXVPreprocess`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `CR Text`
- `SetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GetNode`
- `ImageScaleBy`
- `SetNode`
- `SetNode`
- `LTXVImgToVideoInplace`
- `Int`
- `SetNode`
- `CR Text`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CR Text`
- `CR Text`
- `SetNode`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LTXVCropGuides`
- `CFGGuider`
- `RandomNoise`
- `easy cleanGpuUsed`
- `GetNode`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler` ★核心
- `SamplerCustomAdvanced` ★核心
- `CR Text`
- `SetNode`
- `easy cleanGpuUsed`
- `Any To String (mtb)`
- `GetNode`
- `llama_cpp_instruct_adv`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CR Text`
- `CR Text`
- `Any To String (mtb)`
- `CR Text`
- `Any To String (mtb)`
- `Any To String (mtb)`
- `SetNode`
- `GetNode`
- `easy convertAnything`
- `ttN concat`
- `CR Text Concatenate`
- `SetNode`
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `ResizeImagesByLongerEdge`
- `DualCLIPLoader`
- `SetNode`
- `PrimitiveInt`
- `Int`
- `GetNode`
- `MathExpression|pysssss`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `GetNode`
- `LTXVScheduler`
- `GetNode`
- `CR Value`
- `easy convertAnything`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVChunkFeedForward`
- `VRAMReserver`
- `CR Text`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `SaveVideo`
- `LatentUpscaleModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `CR Text`
- `EmptyImage`
- `GetImageSize`
- `LTXVConcatAVLatent`
- `easy cleanGpuUsed`
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `CR Text`
- `CR Text`
- `GetNode`
- `GetNode`
- `ImageScaleBy`
- `SetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `SetNode`
- `CR Text`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `CLIPTextEncode` ★核心
- `CR Text`
- `CLIPTextEncode` ★核心
- `GetNode`
- `LTXVCropGuides`
- `CFGGuider`
- `RandomNoise`
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler` ★核心
- `CR Text`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `PrimitiveInt`
- `GetNode`
- `MathExpression|pysssss`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `RandomNoise`
- `LTXVSeparateAVLatent`
- `KSamplerSelect` ★核心
- `CR Text`
- `easy cleanGpuUsed`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `VAEDecodeTiled` ★核心
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
- `Any To String (mtb)`
- `SetNode`
- `GetNode`
- `SaveVideo`
- `GetImageSize`
- `CR Text`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `CR Text`
- `CR String To Combo`
- `SetNode`
- `CR String To Combo`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CreateVideo`
- `CreateVideo`
- `UNETLoader` ★核心
- `CheckpointLoaderSimple` ★核心
- `GetNode`
- `CFGGuider`
- `GetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `EmptyLTXVLatentVideo`
- `LatentUpscaleModelLoader`
- `GetNode`
- `SetNode`
- `CR Text`
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `GetNode`
- `LTXVChunkFeedForward`
- `VRAMReserver`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `ShowText|pysssss`
- `llama_cpp_model_loader`
- `LTXVScheduler`
- `ManualSigmas`
- `ManualSigmas`
- `Fast Groups Muter (rgthree)`
- `ImpactSwitch`
- `ImpactSwitch`
- `ImpactSwitch`
- `CR Text`
- `CR Text`
- `ImpactSwitch`
- `easy int`
- `Display Any (rgthree)`
- `LoadImage`
- `CR Text`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **62%**（184/299）

**有卡**：`CR Text`、`EmptyImage`、`LTXVConcatAVLatent`、`easy cleanGpuUsed`、`LTXVConditioning`、`LTXVPreprocess`、`LayerUtility: ImageScaleByAspectRatio V2`、`EmptyLTXVLatentVideo`、`ImageScaleBy`、`LTXVImgToVideoInplace`、`Int`、`VAELoaderKJ`、`CLIPTextEncode`、`LTXVCropGuides`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`LTXVLatentUpsampler`、`SamplerCustomAdvanced`、`Any To String (mtb)`、`llama_cpp_instruct_adv`、`easy convertAnything`、`ttN concat`、`CR Text Concatenate`、`LoraLoaderModelOnly`、`ResizeImagesByLongerEdge`、`DualCLIPLoader`、`MathExpression|pysssss`、`LTXVEmptyLatentAudio`、`LTXVSeparateAVLatent`、`LTXVScheduler`、`CR Value`、`LTXVChunkFeedForward`、`VRAMReserver`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`SaveVideo`、`LatentUpscaleModelLoader`、`GetImageSize`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`CR String To Combo`、`CreateVideo`、`UNETLoader`、`CheckpointLoaderSimple`、`ManualSigmas`、`llama_cpp_model_loader`、`easy int`、`Display Any (rgthree)`、`LoadImage`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
