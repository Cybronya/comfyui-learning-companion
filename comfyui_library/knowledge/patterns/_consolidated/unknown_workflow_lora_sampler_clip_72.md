---
name: unknown_workflow_lora_sampler_clip_72
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.784667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSampler, LoraLoader, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, easy int]
members: [图片生成/文生图/1950169292044197890.json, 图片生成/文生图/1954733353410949121.json, 图片生成/文生图/1968282023137824769.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_72

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1950169292044197890.json、图片生成/文生图/1954733353410949121.json、图片生成/文生图/1968282023137824769.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSampler`
- `LoraLoader`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGZeroStarAndInit` —— 2/3 个有
- `easy int` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `ModelSamplingSD3` —— 1/3 个有
- `PathchSageAttentionKJ` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `PrimitiveInt` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 0.8 - 1 | 3 | 90% |
| LoRA 文本强度 | 1 | 0.8 - 1 | 3 | 90% |
| 采样步数 | 8 | 5 - 8 | 3 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 3 | 36% |
| 采样算法 | res_2s | - | 3 | 67% |
| 调度器 | bong_tangent | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 0.8 - 1，3 个样本，取值集中（一致性 90%）
- LoRA 文本强度 中位数 1，观测区间 0.8 - 1，3 个样本，取值集中（一致性 90%）
- 采样步数 中位数 8，观测区间 5 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，3 个样本，取值分散，一致性仅 36%
- 采样算法 最常用 res_2s，3 个样本，一致性 67%
- 调度器 最常用 bong_tangent，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、easy int
