---
key: 视频生成/图生视频/多主体生视频｜LTX2.3+MSR图生视频生成_2092155116446117890.json
name: 多主体生视频｜LTX2.3+MSR图生视频生成_2092155116446117890
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/多主体生视频｜LTX2.3+MSR图生视频生成_2092155116446117890.json
hash: ecfc040d70c82884
coverage: 0.524096
learned_at: 2026-10-16 22:59:56
nodes: [SetNode, SimpleCalculatorKJ, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, PathchSageAttentionKJ, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, LTX2MemoryEfficientSageAttentionPatch, GetNode, GetNode, ComfyNumberConvert, GetNode, GetNode, GetNode, SetNode, SetNode, LTXVAudioVAEDecode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, LTXVSeparateAVLatent, GetNode, CFGGuider, ComfySwitchNode, GetNode, LTXVSeparateAVLatent, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, LTXVCropGuides, LTXVLatentUpsampler, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, LTXAddVideoICLoRAGuide, ManualSigmas, KSamplerSelect, ModelSamplingSD3, LTX2SamplingPreviewOverride, CFGGuider, KSamplerSelect, BasicScheduler, GetNode, GetNode, ImageResizeKJv2, ComfyMathExpression, ComfyMathExpression, GetNode, ComfySwitchNode, ComfySwitchNode, LTXVConcatAVLatent, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVConditioning, ComfySwitchNode, GetNode, GetNode, GetNode, LTXVCropGuides, RandomNoise, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, LoraLoaderModelOnly, PrimitiveBoolean, GetNode, LoadImage, LoadImage, LiconMSR, ImageResizeKJv2, ImageResizeKJv2, LTXAddVideoICLoRAGuide, LTX2_NAG, CLIPTextEncode, SamplerCustomAdvanced, SamplerCustomAdvanced, VAEDecode, LTX2AttentionTunerPatch, LTXVChunkFeedForward, RandomNoise, INTConstant, INTConstant, INTConstant, PrimitiveFloat, LoadImage, LoadImage, LoadImage, UNETLoader, LatentUpscaleModelLoader, DualCLIPLoader, VAELoader, VAELoaderKJ, VAELoader, LTXICLoRALoaderModelOnly, GetImageSizeAndCount, SetNode, GetNode, GetNode, ComfySwitchNode, GetNode, LTXICLoRALoaderModelOnly, LTXICLoRALoaderModelOnly, PromptRelayEncode, VHS_VideoCombine, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/多主体生视频｜LTX2.3+MSR图生视频生成_2092155116446117890.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/多主体生视频｜LTX2.3+MSR图生视频生成_2092155116446117890.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（166 个）：
- `SetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTX2MemoryEfficientSageAttentionPatch`
- `GetNode`
- `GetNode`
- `ComfyNumberConvert`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `GetNode`
- `CFGGuider`
- `ComfySwitchNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ModelSamplingSD3`
- `LTX2SamplingPreviewOverride`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `ComfySwitchNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `RandomNoise`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveBoolean`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LiconMSR`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LTXAddVideoICLoRAGuide`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `LTX2AttentionTunerPatch`
- `LTXVChunkFeedForward`
- `RandomNoise`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `PrimitiveFloat`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `LTXICLoRALoaderModelOnly` ★核心
- `GetImageSizeAndCount`
- `SetNode`
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `LTXICLoRALoaderModelOnly` ★核心
- `LTXICLoRALoaderModelOnly` ★核心
- `PromptRelayEncode`
- `VHS_VideoCombine`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
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
- `Note`

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

覆盖率 **52%**（87/166）

**有卡**：`SimpleCalculatorKJ`、`PathchSageAttentionKJ`、`LTX2MemoryEfficientSageAttentionPatch`、`ComfyNumberConvert`、`LTXVAudioVAEDecode`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`CFGGuider`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXAddVideoICLoRAGuide`、`ManualSigmas`、`KSamplerSelect`、`ModelSamplingSD3`、`LTX2SamplingPreviewOverride`、`BasicScheduler`、`ImageResizeKJv2`、`ComfyMathExpression`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`RandomNoise`、`LoraLoaderModelOnly`、`PrimitiveBoolean`、`LoadImage`、`LiconMSR`、`LTX2_NAG`、`CLIPTextEncode`、`SamplerCustomAdvanced`、`VAEDecode`、`LTX2AttentionTunerPatch`、`LTXVChunkFeedForward`、`INTConstant`、`UNETLoader`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoader`、`VAELoaderKJ`、`LTXICLoRALoaderModelOnly`、`GetImageSizeAndCount`、`PromptRelayEncode`、`VHS_VideoCombine`、`CLIPLoader`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
