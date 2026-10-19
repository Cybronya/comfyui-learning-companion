---
name: unknown_workflow_sampler_clip_checkpoint_9
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.871167
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyHunyuanLatentVideo, KSampler, ModelSamplingSD3, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: [LayerUtility: PurgeVRAM, CR Prompt Text]
members: [图片生成/文生图/1965952460185579522.json, 视频生成/图生视频/1950720538975096834.json, 视频生成/文生视频/1955969425952395266.json, 视频生成/文生视频/1958204024900227073.json, 视频生成/文生视频/1959492706500292610.json, 视频生成/文生视频/1962792297958125570.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_9

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1965952460185579522.json、视频生成/图生视频/1950720538975096834.json、视频生成/文生视频/1955969425952395266.json、视频生成/文生视频/1958204024900227073.json、视频生成/文生视频/1959492706500292610.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `ModelSamplingSD3`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 5/6 个有
- `VHS_VideoCombine` —— 5/6 个有
- `JWInteger` —— 4/6 个有
- `LoadImage` —— 4/6 个有
- `SaveLatent` —— 4/6 个有
- `CLIPLoader` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `CR Prompt Text` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `INTConstant` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | sa_solver | - | 6 | 83% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，6 个样本，一致性 83%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: PurgeVRAM、CR Prompt Text
