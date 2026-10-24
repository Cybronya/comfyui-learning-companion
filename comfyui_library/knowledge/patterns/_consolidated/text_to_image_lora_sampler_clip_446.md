---
name: text_to_image_lora_sampler_clip_446
type: Text To Image
frequency: 4
level: moderate
coverage: 0.99625
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Wan2.2 文生图 48出_1954055995188236290.json, 图片生成/文生图/Wan2.2 超真实文生图+放大_1950719208512491521.json, 图片生成/文生图/Wan2.2真实系INS风组合调度非常规文生图工作流（海外版）_1955547695828144130.json, 图片生成/文生图/Wan2.2超绝真实系组合调度非常规文生图工作流_1950528087563948034.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_446

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Wan2.2 文生图 48出_1954055995188236290.json、图片生成/文生图/Wan2.2 超真实文生图+放大_1950719208512491521.json、图片生成/文生图/Wan2.2真实系INS风组合调度非常规文生图工作流（海外版）_1955547695828144130.json、图片生成/文生图/Wan2.2超绝真实系组合调度非常规文生图工作流_1950528087563948034.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_TextToStringAndSeed` —— 3/4 个有
- `JWInteger` —— 2/4 个有
- `PMRF` —— 2/4 个有
- `Anything Everywhere` —— 1/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `SeedVR2` —— 1/4 个有
- `SeedVR2BlockSwap` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 616 | 512 - 1024 | 4 | 70% |
| 高度 | 896 | 512 - 1536 | 4 | 52% |
| 采样步数 | 10 | 8 - 10 | 4 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 75% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 48/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 616，观测区间 512 - 1024，4 个样本
- 高度 中位数 896，观测区间 512 - 1536，4 个样本
- 采样步数 中位数 10，观测区间 8 - 10，4 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 75%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（48/4 个样本）：Steps较低可能导致细节不足
