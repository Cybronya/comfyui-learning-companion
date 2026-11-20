---
key: 平台全量/1-Aiden-MinimaxH3-超快速视频编辑流，v0.1版本！_2098469069073764353.json
name: 1-Aiden-MinimaxH3-超快速视频编辑流，v0.1版本！_2098469069073764353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/1-Aiden-MinimaxH3-超快速视频编辑流，v0.1版本！_2098469069073764353.json
hash: faba15762421fef7
coverage: 0.865385
learned_at: 2026-11-14 00:10:12
nodes: [MarkdownNote, MiniMaxLowVRAMAttention, ComfyMathExpression, CLIPTextEncode, SAM3_VideoTrack, SAM3_TrackToMask, GrowMaskWithBlur, VHS_VideoCombine, BlockifyMask, VHS_VideoCombine, MiniMaxChunkFeedForward, 孤海注释, CheckpointLoaderSimple, 孤海注释, easy showAnything, ModelPreviewOverrideKJ, VHS_VideoInfoLoaded, MaskToImage, KSamplerSelect, BasicScheduler, BasicGuider, SamplerCustomAdvanced, ModelAttentionBackend, MiniMaxH3SigmaShift, RandomNoise, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, 孤海注释, ImageFromBatch, LoadImage, ImageAndMaskPreview, CreateVideo, easy positive, PreviewAny, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, VHS_VideoCombine, RHLLMChatNode, VAEDecode, MiniMaxH3ReferenceToVideo, MarkdownNote, VHS_VideoCombine, VHS_VideoCombine, ColorMatchV2, VHS_LoadVideo, easy positive, ComfyMathExpression, easy positive, easy int, easy int]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 平台全量/1-Aiden-MinimaxH3-超快速视频编辑流，v0.1版本！_2098469069073764353.json

> 来源文件 `comfyui_library/workflows/平台全量/1-Aiden-MinimaxH3-超快速视频编辑流，v0.1版本！_2098469069073764353.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（52 个）：
- `MarkdownNote`
- `MiniMaxLowVRAMAttention`
- `ComfyMathExpression`
- `CLIPTextEncode` ★核心
- `SAM3_VideoTrack`
- `SAM3_TrackToMask`
- `GrowMaskWithBlur`
- `VHS_VideoCombine`
- `BlockifyMask`
- `VHS_VideoCombine`
- `MiniMaxChunkFeedForward`
- `孤海注释`
- `CheckpointLoaderSimple` ★核心
- `孤海注释`
- `easy showAnything`
- `ModelPreviewOverrideKJ`
- `VHS_VideoInfoLoaded`
- `MaskToImage`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `ModelAttentionBackend`
- `MiniMaxH3SigmaShift`
- `RandomNoise`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSizeAndCount`
- `孤海注释`
- `ImageFromBatch`
- `LoadImage`
- `ImageAndMaskPreview`
- `CreateVideo`
- `easy positive`
- `PreviewAny`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `VHS_VideoCombine`
- `RHLLMChatNode`
- `VAEDecode` ★核心
- `MiniMaxH3ReferenceToVideo`
- `MarkdownNote`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ColorMatchV2`
- `VHS_LoadVideo`
- `easy positive`
- `ComfyMathExpression`
- `easy positive`
- `easy int`
- `easy int`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **87%**（45/52）

**有卡**：`MiniMaxLowVRAMAttention`、`ComfyMathExpression`、`CLIPTextEncode`、`SAM3_VideoTrack`、`SAM3_TrackToMask`、`GrowMaskWithBlur`、`VHS_VideoCombine`、`BlockifyMask`、`MiniMaxChunkFeedForward`、`CheckpointLoaderSimple`、`ModelPreviewOverrideKJ`、`VHS_VideoInfoLoaded`、`MaskToImage`、`KSamplerSelect`、`BasicScheduler`、`BasicGuider`、`SamplerCustomAdvanced`、`ModelAttentionBackend`、`MiniMaxH3SigmaShift`、`RandomNoise`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSizeAndCount`、`ImageFromBatch`、`LoadImage`、`ImageAndMaskPreview`、`CreateVideo`、`easy positive`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`RHLLMChatNode`、`VAEDecode`、`MiniMaxH3ReferenceToVideo`、`ColorMatchV2`、`VHS_LoadVideo`、`easy int`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage
