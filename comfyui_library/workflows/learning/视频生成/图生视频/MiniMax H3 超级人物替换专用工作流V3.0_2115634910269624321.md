---
key: 视频生成/图生视频/MiniMax H3 超级人物替换专用工作流V3.0_2115634910269624321.json
name: MiniMax H3 超级人物替换专用工作流V3.0_2115634910269624321
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 超级人物替换专用工作流V3.0_2115634910269624321.json
hash: 5444782058b2a09a
coverage: 0.882353
learned_at: 2026-10-30 23:28:29
nodes: [LTXVSeparateAVLatent, MiniMaxLowVRAMAttention, RandomNoise, MiniMaxChunkFeedForward, BasicGuider, KSamplerSelect, ResizeImagesByShorterEdge, ResizeImagesByShorterEdge, MinimaxH3LatentUpscaler3D, BasicGuider, SamplerCustomAdvanced, MiniMaxLowVRAMAttention, VAEDecodeAudio, MiniMaxChunkFeedForward, LoraLoaderModelOnly, CLIPLoader, ManualSigmas, SamplerCustomAdvanced, UNETLoader, ModelPreviewOverrideKJ, H3SigmaRefiner, VHS_VideoCombine, RandomNoise, VAELoader, LTXVConcatAVLatent, ImageFromBatch, VAELoader, VAEDecodeAudio, VAEDecode, ComfyMathExpression, ImageBatchMulti, ImageFromBatch, RepeatImageBatch, ImageFromBatch, VHS_VideoInfo, ComfyMathExpression, ComfyMathExpression, PrimitiveFloat, VAEDecode, VHS_VideoCombine, ResizeImagesByShorterEdge, LoadImage, LoadImage, PrimitiveInt, MiniMaxH3ReferenceToVideo, ResizeImagesByShorterEdge, ResizeImagesByShorterEdge, ResizeImagesByShorterEdge, LoadImage, ResolutionSelector, BasicScheduler, KSamplerSelect, ComfyMathExpression, ComfyMathExpression, ModelAttentionBackend, ModelAttentionBackend, MarkdownNote, LoraLoaderModelOnly, ImageScaleToTotalPixels, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, VHS_LoadVideo, easy showAnything, PrimitiveStringMultiline, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax H3 超级人物替换专用工作流V3.0_2115634910269624321.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 超级人物替换专用工作流V3.0_2115634910269624321.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（68 个）：
- `LTXVSeparateAVLatent`
- `MiniMaxLowVRAMAttention`
- `RandomNoise`
- `MiniMaxChunkFeedForward`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `ResizeImagesByShorterEdge`
- `ResizeImagesByShorterEdge`
- `MinimaxH3LatentUpscaler3D`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxLowVRAMAttention`
- `VAEDecodeAudio` ★核心
- `MiniMaxChunkFeedForward`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `ModelPreviewOverrideKJ`
- `H3SigmaRefiner`
- `VHS_VideoCombine`
- `RandomNoise`
- `VAELoader`
- `LTXVConcatAVLatent`
- `ImageFromBatch`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `ComfyMathExpression`
- `ImageBatchMulti`
- `ImageFromBatch`
- `RepeatImageBatch`
- `ImageFromBatch`
- `VHS_VideoInfo`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `ResizeImagesByShorterEdge`
- `LoadImage`
- `LoadImage`
- `PrimitiveInt`
- `MiniMaxH3ReferenceToVideo`
- `ResizeImagesByShorterEdge`
- `ResizeImagesByShorterEdge`
- `ResizeImagesByShorterEdge`
- `LoadImage`
- `ResolutionSelector`
- `BasicScheduler`
- `KSamplerSelect` ★核心
- `ComfyMathExpression`
- `ComfyMathExpression`
- `ModelAttentionBackend`
- `ModelAttentionBackend`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToTotalPixels`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `VHS_LoadVideo`
- `easy showAnything`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **88%**（60/68）

**有卡**：`LTXVSeparateAVLatent`、`MiniMaxLowVRAMAttention`、`RandomNoise`、`MiniMaxChunkFeedForward`、`BasicGuider`、`KSamplerSelect`、`ResizeImagesByShorterEdge`、`MinimaxH3LatentUpscaler3D`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`LoraLoaderModelOnly`、`CLIPLoader`、`ManualSigmas`、`UNETLoader`、`ModelPreviewOverrideKJ`、`H3SigmaRefiner`、`VHS_VideoCombine`、`VAELoader`、`LTXVConcatAVLatent`、`ImageFromBatch`、`VAEDecode`、`ComfyMathExpression`、`ImageBatchMulti`、`RepeatImageBatch`、`VHS_VideoInfo`、`LoadImage`、`MiniMaxH3ReferenceToVideo`、`ResolutionSelector`、`BasicScheduler`、`ModelAttentionBackend`、`ImageScaleToTotalPixels`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
