---
name: unknown_workflow_upscale_latent_upscale_sampler_20
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.54775
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, Fast Groups Bypasser (rgthree), KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadImage, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SplitSigmas, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/MiniMax H3-单模双采放大工作流（8G显存版）_2106241845180329986.json, 视频生成/图生视频/MiniMax H3-多参考生视频-优化版_2098769440409219073.json, 视频生成/文生视频/MiniMax H3 二采去油不爆音加速工作流_2096198192596606977.json, 视频生成/文生视频/Minimax H3 双采万能流_2094836628819894274.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_20

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3-单模双采放大工作流（8G显存版）_2106241845180329986.json、视频生成/图生视频/MiniMax H3-多参考生视频-优化版_2098769440409219073.json、视频生成/文生视频/MiniMax H3 二采去油不爆音加速工作流_2096198192596606977.json、视频生成/文生视频/Minimax H3 双采万能流_2094836628819894274.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `Fast Groups Bypasser (rgthree)`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SplitSigmas`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 3/4 个有
- `GetNode` —— 3/4 个有
- `LoadAudio` —— 3/4 个有
- `ModelAttentionBackend` —— 3/4 个有
- `SaveVideo` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `easy float` —— 3/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 2/4 个有
- `ModelPreviewOverrideKJ` —— 2/4 个有
- `Text` —— 2/4 个有
- `VHS_VideoCombine` —— 2/4 个有
- `easy loraStack` —— 2/4 个有
- `easy loraStackApply` —— 2/4 个有
- `MiniMaxChunkFeedForward` —— 1/4 个有
- `MiniMaxH3TurboSampler` —— 1/4 个有
- `MiniMaxLowVRAMAttention` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `Text Multiline` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy getNode` —— 1/4 个有
- `easy int` —— 1/4 个有
- `easy setNode` —— 1/4 个有
- `easy sleep` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
