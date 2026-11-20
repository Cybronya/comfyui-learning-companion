---
name: unknown_workflow_sampler_clip_checkpoint_23
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.9545
common_nodes: [BrushNet, BrushNetLoader, CLIPTextEncode, CheckpointLoaderSimple, KSampler, LoadImage, SaveImage, VAEDecode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/brushnet 扩图_1985414341312790530.json, 图片生成/图生图/局部重绘工作流_2002978130610515970.json, 图片生成/图生图/强力控制产品更换背景XLL 大模型产品背景生成_1918116467445792770.json, 图片生成/图生图/简单的局部重绘_1914049660208541698.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_23

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/brushnet 扩图_1985414341312790530.json、图片生成/图生图/局部重绘工作流_2002978130610515970.json、图片生成/图生图/强力控制产品更换背景XLL 大模型产品背景生成_1918116467445792770.json、图片生成/图生图/简单的局部重绘_1914049660208541698.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `BrushNet`
- `BrushNetLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/4 个有
- `ImagePadForOutpaint` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `RepeatLatentBatch` —— 1/4 个有
- `VAELoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 5 - 20 | 4 | 60% |
| Prompt 约束强度(CFG) | 8 | 1.5 - 8 | 4 | 56% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | normal | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 5 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 1.5 - 8，4 个样本
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 normal，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
