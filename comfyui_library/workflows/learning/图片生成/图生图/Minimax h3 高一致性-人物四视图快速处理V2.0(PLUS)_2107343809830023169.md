---
key: 图片生成/图生图/Minimax h3 高一致性-人物四视图快速处理V2.0(PLUS)_2107343809830023169.json
name: Minimax h3 高一致性-人物四视图快速处理V2.0(PLUS)_2107343809830023169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Minimax h3 高一致性-人物四视图快速处理V2.0(PLUS)_2107343809830023169.json
hash: 20ef384cc62c8334
coverage: 0.263158
learned_at: 2026-10-06 21:40:41
nodes: [MiniMaxH3ReferenceToVideo, VAELoader, VAELoader, GetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, SetNode, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, BasicScheduler, BasicGuider, RandomNoise, KSamplerSelect, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveFloat, ComfyMathExpression, VHS_VideoCombine, Any Switch (rgthree), MarkdownNote, ImageConcatFromBatch, ImageConcatFromBatch, MarkdownNote, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, CLIPLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, CreateVideo, GetVideoComponents, MarkdownNote, Fast Groups Bypasser (rgthree), ResizeImageMaskNode, workflow>SeedVR放大节点, MarkdownNote, GetImagesFromBatchIndexed, Any Switch (rgthree), MarkdownNote, ResolutionSelector, UNETLoader, LoraLoaderModelOnly, AutoCropFaces, PreviewImage, SaveImage, Image Comparer (rgthree), SaveImage, Fast Groups Bypasser (rgthree), Fast Muter (rgthree), PrimitiveStringMultiline, LoadImage, LoadImage]
patterns: []
missing: [AutoCropFaces, BasicGuider, BasicScheduler, ComfyMathExpression, CreateVideo, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Muter (rgthree), GetImagesFromBatchIndexed, GetVideoComponents, ImageConcatFromBatch, ImageConcatFromBatch, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, VHS_VideoCombine, SamplerCustomAdvanced, VAEDecodeAudio, ResizeImageMaskNode, workflow>SeedVR放大节点]
discoveries: [次要节点 `AutoCropFaces` 知识库中没有该节点类型的任何知识, 次要节点 `BasicGuider` 知识库中没有该节点类型的任何知识, 次要节点 `BasicScheduler` 知识库中没有该节点类型的任何知识, 次要节点 `ComfyMathExpression` 知识库中没有该节点类型的任何知识, 次要节点 `CreateVideo` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Muter (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `GetImagesFromBatchIndexed` 知识库中没有该节点类型的任何知识, 次要节点 `GetVideoComponents` 知识库中没有该节点类型的任何知识, 次要节点 `ImageConcatFromBatch` 知识库中没有该节点类型的任何知识, 次要节点 `ImageConcatFromBatch` 知识库中没有该节点类型的任何知识, 次要节点 `MiniMaxH3MemoryEfficientSageAttentionPatch` 知识库中没有该节点类型的任何知识, 次要节点 `MiniMaxH3ReferenceToVideo` 知识库中没有该节点类型的任何知识, 次要节点 `RandomNoise` 知识库中没有该节点类型的任何知识, 次要节点 `VHS_VideoCombine` 知识库中没有该节点类型的任何知识, 核心节点 `SamplerCustomAdvanced` 仅有 KSampler 的通用知识，没有该节点自己的说明, 核心节点 `VAEDecodeAudio` 仅有 VAE 的通用知识，没有该节点自己的说明, 次要节点 `ResizeImageMaskNode` 仅有 Resolution 的通用知识，没有该节点自己的说明, 次要节点 `workflow>SeedVR放大节点` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Minimax h3 高一致性-人物四视图快速处理V2.0(PLUS)_2107343809830023169.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Minimax h3 高一致性-人物四视图快速处理V2.0(PLUS)_2107343809830023169.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（57 个）：
- `MiniMaxH3ReferenceToVideo`
- `VAELoader`
- `VAELoader`
- `GetNode`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `SetNode`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicScheduler`
- `BasicGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `Any Switch (rgthree)`
- `MarkdownNote`
- `ImageConcatFromBatch`
- `ImageConcatFromBatch`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `CLIPLoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `CreateVideo`
- `GetVideoComponents`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `ResizeImageMaskNode`
- `workflow>SeedVR放大节点`
- `MarkdownNote`
- `GetImagesFromBatchIndexed`
- `Any Switch (rgthree)`
- `MarkdownNote`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `AutoCropFaces`
- `PreviewImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Muter (rgthree)`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **26%**（15/57）

**有卡**：`VAELoader`、`VAEDecode`、`LoadImage`、`CLIPLoader`、`ResolutionSelector`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveImage`

**缺卡**（20）：`AutoCropFaces`、`BasicGuider`、`BasicScheduler`、`ComfyMathExpression`、`CreateVideo`、`Fast Groups Bypasser (rgthree)`、`Fast Groups Bypasser (rgthree)`、`Fast Muter (rgthree)`、`GetImagesFromBatchIndexed`、`GetVideoComponents`、`ImageConcatFromBatch`、`ImageConcatFromBatch`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3ReferenceToVideo`、`RandomNoise`、`VHS_VideoCombine`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`ResizeImageMaskNode`、`workflow>SeedVR放大节点`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SaveImage

## 学习发现

- 次要节点 `AutoCropFaces` 知识库中没有该节点类型的任何知识
- 次要节点 `BasicGuider` 知识库中没有该节点类型的任何知识
- 次要节点 `BasicScheduler` 知识库中没有该节点类型的任何知识
- 次要节点 `ComfyMathExpression` 知识库中没有该节点类型的任何知识
- 次要节点 `CreateVideo` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Groups Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Muter (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `GetImagesFromBatchIndexed` 知识库中没有该节点类型的任何知识
- 次要节点 `GetVideoComponents` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageConcatFromBatch` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageConcatFromBatch` 知识库中没有该节点类型的任何知识
- 次要节点 `MiniMaxH3MemoryEfficientSageAttentionPatch` 知识库中没有该节点类型的任何知识
- 次要节点 `MiniMaxH3ReferenceToVideo` 知识库中没有该节点类型的任何知识
- 次要节点 `RandomNoise` 知识库中没有该节点类型的任何知识
- 次要节点 `VHS_VideoCombine` 知识库中没有该节点类型的任何知识
- 核心节点 `SamplerCustomAdvanced` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 核心节点 `VAEDecodeAudio` 仅有 VAE 的通用知识，没有该节点自己的说明
- 次要节点 `ResizeImageMaskNode` 仅有 Resolution 的通用知识，没有该节点自己的说明
- 次要节点 `workflow>SeedVR放大节点` 仅有 KSampler 的通用知识，没有该节点自己的说明
