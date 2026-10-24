---
name: unknown_workflow_video_sampler_clip_280
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.889
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler (Efficient), ModelSamplingSD3, Seed Everywhere, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/一键运行：最新 WAN2.2 融合模型 文生视频_1958711143466483714.json, 视频生成/文生视频/文生视频 Wan2.2 WAN2.2-14B-Rapid-AlO Mega V7  融合_1977557329031897089.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_280

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/一键运行：最新 WAN2.2 融合模型 文生视频_1958711143466483714.json、视频生成/文生视频/文生视频 Wan2.2 WAN2.2-14B-Rapid-AlO Mega V7  融合_1977557329031897089.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler (Efficient)`
- `ModelSamplingSD3`
- `Seed Everywhere`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `EmptyHunyuanLatentVideo` —— 1/2 个有
- `WanVaceToVideo` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | - | 2 | 67% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | sa_solver | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 6，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
