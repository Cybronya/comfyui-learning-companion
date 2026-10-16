---
key: 视频生成/图生视频/LTX2.3-MSR-V2多图生视频_2083001091343601666.json
name: LTX2.3-MSR-V2多图生视频_2083001091343601666
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3-MSR-V2多图生视频_2083001091343601666.json
hash: 9da152e1991f4c2a
coverage: 0.683761
learned_at: 2026-10-16 01:17:11
nodes: [LTXVEmptyLatentAudio, Reroute, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTX2_NAG, ManualSigmas, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, RandomNoise, LayerUtility: PurgeVRAM, SamplerCustomAdvanced, PathchSageAttentionKJ, ResizeImagesByLongerEdge, EmptyLTXVLatentVideo, SetNode, GetNode, SetNode, ResizeImagesByLongerEdge, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXAddVideoICLoRAGuide, GetNode, RandomNoise, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, LatentUpscaleModelLoader, LTXVLatentUpsampler, ComfyMathExpression, ComfyMathExpression, LTXVCropGuides, ManualSigmas, GetNode, GetNode, GetNode, GetNode, UNETLoader, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, LTXICLoRALoaderModelOnly, LTXVAddGuideMulti, LTXVAddGuideMulti, 孤海注释, 孤海注释, 孤海注释, 孤海注释, LoraLoaderModelOnly, VAEDecodeTiled, LTXVCropGuides, LayerUtility: PurgeVRAM, MarkdownNote, LoraLoaderModelOnly, LTXVAudioVAEDecode, RTXVideoSuperResolution, FrameInterpolationModelLoader, FrameInterpolate, UNETLoader, LoraLoaderModelOnly, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, JjkText, solarL_SaveImagesToZip, LoraLoaderModelOnly, CLIPTextEncode, Note, SetNode, LoadImage, PrimitiveInt, 孤海注释, LoadImage, SetNode, ResizeImagesByLongerEdge, LoadImage, PrimitiveInt, ResizeImagesByLongerEdge, SetNode, PrimitiveInt, PrimitiveStringMultiline, GetNode, CLIPTextEncode, GetNode, GetNode, SetNode, VHS_VideoCombine, LTXVSeparateAVLatent, SamplerCustomAdvanced, ComfyMathExpression, GetNode, CLIPTextEncode, LTXVConditioning, LoadImage, LiconMSR, PrimitiveStringMultiline, PrimitiveInt, ResizeImagesByLongerEdge]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3-MSR-V2多图生视频_2083001091343601666.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3-MSR-V2多图生视频_2083001091343601666.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（117 个）：
- `LTXVEmptyLatentAudio` ★核心
- `Reroute`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTX2_NAG`
- `ManualSigmas`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `RandomNoise`
- `LayerUtility: PurgeVRAM`
- `SamplerCustomAdvanced` ★核心
- `PathchSageAttentionKJ`
- `ResizeImagesByLongerEdge`
- `EmptyLTXVLatentVideo`
- `SetNode`
- `GetNode`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsampler` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `LTXVCropGuides`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXVAddGuideMulti`
- `LTXVAddGuideMulti`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `LTXVCropGuides`
- `LayerUtility: PurgeVRAM`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LTXVAudioVAEDecode` ★核心
- `RTXVideoSuperResolution`
- `FrameInterpolationModelLoader`
- `FrameInterpolate`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `SetNode`
- `LoadImage`
- `PrimitiveInt`
- `孤海注释`
- `LoadImage`
- `SetNode`
- `ResizeImagesByLongerEdge`
- `LoadImage`
- `PrimitiveInt`
- `ResizeImagesByLongerEdge`
- `SetNode`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `GetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `ComfyMathExpression`
- `GetNode`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LoadImage`
- `LiconMSR`
- `PrimitiveStringMultiline`
- `PrimitiveInt`
- `ResizeImagesByLongerEdge`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **68%**（80/117）

**有卡**：`LTXVEmptyLatentAudio`、`CFGGuider`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LTX2_NAG`、`ManualSigmas`、`ComfyMathExpression`、`RandomNoise`、`LayerUtility: PurgeVRAM`、`SamplerCustomAdvanced`、`PathchSageAttentionKJ`、`ResizeImagesByLongerEdge`、`EmptyLTXVLatentVideo`、`LoadImage`、`LTXAddVideoICLoRAGuide`、`LatentUpscaleModelLoader`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`UNETLoader`、`VAELoaderKJ`、`DualCLIPLoader`、`LTXICLoRALoaderModelOnly`、`LTXVAddGuideMulti`、`LoraLoaderModelOnly`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`RTXVideoSuperResolution`、`FrameInterpolationModelLoader`、`FrameInterpolate`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`solarL_SaveImagesToZip`、`VHS_VideoCombine`、`LTXVConditioning`、`LiconMSR`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
