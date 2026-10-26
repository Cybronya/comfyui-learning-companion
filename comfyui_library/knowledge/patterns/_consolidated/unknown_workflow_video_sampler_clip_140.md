---
name: unknown_workflow_video_sampler_clip_140
type: Unknown Workflow
frequency: 5
level: weak
coverage: 1
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/最新MagCache视频加速-文生视频_1933315042408312834.json, 视频生成/图生视频/超简单--Wan2.2 All-in-on 目前最快2.2文生视频+图生视频工作流_2043858986851639297.json, 视频生成/图生视频/超简单--Wan2.2 All-in-on 目前最快2.2文生视频+图生视频工作流_2043862678724157442.json, 视频生成/文生视频/Aiwood-Wan2.2 All-in-on 目前最快2.2文生视频+图生视频工作流_1950654567312740354.json, 视频生成/文生视频/Self Forcing原生文生视频_1933102536746471425.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_140

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/最新MagCache视频加速-文生视频_1933315042408312834.json、视频生成/图生视频/超简单--Wan2.2 All-in-on 目前最快2.2文生视频+图生视频工作流_2043858986851639297.json、视频生成/图生视频/超简单--Wan2.2 All-in-on 目前最快2.2文生视频+图生视频工作流_2043862678724157442.json、视频生成/文生视频/Aiwood-Wan2.2 All-in-on 目前最快2.2文生视频+图生视频工作流_1950654567312740354.json、视频生成/文生视频/Self Forcing原生文生视频_1933102536746471425.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/5 个有
- `WanImageToVideo` —— 3/5 个有
- `MagCache` —— 1/5 个有
- `Primitive integer [Crystools]` —— 1/5 个有
- `VAEDecodeTiled` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 30 | 5 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 5 | 0% |
| 采样算法 | sa_solver | - | 5 | 60% |
| 调度器 | beta | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 30，5 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 sa_solver，5 个样本，一致性 60%
- 调度器 最常用 beta，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（7/5 个样本）：Steps较低可能导致细节不足
