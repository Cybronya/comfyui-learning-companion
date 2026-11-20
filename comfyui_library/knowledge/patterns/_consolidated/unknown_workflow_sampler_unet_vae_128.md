---
name: unknown_workflow_sampler_unet_vae_128
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.7595
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, ComfyMathExpression, CreateVideo, KSamplerSelect, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/R2V-参考生视频-5060Ti16G-极速加速版_2102730812373422081.json, 视频生成/图生视频/h3参考生视频_2110215490152001538.json, 视频生成/图生视频/minMax H3 多参考生视频+加速_2090270612068585473.json, 视频生成/图生视频/minimax_h3_r2v官方参考_2114198314131484674.json, 视频生成/图生视频/海螺Minimax H3_r2v 官方加速版_2091451868676452353.json, 视频生成/图生视频/（首尾帧 2图）MINIMAX H3  图生视频_2111267377957658625.json, 视频生成/文生视频/MiniMax-4步加速工作流_2085226868072083458.json, 视频生成/文生视频/Minimax H3 Veda 稀疏注意力8步极速版 文生视频_2108479691337326593.json, 视频生成/文生视频/azheng_2095047905232121858.json, 视频生成/文生视频/极速生成视频｜H3 FAST VSA + 真实人物 LoRA H3 Realism_2094205448344920065.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_128

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/R2V-参考生视频-5060Ti16G-极速加速版_2102730812373422081.json、视频生成/图生视频/h3参考生视频_2110215490152001538.json、视频生成/图生视频/minMax H3 多参考生视频+加速_2090270612068585473.json、视频生成/图生视频/minimax_h3_r2v官方参考_2114198314131484674.json、视频生成/图生视频/海螺Minimax H3_r2v 官方加速版_2091451868676452353.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 10 个 workflow 都包含：
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
- `LoadImage` —— 9/10 个有
- `LoraLoaderModelOnly` —— 9/10 个有
- `MiniMaxH3ReferenceToVideo` —— 8/10 个有
- `PrimitiveStringMultiline` —— 8/10 个有
- `ComfySwitchNode` —— 7/10 个有
- `PrimitiveBoolean` —— 7/10 个有
- `PrimitiveInt` —— 7/10 个有
- `LoadAudio` —— 3/10 个有
- `MiniMaxH3ImageToVideo` —— 3/10 个有
- `ModelAttentionBackend` —— 2/10 个有
- `PathchSageAttentionKJ` —— 2/10 个有
- `LoraLoaderBypassModelOnly` —— 1/10 个有
- `MiniMaxH3QwenReferencePrefixCacheT8Advanced` —— 1/10 个有
- `RHMiniMaxH3PromptOptimizerMedia` —— 1/10 个有
- `SolAttnMiniMax` —— 1/10 个有
- `VedaSparseAttention` —— 1/10 个有
- `XB_ReferenceAny` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
