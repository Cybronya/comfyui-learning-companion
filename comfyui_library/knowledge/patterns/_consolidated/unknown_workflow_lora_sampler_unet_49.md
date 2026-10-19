---
name: unknown_workflow_lora_sampler_unet_49
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.936
common_nodes: [CLIPLoader, GetImageSize, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEdit, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1958563656520855554.json, 图片生成/文生图/1960161305468547074.json, 图片生成/文生图/1976907729967190018.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_49

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1958563656520855554.json、图片生成/文生图/1960161305468547074.json、图片生成/文生图/1976907729967190018.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `GetImageSize`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `EmptySD3LatentImage` —— 2/3 个有
- `CLIPTextEncode` —— 1/3 个有
- `EmptyLatentImage` —— 1/3 个有
- `FluxKontextImageScale` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageScaleToMegapixels` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `PrimitiveString` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 512 | - | 1 | 100% |
| 高度 | 512 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
