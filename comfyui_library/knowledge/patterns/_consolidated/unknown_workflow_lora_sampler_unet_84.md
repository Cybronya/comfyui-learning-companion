---
name: unknown_workflow_lora_sampler_unet_84
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.661
common_nodes: [AD_video_merge, Any Switch (rgthree), BasicGuider, BasicScheduler, BlockSparseAttention, CLIPLoader, ComfyMathExpression, CreateVideo, Fast Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Muter (rgthree), GetNode, GetVideoComponents, HAIGC_VideoLoader, ImageFromBatch, KSamplerSelect, LoadAudio, LoadImage, LoadVideo, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3AddGuide, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, SetNode, TrimAudioDuration, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VRGDG_MiniMaxH3AudioDrive, Video Slice, VideoTemporalCrop]
problems: []
missing: []
members: [视频生成/图生视频/Minimax h3 多帧+参考+长视频（byCc菜）_2106258896963850241.json, 视频生成/视频生视频/Minimax h3 多帧+参考+长视频（byCc菜）_2106258896963850241.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_84

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Minimax h3 多帧+参考+长视频（byCc菜）_2106258896963850241.json、视频生成/视频生视频/Minimax h3 多帧+参考+长视频（byCc菜）_2106258896963850241.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `AD_video_merge`
- `Any Switch (rgthree)`
- `BasicGuider`
- `BasicScheduler`
- `BlockSparseAttention`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `Fast Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `GetVideoComponents`
- `HAIGC_VideoLoader`
- `ImageFromBatch`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3AddGuide`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetNode`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VRGDG_MiniMaxH3AudioDrive`
- `Video Slice`
- `VideoTemporalCrop`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
