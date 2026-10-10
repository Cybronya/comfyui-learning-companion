---
key: 视频生成/文生视频/LTX2.3 9宫格 AI 漫剧生成 工作流（仅供娱乐测试）_2054171445080666114.json
name: LTX2.3 9宫格 AI 漫剧生成 工作流（仅供娱乐测试）_2054171445080666114
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/LTX2.3 9宫格 AI 漫剧生成 工作流（仅供娱乐测试）_2054171445080666114.json
hash: 11740b58d3870edc
coverage: 0.40099
learned_at: 2026-10-10 23:00:19
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, LTX2MemoryEfficientSageAttentionPatch, LTXVChunkFeedForward, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, PathchSageAttentionKJ, SetNode, LTXVScheduler, SetNode, GetNode, GetNode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, VAELoaderKJ, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, GetNode, GetNode, ComfyMathExpression, GetNode, SetNode, LTXVLatentUpsampler, LTXVCropGuides, LTXVSeparateAVLatent, GetNode, GetNode, SetNode, VAELoader, LTXVConcatAVLatent, LTXVConditioning, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, SetNode, ComfyMathExpression, GetNode, GetNode, EmptyLTXVLatentVideo, SamplerCustomAdvanced, RandomNoise, GetNode, DualCLIPLoader, ImageResizeKJv2, ComfyMathExpression, GuHaiAutoImageSplit, ImageResizeKJv2, ImageResizeKJv2, SetNode, SetNode, GetNode, CFGGuider, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, ManualSigmas, KSamplerSelect, LTX2SamplingPreviewOverride, GetNode, LatentUpscaleModelLoader, LoraLoaderModelOnly, LTX2AttentionTunerPatch, PreviewImage, TTResolutionSelector, UNETLoader, Note, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, PrimitiveFloat, PrimitiveFloat, LTXVAddGuideMulti, LTX2_NAG, GetNode, SetNode, SetNode, SetNode, SetNode, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, ComfyMathExpression, GetNode, GetNode, ImageResizeKJv2, CLIPTextEncode, ImageResizeKJv2, GetNode, GetNode, ImageFromBatch+, GetNode, ImageFromBatch+, GetNode, SetNode, GetNode, GetNode, GetNode, ComfyMathExpression, GetNode, LTXVEmptyLatentAudio, GetNode, LoadImage, RandomNoise, 1hewOffice_Qwen35397BA17B, PreviewAny, Note, VHS_VideoCombine, GetNode, LTXVAudioVAEDecode, SetNode, VAEDecodeTiled, GetNode, SetNode, LTXVCropGuides, GetNode, GetNode, LTXVSeparateAVLatent, ManualSigmas, LTXVConcatAVLatent, CFGGuider, KSamplerSelect, ManualSigmas, easy cleanGpuUsed, SamplerCustomAdvanced, LTXVAddGuideMulti, easy cleanGpuUsed, SetNode, LoraLoaderModelOnly, INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, PrimitiveNode, PromptRelayEncodeTimeline, Textbox, MarkdownNote, GetNode, SetNode, PrimitiveFloat]
patterns: []
missing: [ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, ImageFromBatch+, easy cleanGpuUsed, easy cleanGpuUsed]
parameters: {"batch_size": 1, "height": 25, "width": 289}
discoveries: [次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/LTX2.3 9宫格 AI 漫剧生成 工作流（仅供娱乐测试）_2054171445080666114.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/LTX2.3 9宫格 AI 漫剧生成 工作流（仅供娱乐测试）_2054171445080666114.json`

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
- `LoadImage`
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
- `PromptRelayEncodeTimeline`
- `Textbox`
- `MarkdownNote`
- `GetNode`
- `SetNode`
- `PrimitiveFloat`

## 关键参数

- `width` = `289`
- `height` = `25`
- `batch_size` = `1`

## 知识

覆盖率 **40%**（81/202）

**有卡**：`LTX2MemoryEfficientSageAttentionPatch`、`LTXVChunkFeedForward`、`PathchSageAttentionKJ`、`LTXVScheduler`、`ImageResizeKJv2`、`VAELoaderKJ`、`VAELoader`、`ComfyMathExpression`、`LTXVLatentUpsampler`、`LTXVCropGuides`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`LTXVConditioning`、`EmptyLTXVLatentVideo`、`SamplerCustomAdvanced`、`RandomNoise`、`DualCLIPLoader`、`GuHaiAutoImageSplit`、`CFGGuider`、`ManualSigmas`、`KSamplerSelect`、`LTX2SamplingPreviewOverride`、`LatentUpscaleModelLoader`、`LoraLoaderModelOnly`、`LTX2AttentionTunerPatch`、`TTResolutionSelector`、`UNETLoader`、`LTXVAddGuideMulti`、`LTX2_NAG`、`CLIPTextEncode`、`LTXVEmptyLatentAudio`、`LoadImage`、`1hewOffice_Qwen35397BA17B`、`VHS_VideoCombine`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`INTConstant`、`PromptRelayEncodeTimeline`、`Textbox`

**缺卡**（11）：`ImageFromBatch+`、`ImageFromBatch+`、`ImageFromBatch+`、`ImageFromBatch+`、`ImageFromBatch+`、`ImageFromBatch+`、`ImageFromBatch+`、`ImageFromBatch+`、`ImageFromBatch+`、`easy cleanGpuUsed`、`easy cleanGpuUsed`

**用到的条目**：VAELoader、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、UNETLoader、CFGGuider、KSamplerSelect、SamplerCustomAdvanced

## 学习发现

- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageFromBatch+` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
