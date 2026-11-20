---
name: unknown_workflow_video_lora_sampler_986
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.929
common_nodes: [ACE_AudioCrop, BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, GrowMaskWithBlur, ImageAndMaskPreview, ImageFromBatch, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadSAM3Model, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PreviewAny, PreviewImage, RH_LLMAPI_Pro_Node, RandomNoise, SAM3BBoxCollector, SAM3PointCollector, SAM3Segmentation, SAM3_TrackToMask, SAM3_VideoTrack, SamplerCustomAdvanced, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive, easy convertAnything, easy int, ttN concat]
problems: []
missing: []
members: [平台全量/minimax H3视频换头_2100457657323843586.json, 视频生成/图生视频/minimax H3视频换头-自动遮罩_2103390777660502017.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_986

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/minimax H3视频换头_2100457657323843586.json、视频生成/图生视频/minimax H3视频换头-自动遮罩_2103390777660502017.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `ACE_AudioCrop`
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `GrowMaskWithBlur`
- `ImageAndMaskPreview`
- `ImageFromBatch`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadSAM3Model`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PreviewAny`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SAM3BBoxCollector`
- `SAM3PointCollector`
- `SAM3Segmentation`
- `SAM3_TrackToMask`
- `SAM3_VideoTrack`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`
- `easy convertAnything`
- `easy int`
- `ttN concat`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
