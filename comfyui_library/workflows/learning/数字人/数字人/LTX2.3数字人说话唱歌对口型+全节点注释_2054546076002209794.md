---
key: 数字人/数字人/LTX2.3数字人说话唱歌对口型+全节点注释_2054546076002209794.json
name: LTX2.3数字人说话唱歌对口型+全节点注释_2054546076002209794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3数字人说话唱歌对口型+全节点注释_2054546076002209794.json
hash: 10d9c7848c81ef63
coverage: 0.445545
learned_at: 2026-10-26 01:56:08
nodes: [SolidMask, LTXVConcatAVLatent, SetNode, SetNode, BasicScheduler, KSamplerSelect, CFGGuider, SetLatentNoiseMask, LTX2SamplingPreviewOverride, LTXVAudioVAEEncode, SimpleCalculatorKJ, RandomNoise, VAELoader, VAELoaderKJ, INTConstant, TrimAudioDuration, INTConstant, INTConstant, ImageResizeKJv2, DualCLIPLoader, VAELoader, ImageResizeKJv2, SamplerCustomAdvanced, PathchSageAttentionKJ, LTX2AttentionTunerPatch, LTXVPreprocess, PrimitiveStringMultiline, JoinStrings, CLIPTextEncode, LTXVChunkFeedForward, UNETLoader, SimpleCalculatorKJ, LTXVConditioning, VAEDecode, LTXVSeparateAVLatent, LoraLoaderModelOnly, EmptyLTXVLatentVideo, INTConstant, PrimitiveFloat, LTXVImgToVideoInplaceKJ, LTX2_NAG, CLIPTextEncode, PrimitiveFloat, ModelSamplingSD3, PrimitiveStringMultiline, INTConstant, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, LoadImage, VHS_VideoCombine, LoadImage, SimpleCalculatorKJ, LoadAudio]
patterns: []
missing: []
---

# 数字人/数字人/LTX2.3数字人说话唱歌对口型+全节点注释_2054546076002209794.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3数字人说话唱歌对口型+全节点注释_2054546076002209794.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Other

**节点**（101 个）：
- `SolidMask`
- `LTXVConcatAVLatent`
- `SetNode`
- `SetNode`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `SetLatentNoiseMask`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEEncode` ★核心
- `SimpleCalculatorKJ`
- `RandomNoise`
- `VAELoader`
- `VAELoaderKJ`
- `INTConstant`
- `TrimAudioDuration`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `DualCLIPLoader`
- `VAELoader`
- `ImageResizeKJv2`
- `SamplerCustomAdvanced` ★核心
- `PathchSageAttentionKJ`
- `LTX2AttentionTunerPatch`
- `LTXVPreprocess`
- `PrimitiveStringMultiline`
- `JoinStrings`
- `CLIPTextEncode` ★核心
- `LTXVChunkFeedForward`
- `UNETLoader` ★核心
- `SimpleCalculatorKJ`
- `LTXVConditioning`
- `VAEDecode` ★核心
- `LTXVSeparateAVLatent`
- `LoraLoaderModelOnly` ★核心
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `PrimitiveFloat`
- `LTXVImgToVideoInplaceKJ`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `PrimitiveFloat`
- `ModelSamplingSD3`
- `PrimitiveStringMultiline`
- `INTConstant`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `LoadImage`
- `VHS_VideoCombine`
- `LoadImage`
- `SimpleCalculatorKJ`
- `LoadAudio`

## 知识

覆盖率 **45%**（45/101）

**有卡**：`SolidMask`、`LTXVConcatAVLatent`、`BasicScheduler`、`KSamplerSelect`、`CFGGuider`、`SetLatentNoiseMask`、`LTX2SamplingPreviewOverride`、`LTXVAudioVAEEncode`、`SimpleCalculatorKJ`、`RandomNoise`、`VAELoader`、`VAELoaderKJ`、`INTConstant`、`TrimAudioDuration`、`ImageResizeKJv2`、`DualCLIPLoader`、`SamplerCustomAdvanced`、`PathchSageAttentionKJ`、`LTX2AttentionTunerPatch`、`LTXVPreprocess`、`JoinStrings`、`CLIPTextEncode`、`LTXVChunkFeedForward`、`UNETLoader`、`LTXVConditioning`、`VAEDecode`、`LTXVSeparateAVLatent`、`LoraLoaderModelOnly`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplaceKJ`、`LTX2_NAG`、`ModelSamplingSD3`、`LoadImage`、`VHS_VideoCombine`、`LoadAudio`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
