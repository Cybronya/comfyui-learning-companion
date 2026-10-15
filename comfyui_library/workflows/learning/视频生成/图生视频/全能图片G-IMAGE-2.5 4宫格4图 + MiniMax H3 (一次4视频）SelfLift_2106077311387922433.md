---
key: 视频生成/图生视频/全能图片G-IMAGE-2.5 4宫格4图 + MiniMax H3 (一次4视频）SelfLift_2106077311387922433.json
name: 全能图片G-IMAGE-2.5 4宫格4图 + MiniMax H3 (一次4视频）SelfLift_2106077311387922433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/全能图片G-IMAGE-2.5 4宫格4图 + MiniMax H3 (一次4视频）SelfLift_2106077311387922433.json
hash: 6440c38e2efdff71
coverage: 0.855422
learned_at: 2026-10-15 22:43:01
nodes: [PixaromaGetNode, PixaromaGetNode, Reroute, Reroute, ModelAttentionBackend, MiniMaxLowVRAMAttention, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, PixaromaSetNode, PixaromaGetNode, ComfyMathExpression, Reroute, Reroute, PixaromaGetNode, PixaromaGetNode, Reroute, PixaromaGetNode, PixaromaGetNode, PixaromaGetNode, PixaromaSetNode, ComfyMathExpression, Reroute, Reroute, ResolutionSelector, ComfyMathExpression, easy imageListToImageBatch, easy imageListToImageBatch, easy imageListToImageBatch, easy imageListToImageBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, CR Text Concatenate, easy showAnything, PrimitiveFloat, PixaromaSetNode, PrimitiveNode, MarkdownNote, PixaromaGroupSwitch, RHLLMChatNode, ModelPreviewOverrideKJ, RHLLMChatNode, ModelPreviewOverrideKJ, ModelPreviewOverrideKJ, Reroute, Reroute, Reroute, Reroute, CR Prompt Text, ResolutionSelector, RHLLMChatNode, ModelPreviewOverrideKJ, RHLLMChatNode, LoadImage, easy imageSplitGrid, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveNode, PixaromaResolution, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, PixaromaLabel, LoadImage, LoadImage, MarkdownNote, ResolutionSelector, ComfyMathExpression, MiniMaxH3ReferenceToVideo, MiniMaxH3ReferenceToVideo, Reroute, RHLLMChatNode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, VAELoader, VAELoader, CLIPLoader, LoraLoaderModelOnly, UNETLoader, PixaromaGetNode, PixaromaGetNode, PixaromaGetNode, PixaromaGetNode, VHS_VideoCombine, VHS_VideoCombine, ExtendIntermediateSigmas, MiniMaxH3ReferenceToVideo, SaveImage, ExtendIntermediateSigmas, ExtendIntermediateSigmas, MiniMaxH3ReferenceToVideo, ConditioningZeroOut, KSamplerSelect, BasicScheduler, VAEDecode, VAEDecodeAudio, SelfLiftAvatarH3Sampler, PixaromaSetNode, PixaromaSetNode, VAEDecodeAudio, VAEDecode, ConditioningZeroOut, KSamplerSelect, BasicScheduler, SelfLiftAvatarH3Sampler, PixaromaSetNode, BasicScheduler, KSamplerSelect, ConditioningZeroOut, VAEDecode, VAEDecodeAudio, SelfLiftAvatarH3Sampler, PixaromaSetNode, PixaromaSetNode, ExtendIntermediateSigmas, BasicScheduler, KSamplerSelect, ConditioningZeroOut, VAEDecodeAudio, VAEDecode, SelfLiftAvatarH3Sampler, PixaromaSetNode, PixaromaSetNode, PixaromaGetNode, PixaromaGetNode, PixaromaGetNode, PixaromaGetNode, VHS_VideoCombine, PixaromaGetNode, VHS_VideoCombine, PixaromaGetNode, VHS_VideoCombine, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PixaromaLabel, PixaromaLabel, Note, PixaromaLabel, Text, Text, Text, Text, ResolutionSelector, PrimitiveFloat, VHS_VideoCombine, RH_RhartImageG25OfficialTokenSunburstEdit, PixaromaGetNode, PixaromaGetNode, VHS_VideoCombine, VHS_VideoCombine, RHSettingsNode, CR Prompt Text, CR Text, CR Text, CR Text, CR Text, PixaromaSetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/全能图片G-IMAGE-2.5 4宫格4图 + MiniMax H3 (一次4视频）SelfLift_2106077311387922433.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/全能图片G-IMAGE-2.5 4宫格4图 + MiniMax H3 (一次4视频）SelfLift_2106077311387922433.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（166 个）：
- `PixaromaGetNode`
- `PixaromaGetNode`
- `Reroute`
- `Reroute`
- `ModelAttentionBackend`
- `MiniMaxLowVRAMAttention`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `PixaromaSetNode`
- `PixaromaGetNode`
- `ComfyMathExpression`
- `Reroute`
- `Reroute`
- `PixaromaGetNode`
- `PixaromaGetNode`
- `Reroute`
- `PixaromaGetNode`
- `PixaromaGetNode`
- `PixaromaGetNode`
- `PixaromaSetNode`
- `ComfyMathExpression`
- `Reroute`
- `Reroute`
- `ResolutionSelector`
- `ComfyMathExpression`
- `easy imageListToImageBatch`
- `easy imageListToImageBatch`
- `easy imageListToImageBatch`
- `easy imageListToImageBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `CR Text Concatenate`
- `easy showAnything`
- `PrimitiveFloat`
- `PixaromaSetNode`
- `PrimitiveNode`
- `MarkdownNote`
- `PixaromaGroupSwitch`
- `RHLLMChatNode`
- `ModelPreviewOverrideKJ`
- `RHLLMChatNode`
- `ModelPreviewOverrideKJ`
- `ModelPreviewOverrideKJ`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CR Prompt Text`
- `ResolutionSelector`
- `RHLLMChatNode`
- `ModelPreviewOverrideKJ`
- `RHLLMChatNode`
- `LoadImage`
- `easy imageSplitGrid`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveNode`
- `PixaromaResolution`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `CR Text Concatenate`
- `PixaromaLabel`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `ResolutionSelector`
- `ComfyMathExpression`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3ReferenceToVideo`
- `Reroute`
- `RHLLMChatNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `PixaromaGetNode`
- `PixaromaGetNode`
- `PixaromaGetNode`
- `PixaromaGetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ExtendIntermediateSigmas`
- `MiniMaxH3ReferenceToVideo`
- `SaveImage`
- `ExtendIntermediateSigmas`
- `ExtendIntermediateSigmas`
- `MiniMaxH3ReferenceToVideo`
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SelfLiftAvatarH3Sampler` ★核心
- `PixaromaSetNode`
- `PixaromaSetNode`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SelfLiftAvatarH3Sampler` ★核心
- `PixaromaSetNode`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `SelfLiftAvatarH3Sampler` ★核心
- `PixaromaSetNode`
- `PixaromaSetNode`
- `ExtendIntermediateSigmas`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SelfLiftAvatarH3Sampler` ★核心
- `PixaromaSetNode`
- `PixaromaSetNode`
- `PixaromaGetNode`
- `PixaromaGetNode`
- `PixaromaGetNode`
- `PixaromaGetNode`
- `VHS_VideoCombine`
- `PixaromaGetNode`
- `VHS_VideoCombine`
- `PixaromaGetNode`
- `VHS_VideoCombine`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PixaromaLabel`
- `PixaromaLabel`
- `Note`
- `PixaromaLabel`
- `Text`
- `Text`
- `Text`
- `Text`
- `ResolutionSelector`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `RH_RhartImageG25OfficialTokenSunburstEdit`
- `PixaromaGetNode`
- `PixaromaGetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RHSettingsNode`
- `CR Prompt Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `PixaromaSetNode`

## 知识

覆盖率 **86%**（142/166）

**有卡**：`PixaromaGetNode`、`ModelAttentionBackend`、`MiniMaxLowVRAMAttention`、`MiniMaxChunkFeedForward`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`PixaromaSetNode`、`ComfyMathExpression`、`ResolutionSelector`、`easy imageListToImageBatch`、`ImageFromBatch`、`CR Text Concatenate`、`PixaromaGroupSwitch`、`RHLLMChatNode`、`ModelPreviewOverrideKJ`、`CR Prompt Text`、`LoadImage`、`easy imageSplitGrid`、`PixaromaResolution`、`PixaromaLabel`、`MiniMaxH3ReferenceToVideo`、`ImageResizeKJv2`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`VHS_VideoCombine`、`ExtendIntermediateSigmas`、`SaveImage`、`ConditioningZeroOut`、`KSamplerSelect`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`SelfLiftAvatarH3Sampler`、`Text`、`RH_RhartImageG25OfficialTokenSunburstEdit`、`RHSettingsNode`、`CR Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
