---
key: 视频生成/图生视频/Qwen Image 2_1 一键4图_Minimax H3 SelfLift _2105768139874201602.json
name: Qwen Image 2_1 一键4图_Minimax H3 SelfLift _2105768139874201602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Qwen Image 2_1 一键4图_Minimax H3 SelfLift _2105768139874201602.json
hash: ef347a07d19eada5
coverage: 0.631356
learned_at: 2026-10-07 00:34:47
nodes: [SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, GetNode, GetNode, GetNode, PathchSageAttentionKJ, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ShowText|pysssss, Any Switch (rgthree), GetNode, EmptyLatentImage, KSampler, QwenImage21Cache, ModelAttentionBackend, MarkdownNote, ResolutionSelector, PixaromaGroupSwitch, CR Prompt Text, PixaromaGetNode, PixaromaGetNode, PixaromaGetNode, PixaromaGetNode, PixaromaGetNode, PixaromaGetNode, PixaromaGetNode, PixaromaGetNode, PixaromaGetNode, ConditioningZeroOut, KSamplerSelect, PixaromaGetNode, PixaromaGetNode, KSamplerSelect, PixaromaSetNode, PixaromaGetNode, PixaromaGetNode, KSamplerSelect, PixaromaSetNode, PixaromaSetNode, VAEDecode, easy imageListToImageBatch, easy imageSplitGrid, easy imageListToImageBatch, easy imageListToImageBatch, easy imageListToImageBatch, SaveImage, SaveImage, ImageFromBatch, ImageFromBatch, ImageFromBatch, ImageFromBatch, PixaromaGetNode, PixaromaSetNode, PixaromaSetNode, ModelPreviewOverrideKJ, ModelPreviewOverrideKJ, PixaromaSetNode, PixaromaSetNode, VAEDecode, ModelPreviewOverrideKJ, ModelPreviewOverrideKJ, GetNode, GetNode, VRAM_Debug, VRAM_Debug, GetNode, GetNode, MarkdownNote, PixaromaSetNode, PrimitiveFloat, PixaromaLabel, LayerUtility: PurgeVRAM V2, GetNode, GetNode, GetNode, BasicScheduler, ExtendIntermediateSigmas, KSamplerSelect, ConditioningZeroOut, BasicScheduler, ExtendIntermediateSigmas, ConditioningZeroOut, BasicScheduler, ExtendIntermediateSigmas, VAEDecodeAudio, ConditioningZeroOut, BasicScheduler, ExtendIntermediateSigmas, VAEDecodeAudio, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LayerUtility: PurgeVRAM V2, ResolutionSelector, SetNode, SetNode, ComfyMathExpression, MiniMaxH3ReferenceToVideo, MiniMaxH3ReferenceToVideo, MiniMaxH3ReferenceToVideo, GetNode, PixaromaGetNode, GetNode, GetNode, PixaromaGetNode, GetNode, PixaromaGetNode, GetNode, PixaromaGetNode, VRAM_Debug, GetNode, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, ShowText|pysssss, PixaromaLabel, llama_cpp_parameters, llama_cpp_parameters, llama_cpp_parameters, VRAM_Debug, MiniMaxH3ReferenceToVideo, GetNode, GetNode, GetNode, GetNode, VRAM_Debug, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, LayerUtility: PurgeVRAM V2, CLIPLoader, VAELoader, SetNode, SetNode, llama_cpp_parameters, SetNode, ImageRGBA2RGB, SetNode, ImageRGBA2RGB, ImageRGBA2RGB, SetNode, ImageRGBA2RGB, ImageResizeKJv2, ImageResizeKJv2, VHS_VideoCombine, PixaromaLabel, TextEncodeQwenImage21, llama_cpp_instruct_adv, llama_cpp_instruct_adv, llama_cpp_instruct_adv, VAELoader, PixaromaSetNode, SetNode, PixaromaLabel, VHS_VideoCombine, VHS_VideoCombine, PixaromaGetNode, PixaromaGetNode, VHS_VideoCombine, PixaromaSetNode, VAEDecode, SetNode, GetNode, llama_cpp_instruct_adv, GetNode, PixaromaGroupSwitch, LoadImage, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, ImageResizeKJv2, ImageResizeKJv2, PixaromaResolution, LoadImage, LoadImage, MarkdownNote, PixaromaLabel, CR Text Concatenate, Text, Text, Text, llama_cpp_model_loader, llama_cpp_model_loader, llama_cpp_model_loader, llama_cpp_model_loader, UNETLoader, LoraLoaderModelOnly, SelfLiftAvatarH3Sampler, SelfLiftAvatarH3Sampler, SelfLiftAvatarH3Sampler, SelfLiftAvatarH3Sampler, CLIPLoader, VAELoader, QwenPERewriteT8, MiniMaxLowVRAMAttention, MiniMaxChunkFeedForward, SetNode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, SetNode, LoadImage, VAEDecode, SaveImage, SaveImage, SaveImage, UNETLoader, VAEDecode, CR Prompt Text, Text, VAEDecodeAudio, VAEDecodeAudio, CR Prompt Text, CR Text, CR Text, CR Text, CR Text, PixaromaLabel, PixaromaLabel]
patterns: []
missing: [CR Text, CR Text, CR Text, CR Text, CR Text Concatenate, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, LayerUtility: PurgeVRAM V2, easy imageListToImageBatch, easy imageListToImageBatch, easy imageListToImageBatch, easy imageListToImageBatch, easy imageSplitGrid, CR Prompt Text, CR Prompt Text, CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 806382002299618, "steps": 40, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识, 次要节点 `easy imageSplitGrid` 知识库中没有该节点类型的任何知识, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明, 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 视频生成/图生视频/Qwen Image 2_1 一键4图_Minimax H3 SelfLift _2105768139874201602.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Qwen Image 2_1 一键4图_Minimax H3 SelfLift _2105768139874201602.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（236 个）：
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PathchSageAttentionKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ShowText|pysssss`
- `Any Switch (rgthree)`
- `GetNode`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `ModelAttentionBackend`
- `MarkdownNote`
- `ResolutionSelector`
- `PixaromaGroupSwitch`
- `CR Prompt Text`
- `PixaromaGetNode`
- `PixaromaGetNode`
- `PixaromaGetNode`
- `PixaromaGetNode`
- `PixaromaGetNode`
- `PixaromaGetNode`
- `PixaromaGetNode`
- `PixaromaGetNode`
- `PixaromaGetNode`
- `ConditioningZeroOut`
- `KSamplerSelect` ★核心
- `PixaromaGetNode`
- `PixaromaGetNode`
- `KSamplerSelect` ★核心
- `PixaromaSetNode`
- `PixaromaGetNode`
- `PixaromaGetNode`
- `KSamplerSelect` ★核心
- `PixaromaSetNode`
- `PixaromaSetNode`
- `VAEDecode` ★核心
- `easy imageListToImageBatch`
- `easy imageSplitGrid`
- `easy imageListToImageBatch`
- `easy imageListToImageBatch`
- `easy imageListToImageBatch`
- `SaveImage`
- `SaveImage`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `PixaromaGetNode`
- `PixaromaSetNode`
- `PixaromaSetNode`
- `ModelPreviewOverrideKJ`
- `ModelPreviewOverrideKJ`
- `PixaromaSetNode`
- `PixaromaSetNode`
- `VAEDecode` ★核心
- `ModelPreviewOverrideKJ`
- `ModelPreviewOverrideKJ`
- `GetNode`
- `GetNode`
- `VRAM_Debug`
- `VRAM_Debug`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `PixaromaSetNode`
- `PrimitiveFloat`
- `PixaromaLabel`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `GetNode`
- `GetNode`
- `BasicScheduler`
- `ExtendIntermediateSigmas`
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `BasicScheduler`
- `ExtendIntermediateSigmas`
- `ConditioningZeroOut`
- `BasicScheduler`
- `ExtendIntermediateSigmas`
- `VAEDecodeAudio` ★核心
- `ConditioningZeroOut`
- `BasicScheduler`
- `ExtendIntermediateSigmas`
- `VAEDecodeAudio` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LayerUtility: PurgeVRAM V2`
- `ResolutionSelector`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3ReferenceToVideo`
- `GetNode`
- `PixaromaGetNode`
- `GetNode`
- `GetNode`
- `PixaromaGetNode`
- `GetNode`
- `PixaromaGetNode`
- `GetNode`
- `PixaromaGetNode`
- `VRAM_Debug`
- `GetNode`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `PixaromaLabel`
- `llama_cpp_parameters`
- `llama_cpp_parameters`
- `llama_cpp_parameters`
- `VRAM_Debug`
- `MiniMaxH3ReferenceToVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VRAM_Debug`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `LayerUtility: PurgeVRAM V2`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `llama_cpp_parameters`
- `SetNode`
- `ImageRGBA2RGB`
- `SetNode`
- `ImageRGBA2RGB`
- `ImageRGBA2RGB`
- `SetNode`
- `ImageRGBA2RGB`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `PixaromaLabel`
- `TextEncodeQwenImage21`
- `llama_cpp_instruct_adv`
- `llama_cpp_instruct_adv`
- `llama_cpp_instruct_adv`
- `VAELoader`
- `PixaromaSetNode`
- `SetNode`
- `PixaromaLabel`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PixaromaGetNode`
- `PixaromaGetNode`
- `VHS_VideoCombine`
- `PixaromaSetNode`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `llama_cpp_instruct_adv`
- `GetNode`
- `PixaromaGroupSwitch`
- `LoadImage`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `PixaromaResolution`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `PixaromaLabel`
- `CR Text Concatenate`
- `Text`
- `Text`
- `Text`
- `llama_cpp_model_loader`
- `llama_cpp_model_loader`
- `llama_cpp_model_loader`
- `llama_cpp_model_loader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SelfLiftAvatarH3Sampler` ★核心
- `SelfLiftAvatarH3Sampler` ★核心
- `SelfLiftAvatarH3Sampler` ★核心
- `SelfLiftAvatarH3Sampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `QwenPERewriteT8`
- `MiniMaxLowVRAMAttention`
- `MiniMaxChunkFeedForward`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `CR Prompt Text`
- `Text`
- `VAEDecodeAudio` ★核心
- `VAEDecodeAudio` ★核心
- `CR Prompt Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `CR Text`
- `PixaromaLabel`
- `PixaromaLabel`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `806382002299618`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **63%**（149/236）

**有卡**：`PathchSageAttentionKJ`、`EmptyLatentImage`、`KSampler`、`QwenImage21Cache`、`ModelAttentionBackend`、`ResolutionSelector`、`PixaromaGroupSwitch`、`PixaromaGetNode`、`ConditioningZeroOut`、`KSamplerSelect`、`PixaromaSetNode`、`VAEDecode`、`SaveImage`、`ImageFromBatch`、`ModelPreviewOverrideKJ`、`VRAM_Debug`、`PixaromaLabel`、`BasicScheduler`、`ExtendIntermediateSigmas`、`VAEDecodeAudio`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`llama_cpp_parameters`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`CLIPLoader`、`VAELoader`、`ImageRGBA2RGB`、`ImageResizeKJv2`、`VHS_VideoCombine`、`TextEncodeQwenImage21`、`llama_cpp_instruct_adv`、`LoadImage`、`PixaromaResolution`、`Text`、`llama_cpp_model_loader`、`UNETLoader`、`LoraLoaderModelOnly`、`SelfLiftAvatarH3Sampler`、`QwenPERewriteT8`、`MiniMaxLowVRAMAttention`、`MiniMaxChunkFeedForward`

**缺卡**（22）：`CR Text`、`CR Text`、`CR Text`、`CR Text`、`CR Text Concatenate`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`LayerUtility: PurgeVRAM V2`、`easy imageListToImageBatch`、`easy imageListToImageBatch`、`easy imageListToImageBatch`、`easy imageListToImageBatch`、`easy imageSplitGrid`、`CR Prompt Text`、`CR Prompt Text`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Concatenate` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: PurgeVRAM V2` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageListToImageBatch` 知识库中没有该节点类型的任何知识
- 次要节点 `easy imageSplitGrid` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
