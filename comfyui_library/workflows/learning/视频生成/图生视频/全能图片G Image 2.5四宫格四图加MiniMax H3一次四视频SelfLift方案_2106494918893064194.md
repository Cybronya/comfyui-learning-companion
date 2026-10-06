---
key: 视频生成/图生视频/全能图片G Image 2.5四宫格四图加MiniMax H3一次四视频SelfLift方案_2106494918893064194.json
name: 全能图片G Image 2.5四宫格四图加MiniMax H3一次四视频SelfLift方案_2106494918893064194
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/全能图片G Image 2.5四宫格四图加MiniMax H3一次四视频SelfLift方案_2106494918893064194.json
hash: 3ff8b39dad2503f4
coverage: 0.77957
learned_at: 2026-10-07 00:34:54
nodes: [PixaromaGetNode, PixaromaGetNode, Reroute, Reroute, ModelAttentionBackend, MiniMaxLowVRAMAttention, MiniMaxChunkFeedForward, MiniMaxH3MemoryEfficientSageAttentionPatch, PixaromaSetNode, PixaromaGetNode, ComfyMathExpression, Reroute, Reroute, PixaromaGetNode, PixaromaGetNode, Reroute, PixaromaGetNode, PixaromaGetNode, PixaromaGetNode, PixaromaSetNode, ComfyMathExpression, Reroute, Reroute, ResolutionSelector, ComfyMathExpression, easy imageListToImageBatch, easy imageListToImageBatch, easy imageListToImageBatch, easy imageListToImageBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, CR Text Concatenate, easy showAnything, PrimitiveFloat, PixaromaSetNode, PrimitiveNode, PixaromaGroupSwitch, RHLLMChatNode, ModelPreviewOverrideKJ, RHLLMChatNode, ModelPreviewOverrideKJ, ModelPreviewOverrideKJ, Reroute, Reroute, Reroute, Reroute, CR Prompt Text, ResolutionSelector, RHLLMChatNode, ModelPreviewOverrideKJ, RHLLMChatNode, LoadImage, easy imageSplitGrid, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveNode, PixaromaResolution, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, ResolutionSelector, ComfyMathExpression, MiniMaxH3ReferenceToVideo, MiniMaxH3ReferenceToVideo, Reroute, RHLLMChatNode, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, ImageResizeKJv2, VAELoader, VAELoader, CLIPLoader, LoraLoaderModelOnly, UNETLoader, PixaromaGetNode, PixaromaGetNode, PixaromaGetNode, PixaromaGetNode, VHS_VideoCombine, VHS_VideoCombine, ExtendIntermediateSigmas, MiniMaxH3ReferenceToVideo, SaveImage, ExtendIntermediateSigmas, ExtendIntermediateSigmas, MiniMaxH3ReferenceToVideo, ConditioningZeroOut, KSamplerSelect, BasicScheduler, VAEDecode, VAEDecodeAudio, SelfLiftAvatarH3Sampler, PixaromaSetNode, PixaromaSetNode, VAEDecodeAudio, VAEDecode, ConditioningZeroOut, KSamplerSelect, BasicScheduler, SelfLiftAvatarH3Sampler, PixaromaSetNode, BasicScheduler, KSamplerSelect, ConditioningZeroOut, VAEDecode, VAEDecodeAudio, SelfLiftAvatarH3Sampler, PixaromaSetNode, PixaromaSetNode, ExtendIntermediateSigmas, BasicScheduler, KSamplerSelect, ConditioningZeroOut, VAEDecodeAudio, VAEDecode, SelfLiftAvatarH3Sampler, PixaromaSetNode, PixaromaSetNode, PixaromaGetNode, PixaromaGetNode, PixaromaGetNode, PixaromaGetNode, VHS_VideoCombine, PixaromaGetNode, VHS_VideoCombine, PixaromaGetNode, VHS_VideoCombine, PreviewImage, PreviewImage, PreviewImage, PreviewImage, Text, Text, Text, Text, ResolutionSelector, PrimitiveFloat, VHS_VideoCombine, RH_RhartImageG25OfficialTokenSunburstEdit, PixaromaGetNode, PixaromaGetNode, VHS_VideoCombine, VHS_VideoCombine, RHSettingsNode, CR Prompt Text, CR Text, CR Text, CR Text, CR Text, PixaromaSetNode, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: [CR Text, CR Text, CR Text, CR Text, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, CR Text Concatenate, easy imageListToImageBatch, easy imageListToImageBatch, easy imageListToImageBatch, easy imageListToImageBatch, easy imageSplitGrid, CR Prompt Text, CR Prompt Text]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSplitGrid` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/全能图片G Image 2.5四宫格四图加MiniMax H3一次四视频SelfLift方案_2106494918893064194.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/全能图片G Image 2.5四宫格四图加MiniMax H3一次四视频SelfLift方案_2106494918893064194.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（186 个）：
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（145/186）

**有卡**：`PixaromaGetNode`、`ModelAttentionBackend`、`MiniMaxLowVRAMAttention`、`MiniMaxChunkFeedForward`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`PixaromaSetNode`、`ComfyMathExpression`、`ResolutionSelector`、`ImageFromBatch`、`PixaromaGroupSwitch`、`RHLLMChatNode`、`ModelPreviewOverrideKJ`、`LoadImage`、`PixaromaResolution`、`MiniMaxH3ReferenceToVideo`、`ImageResizeKJv2`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`VHS_VideoCombine`、`ExtendIntermediateSigmas`、`SaveImage`、`ConditioningZeroOut`、`KSamplerSelect`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`SelfLiftAvatarH3Sampler`、`Text`、`RH_RhartImageG25OfficialTokenSunburstEdit`、`RHSettingsNode`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（16）：`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text Concatenate`、`CR Text Concatenate`、`CR Text Concatenate`、`CR Text Concatenate`、`CR Text Concatenate`、`easy imageListToImageBatch`、`easy imageListToImageBatch`、`easy imageListToImageBatch`、`easy imageListToImageBatch`、`easy imageSplitGrid`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSplitGrid` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
