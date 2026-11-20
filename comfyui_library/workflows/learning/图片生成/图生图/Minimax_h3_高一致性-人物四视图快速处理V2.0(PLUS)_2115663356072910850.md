---
key: 图片生成/图生图/Minimax_h3_高一致性-人物四视图快速处理V2.0(PLUS)_2115663356072910850.json
name: Minimax_h3_高一致性-人物四视图快速处理V2.0(PLUS)_2115663356072910850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Minimax_h3_高一致性-人物四视图快速处理V2.0(PLUS)_2115663356072910850.json
hash: ef8e1c215cd16e8e
coverage: 0.641509
learned_at: 2026-10-30 17:50:40
nodes: [MiniMaxH3ReferenceToVideo, VAELoader, VAELoader, GetNode, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, SetNode, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, BasicScheduler, BasicGuider, RandomNoise, KSamplerSelect, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveFloat, ComfyMathExpression, VHS_VideoCombine, Any Switch (rgthree), ImageConcatFromBatch, ImageConcatFromBatch, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, CLIPLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, CreateVideo, GetVideoComponents, Fast Groups Bypasser (rgthree), ResizeImageMaskNode, GetImagesFromBatchIndexed, Any Switch (rgthree), ResolutionSelector, UNETLoader, LoraLoaderModelOnly, AutoCropFaces, PreviewImage, SaveImage, Image Comparer (rgthree), SaveImage, Fast Muter (rgthree), Fast Groups Bypasser (rgthree), LoadImage, LoadImage, PrimitiveStringMultiline, 39de0e19-7117-42df-9b3d-b677b1d4bf50, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 图片生成/图生图/Minimax_h3_高一致性-人物四视图快速处理V2.0(PLUS)_2115663356072910850.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Minimax_h3_高一致性-人物四视图快速处理V2.0(PLUS)_2115663356072910850.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
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
- `Fast Groups Bypasser (rgthree)`
- `ResizeImageMaskNode`
- `GetImagesFromBatchIndexed`
- `Any Switch (rgthree)`
- `ResolutionSelector`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `AutoCropFaces`
- `PreviewImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Fast Muter (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `39de0e19-7117-42df-9b3d-b677b1d4bf50`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **64%**（34/53）

**有卡**：`MiniMaxH3ReferenceToVideo`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicScheduler`、`BasicGuider`、`RandomNoise`、`KSamplerSelect`、`LoadImage`、`ComfyMathExpression`、`VHS_VideoCombine`、`ImageConcatFromBatch`、`CLIPLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`CreateVideo`、`GetVideoComponents`、`ResizeImageMaskNode`、`GetImagesFromBatchIndexed`、`ResolutionSelector`、`UNETLoader`、`LoraLoaderModelOnly`、`AutoCropFaces`、`SaveImage`、`Fast Muter (rgthree)`、`39de0e19-7117-42df-9b3d-b677b1d4bf50`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
