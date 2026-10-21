---
name: unknown_workflow_sampler_unet_vae_135
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.8965
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3 极速单图或首尾帧视频工作流_2085305466082643970.json, 视频生成/图生视频/Minimax H3-i2v 加速版图生视频-文生视频_2091734941167087618.json, 视频生成/图生视频/Minimax H3-图生视频（高动态去噪点）_2089348010357641217.json, 视频生成/图生视频/Minimax H3-多参视频生成（高动态去噪点）_2089353256249151489.json, 视频生成/图生视频/Minimax H3-长视频生成_2095517026205913089.json, 视频生成/文生视频/Minimax H3-文生视频（高动态去噪点）_2089345292486402050.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_135

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Minimax H3 极速单图或首尾帧视频工作流_2085305466082643970.json、视频生成/图生视频/Minimax H3-i2v 加速版图生视频-文生视频_2091734941167087618.json、视频生成/图生视频/Minimax H3-图生视频（高动态去噪点）_2089348010357641217.json、视频生成/图生视频/Minimax H3-多参视频生成（高动态去噪点）_2089353256249151489.json、视频生成/图生视频/Minimax H3-长视频生成_2095517026205913089.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 5/6 个有
- `LoraLoaderModelOnly` —— 5/6 个有
- `MiniMaxH3ImageToVideo` —— 5/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/6 个有
- `ModelAttentionBackend` —— 4/6 个有
- `ExtendIntermediateSigmas` —— 3/6 个有
- `H3SigmaRefiner` —— 3/6 个有
- `Label (rgthree)` —— 2/6 个有
- `MiniMaxH3SigmaShift` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `CacheDiT_Model_Optimizer` —— 1/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `ImageFromBatch` —— 1/6 个有
- `MiniMaxH3AddGuide` —— 1/6 个有
- `MiniMaxH3ReferenceToVideo` —— 1/6 个有
- `ModelPreviewOverrideKJ` —— 1/6 个有
- `SolAttnPatch` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
