---
name: unknown_workflow_video_sampler_clip_53
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8262
common_nodes: [CLIPTextEncode, INTConstant, KSampler, LoadImage, VAEDecode, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame]
problems: [Steps较低可能导致细节不足]
missing: [SimpleMath+]
members: [视频生成/文生视频/1979091835861766145.json, 视频生成/文生视频/2074055249905860608.json, 视频生成/文生视频/文生视频+图生视频+首尾帧工作流_2046504485811396609.json, 视频生成/文生视频/文生视频+图生视频+首尾帧工作流_2046752274625597441.json, 视频生成/文生视频/文生视频+图生视频+首尾帧工作流_2046762436140736513.json, 视频生成/文生视频/文生视频+图生视频+首尾帧工作流（Wan2.2-Rapid-AIO-Mega）_2044790035236528130.json, 视频生成/文生视频/文生视频+图生视频+首尾帧工作流（Wan2.2-Rapid-AIO-Mega）_2048651987276800002.json, 视频生成/文生视频/文生视频-AIO-MegaV7_2041408782072287234.json, 视频生成/文生视频/1968902178624741378.json, 视频生成/文生视频/文生视频千里江山图_2048964410516967425.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_53

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/1979091835861766145.json、视频生成/文生视频/2074055249905860608.json、视频生成/文生视频/文生视频+图生视频+首尾帧工作流_2046504485811396609.json、视频生成/文生视频/文生视频+图生视频+首尾帧工作流_2046752274625597441.json、视频生成/文生视频/文生视频+图生视频+首尾帧工作流_2046762436140736513.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `INTConstant`
- `KSampler`
- `LoadImage`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 8/10 个有
- `ModelSamplingSD3` —— 8/10 个有
- `PrimitiveInt` —— 8/10 个有
- `SimpleMath+` —— 7/10 个有
- `CM_IntToFloat` —— 5/10 个有
- `Fast Groups Bypasser (rgthree)` —— 5/10 个有
- `RHHiddenNodes` —— 2/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | ipndm | - | 10 | 60% |
| 调度器 | beta | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，10 个样本，一致性 60%
- 调度器 最常用 beta，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：SimpleMath+
