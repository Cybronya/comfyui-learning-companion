---
name: unknown_workflow_sampler_unet_vae_237
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.699167
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [平台全量/（Cc菜2026-09-08）Minimax h3 高一致性 多镜头、音频参考_2097488721066160130.json, 数字人/数字人/7度工作流改版1_2098964914600763393.json, 视频生成/图生视频/FastH3 Ominiref 8步高质量视频_2113137033521754114.json, 视频生成/图生视频/FastH3 OmniRef_ Reference to Video_2114729919665233922.json, 视频生成/图生视频/MINIMAXH3图生视频_2093009790346813441.json, 视频生成/图生视频/MiniMax H3 长视频  音频驱动（数字人）唱歌30s_1分钟 切换_2099343389337673730.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_237

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/（Cc菜2026-09-08）Minimax h3 高一致性 多镜头、音频参考_2097488721066160130.json、数字人/数字人/7度工作流改版1_2098964914600763393.json、视频生成/图生视频/FastH3 Ominiref 8步高质量视频_2113137033521754114.json、视频生成/图生视频/FastH3 OmniRef_ Reference to Video_2114729919665233922.json、视频生成/图生视频/MINIMAXH3图生视频_2093009790346813441.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 5/6 个有
- `SaveVideo` —— 5/6 个有
- `CreateVideo` —— 4/6 个有
- `GetNode` —— 4/6 个有
- `MiniMaxH3SigmaShift` —— 4/6 个有
- `ModelAttentionBackend` —— 4/6 个有
- `PrimitiveStringMultiline` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `BlockSparseAttention` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `MiniMaxH3AddGuide` —— 2/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `忽略多组孤海` —— 2/6 个有
- `AudioConcat` —— 1/6 个有
- `ImageBatch` —— 1/6 个有
- `MiniMaxH3SLAPrecisionV2T8Advanced` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `SelectImages` —— 1/6 个有
- `Text` —— 1/6 个有
- `TrimAudioDuration` —— 1/6 个有
- `VHS_VideoCombine` —— 1/6 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 1/6 个有
- `VideoCombineV2` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
