---
name: unknown_workflow_video_lora_sampler_962
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.865
common_nodes: [BasicGuider, BasicScheduler, BlockifyMask, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ColorMatchV2, ComfyMathExpression, CreateVideo, GetImageSizeAndCount, GrowMaskWithBlur, ImageAndMaskPreview, ImageFromBatch, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MaskToImage, MiniMaxChunkFeedForward, MiniMaxH3ReferenceToVideo, MiniMaxH3SigmaShift, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewAny, RHLLMChatNode, RandomNoise, SAM3_TrackToMask, SAM3_VideoTrack, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, easy int, easy positive, easy showAnything, 孤海注释]
problems: []
missing: []
members: [平台全量/1-Aiden-MinimaxH3-超快速视频编辑流，v0.1版本！_2098469069073764353.json, 视频生成/图生视频/MinimaxH3-超快速视频换人自动提示词版_2100599403835912194.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_962

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/1-Aiden-MinimaxH3-超快速视频编辑流，v0.1版本！_2098469069073764353.json、视频生成/图生视频/MinimaxH3-超快速视频换人自动提示词版_2100599403835912194.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `BlockifyMask`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatchV2`
- `ComfyMathExpression`
- `CreateVideo`
- `GetImageSizeAndCount`
- `GrowMaskWithBlur`
- `ImageAndMaskPreview`
- `ImageFromBatch`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3SigmaShift`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewAny`
- `RHLLMChatNode`
- `RandomNoise`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `easy int`
- `easy positive`
- `easy showAnything`
- `孤海注释`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
