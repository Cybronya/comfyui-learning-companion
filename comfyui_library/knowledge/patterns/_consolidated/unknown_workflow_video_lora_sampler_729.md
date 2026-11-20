---
name: unknown_workflow_video_lora_sampler_729
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.838
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, KSamplerSelect, LayerUtility: PurgeVRAM V2, LoraLoaderModelOnly, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/ki_MiniMax H3_多参分镜硬控流_2096068614947434498.json, 视频生成/图生视频/minimax_h3_多参_单图版注意力再加速_2105908156558823425.json, 视频生成/图生视频/minimax_h3_多参_短剧批量专用（支持90个角色、场景、道具）_2101317527325470722.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_729

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/ki_MiniMax H3_多参分镜硬控流_2096068614947434498.json、视频生成/图生视频/minimax_h3_多参_单图版注意力再加速_2105908156558823425.json、视频生成/图生视频/minimax_h3_多参_短剧批量专用（支持90个角色、场景、道具）_2101317527325470722.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LoraLoaderModelOnly`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `ManualSigmas` —— 2/3 个有
- `MiniMaxChunkFeedForward` —— 2/3 个有
- `ki_MiniMaxH3ReferenceToVideo` —— 2/3 个有
- `ExtendIntermediateSigmas` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `MiniMaxH3AudioConditioningT8` —— 1/3 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 1/3 个有
- `MiniMaxH3TurboSampler` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `SolAttnPatch` —— 1/3 个有
- `ki_宫格拼图高阶版` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
