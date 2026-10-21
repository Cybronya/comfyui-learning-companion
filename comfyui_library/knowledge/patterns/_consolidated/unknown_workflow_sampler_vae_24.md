---
name: unknown_workflow_sampler_vae_24
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8727
common_nodes: [CreateVideo, RHMiniMaxH3DecodeAV, RHMiniMaxH3DirectModelLoader, RHMiniMaxH3DirectTextEncoderLoader, RHMiniMaxH3DirectVAELoader, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3T2VATarget, RHMiniMaxH3T2VATextEncode, SaveVideo]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax-H3_文生视频_RH版_零质量损失_2100197900319027202.json, 视频生成/文生视频/MiniMax-H3_文生视频_RH版_零质量损失_2101873315043430401.json, 视频生成/文生视频/MiniMax-H3文生视频_2084112909017378818.json, 视频生成/文生视频/MiniMaxH3开源版-文生视频满血版_2085664955076014081.json, 视频生成/文生视频/MiniMax_H3_FL2VA开源版-文生视频_2098934858633535489.json, 视频生成/文生视频/MiniMax_H3_FL2VA开源版-文生视频_2098992624169472002.json, 视频生成/文生视频/MiniMax_H3_FL2VA开源版-文生视频_2099668092489125890.json, 视频生成/文生视频/Minimax H3文生视频工作流_2084627156352720897.json, 视频生成/文生视频/Mini开源Max+H3+-文生视频满血版_2084270525710426114.json, 视频生成/文生视频/【开源】MiniMax_H3 文生视频满血版_2084157675742519298.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_24

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/MiniMax-H3_文生视频_RH版_零质量损失_2100197900319027202.json、视频生成/文生视频/MiniMax-H3_文生视频_RH版_零质量损失_2101873315043430401.json、视频生成/文生视频/MiniMax-H3文生视频_2084112909017378818.json、视频生成/文生视频/MiniMaxH3开源版-文生视频满血版_2085664955076014081.json、视频生成/文生视频/MiniMax_H3_FL2VA开源版-文生视频_2098934858633535489.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `CreateVideo`
- `RHMiniMaxH3DecodeAV`
- `RHMiniMaxH3DirectModelLoader`
- `RHMiniMaxH3DirectTextEncoderLoader`
- `RHMiniMaxH3DirectVAELoader`
- `RHMiniMaxH3DualSigmaSampler`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3T2VATarget`
- `RHMiniMaxH3T2VATextEncode`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 5/10 个有
- `PreviewImage` —— 5/10 个有
- `PrimitiveFloat` —— 2/10 个有
- `ResolutionSelector` —— 2/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `Text` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
