---
key: 平台全量/LTX2.3_自定义音频+人物动作迁移V3（单采IDLoRA）_2044017351640748034.json
name: LTX2.3_自定义音频+人物动作迁移V3（单采IDLoRA）_2044017351640748034
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/LTX2.3_自定义音频+人物动作迁移V3（单采IDLoRA）_2044017351640748034.json
hash: f285804ce5c81bbe
coverage: 0.693333
learned_at: 2026-11-14 00:38:25
nodes: [VHS_VideoInfoLoaded, SetNode, easy imageSizeBySide, GetNode, easy positive, ComfyMathExpression, GetNode, GetNode, ResizeImageMaskNode, EmptyLTXVLatentVideo, LTXVConditioning, GetImageSize, CLIPTextEncode, GetNode, SetNode, ResizeImageMaskNode, LTXVPreprocess, MelBandRoFormerSampler, LTXVAudioVAEEncode, SetNode, SolidMask, LTXAddVideoICLoRAGuide, LTXVImgToVideoConditionOnly, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, LTXVCropGuides, GetNode, VAEDecodeTiled, PrimitiveStringMultiline, CLIPTextEncode, GetNode, SetNode, SetNode, UNETLoader, SetNode, SetNode, LTXICLoRALoaderModelOnly, LoraLoaderModelOnly, VHS_LoadVideo, LoadImage, LoadAudio, ComfyMathExpression, VAELoaderKJ, DualCLIPLoader, VAELoaderKJ, ResizeImageMaskNode, DWPreprocessor, GetNode, LTXVSeparateAVLatent, LTXVReferenceAudio, GetNode, GetNode, PathchSageAttentionKJ, ModelPatchTorchSettings, LTXVChunkFeedForward, VHS_VideoCombine, MelBandRoFormerModelLoader, ComfyMathExpression, Qwen3ASRTranscribe, Qwen3ASRLoader, SetLatentNoiseMask, easy ifElse, LTXVEmptyLatentAudio, easy promptReplace, GetNode, LTXVConcatAVLatent, GetNode, LTXVAudioVAEDecode, easy ifElse, GetNode, GetNode, PrimitiveBoolean]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 97}
---

# 平台全量/LTX2.3_自定义音频+人物动作迁移V3（单采IDLoRA）_2044017351640748034.json

> 来源文件 `comfyui_library/workflows/平台全量/LTX2.3_自定义音频+人物动作迁移V3（单采IDLoRA）_2044017351640748034.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（75 个）：
- `VHS_VideoInfoLoaded`
- `SetNode`
- `easy imageSizeBySide`
- `GetNode`
- `easy positive`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `EmptyLTXVLatentVideo`
- `LTXVConditioning`
- `GetImageSize`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `ResizeImageMaskNode`
- `LTXVPreprocess`
- `MelBandRoFormerSampler` ★核心
- `LTXVAudioVAEEncode` ★核心
- `SetNode`
- `SolidMask`
- `LTXAddVideoICLoRAGuide`
- `LTXVImgToVideoConditionOnly`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVCropGuides`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `PrimitiveStringMultiline`
- `CLIPTextEncode` ★核心
- `GetNode`
- `SetNode`
- `SetNode`
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `LTXICLoRALoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VHS_LoadVideo`
- `LoadImage`
- `LoadAudio`
- `ComfyMathExpression`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `VAELoaderKJ`
- `ResizeImageMaskNode`
- `DWPreprocessor`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LTXVReferenceAudio`
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `ModelPatchTorchSettings`
- `LTXVChunkFeedForward`
- `VHS_VideoCombine`
- `MelBandRoFormerModelLoader`
- `ComfyMathExpression`
- `Qwen3ASRTranscribe`
- `Qwen3ASRLoader`
- `SetLatentNoiseMask`
- `easy ifElse`
- `LTXVEmptyLatentAudio` ★核心
- `easy promptReplace`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `easy ifElse`
- `GetNode`
- `GetNode`
- `PrimitiveBoolean`

## 关键参数

- `width` = `97`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **69%**（52/75）

**有卡**：`VHS_VideoInfoLoaded`、`easy imageSizeBySide`、`easy positive`、`ComfyMathExpression`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`LTXVConditioning`、`GetImageSize`、`CLIPTextEncode`、`LTXVPreprocess`、`MelBandRoFormerSampler`、`LTXVAudioVAEEncode`、`SolidMask`、`LTXAddVideoICLoRAGuide`、`LTXVImgToVideoConditionOnly`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`LTXVCropGuides`、`VAEDecodeTiled`、`UNETLoader`、`LTXICLoRALoaderModelOnly`、`LoraLoaderModelOnly`、`VHS_LoadVideo`、`LoadImage`、`LoadAudio`、`VAELoaderKJ`、`DualCLIPLoader`、`DWPreprocessor`、`LTXVSeparateAVLatent`、`LTXVReferenceAudio`、`PathchSageAttentionKJ`、`ModelPatchTorchSettings`、`LTXVChunkFeedForward`、`VHS_VideoCombine`、`MelBandRoFormerModelLoader`、`Qwen3ASRTranscribe`、`Qwen3ASRLoader`、`SetLatentNoiseMask`、`LTXVEmptyLatentAudio`、`easy promptReplace`、`LTXVConcatAVLatent`、`LTXVAudioVAEDecode`、`PrimitiveBoolean`

**用到的条目**：LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、MelBandRoFormerSampler、SamplerCustomAdvanced
