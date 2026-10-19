---
key: 数字人/数字人/数字人LTX2.3 Eros首尾帧一致_2092114420569825281.json
name: 数字人LTX2.3 Eros首尾帧一致_2092114420569825281
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/数字人LTX2.3 Eros首尾帧一致_2092114420569825281.json
hash: d1dad88479692d99
coverage: 0.613924
learned_at: 2026-10-18 22:17:16
nodes: [ManualSigmas, LTXVConcatAVLatent, GetNode, KSamplerSelect, SetNode, PathchSageAttentionKJ, ModelPatchTorchSettings, SetNode, SetNode, VAELoaderKJ, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, SetNode, LTXVCropGuides, Fast Groups Bypasser (rgthree), LTXLatentAnchorAware, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVEmptyLatentAudio, LTXTextAttentionAmplifier, LTX2SamplingPreviewOverride, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, LTXAVTextEncoderLoader, ImageScaleBy, EmptyLTXVLatentVideo, GetNode, SamplerCustomAdvanced, LTXVSeparateAVLatent, SetNode, VAEDecode, SetNode, ShowText|pysssss, SetNode, SetNode, PrimitiveFloat, ComfyMathExpression, SetNode, SetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, Sigmas Easing, KSamplerSelect, STGGuiderAdvanced, RandomNoise, GetNode, SetNode, SetNode, GetNode, GetNode, VHS_VideoCombine, ComfyMathExpression, GetNode, LTXVConditioning, LTXVImgToVideoInplaceKJ, SetNode, CLIPTextEncode, SetNode, SetNode, LTX2LoraLoaderAdvanced, LTX2LoraLoaderAdvanced, LTX2LoraLoaderAdvanced, LTX2LoraLoaderAdvanced, Apply Whisper, LoraLoaderModelOnly, easy showAnything, SetNode, GetNode, easy showAnything, GetNode, ComfyMathExpression, GetNode, LTXVAudioVAEEncode, GetNode, LTXVAudioVideoMask, SolidMask, GetNode, TrimAudioDuration, GetNode, AudioAdjustVolume, GetNode, GetNode, ImageFromBatch, GetNode, GetNode, ComfyMathExpression, SoundFlow_GetLength, ComfyMathExpression, SetLatentNoiseMask, SetNode, ComfyMathExpression, LatentUpscaleModelLoader, LTXVLatentUpsamplerTiled, LTXVLatentUpsampler, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, GetNode, easy float, GetImageSize, LoadAudio, GetNode, PreviewAudio, PreviewAudio, Any Switch (rgthree), CLIPTextEncode, ImageResizeKJv2, PreviewImage, PrimitiveStringMultiline, LoadImage, PrimitiveInt, PrimitiveInt, LTXVAudioVAELoader, Qwen3TTSVoiceClone, SaveAudioAdvanced, VHS_VideoCombine, LoadAudio, PrimitiveStringMultiline, CFGGuider, LTXVImgToVideoInplaceKJ, GroupSwitcher, Qwen3TTSModelLoader, CheckpointLoaderSimple]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "10Eros_v1.4_fp8mixed_learned.safetensors", "denoise": 1, "height": 80, "lora_name": "ltx-2.3-22b-distilled-lora-1.1_fro90_ceil72_condsafe.safetensors", "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "strength_clip": 1, "strength_model": 0.5800000000000001, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/数字人LTX2.3 Eros首尾帧一致_2092114420569825281.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/数字人LTX2.3 Eros首尾帧一致_2092114420569825281.json`

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
- `LTXLatentAnchorAware`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `LTXTextAttentionAmplifier`
- `LTX2SamplingPreviewOverride`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `LTXAVTextEncoderLoader`
- `ImageScaleBy`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `ShowText|pysssss`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `Sigmas Easing`
- `KSamplerSelect` ★核心
- `STGGuiderAdvanced`
- `RandomNoise`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `ComfyMathExpression`
- `GetNode`
- `LTXVConditioning`
- `LTXVImgToVideoInplaceKJ`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `LTX2LoraLoaderAdvanced` ★核心
- `LTX2LoraLoaderAdvanced` ★核心
- `LTX2LoraLoaderAdvanced` ★核心
- `LTX2LoraLoaderAdvanced` ★核心
- `Apply Whisper`
- `LoraLoaderModelOnly` ★核心
- `easy showAnything`
- `SetNode`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
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
- `LatentUpscaleModelLoader`
- `LTXVLatentUpsamplerTiled` ★核心
- `LTXVLatentUpsampler` ★核心
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
- `GetNode`
- `easy float`
- `GetImageSize`
- `LoadAudio`
- `GetNode`
- `PreviewAudio`
- `PreviewAudio`
- `Any Switch (rgthree)`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `LoadImage`
- `PrimitiveInt`
- `PrimitiveInt`
- `LTXVAudioVAELoader`
- `Qwen3TTSVoiceClone`
- `SaveAudioAdvanced`
- `VHS_VideoCombine`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `CFGGuider`
- `LTXVImgToVideoInplaceKJ`
- `GroupSwitcher`
- `Qwen3TTSModelLoader`
- `CheckpointLoaderSimple` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `lora_name` = `ltx-2.3-22b-distilled-lora-1.1_fro90_ceil72_condsafe.safetensors`
- `strength_model` = `0.5800000000000001`
- `strength_clip` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `10Eros_v1.4_fp8mixed_learned.safetensors`

## 知识

覆盖率 **61%**（97/158）

**有卡**：`ManualSigmas`、`LTXVConcatAVLatent`、`KSamplerSelect`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`VAELoaderKJ`、`LTXVAudioVAEDecode`、`LTXVCropGuides`、`LTXLatentAnchorAware`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`LTXVEmptyLatentAudio`、`LTXTextAttentionAmplifier`、`LTX2SamplingPreviewOverride`、`LTXAVTextEncoderLoader`、`ImageScaleBy`、`EmptyLTXVLatentVideo`、`VAEDecode`、`ComfyMathExpression`、`Sigmas Easing`、`STGGuiderAdvanced`、`RandomNoise`、`VHS_VideoCombine`、`LTXVConditioning`、`LTXVImgToVideoInplaceKJ`、`CLIPTextEncode`、`LTX2LoraLoaderAdvanced`、`Apply Whisper`、`LoraLoaderModelOnly`、`LTXVAudioVAEEncode`、`LTXVAudioVideoMask`、`SolidMask`、`TrimAudioDuration`、`AudioAdjustVolume`、`ImageFromBatch`、`SoundFlow_GetLength`、`SetLatentNoiseMask`、`LatentUpscaleModelLoader`、`LTXVLatentUpsamplerTiled`、`LTXVLatentUpsampler`、`UNETLoader`、`KSampler`、`solarL_SaveImagesToZip`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`、`easy float`、`GetImageSize`、`LoadAudio`、`PreviewAudio`、`ImageResizeKJv2`、`LoadImage`、`LTXVAudioVAELoader`、`Qwen3TTSVoiceClone`、`SaveAudioAdvanced`、`CFGGuider`、`GroupSwitcher`、`Qwen3TTSModelLoader`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
