---
name: unknown_workflow_video_sampler_clip_215
type: Unknown Workflow
frequency: 3
level: strong
coverage: 1
common_nodes: [CLIPTextEncode, INTConstant, KSampler, ModelSamplingSD3, TrimVideoLatent, VAEDecode, VHS_VideoCombine, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-双图参考_1968254465616826370.json, 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-双图参考_1982050786727337985.json, 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-文生视频_1982047914778337281.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_215

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-双图参考_1968254465616826370.json、视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-双图参考_1982050786727337985.json、视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-文生视频_1982047914778337281.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：100%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `INTConstant`
- `KSampler`
- `ModelSamplingSD3`
- `TrimVideoLatent`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `AV_VAELoader` —— 2/3 个有
- `CLIPLoader` —— 2/3 个有
- `Image Rembg (Remove Background)` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `TTP_Expand_And_Mask` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 67% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
