---
name: unknown_workflow_sampler_vae_25
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.836
common_nodes: [BasicGuider, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, LoadImage, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: [Seed (rgthree)]
members: [视频生成/图生视频/新手短剧_MiniMax H3 多参考视频生成工作流 v1_0_2106283115156172802.json, 视频生成/图生视频/海螺H3 图生视频（8步加速LoRA）_2085286347509686274.json, 视频生成/图生视频/海螺H3 多参视频（加速节点-加速版）768P_2085282734813044738.json, 视频生成/图生视频/海螺H3八步极速生成全能参考生视频_2087529254698446850.json, 视频生成/图生视频/海螺Minimax H3_r2v 官方加速版_2091451868676452353.json, 视频生成/图生视频/自用版 Minimax H3 全能多参生视频_2085256791130202114.json, 视频生成/图生视频/（2320）H3-最优官流_2089001915131711490.json, 视频生成/文生视频/H3-最优官流_2088982134630469634.json, 视频生成/文生视频/azheng_2095047905232121858.json, 视频生成/文生视频/minimaxH3多参考视频工作流（超级加速版）_2080928622717784066.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_25

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/新手短剧_MiniMax H3 多参考视频生成工作流 v1_0_2106283115156172802.json、视频生成/图生视频/海螺H3 图生视频（8步加速LoRA）_2085286347509686274.json、视频生成/图生视频/海螺H3 多参视频（加速节点-加速版）768P_2085282734813044738.json、视频生成/图生视频/海螺H3八步极速生成全能参考生视频_2087529254698446850.json、视频生成/图生视频/海螺Minimax H3_r2v 官方加速版_2091451868676452353.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `KSamplerSelect`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `UNETLoader` —— 9/10 个有
- `LoraLoaderModelOnly` —— 8/10 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 5/10 个有
- `PrimitiveBoolean` —— 5/10 个有
- `ComfySwitchNode` —— 4/10 个有
- `ModelPreviewOverrideKJ` —— 4/10 个有
- `PathchSageAttentionKJ` —— 4/10 个有
- `LoadAudio` —— 3/10 个有
- `VHS_LoadVideo` —— 3/10 个有
- `ManualSigmas` —— 2/10 个有
- `PrimitiveInt` —— 2/10 个有
- `AnyBooleanSwitch` —— 1/10 个有
- `DiffusionModelLoaderKJ` —— 1/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `Load Lora` —— 1/10 个有
- `MiniMaxH3BlockCacheT8` —— 1/10 个有
- `Seed (rgthree)` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Seed (rgthree)
