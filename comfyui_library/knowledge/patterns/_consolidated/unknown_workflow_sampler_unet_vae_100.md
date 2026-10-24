---
name: unknown_workflow_sampler_unet_vae_100
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8604
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Minimax H3 数字人带货视频_2084925025257353218.json, 视频生成/图生视频/Minimax H3 极速单图或首尾帧视频工作流_2085305466082643970.json, 视频生成/图生视频/Minimax H3-i2v 加速版图生视频-文生视频_2091734941167087618.json, 视频生成/图生视频/Minimax H3-t2v 多图参考生视频_2084205760405397505.json, 视频生成/图生视频/Minimax H3-图生视频（高动态去噪点）_2089348010357641217.json, 视频生成/图生视频/Minimax H3-多参视频生成（高动态去噪点）_2089353256249151489.json, 视频生成/图生视频/Minimax H3-最佳动态战斗版V2_2096214859611467777.json, 视频生成/图生视频/minimax h3多参模式武器打斗_2095692154944442370.json, 视频生成/图生视频/minimaxH3首尾帧视频工作流（超级加速版）_2084965664602804226.json, 视频生成/图生视频/黄色的大宝剑打斗流_2109476674894131202.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_100

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/Minimax H3 数字人带货视频_2084925025257353218.json、视频生成/图生视频/Minimax H3 极速单图或首尾帧视频工作流_2085305466082643970.json、视频生成/图生视频/Minimax H3-i2v 加速版图生视频-文生视频_2091734941167087618.json、视频生成/图生视频/Minimax H3-t2v 多图参考生视频_2084205760405397505.json、视频生成/图生视频/Minimax H3-图生视频（高动态去噪点）_2089348010357641217.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
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
- `LoraLoaderModelOnly` —— 7/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/10 个有
- `MiniMaxH3ReferenceToVideo` —— 6/10 个有
- `PrimitiveStringMultiline` —— 6/10 个有
- `ExtendIntermediateSigmas` —— 5/10 个有
- `MiniMaxH3ImageToVideo` —— 4/10 个有
- `ModelAttentionBackend` —— 4/10 个有
- `DisableNoise` —— 3/10 个有
- `Label (rgthree)` —— 3/10 个有
- `ModelPreviewOverrideKJ` —— 3/10 个有
- `SplitSigmasDenoise` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `H3SigmaRefiner` —— 2/10 个有
- `MiniMaxH3SigmaShift` —— 2/10 个有
- `easy cleanGpuUsed` —— 2/10 个有
- `BlockSparseAttention` —— 1/10 个有
- `CLIPTextEncode` —— 1/10 个有
- `CacheDiT_Model_Optimizer` —— 1/10 个有
- `Fast Groups Muter (rgthree)` —— 1/10 个有
- `ImageScaleToTotalPixels` —— 1/10 个有
- `LoadAudio` —— 1/10 个有
- `PathchSageAttentionKJ` —— 1/10 个有
- `SolAttnPatch` —— 1/10 个有
- `Text Concatenate` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
