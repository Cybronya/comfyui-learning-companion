---
key: 数字人/数字人/LTX2.3 Eros 口播数字人-首尾帧相同-V1.3_2082491190057988097.json
name: LTX2.3 Eros 口播数字人-首尾帧相同-V1.3_2082491190057988097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3 Eros 口播数字人-首尾帧相同-V1.3_2082491190057988097.json
hash: c6b1f04ec09bf0db
coverage: 0.545455
learned_at: 2026-10-18 19:07:41
nodes: [ManualSigmas, LTXVConcatAVLatent, GetNode, KSamplerSelect, SetNode, PathchSageAttentionKJ, ModelPatchTorchSettings, SetNode, SetNode, VAELoaderKJ, Note, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, SetNode, LTXVCropGuides, Fast Groups Bypasser (rgthree), CLIPTextEncode, LTXLatentAnchorAware, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVEmptyLatentAudio, LTXTextAttentionAmplifier, CFGGuider, LTX2SamplingPreviewOverride, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, LTXVAudioVAELoader, LTXAVTextEncoderLoader, CheckpointLoaderSimple, ImageScaleBy, GetNode, EmptyLTXVLatentVideo, GetNode, LTXVImgToVideoInplaceKJ, SamplerCustomAdvanced, LTXVSeparateAVLatent, SetNode, VAEDecode, SetNode, GetImageSize, ImageResizeKJv2, Qwen3TTSModelLoader, ShowText|pysssss, SaveAudioAdvanced, SetNode, PrimitiveInt, SetNode, PrimitiveFloat, ComfyMathExpression, SetNode, SetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, PreviewImage, Sigmas Easing, KSamplerSelect, STGGuiderAdvanced, RandomNoise, GetNode, easy float, SetNode, SetNode, GetNode, GetNode, Note, VHS_VideoCombine, ComfyMathExpression, GetNode, LTXVConditioning, LTXVImgToVideoInplaceKJ, Any Switch (rgthree), SetNode, CLIPTextEncode, SetNode, SetNode, LTX2LoraLoaderAdvanced, LTX2LoraLoaderAdvanced, LTX2LoraLoaderAdvanced, LTX2LoraLoaderAdvanced, Apply Whisper, PrimitiveInt, VHS_VideoCombine, LoraLoaderModelOnly, easy showAnything, SetNode, GetNode, easy showAnything, GetNode, ComfyMathExpression, Note, LoadAudio, GroupSwitcher, Qwen3TTSVoiceClone, PreviewAudio, PreviewAudio, GetNode, LTXVAudioVAEEncode, GetNode, GetNode, LTXVAudioVideoMask, SolidMask, GetNode, TrimAudioDuration, GetNode, AudioAdjustVolume, GetNode, GetNode, ImageFromBatch, GetNode, GetNode, ComfyMathExpression, SoundFlow_GetLength, ComfyMathExpression, SetLatentNoiseMask, SetNode, ComfyMathExpression, PrimitiveStringMultiline, LoadAudio, LoadImage, LatentUpscaleModelLoader, LTXVLatentUpsamplerTiled, LTXVLatentUpsampler, PrimitiveStringMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "10Eros_v1-fp8mixed_learned.safetensors", "height": 24, "lora_name": "ltx-2.3-22b-distilled-lora-1.1_fro90_ceil72_condsafe.safetensors", "strength_clip": 1, "strength_model": 0.5800000000000001, "width": 1}
---

# 数字人/数字人/LTX2.3 Eros 口播数字人-首尾帧相同-V1.3_2082491190057988097.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3 Eros 口播数字人-首尾帧相同-V1.3_2082491190057988097.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（132 个）：
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `GetNode`
- `KSamplerSelect` ★核心
- `SetNode`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `SetNode`
- `LTXVCropGuides`
- `Fast Groups Bypasser (rgthree)`
- `CLIPTextEncode` ★核心
- `LTXLatentAnchorAware`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `LTXTextAttentionAmplifier`
- `CFGGuider`
- `LTX2SamplingPreviewOverride`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXVAudioVAELoader`
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `ImageScaleBy`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `LTXVImgToVideoInplaceKJ`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `GetImageSize`
- `ImageResizeKJv2`
- `Qwen3TTSModelLoader`
- `ShowText|pysssss`
- `SaveAudioAdvanced`
- `SetNode`
- `PrimitiveInt`
- `SetNode`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PreviewImage`
- `Sigmas Easing`
- `KSamplerSelect` ★核心
- `STGGuiderAdvanced`
- `RandomNoise`
- `GetNode`
- `easy float`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Note`
- `VHS_VideoCombine`
- `ComfyMathExpression`
- `GetNode`
- `LTXVConditioning`
- `LTXVImgToVideoInplaceKJ`
- `Any Switch (rgthree)`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `LTX2LoraLoaderAdvanced` ★核心
- `LTX2LoraLoaderAdvanced` ★核心
- `LTX2LoraLoaderAdvanced` ★核心
- `LTX2LoraLoaderAdvanced` ★核心
- `Apply Whisper`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `SetNode`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `ComfyMathExpression`
- `Note`
- `LoadAudio`
- `GroupSwitcher`
- `Qwen3TTSVoiceClone`
- `PreviewAudio`
- `PreviewAudio`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `GetNode`
- `LTXVAudioVideoMask`
- `SolidMask`
- `GetNode`
- `TrimAudioDuration`
- `GetNode`
- `AudioAdjustVolume`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `SoundFlow_GetLength`
- `ComfyMathExpression`
- `SetLatentNoiseMask`
- `SetNode`
- `ComfyMathExpression`
- `PrimitiveStringMultiline`
- `LoadAudio`
- `LoadImage`
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsamplerTiled` ★核心
- `LTXVLatentUpsampler` ★核心
- `PrimitiveStringMultiline`

## 关键参数

- `width` = `1`
- `height` = `24`
- `batch_size` = `1`
- `checkpoint` = `10Eros_v1-fp8mixed_learned.safetensors`
- `lora_name` = `ltx-2.3-22b-distilled-lora-1.1_fro90_ceil72_condsafe.safetensors`
- `strength_model` = `0.5800000000000001`
- `strength_clip` = `1`

## 知识

覆盖率 **55%**（72/132）

**有卡**：`ManualSigmas`、`LTXVConcatAVLatent`、`KSamplerSelect`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAELoaderKJ`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`CLIPTextEncode`、`LTXLatentAnchorAware`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVEmptyLatentAudio`、`LTXTextAttentionAmplifier`、`CFGGuider`、`LTX2SamplingPreviewOverride`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`ImageScaleBy`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplaceKJ`、`VAEDecode`、`GetImageSize`、`ImageResizeKJv2`、`Qwen3TTSModelLoader`、`SaveAudioAdvanced`、`ComfyMathExpression`、`Sigmas Easing`、`STGGuiderAdvanced`、`RandomNoise`、`easy float`、`VHS_VideoCombine`、`LTXVConditioning`、`LTX2LoraLoaderAdvanced`、`Apply Whisper`、`LoraLoaderModelOnly`、`LoadAudio`、`GroupSwitcher`、`Qwen3TTSVoiceClone`、`PreviewAudio`、`LTXVAudioVAEEncode`、`LTXVAudioVideoMask`、`SolidMask`、`TrimAudioDuration`、`AudioAdjustVolume`、`ImageFromBatch`、`SoundFlow_GetLength`、`SetLatentNoiseMask`、`LoadImage`、`LatentUpscaleModelLoader`、`LTXVLatentUpsamplerTiled`、`LTXVLatentUpsampler`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
