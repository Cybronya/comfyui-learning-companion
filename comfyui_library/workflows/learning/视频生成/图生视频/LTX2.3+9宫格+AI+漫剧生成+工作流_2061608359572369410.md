---
key: 视频生成/图生视频/LTX2.3+9宫格+AI+漫剧生成+工作流_2061608359572369410.json
name: LTX2.3+9宫格+AI+漫剧生成+工作流_2061608359572369410.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2061608359572369410.json
hash: 041184305c311219
coverage: 0.455446
learned_at: 2026-10-15 22:38:55
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, LTX2MemoryEfficientSageAttentionPatch, LTXVChunkFeedForward, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, PathchSageAttentionKJ, SetNode, LTXVScheduler, SetNode, GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, VAELoaderKJ, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, GetNode, GetNode, ComfyMathExpression, GetNode, SetNode, LTXVLatentUpsampler, LTXVCropGuides, LTXVSeparateAVLatent, GetNode, GetNode, SetNode, VAELoader, LTXVConcatAVLatent, LTXVConditioning, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, SetNode, ComfyMathExpression, GetNode, GetNode, EmptyLTXVLatentVideo, SamplerCustomAdvanced, RandomNoise, GetNode, DualCLIPLoader, ImageResizeKJv2, ComfyMathExpression, GuHaiAutoImageSplit, ImageResizeKJv2, ImageResizeKJv2, SetNode, SetNode, GetNode, CFGGuider, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, ManualSigmas, KSamplerSelect, LTX2SamplingPreviewOverride, GetNode, LatentUpscaleModelLoader, LoraLoaderModelOnly, LTX2AttentionTunerPatch, PreviewImage, TTResolutionSelector, UNETLoader, Note, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, PrimitiveFloat, PrimitiveFloat, LTXVAddGuideMulti, LTX2_NAG, GetNode, SetNode, SetNode, SetNode, SetNode, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, GetNode, GetNode, ImageResizeKJv2, CLIPTextEncode, ImageResizeKJv2, GetNode, GetNode, ImageFromBatch+, GetNode, ImageFromBatch+, GetNode, SetNode, GetNode, GetNode, GetNode, ComfyMathExpression, GetNode, LTXVEmptyLatentAudio, GetNode, RandomNoise, 1hewOffice_Qwen35397BA17B, PreviewAny, Note, VHS_VideoCombine, GetNode, LTXVAudioVAEDecode, SetNode, VAEDecodeTiled, GetNode, SetNode, LTXVCropGuides, GetNode, GetNode, LTXVSeparateAVLatent, ManualSigmas, LTXVConcatAVLatent, CFGGuider, KSamplerSelect, ManualSigmas, easy cleanGpuUsed, SamplerCustomAdvanced, LTXVAddGuideMulti, easy cleanGpuUsed, SetNode, LoraLoaderModelOnly, INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, PrimitiveNode, Textbox, MarkdownNote, GetNode, SetNode, PrimitiveFloat, PromptRelayEncodeTimeline, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 25, "width": 289}
---

# 视频生成/图生视频/LTX2.3+9宫格+AI+漫剧生成+工作流_2061608359572369410.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2061608359572369410.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（202 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTX2MemoryEfficientSageAttentionPatch`
- `LTXVChunkFeedForward`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `LTXVScheduler`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAELoaderKJ`
- `VAELoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `SetNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `GetNode`
- `GetNode`
- `SetNode`
- `VAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `SetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `EmptyLTXVLatentVideo`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `GetNode`
- `DualCLIPLoader`
- `ImageResizeKJv2`
- `ComfyMathExpression`
- `GuHaiAutoImageSplit`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `GetNode`
- `CFGGuider`
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
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `LTX2SamplingPreviewOverride`
- `GetNode`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly` ★核心
- `LTX2AttentionTunerPatch`
- `PreviewImage`
- `TTResolutionSelector`
- `UNETLoader` ★核心
- `Note`
- `SetNode`
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `LTXVAddGuideMulti`
- `LTX2_NAG`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `CLIPTextEncode` ★核心
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `ImageFromBatch+`
- `GetNode`
- `ImageFromBatch+`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `GetNode`
- `LTXVEmptyLatentAudio` ★核心
- `GetNode`
- `RandomNoise`
- `1hewOffice_Qwen35397BA17B`
- `PreviewAny`
- `Note`
- `VHS_VideoCombine`
- `GetNode`
- `LTXVAudioVAEDecode` ★核心
- `SetNode`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `SetNode`
- `LTXVCropGuides`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `easy cleanGpuUsed`
- `SamplerCustomAdvanced` ★核心
- `LTXVAddGuideMulti`
- `easy cleanGpuUsed`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `PrimitiveNode`
- `Textbox`
- `MarkdownNote`
- `GetNode`
- `SetNode`
- `PrimitiveFloat`
- `PromptRelayEncodeTimeline`
- `LoadImage`

## 关键参数

- `width` = `289`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **46%**（92/202）

**有卡**：`LTX2MemoryEfficientSageAttentionPatch`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`LTXVScheduler`、`ImageResizeKJv2`、`ImageFromBatch+`、`VAELoaderKJ`、`VAELoader`、`ComfyMathExpression`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`RandomNoise`、`DualCLIPLoader`、`GuHaiAutoImageSplit`、`CFGGuider`、`ManualSigmas`、`KSamplerSelect`、`LTX2SamplingPreviewOverride`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`LTX2AttentionTunerPatch`、`TTResolutionSelector`、`UNETLoader`、`LTXVAddGuideMulti`、`LTX2_NAG`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`1hewOffice_Qwen35397BA17B`、`VHS_VideoCombine`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`INTConstant`、`Textbox`、`PromptRelayEncodeTimeline`、`LoadImage`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced
