---
name: unknown_workflow_lora_sampler_clip_39
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.911833
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [String Literal, easy seed]
members: [图片生成/文生图/1955503632722661377.json, 图片生成/文生图/1955586331033288705.json, 图片生成/文生图/1970690059521454082.json, 图片生成/文生图/1985959773130633217.json, 图片生成/文生图/1987149238826151938.json, 图片生成/文生图/1987158769756999681.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_39

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1955503632722661377.json、图片生成/文生图/1955586331033288705.json、图片生成/文生图/1970690059521454082.json、图片生成/文生图/1985959773130633217.json、图片生成/文生图/1987149238826151938.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 4/6 个有
- `easy seed` —— 3/6 个有
- `String Literal` —— 2/6 个有
- `UnetLoaderGGUF` —— 2/6 个有
- `AddLabel` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 8 | 6 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 8，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（25/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：String Literal、easy seed
