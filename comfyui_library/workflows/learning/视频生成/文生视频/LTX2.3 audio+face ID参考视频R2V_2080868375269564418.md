---
key: 视频生成/文生视频/LTX2.3 audio+face ID参考视频R2V_2080868375269564418.json
name: LTX2.3 audio+face ID参考视频R2V_2080868375269564418
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 audio+face ID参考视频R2V_2080868375269564418.json
hash: bddcfc6d3e344a4b
coverage: 0.482517
learned_at: 2026-10-15 22:44:58
nodes: [GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, VAEDecodeAudio, ComfySwitchNode, SimpleCalculatorKJ, PrimitiveBoolean, ComfySwitchNode, SetNode, GetNode, Reroute, PrimitiveBoolean, KSamplerSelect, INTConstant, GetNode, GetNode, GetNode, ComfyMathExpression, ComfySwitchNode, ComfyMathExpression, GetNode, RecordAudio, MelBandRoFormerSampler, SetNode, CLIPTextEncode, SetNode, SetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, SetNode, SetNode, SetNode, GetNode, ComfyNumberConvert, GetNode, GetNode, GetNode, SamplerCustomAdvanced, GetNode, KSamplerSelect, ManualSigmas, PrimitiveFloat, LTXVSeparateAVLatent, LTX2_NAG, LTX2SamplingPreviewOverride, GetNode, GetNode, GetNode, VAEDecodeTiled, LTXVChunkFeedForward, LTX2AttentionTunerPatch, CLIPTextEncode, LTXVEmptyLatentAudio, GetNode, GetNode, GetNode, LTXIdentityOverlapConditioning, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVSeparateAVLatent, GetNode, GetNode, LTXVCropGuides, LTXVLatentUpsampler, CFGGuider, MarkdownNote, ModelSamplingSD3, ManualSigmas, BasicScheduler, CFGGuider, GetNode, StringConcatenate, StringConcatenate, GetNode, GetNode, ComfySwitchNode, LTXIdentityOverlapConditioning, SetNode, UNETLoader, LatentUpscaleModelLoader, DualCLIPLoader, VAELoaderKJ, VAELoader, VAELoader, LTXVReferenceAudio, INTConstant, INTConstant, TrimAudioDuration, ComfySwitchNode, LTXVCropGuides, GetNode, GetNode, GetNode, MelBandRoFormerModelLoader, LoadAudio, EmptyLTXVLatentVideo, LTXVConditioning, TextGenerate, RandomNoise, RandomNoise, SeedGenerator, LTX2LoraLoaderAdvanced, PrimitiveStringMultiline, SetNode, RMBG, ImageResizeKJv2, ResizeImageMaskNode, PreviewImage, CropFace, LoadImage, VHS_VideoCombine, LTX2LoraLoaderAdvanced, Power Lora Loader (rgthree), LTX2MemoryEfficientSageAttentionPatch, PathchSageAttentionKJ, LoraLoaderModelOnly, PreviewAny, PreviewAny]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "lora_name": "ltx-2.3-ID-LoRA-TalkVid-3k-V1.0.safetensors", "strength_clip": 0, "strength_model": 1.5, "width": 97}
---

# 视频生成/文生视频/LTX2.3 audio+face ID参考视频R2V_2080868375269564418.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 audio+face ID参考视频R2V_2080868375269564418.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（143 个）：
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
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VAEDecodeAudio` ★核心
- `ComfySwitchNode`
- `SimpleCalculatorKJ`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `SetNode`
- `GetNode`
- `Reroute`
- `PrimitiveBoolean`
- `KSamplerSelect` ★核心
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `ComfySwitchNode`
- `ComfyMathExpression`
- `GetNode`
- `RecordAudio`
- `MelBandRoFormerSampler` ★核心
- `SetNode`
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `ComfyNumberConvert`
- `GetNode`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `PrimitiveFloat`
- `LTXVSeparateAVLatent`
- `LTX2_NAG`
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `LTXVChunkFeedForward`
- `LTX2AttentionTunerPatch`
- `CLIPTextEncode` ★核心
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXIdentityOverlapConditioning`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `CFGGuider`
- `MarkdownNote`
- `ModelSamplingSD3`
- `ManualSigmas`
- `BasicScheduler`
- `CFGGuider`
- `GetNode`
- `StringConcatenate`
- `StringConcatenate`
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `LTXIdentityOverlapConditioning`
- `SetNode`
- `UNETLoader` ★核心
- `LatentUpscaleModelLoader`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `VAELoader`
- `VAELoader`
- `LTXVReferenceAudio`
- `INTConstant`
- `INTConstant`
- `TrimAudioDuration`
- `ComfySwitchNode`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `GetNode`
- `MelBandRoFormerModelLoader`
- `LoadAudio`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `TextGenerate`
- `RandomNoise`
- `RandomNoise`
- `SeedGenerator`
- `LTX2LoraLoaderAdvanced` ★核心
- `PrimitiveStringMultiline`
- `SetNode`
- `RMBG`
- `ImageResizeKJv2`
- `ResizeImageMaskNode`
- `PreviewImage`
- `CropFace`
- `LoadImage`
- `VHS_VideoCombine`
- `LTX2LoraLoaderAdvanced` ★核心
- `Power Lora Loader (rgthree)`
- `LTX2MemoryEfficientSageAttentionPatch`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `PreviewAny`
- `PreviewAny`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`
- `lora_name` = `ltx-2.3-ID-LoRA-TalkVid-3k-V1.0.safetensors`
- `strength_model` = `1.5`
- `strength_clip` = `0`

## 知识

覆盖率 **48%**（69/143）

**有卡**：`VAEDecodeAudio`、`SimpleCalculatorKJ`、`PrimitiveBoolean`、`KSamplerSelect`、`INTConstant`、`ComfyMathExpression`、`RecordAudio`、`MelBandRoFormerSampler`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`ComfyNumberConvert`、`SamplerCustomAdvanced`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`VAEDecodeTiled`、`LTXVChunkFeedForward`、`LTX2AttentionTunerPatch`、`LTXVEmptyLatentAudio`、`LTXIdentityOverlapConditioning`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`CFGGuider`、`ModelSamplingSD3`、`BasicScheduler`、`StringConcatenate`、`UNETLoader`、`LatentUpscaleModelLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`VAELoader`、`LTXVReferenceAudio`、`TrimAudioDuration`、`MelBandRoFormerModelLoader`、`LoadAudio`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`TextGenerate`、`RandomNoise`、`SeedGenerator`、`LTX2LoraLoaderAdvanced`、`RMBG`、`ImageResizeKJv2`、`ResizeImageMaskNode`、`CropFace`、`LoadImage`、`VHS_VideoCombine`、`Power Lora Loader (rgthree)`、`LTX2MemoryEfficientSageAttentionPatch`、`PathchSageAttentionKJ`、`LoraLoaderModelOnly`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
