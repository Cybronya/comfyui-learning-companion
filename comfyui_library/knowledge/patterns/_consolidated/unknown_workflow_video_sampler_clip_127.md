---
name: unknown_workflow_video_sampler_clip_127
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.979
common_nodes: [CLIPTextEncode, INTConstant, KSampler, ModelSamplingSD3, TrimVideoLatent, VAEDecode, VHS_VideoCombine, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: [Image Rembg (Remove Background)]
members: [视频生成/文生视频/1968253797757792257.json, 视频生成/文生视频/1968254465616826370.json, 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-双图参考_2072999566997495808.json, 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-双图参考_1982050786727337985.json, 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-文生视频_1982047914778337281.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_127

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/文生视频/1968253797757792257.json、视频生成/文生视频/1968254465616826370.json、视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-双图参考_2072999566997495808.json、视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-双图参考_1982050786727337985.json、视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-文生视频_1982047914778337281.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `INTConstant`
- `KSampler`
- `ModelSamplingSD3`
- `TrimVideoLatent`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 3/5 个有
- `Image Rembg (Remove Background)` —— 3/5 个有
- `ImageConcanate` —— 3/5 个有
- `LoadImage` —— 3/5 个有
- `TTP_Expand_And_Mask` —— 3/5 个有
- `AV_VAELoader` —— 2/5 个有
- `CLIPLoader` —— 2/5 个有
- `UNETLoader` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 5 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，5 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Image Rembg (Remove Background)
