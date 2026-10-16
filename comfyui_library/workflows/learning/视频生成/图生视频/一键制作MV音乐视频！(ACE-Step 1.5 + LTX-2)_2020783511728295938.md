---
key: 视频生成/图生视频/一键制作MV音乐视频！(ACE-Step 1.5 + LTX-2)_2020783511728295938.json
name: 一键制作MV音乐视频！(ACE-Step 1.5 + LTX-2)_2020783511728295938.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2020783511728295938.json
hash: b39ab15b26a49a43
coverage: 0.479675
learned_at: 2026-10-15 22:35:07
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, VAEDecodeTiled, ManualSigmas, LTXVConcatAVLatent, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, ResizeImageMaskNode, GetImageSize, GetNode, GetNode, GetNode, GetNode, SolidMask, SimpleMath+, GetNode, ImageResizeKJv2, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, LTXVConcatAVLatent, LTXVEmptyLatentAudio, EmptyLTXVLatentVideo, LTXVPreprocess, KSamplerSelect, KSamplerSelect, LTXVScheduler, SetNode, GetNode, LTXVLatentUpsampler, GetNode, RandomNoise, SetNode, SetNode, GetNode, LTXVImgToVideoInplace, ComfySwitchNode, SamplerCustomAdvanced, ResizeImagesByLongerEdge, GetNode, GetNode, GetNode, CFGGuider, SetNode, SetNode, SetLatentNoiseMask, GetNode, LTXVImgToVideoInplace, LTXVAudioVAEEncode, MelBandRoFormerSampler, GetNode, RandomNoise, SetNode, SetNode, SimpleCalculatorKJ, GetNode, GetNode, SetNode, SetNode, CLIPTextEncode, MarkdownNote, PrimitiveBoolean, LTXVConditioning, LTXVSeparateAVLatent, ComfySwitchNode, SamplerCustomAdvanced, LTXVSeparateAVLatent, VHS_VideoCombine, CFGGuider, MarkdownNote, MarkdownNote, MarkdownNote, ModelSamplingAuraFlow, ConditioningZeroOut, MarkdownNote, CheckpointLoaderSimple, KSampler, EmptyAceStep1.5LatentAudio, PrimitiveNode, TextEncodeAceStepAudio1.5, GetNode, GetNode, SimpleCalculatorKJ, INTConstant, INTConstant, PrimitiveFloat, DualCLIPLoaderGGUF, VAELoader, VAELoaderKJ, LatentUpscaleModelLoader, MelBandRoFormerModelLoader, UnetLoaderGGUF, GetNode, PrimitiveNode, CR Text, TrimAudioDuration, INTConstant, SetNode, LoraLoaderModelOnly, VAEDecodeAudio, SaveAudioMP3, CLIPTextEncode, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "ace_step_1.5_turbo_aio.safetensors", "denoise": 1, "height": 25, "sampler_name": "euler", "scheduler": "simple", "seed": 31, "steps": 8, "width": 121}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/一键制作MV音乐视频！(ACE-Step 1.5 + LTX-2)_2020783511728295938.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2020783511728295938.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（123 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `ResizeImageMaskNode`
- `GetImageSize`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SolidMask`
- `SimpleMath+`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio` ★核心
- `EmptyLTXVLatentVideo`
- `LTXVPreprocess`
- `KSamplerSelect` ★核心
- `KSamplerSelect` ★核心
- `LTXVScheduler`
- `SetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `RandomNoise`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `ComfySwitchNode`
- `SamplerCustomAdvanced` ★核心
- `ResizeImagesByLongerEdge`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `SetNode`
- `SetNode`
- `SetLatentNoiseMask`
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVAudioVAEEncode` ★核心
- `MelBandRoFormerSampler` ★核心
- `GetNode`
- `RandomNoise`
- `SetNode`
- `SetNode`
- `SimpleCalculatorKJ`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `MarkdownNote`
- `PrimitiveBoolean`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `ComfySwitchNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VHS_VideoCombine`
- `CFGGuider`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ModelSamplingAuraFlow`
- `ConditioningZeroOut`
- `MarkdownNote`
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心
- `EmptyAceStep1.5LatentAudio`
- `PrimitiveNode`
- `TextEncodeAceStepAudio1.5`
- `GetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `INTConstant`
- `INTConstant`
- `PrimitiveFloat`
- `DualCLIPLoaderGGUF`
- `VAELoader`
- `VAELoaderKJ`
- `LatentUpscaleModelLoader`
- `MelBandRoFormerModelLoader`
- `UnetLoaderGGUF` ★核心
- `GetNode`
- `PrimitiveNode`
- `CR Text`
- `TrimAudioDuration`
- `INTConstant`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeAudio` ★核心
- `SaveAudioMP3`
- `CLIPTextEncode` ★核心
- `LoadImage`

## 关键参数

- `width` = `121`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ace_step_1.5_turbo_aio.safetensors`
- `seed` = `31`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **48%**（59/123）

**有卡**：`VAEDecodeTiled`、`ManualSigmas`、`LTXVConcatAVLatent`、`ResizeImageMaskNode`、`GetImageSize`、`SolidMask`、`SimpleMath+`、`ImageResizeKJv2`、`LTXVAudioVAEDecode`、`LTXVEmptyLatentAudio`、`EmptyLTXVLatentVideo`、`LTXVPreprocess`、`KSamplerSelect`、`LTXVScheduler`、`LTXVLatentUpsampler`、`RandomNoise`、`LTXVImgToVideoInplace`、`SamplerCustomAdvanced`、`ResizeImagesByLongerEdge`、`CFGGuider`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`MelBandRoFormerSampler`、`SimpleCalculatorKJ`、`CLIPTextEncode`、`PrimitiveBoolean`、`LTXVConditioning`、`LTXVSeparateAVLatent`、`VHS_VideoCombine`、`ModelSamplingAuraFlow`、`ConditioningZeroOut`、`CheckpointLoaderSimple`、`KSampler`、`EmptyAceStep1.5LatentAudio`、`TextEncodeAceStepAudio1.5`、`INTConstant`、`DualCLIPLoaderGGUF`、`VAELoader`、`VAELoaderKJ`、`LatentUpscaleModelLoader`、`MelBandRoFormerModelLoader`、`UnetLoaderGGUF`、`CR Text`、`TrimAudioDuration`、`LoraLoaderModelOnly`、`VAEDecodeAudio`、`SaveAudioMP3`、`LoadImage`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、LoadImage、CFGGuider

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
