---
name: unknown_workflow_sampler_vae_73
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.979333
common_nodes: [CreateVideo, RHMiniMaxH3DecodeAV, RHMiniMaxH3DirectModelLoader, RHMiniMaxH3DirectTextEncoderLoader, RHMiniMaxH3DirectVAELoader, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3T2VATarget, RHMiniMaxH3T2VATextEncode, SaveVideo]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax+H3文生视频_2084569586896297985.json, 视频生成/文生视频/MiniMax-H3-文生视频-提示词自动扩写_2085187597655166978.json, 视频生成/文生视频/MiniMax-H3-文生视频-极简-手动提示词_2084575861231144962.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_73

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/MiniMax+H3文生视频_2084569586896297985.json、视频生成/文生视频/MiniMax-H3-文生视频-提示词自动扩写_2085187597655166978.json、视频生成/文生视频/MiniMax-H3-文生视频-极简-手动提示词_2084575861231144962.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
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
- `easy float` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `PreviewVideoNode` —— 1/3 个有
- `RH_LLMAPI_Pro_Node` —— 1/3 个有
- `ShellAgentPluginOutputText` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
