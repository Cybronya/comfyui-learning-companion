---
name: unknown_workflow_sampler_checkpoint_vae_17
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.921333
common_nodes: [ImageOnlyCheckpointLoader, KSampler, LoadImage, SVD_img2vid_Conditioning, VAEDecode, VideoLinearCFGGuidance]
problems: []
missing: []
members: [视频生成/图生视频/1777958599344066561.json, 视频生成/图生视频/1791025738556755969.json, 视频生成/图生视频/1791027207213273090.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_checkpoint_vae_17

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1777958599344066561.json、视频生成/图生视频/1791025738556755969.json、视频生成/图生视频/1791027207213273090.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageOnlyCheckpointLoader`
- `KSampler`
- `LoadImage`
- `SVD_img2vid_Conditioning`
- `VAEDecode`
- `VideoLinearCFGGuidance`

**可变部分**（部分 workflow 才有）：
- `ADE_AnimateDiffCombine` —— 2/3 个有
- `ImageResize+` —— 2/3 个有
- `VHS_VideoCombine` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
