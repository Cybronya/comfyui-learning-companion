---
key: 视频生成/图生视频/Ltx2.3 MSR导演分镜全模态_2070834742676779009.json
name: Ltx2.3 MSR导演分镜全模态_2070834742676779009.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Ltx2.3 MSR导演分镜全模态_2070834742676779009.json
hash: 16bb26badfe7f5a6
coverage: 0.58042
learned_at: 2026-10-15 22:40:42
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, PathchSageAttentionKJ, LTXVChunkFeedForward, LTX2AttentionTunerPatch, GetNode, GetNode, GetNode, GetNode, LTXVLatentUpsampler, GetNode, GetNode, ManualSigmas, GetNode, GetNode, ManualSigmas, GetNode, LatentUpscaleModelLoader, VAELoader, VAELoaderKJ, VAELoader, LoraLoaderModelOnly, SetNode, GetNode, GetNode, DualCLIPLoader, KSamplerSelect, EmptyAudio, CFGGuider, ImageBatchMulti, SetNode, LTXVAddGuidesFromBatch, BasicScheduler, SetNode, LoraLoaderModelOnly, easy timelineInfoOutput, SetNode, SetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, LTXVAddGuideMulti, RandomNoise, LTXAddVideoICLoRAGuide, GetNode, GetNode, GetNode, SetNode, LTXVSeparateAVLatent, GetNode, RH_LLMAPI_NODE, TTP_text_mix, StringReplace, StringReplace, LTX2_NAG, GetNode, ComfySwitchNode, ComfyMathExpression, GetImageSizeAndCount, GetNode, SetNode, SetNode, Reroute, VHS_GetImageCount, MathExpression|pysssss, GetImageRangeFromBatch, MathExpression|pysssss, CLIPTextEncode, ComfyMathExpression, LTXVAddGuideMulti, SetNode, PrimitiveFloat, SetNode, LTXVConcatAVLatent, easy timelineSegmentOutput, LoraLoaderModelOnly, VAEDecode, LTXVAudioVAEDecode, GetNode, GetNode, ComfySwitchNode, SetNode, GetNode, LTXVAudioVAEDecode, SamplerCustomAdvanced, ManualSigmas, LTXAddVideoICLoRAGuide, LTXVConditioning, PromptRelayEncode, LTXVAddGuidesFromBatch, LTXVSeparateAVLatent, RandomNoise, GetNode, ComfyMathExpression, LTXVConcatAVLatent, KSamplerSelect, CFGGuider, ModelSamplingSD3, LTX2SamplingPreviewOverride, LTXICLoRALoaderModelOnly, ImageBatchRepeatInterleaving, SamplerCustomAdvanced, GetNode, EmptyLTXVLatentVideo, SplitStringByDelimiter, SeedGenerator, LTXVEmptyLatentAudio, SetNode, SimpleCalculatorKJ, SetNode, UNETLoader, easy timelineSegmentCount, Image Batch, ImageBatchRepeatInterleaving, LTXVCropGuides, PreviewAny, TextInput_, VRAM_Debug, easy timelineEditor, easy forLoopStart, easy batchAnything, AudioConcat, easy forLoopEnd, LTXVCropGuides, VAEDecode, GetNode, GetNode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 24, "width": 145}
---

# 视频生成/图生视频/Ltx2.3 MSR导演分镜全模态_2070834742676779009.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2070834742676779009.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（143 个）：
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
- `GetNode`
- `PathchSageAttentionKJ`
- `LTXVChunkFeedForward`
- `LTX2AttentionTunerPatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `GetNode`
- `GetNode`
- `ManualSigmas`
- `GetNode`
- `LatentUpscaleModelLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `DualCLIPLoader`
- `KSamplerSelect` ★核心
- `EmptyAudio`
- `CFGGuider`
- `ImageBatchMulti`
- `SetNode`
- `LTXVAddGuidesFromBatch`
- `BasicScheduler`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `easy timelineInfoOutput`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVAddGuideMulti`
- `RandomNoise`
- `LTXAddVideoICLoRAGuide`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `RH_LLMAPI_NODE`
- `TTP_text_mix`
- `StringReplace`
- `StringReplace`
- `LTX2_NAG`
- `GetNode`
- `ComfySwitchNode`
- `ComfyMathExpression`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `SetNode`
- `Reroute`
- `VHS_GetImageCount`
- `MathExpression|pysssss`
- `GetImageRangeFromBatch`
- `MathExpression|pysssss`
- `CLIPTextEncode` ★核心
- `ComfyMathExpression`
- `LTXVAddGuideMulti`
- `SetNode`
- `PrimitiveFloat`
- `SetNode`
- `LTXVConcatAVLatent`
- `easy timelineSegmentOutput`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `SetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `LTXAddVideoICLoRAGuide`
- `LTXVConditioning`
- `PromptRelayEncode`
- `LTXVAddGuidesFromBatch`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `GetNode`
- `ComfyMathExpression`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `ModelSamplingSD3`
- `LTX2SamplingPreviewOverride`
- `LTXICLoRALoaderModelOnly` ★核心
- `ImageBatchRepeatInterleaving`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `EmptyLTXVLatentVideo`
- `SplitStringByDelimiter`
- `SeedGenerator`
- `LTXVEmptyLatentAudio` ★核心
- `SetNode`
- `SimpleCalculatorKJ`
- `SetNode`
- `UNETLoader` ★核心
- `easy timelineSegmentCount`
- `Image Batch`
- `ImageBatchRepeatInterleaving`
- `LTXVCropGuides`
- `PreviewAny`
- `TextInput_`
- `VRAM_Debug`
- `easy timelineEditor`
- `easy forLoopStart`
- `easy batchAnything`
- `AudioConcat`
- `easy forLoopEnd`
- `LTXVCropGuides`
- `VAEDecode` ★核心
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 关键参数

- `width` = `145`
- `height` = `24`
- `batch_size` = `1`

## 知识

覆盖率 **58%**（83/143）

**有卡**：`PathchSageAttentionKJ`、`LTXVChunkFeedForward`、`LTX2AttentionTunerPatch`、`LTXVLatentUpsampler`、`ManualSigmas`、`LatentUpscaleModelLoader`、`VAELoader`、`VAELoaderKJ`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`KSamplerSelect`、`EmptyAudio`、`CFGGuider`、`ImageBatchMulti`、`LTXVAddGuidesFromBatch`、`BasicScheduler`、`easy timelineInfoOutput`、`LTXVAddGuideMulti`、`RandomNoise`、`LTXAddVideoICLoRAGuide`、`LTXVSeparateAVLatent`、`RH_LLMAPI_NODE`、`TTP_text_mix`、`StringReplace`、`LTX2_NAG`、`ComfyMathExpression`、`GetImageSizeAndCount`、`VHS_GetImageCount`、`MathExpression|pysssss`、`GetImageRangeFromBatch`、`CLIPTextEncode`、`LTXVConcatAVLatent`、`easy timelineSegmentOutput`、`VAEDecode`、`LTXVAudioVAEDecode`、`SamplerCustomAdvanced`、`LTXVConditioning`、`PromptRelayEncode`、`ModelSamplingSD3`、`LTX2SamplingPreviewOverride`、`LTXICLoRALoaderModelOnly`、`ImageBatchRepeatInterleaving`、`EmptyLTXVLatentVideo`、`SplitStringByDelimiter`、`SeedGenerator`、`LTXVEmptyLatentAudio`、`SimpleCalculatorKJ`、`UNETLoader`、`easy timelineSegmentCount`、`Image Batch`、`LTXVCropGuides`、`TextInput_`、`VRAM_Debug`、`easy timelineEditor`、`easy forLoopStart`、`easy batchAnything`、`AudioConcat`、`easy forLoopEnd`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
