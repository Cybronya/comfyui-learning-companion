---
key: 平台全量/LTX2.3_自定义音频+人物动作迁移V4（三采IDLoRA）_2044022005221036033.json
name: LTX2.3_自定义音频+人物动作迁移V4（三采IDLoRA）_2044022005221036033
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3_自定义音频+人物动作迁移V4（三采IDLoRA）_2044022005221036033.json
hash: 1e1fb3818f01dae7
coverage: 0.718447
learned_at: 2026-11-14 00:38:26
nodes: [SetNode, VHS_VideoInfoLoaded, SetNode, GetNode, easy imageSizeBySide, easy positive, CFGGuider, ManualSigmas, SamplerCustomAdvanced, KSamplerSelect, RandomNoise, LTXVConcatAVLatent, ComfyMathExpression, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, ResizeImageMaskNode, ResizeImageMaskNode, EmptyLTXVLatentVideo, LTXVConditioning, GetImageSize, CLIPTextEncode, GetNode, VAEDecodeTiled, ComfyMathExpression, ResizeImageMaskNode, SetNode, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, SamplerCustomAdvanced, ComfyMathExpression, GetNode, GetNode, ResizeImageMaskNode, LTXVPreprocess, MelBandRoFormerSampler, LTXVAudioVAEEncode, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, GetNode, GetNode, GetNode, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, LTXVConcatAVLatent, GetNode, LTXVSeparateAVLatent, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, GetNode, SolidMask, GetNode, LTXAddVideoICLoRAGuide, LTXVImgToVideoConditionOnly, GetNode, PrimitiveStringMultiline, SetNode, SetNode, SetNode, SetNode, SetNode, LTXICLoRALoaderModelOnly, LoraLoaderModelOnly, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, UNETLoader, LatentUpscaleModelLoader, MelBandRoFormerModelLoader, LoadImage, VHS_LoadVideo, GetNode, ComfyMathExpression, LTXVEmptyLatentAudio, LoadAudio, CLIPTextEncode, easy ifElse, LTXVAudioVAEDecode, easy ifElse, GetNode, PrimitiveBoolean, DWPreprocessor, Qwen3ASRLoader, Qwen3ASRTranscribe, VHS_VideoCombine, LTXVReferenceAudio, PrimitiveInt, SetLatentNoiseMask, GetNode, easy promptReplace]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX2.3_自定义音频+人物动作迁移V4（三采IDLoRA）_2044022005221036033.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3_自定义音频+人物动作迁移V4（三采IDLoRA）_2044022005221036033.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（103 个）：
- `SetNode`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `GetNode`
- `easy imageSizeBySide`
- `easy positive`
- `CFGGuider`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `LTXVConcatAVLatent`
- `ComfyMathExpression`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VAEDecodeTiled` ★核心
- `ComfyMathExpression`
- `ResizeImageMaskNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `SamplerCustomAdvanced` ★核心
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `GetNode`
- `SolidMask`
- `GetNode`
- `LTXAddVideoICLoRAGuide`
- `LTXVImgToVideoConditionOnly`
- `GetNode`
- `PrimitiveStringMultiline`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXICLoRALoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `UNETLoader` ★核心
- `LatentUpscaleModelLoader`
- `MelBandRoFormerModelLoader`
- `LoadImage`
- `VHS_LoadVideo`
- `GetNode`
- `ComfyMathExpression`
- `LTXVEmptyLatentAudio` ★核心
- `LoadAudio`
- `CLIPTextEncode` ★核心
- `easy ifElse`
- `LTXVAudioVAEDecode` ★核心
- `easy ifElse`
- `GetNode`
- `PrimitiveBoolean`
- `DWPreprocessor`
- `Qwen3ASRLoader`
- `Qwen3ASRTranscribe`
- `VHS_VideoCombine`
- `LTXVReferenceAudio`
- `PrimitiveInt`
- `SetLatentNoiseMask`
- `GetNode`
- `easy promptReplace`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **72%**（74/103）

**有卡**：`VHS_VideoInfoLoaded`、`easy imageSizeBySide`、`easy positive`、`CFGGuider`、`ManualSigmas`、`SamplerCustomAdvanced`、`KSamplerSelect`、`RandomNoise`、`LTXVConcatAVLatent`、`ComfyMathExpression`、`LTXVSeparateAVLatent`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`GetImageSize`、`CLIPTextEncode`、`VAEDecodeTiled`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVImgToVideoInplace`、`LTXVPreprocess`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SolidMask`、`LTXAddVideoICLoRAGuide`、`LTXVImgToVideoConditionOnly`、`LTXICLoRALoaderModelOnly`、`LoraLoaderModelOnly`、`VAELoaderKJ`、`DualCLIPLoader`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`UNETLoader`、`LatentUpscaleModelLoader`、`MelBandRoFormerModelLoader`、`LoadImage`、`VHS_LoadVideo`、`LTXVEmptyLatentAudio`、`LoadAudio`、`LTXVAudioVAEDecode`、`PrimitiveBoolean`、`DWPreprocessor`、`Qwen3ASRLoader`、`Qwen3ASRTranscribe`、`VHS_VideoCombine`、`LTXVReferenceAudio`、`SetLatentNoiseMask`、`easy promptReplace`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、LTXVLatentUpsampler、MelBandRoFormerSampler
