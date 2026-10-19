---
key: 数字人/数字人/口播数字人｜LTX2.3 Eros首尾帧一致V1.3 高清直出_2089766191563894785.json
name: 口播数字人｜LTX2.3 Eros首尾帧一致V1.3 高清直出_2089766191563894785
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/口播数字人｜LTX2.3 Eros首尾帧一致V1.3 高清直出_2089766191563894785.json
hash: 6e133004dff8c1bf
coverage: 0.613924
learned_at: 2026-10-18 22:17:14
nodes: [ManualSigmas, LTXVConcatAVLatent, GetNode, KSamplerSelect, SetNode, PathchSageAttentionKJ, ModelPatchTorchSettings, SetNode, SetNode, VAELoaderKJ, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, SetNode, LTXVCropGuides, Fast Groups Bypasser (rgthree), CLIPTextEncode, LTXLatentAnchorAware, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVEmptyLatentAudio, LTXTextAttentionAmplifier, CFGGuider, LTX2SamplingPreviewOverride, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, LTXVAudioVAELoader, LTXAVTextEncoderLoader, CheckpointLoaderSimple, ImageScaleBy, GetNode, EmptyLTXVLatentVideo, GetNode, LTXVImgToVideoInplaceKJ, SamplerCustomAdvanced, LTXVSeparateAVLatent, SetNode, VAEDecode, SetNode, GetImageSize, ImageResizeKJv2, Qwen3TTSModelLoader, ShowText|pysssss, SaveAudioAdvanced, SetNode, PrimitiveInt, SetNode, PrimitiveFloat, ComfyMathExpression, SetNode, SetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, PreviewImage, Sigmas Easing, KSamplerSelect, STGGuiderAdvanced, RandomNoise, GetNode, easy float, SetNode, SetNode, GetNode, GetNode, VHS_VideoCombine, ComfyMathExpression, GetNode, LTXVConditioning, LTXVImgToVideoInplaceKJ, Any Switch (rgthree), SetNode, CLIPTextEncode, SetNode, SetNode, LTX2LoraLoaderAdvanced, LTX2LoraLoaderAdvanced, LTX2LoraLoaderAdvanced, LTX2LoraLoaderAdvanced, Apply Whisper, PrimitiveInt, VHS_VideoCombine, LoraLoaderModelOnly, easy showAnything, SetNode, GetNode, easy showAnything, GetNode, ComfyMathExpression, LoadAudio, GroupSwitcher, Qwen3TTSVoiceClone, PreviewAudio, PreviewAudio, GetNode, LTXVAudioVAEEncode, GetNode, GetNode, LTXVAudioVideoMask, SolidMask, GetNode, TrimAudioDuration, GetNode, AudioAdjustVolume, GetNode, GetNode, ImageFromBatch, GetNode, GetNode, ComfyMathExpression, SoundFlow_GetLength, ComfyMathExpression, SetLatentNoiseMask, SetNode, ComfyMathExpression, PrimitiveStringMultiline, LoadAudio, LoadImage, LatentUpscaleModelLoader, LTXVLatentUpsamplerTiled, LTXVLatentUpsampler, PrimitiveStringMultiline, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "10Eros_v1-fp8mixed_learned.safetensors", "denoise": 1, "height": 80, "lora_name": "ltx-2.3-22b-distilled-lora-1.1_fro90_ceil72_condsafe.safetensors", "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "strength_clip": 1, "strength_model": 0.5800000000000001, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/口播数字人｜LTX2.3 Eros首尾帧一致V1.3 高清直出_2089766191563894785.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/口播数字人｜LTX2.3 Eros首尾帧一致V1.3 高清直出_2089766191563894785.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（158 个）：
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
- `孤海注释`
- `孤海注释`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `checkpoint` = `10Eros_v1-fp8mixed_learned.safetensors`
- `lora_name` = `ltx-2.3-22b-distilled-lora-1.1_fro90_ceil72_condsafe.safetensors`
- `strength_model` = `0.5800000000000001`
- `strength_clip` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **61%**（97/158）

**有卡**：`ManualSigmas`、`LTXVConcatAVLatent`、`KSamplerSelect`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAELoaderKJ`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`CLIPTextEncode`、`LTXLatentAnchorAware`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVEmptyLatentAudio`、`LTXTextAttentionAmplifier`、`CFGGuider`、`LTX2SamplingPreviewOverride`、`LTXVAudioVAELoader`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`ImageScaleBy`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplaceKJ`、`VAEDecode`、`GetImageSize`、`ImageResizeKJv2`、`Qwen3TTSModelLoader`、`SaveAudioAdvanced`、`ComfyMathExpression`、`Sigmas Easing`、`STGGuiderAdvanced`、`RandomNoise`、`easy float`、`VHS_VideoCombine`、`LTXVConditioning`、`LTX2LoraLoaderAdvanced`、`Apply Whisper`、`LoraLoaderModelOnly`、`LoadAudio`、`GroupSwitcher`、`Qwen3TTSVoiceClone`、`PreviewAudio`、`LTXVAudioVAEEncode`、`LTXVAudioVideoMask`、`SolidMask`、`TrimAudioDuration`、`AudioAdjustVolume`、`ImageFromBatch`、`SoundFlow_GetLength`、`SetLatentNoiseMask`、`LoadImage`、`LatentUpscaleModelLoader`、`LTXVLatentUpsamplerTiled`、`LTXVLatentUpsampler`、`UNETLoader`、`KSampler`、`solarL_SaveImagesToZip`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
