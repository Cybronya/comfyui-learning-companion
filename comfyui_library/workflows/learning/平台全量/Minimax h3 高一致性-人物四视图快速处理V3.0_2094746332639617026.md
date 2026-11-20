---
key: 平台全量/Minimax h3 高一致性-人物四视图快速处理V3.0_2094746332639617026.json
name: Minimax h3 高一致性-人物四视图快速处理V3.0_2094746332639617026
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Minimax h3 高一致性-人物四视图快速处理V3.0_2094746332639617026.json
hash: 6ceac8c1c43f83be
coverage: 0.576271
learned_at: 2026-11-14 00:45:42
nodes: [MiniMaxH3ReferenceToVideo, VAELoader, VAELoader, GetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, SetNode, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, BasicScheduler, BasicGuider, RandomNoise, KSamplerSelect, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveFloat, ComfyMathExpression, VHS_VideoCombine, Any Switch (rgthree), MarkdownNote, ImageConcatFromBatch, ImageConcatFromBatch, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, CLIPLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, CreateVideo, GetVideoComponents, MarkdownNote, Fast Groups Bypasser (rgthree), ResizeImageMaskNode, MarkdownNote, GetImagesFromBatchIndexed, Any Switch (rgthree), MarkdownNote, ResolutionSelector, UNETLoader, LoraLoaderModelOnly, AutoCropFaces, PreviewImage, SaveImage, Image Comparer (rgthree), SaveImage, Fast Muter (rgthree), MarkdownNote, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, PrimitiveStringMultiline, 39de0e19-7117-42df-9b3d-b677b1d4bf50, PrimitiveStringMultiline, MarkdownNote]
patterns: []
missing: []
---

# 平台全量/Minimax h3 高一致性-人物四视图快速处理V3.0_2094746332639617026.json

> 来源文件 `comfyui_library/workflows/平台全量/Minimax h3 高一致性-人物四视图快速处理V3.0_2094746332639617026.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
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
- `Fast Muter (rgthree)`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `39de0e19-7117-42df-9b3d-b677b1d4bf50`
- `PrimitiveStringMultiline`
- `MarkdownNote`

## 知识

覆盖率 **58%**（34/59）

**有卡**：`MiniMaxH3ReferenceToVideo`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicScheduler`、`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`LoadImage`、`ComfyMathExpression`、`VHS_VideoCombine`、`ImageConcatFromBatch`、`CLIPLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`CreateVideo`、`GetVideoComponents`、`ResizeImageMaskNode`、`GetImagesFromBatchIndexed`、`ResolutionSelector`、`UNETLoader`、`LoraLoaderModelOnly`、`AutoCropFaces`、`SaveImage`、`Fast Muter (rgthree)`、`39de0e19-7117-42df-9b3d-b677b1d4bf50`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
