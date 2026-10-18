---
key: 视频生成/图生视频/Minimax H3 sigma强化加Selflift双采文不油武不糊 多图音频参考生视频_2109737500267859970.json
name: Minimax H3 sigma强化加Selflift双采文不油武不糊 多图音频参考生视频_2109737500267859970
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax H3 sigma强化加Selflift双采文不油武不糊 多图音频参考生视频_2109737500267859970.json
hash: 0c62344c6ec3ab1d
coverage: 0.571429
learned_at: 2026-10-18 00:23:36
nodes: [ConditioningZeroOut, GetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, GetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, SetNode, KSamplerSelect, GetNode, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), easy cleanGpuUsed, GetNode, GetNode, VAEDecode, LTXVSeparateAVLatent, GetNode, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, SetNode, LoadImage, SetNode, GetNode, PrimitiveInt, Any To String (mtb), SetNode, SetNode, AudioCrop, PrimitiveInt, Any To String (mtb), SetNode, AudioCrop, Any To String (mtb), AudioCrop, SetNode, PrimitiveInt, PreviewAudio, PreviewAudio, LoadAudio, LoadAudio, PreviewAudio, LoadAudio, GetNode, GetNode, GetNode, LoadImage, LoadImage, LoadImage, GetNode, VAEDecodeAudio, LayerUtility: PurgeVRAM V2, SetNode, GetNode, MiniMaxH3ReferenceToVideo, SetNode, ComfyMathExpression, VHS_VideoCombine, Fast Groups Bypasser (rgthree), JjkText, SetNode, SetNode, BasicScheduler, Fast Groups Bypasser (rgthree), LoadImage, VAELoader, ResolutionSelector, UNETLoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelAttentionBackend, MiniMaxChunkFeedForward, H3SigmaRefiner, VAELoader, LoraLoaderModelOnly, MiniMaxLowVRAMAttention, easy seed, Text Concatenate, easy showAnything, GetNode, GetNode, LoraLoaderModelOnly, SetNode, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderBypassModelOnly, Float, Fast Groups Bypasser (rgthree), UNETLoader, SetNode, JjkText, JjkText, PrimitiveFloat, SetNode, GetNode, SelfLiftAvatarH3Sampler, ModelPreviewOverrideKJ, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/Minimax H3 sigma强化加Selflift双采文不油武不糊 多图音频参考生视频_2109737500267859970.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax H3 sigma强化加Selflift双采文不油武不糊 多图音频参考生视频_2109737500267859970.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（147 个）：
- `ConditioningZeroOut`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `SetNode`
- `GetNode`
- `PrimitiveInt`
- `Any To String (mtb)`
- `SetNode`
- `SetNode`
- `AudioCrop`
- `PrimitiveInt`
- `Any To String (mtb)`
- `SetNode`
- `AudioCrop`
- `Any To String (mtb)`
- `AudioCrop`
- `SetNode`
- `PrimitiveInt`
- `PreviewAudio`
- `PreviewAudio`
- `LoadAudio`
- `LoadAudio`
- `PreviewAudio`
- `LoadAudio`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `LayerUtility: PurgeVRAM V2`
- `SetNode`
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
- `SetNode`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `JjkText`
- `SetNode`
- `SetNode`
- `BasicScheduler`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `VAELoader`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelAttentionBackend`
- `MiniMaxChunkFeedForward`
- `H3SigmaRefiner`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxLowVRAMAttention`
- `easy seed`
- `Text Concatenate`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `Float`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `SetNode`
- `JjkText`
- `JjkText`
- `PrimitiveFloat`
- `SetNode`
- `GetNode`
- `SelfLiftAvatarH3Sampler` ★核心
- `ModelPreviewOverrideKJ`
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
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`
- `SaveImage`

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

## 知识

覆盖率 **57%**（84/147）

**有卡**：`ConditioningZeroOut`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSamplerSelect`、`easy cleanGpuUsed`、`VAEDecode`、`LTXVSeparateAVLatent`、`LoadImage`、`Any To String (mtb)`、`AudioCrop`、`PreviewAudio`、`LoadAudio`、`VAEDecodeAudio`、`LayerUtility: PurgeVRAM V2`、`MiniMaxH3ReferenceToVideo`、`ComfyMathExpression`、`VHS_VideoCombine`、`BasicScheduler`、`VAELoader`、`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`ModelAttentionBackend`、`MiniMaxChunkFeedForward`、`H3SigmaRefiner`、`MiniMaxLowVRAMAttention`、`easy seed`、`Text Concatenate`、`LoraLoaderBypassModelOnly`、`Float`、`SelfLiftAvatarH3Sampler`、`ModelPreviewOverrideKJ`、`KSampler`、`CLIPTextEncode`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
