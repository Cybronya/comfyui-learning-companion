---
key: 视频生成/图生视频/ltx2.3-PromptRelay-4宫格工作流-1.66-24G_2063565423085445122.json
name: ltx2.3-PromptRelay-4宫格工作流-1.66-24G_2063565423085445122.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/ltx2.3-PromptRelay-4宫格工作流-1.66-24G_2063565423085445122.json
hash: 8b6ae2515f932e18
coverage: 0.457317
learned_at: 2026-10-15 22:39:15
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, ManualSigmas, ManualSigmas, LTX2MemoryEfficientSageAttentionPatch, LTXVChunkFeedForward, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, ComfyMathExpression, GetNode, GetNode, LTXVAudioVAEDecode, GetNode, LTXVSeparateAVLatent, PathchSageAttentionKJ, SetNode, GetNode, GetNode, LTX2AttentionTunerPatch, GetNode, SetNode, SetNode, SetNode, LTXVSeparateAVLatent, GetNode, ComfyMathExpression, GetNode, ComfyMathExpression, SetNode, GetNode, GetNode, ComfyMathExpression, GetNode, SamplerCustomAdvanced, SamplerCustomAdvanced, VAELoader, VAEDecodeTiled, GetNode, GetNode, CFGGuider, SetNode, PrimitiveFloat, ComfyMathExpression, KSamplerSelect, RandomNoise, PrimitiveFloat, PrimitiveFloat, ComfyMathExpression, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LTXVCropGuides, LTXVLatentUpsampler, GetNode, GetNode, GetNode, GetNode, GetNode, CFGGuider, GetNode, SetNode, SetNode, GetNode, LTXVCropGuides, LTXVConditioning, LTXVEmptyLatentAudio, LTXVConcatAVLatent, UNETLoader, DualCLIPLoader, VAELoader, VAELoaderKJ, VHS_VideoCombine, RandomNoise, GetNode, SetNode, LatentUpscaleModelLoader, ComfyMathExpression, LoraLoaderModelOnly, GetNode, GuHaiAutoImageSplit, PrimitiveNode, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, SetNode, GetNode, GetNode, GetNode, GetNode, ResizeImagesByLongerEdge, GetNode, GetNode, ImageFromBatch+, GetNode, GetNode, GetNode, LTXVScheduler, GetNode, ManualSigmas, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, ResizeImagesByLongerEdge, LTXVPreprocess, LTXVPreprocess, LTXVPreprocess, LTXVPreprocess, LTX2SamplingPreviewOverride, LTXVConcatAVLatent, SetNode, LTX2_NAG, SetNode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, ResizeImageMaskNode, ResizeImageMaskNode, ResizeImageMaskNode, SetNode, ResizeImageMaskNode, EmptyLTXVLatentVideo, INTConstant, SetNode, INTConstant, SetNode, INTConstant, SetNode, INTConstant, SetNode, INTConstant, INTConstant, CLIPTextEncode, LTXVAddGuideMulti, LTXVAddGuideMulti, LoraLoaderModelOnly, LoraLoaderModelOnly, PromptRelayEncodeTimeline, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 361}
---

# 视频生成/图生视频/ltx2.3-PromptRelay-4宫格工作流-1.66-24G_2063565423085445122.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2063565423085445122.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（164 个）：
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
- `SetNode`
- `GetNode`
- `ManualSigmas`
- `ManualSigmas`
- `LTX2MemoryEfficientSageAttentionPatch`
- `LTXVChunkFeedForward`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `GetNode`
- `LTXVSeparateAVLatent`
- `PathchSageAttentionKJ`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTX2AttentionTunerPatch`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVSeparateAVLatent`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `GetNode`
- `CFGGuider`
- `SetNode`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CFGGuider`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `LTXVCropGuides`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio` ★核心
- `LTXVConcatAVLatent`
- `UNETLoader` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `RandomNoise`
- `GetNode`
- `SetNode`
- `LatentUpscaleModelLoader`
- `ComfyMathExpression`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GuHaiAutoImageSplit`
- `PrimitiveNode`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ResizeImagesByLongerEdge`
- `GetNode`
- `GetNode`
- `ImageFromBatch+`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVScheduler`
- `GetNode`
- `ManualSigmas`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTXVPreprocess`
- `LTX2SamplingPreviewOverride`
- `LTXVConcatAVLatent`
- `SetNode`
- `LTX2_NAG`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `SetNode`
- `ResizeImageMaskNode`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `LTXVAddGuideMulti`
- `LTXVAddGuideMulti`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `PromptRelayEncodeTimeline`
- `LoadImage`

## 关键参数

- `width` = `361`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **46%**（75/164）

**有卡**：`ManualSigmas`、`LTX2MemoryEfficientSageAttentionPatch`、`LTXVChunkFeedForward`、`KSamplerSelect`、`ComfyMathExpression`、`LTXVAudioVAEDecode`、`LTXVSeparateAVLatent`、`PathchSageAttentionKJ`、`LTX2AttentionTunerPatch`、`SamplerCustomAdvanced`、`VAELoader`、`VAEDecodeTiled`、`CFGGuider`、`RandomNoise`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVConditioning`、`LTXVEmptyLatentAudio`、`LTXVConcatAVLatent`、`UNETLoader`、`DualCLIPLoader`、`VAELoaderKJ`、`VHS_VideoCombine`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`GuHaiAutoImageSplit`、`ImageFromBatch+`、`ResizeImagesByLongerEdge`、`LTXVScheduler`、`LTXVPreprocess`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`ResizeImageMaskNode`、`EmptyLTXVLatentVideo`、`INTConstant`、`CLIPTextEncode`、`LTXVAddGuideMulti`、`PromptRelayEncodeTimeline`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
