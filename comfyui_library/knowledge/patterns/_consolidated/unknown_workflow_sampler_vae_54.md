---
name: unknown_workflow_sampler_vae_54
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.888
common_nodes: [CreateVideo, LoadImage, RHMiniMaxH3DecodeAV, RHMiniMaxH3DualSigmaSampler, RHMiniMaxH3EmptyAVLatent, RHMiniMaxH3FL2VAEncode, RHMiniMaxH3FL2VAFirstFrameCondition, RHMiniMaxH3FL2VAModelLoader, RHMiniMaxH3FL2VATarget, RHMiniMaxH3FL2VATextEncoderLoader, RHMiniMaxH3FL2VAVAELoader, SaveVideo]
problems: []
missing: []
members: [视频生成/文生视频/MiniMax H3 低显存15秒音画工作流_2085021778228891650.json, 视频生成/文生视频/MiniMax H3 开源版-首帧参考生视频_2084478495324987394.json, 视频生成/文生视频/MiniMax H3开源版-首_尾_文生视频集合版_2084490201048633345.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_54

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/MiniMax H3 低显存15秒音画工作流_2085021778228891650.json、视频生成/文生视频/MiniMax H3 开源版-首帧参考生视频_2084478495324987394.json、视频生成/文生视频/MiniMax H3开源版-首_尾_文生视频集合版_2084490201048633345.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateVideo`
- `LoadImage`
- `RHMiniMaxH3DecodeAV`
- `RHMiniMaxH3DualSigmaSampler`
- `RHMiniMaxH3EmptyAVLatent`
- `RHMiniMaxH3FL2VAEncode`
- `RHMiniMaxH3FL2VAFirstFrameCondition`
- `RHMiniMaxH3FL2VAModelLoader`
- `RHMiniMaxH3FL2VATarget`
- `RHMiniMaxH3FL2VATextEncoderLoader`
- `RHMiniMaxH3FL2VAVAELoader`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 2/3 个有
- `ImpactSwitch` —— 2/3 个有
- `Int` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RHMiniMaxH3DirectModelLoader` —— 1/3 个有
- `RHMiniMaxH3DirectTextEncoderLoader` —— 1/3 个有
- `RHMiniMaxH3DirectVAELoader` —— 1/3 个有
- `RHMiniMaxH3FL2VALastFrameCondition` —— 1/3 个有
- `RHMiniMaxH3T2VATarget` —— 1/3 个有
- `RHMiniMaxH3T2VATextEncode` —— 1/3 个有
- `忽略多组孤海` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
