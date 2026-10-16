---
key: 视频生成/图生视频/Sulphur-2 timelinePrompt时序视频_2053346294621589505.json
name: Sulphur-2 timelinePrompt时序视频_2053346294621589505.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2053346294621589505.json
hash: bba526d138fe362c
coverage: 0.508197
learned_at: 2026-10-15 22:37:38
nodes: [SetNode, MarkdownNote, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, LTXVConcatAVLatent, GetNode, SetNode, ManualSigmas, ManualSigmas, LTXVSeparateAVLatent, GetNode, GetNode, GetNode, LTX2AttentionTunerPatch, GetNode, GetNode, SamplerCustomAdvanced, GetNode, GetNode, LTXVLatentUpsampler, GetNode, GetNode, KSamplerSelect, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, LTXVImgToVideoInplace, RandomNoise, GetNode, GetNode, SetNode, GetNode, SetNode, CLIPTextEncode, LTX2_NAG, LTXVConditioning, LTXVConcatAVLatent, MarkdownNote, PrimitiveBoolean, GetNode, ComfyMathExpression, ComfyMathExpression, SimpleCalculatorKJ, LTXVEmptyLatentAudio, INTConstant, INTConstant, GetNode, SetNode, LTX2SamplingPreviewOverride, SetNode, GetNode, GetNode, VAEDecodeTiled, GetNode, GetNode, SamplerCustomAdvanced, LTXVSeparateAVLatent, VAEDecodeTiled, LTXVAudioVAEDecode, SetNode, LTXVAudioVAEDecode, GetNode, GetNode, PrimitiveNode, PrimitiveFloat, VHS_VideoCombine, LTXVImgToVideoInplace, GetNode, GetNode, PathchSageAttentionKJ, LTX2MemoryEfficientSageAttentionPatch, LTXVChunkFeedForward, SetNode, GetNode, CFGGuider, SetNode, EmptyLTXVLatentVideo, GetNode, LTXVScheduler, KSamplerSelect, ManualSigmas, CFGGuider, LTXVScheduler, RandomNoise, SeedGenerator, LoraLoaderModelOnly, ResizeImagesByLongerEdge, LTXVPreprocess, ImageResizeKJv2, VAELoader, VHS_VideoCombine, DualCLIPLoader, MarkdownNote, SetNode, SetNode, VAELoaderKJ, LTXAVTextEncoderLoader, LTXVAudioVAELoader, SetNode, easy ckptNames, SetNode, easy ckptNames, VAELoader, CheckpointLoaderSimple, LatentUpscaleModelLoader, PathchSageAttentionKJ, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadImage, MarkdownNote, MarkdownNote, MarkdownNote, PromptRelayEncodeTimeline]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "ltx-2.3-22b-dev-fp8.safetensors", "height": 25, "width": 241}
---

# 视频生成/图生视频/Sulphur-2 timelinePrompt时序视频_2053346294621589505.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2053346294621589505.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（122 个）：
- `SetNode`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `GetNode`
- `SetNode`
- `ManualSigmas`
- `ManualSigmas`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTX2AttentionTunerPatch`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVImgToVideoInplace`
- `RandomNoise`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `LTX2_NAG`
- `LTXVConditioning`
- `LTXVConcatAVLatent`
- `MarkdownNote`
- `PrimitiveBoolean`
- `GetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SimpleCalculatorKJ`
- `LTXVEmptyLatentAudio` ★核心
- `INTConstant`
- `INTConstant`
- `GetNode`
- `SetNode`
- `LTX2SamplingPreviewOverride`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `GetNode`
- `PrimitiveNode`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `LTXVImgToVideoInplace`
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `LTX2MemoryEfficientSageAttentionPatch`
- `LTXVChunkFeedForward`
- `SetNode`
- `GetNode`
- `CFGGuider`
- `SetNode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `LTXVScheduler`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `CFGGuider`
- `LTXVScheduler`
- `RandomNoise`
- `SeedGenerator`
- `LoraLoaderModelOnly` ★核心
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `ImageResizeKJv2`
- `VAELoader`
- `VHS_VideoCombine`
- `DualCLIPLoader`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `VAELoaderKJ`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `SetNode`
- `easy ckptNames`
- `SetNode`
- `easy ckptNames`
- `VAELoader`
- `CheckpointLoaderSimple` ★核心
- `LatentUpscaleModelLoader`
- `PathchSageAttentionKJ`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `PromptRelayEncodeTimeline`

## 关键参数

- `width` = `241`
- `height` = `25`
- `batch_size` = `1`
- `checkpoint` = `ltx-2.3-22b-dev-fp8.safetensors`

## 知识

覆盖率 **51%**（62/122）

**有卡**：`LTXVConcatAVLatent`、`ManualSigmas`、`LTXVSeparateAVLatent`、`LTX2AttentionTunerPatch`、`SamplerCustomAdvanced`、`LTXVLatentUpsampler`、`KSamplerSelect`、`LTXVImgToVideoInplace`、`RandomNoise`、`CLIPTextEncode`、`LTX2_NAG`、`LTXVConditioning`、`PrimitiveBoolean`、`ComfyMathExpression`、`SimpleCalculatorKJ`、`LTXVEmptyLatentAudio`、`INTConstant`、`LTX2SamplingPreviewOverride`、`VAEDecodeTiled`、`LTXVAudioVAEDecode`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`LTX2MemoryEfficientSageAttentionPatch`、`LTXVChunkFeedForward`、`CFGGuider`、`EmptyLTXVLatentVideo`、`LTXVScheduler`、`SeedGenerator`、`LoraLoaderModelOnly`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`ImageResizeKJv2`、`VAELoader`、`DualCLIPLoader`、`VAELoaderKJ`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`easy ckptNames`、`CheckpointLoaderSimple`、`LatentUpscaleModelLoader`、`LoadImage`、`PromptRelayEncodeTimeline`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
