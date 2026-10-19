---
name: unknown_workflow_sampler_clip_unet_47
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.831
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [CR Aspect Ratio, easy clearCacheAll, CR Upscale Image]
members: [图片生成/文生图/1955432929541459969.json, 图片生成/文生图/1955444251107606530.json, 图片生成/文生图/1955564286744543234.json, 图片生成/文生图/1955869888814436354.json, 图片生成/文生图/1955919657263923201.json, 图片生成/文生图/1980117131083812865.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_47

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1955432929541459969.json、图片生成/文生图/1955444251107606530.json、图片生成/文生图/1955564286744543234.json、图片生成/文生图/1955869888814436354.json、图片生成/文生图/1955919657263923201.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/6 个有
- `PreviewImage` —— 3/6 个有
- `CR Aspect Ratio` —— 2/6 个有
- `ImagePadKJ` —— 2/6 个有
- `CR Upscale Image` —— 1/6 个有
- `PrimitiveFloat` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 4 - 30 | 6 | 38% |
| Prompt 约束强度(CFG) | 2.25 | 1 - 2.5 | 6 | 65% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 4 - 30，6 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 2.25，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Aspect Ratio、easy clearCacheAll、CR Upscale Image
