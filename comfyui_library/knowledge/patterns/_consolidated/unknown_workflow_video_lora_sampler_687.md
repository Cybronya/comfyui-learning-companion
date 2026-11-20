---
name: unknown_workflow_video_lora_sampler_687
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7505
common_nodes: [BasicScheduler, CLIPLoader, ComfyMathExpression, KSamplerSelect, LayerUtility: PurgeVRAM V2, LoadAudio, LoraLoaderModelOnly, ManualSigmas, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, ModelAttentionBackend, ModelPreviewOverrideKJ, PreviewImage, PrimitiveFloat, PrimitiveStringMultiline, ResolutionSelector, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, ki_MiniMaxH3ReferenceToVideo, ki_宫格拼图高阶版]
problems: []
missing: []
members: [平台全量/ki_MiniMax H3_多参selflift双采分镜硬控流_2105695202211098626.json, 平台全量/ki_MiniMax H3_多参selflift双采分镜硬控流_2119420965615661058.json, 平台全量/ki_MiniMax_H3_多参分镜硬控流_2117404280977186817.json, 视频生成/图生视频/ki_MiniMax H3_多参分镜硬控流_2096068614947434498.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_687

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/ki_MiniMax H3_多参selflift双采分镜硬控流_2105695202211098626.json、平台全量/ki_MiniMax H3_多参selflift双采分镜硬控流_2119420965615661058.json、平台全量/ki_MiniMax_H3_多参分镜硬控流_2117404280977186817.json、视频生成/图生视频/ki_MiniMax H3_多参分镜硬控流_2096068614947434498.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `ModelAttentionBackend`
- `ModelPreviewOverrideKJ`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `ki_MiniMaxH3ReferenceToVideo`
- `ki_宫格拼图高阶版`

**可变部分**（部分 workflow 才有）：
- `BasicGuider` —— 2/4 个有
- `BlockSparseAttention` —— 2/4 个有
- `ConditioningZeroOut` —— 2/4 个有
- `MiniMaxH3SigmaShift` —— 2/4 个有
- `MiniMaxH3TurboSampler` —— 2/4 个有
- `RandomNoise` —— 2/4 个有
- `SamplerCustomAdvanced` —— 2/4 个有
- `SelfLiftH3Sampler` —— 2/4 个有
- `easy ifElse` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
