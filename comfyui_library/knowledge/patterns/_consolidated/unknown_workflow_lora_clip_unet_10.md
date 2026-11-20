---
name: unknown_workflow_lora_clip_unet_10
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8676
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, ConditioningZeroOut, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/ernie+klein双采_2045055189861801985.json, 图片生成/文生图/ernie+zit双采样_2045054582375587842.json, 图片生成/文生图/zimage base 加速高质量lora最高20倍提速_2021771055412547585.json, 图片生成/文生图/zimage base_电影级风格LORA测试_2059298671640010754.json, 图片生成/文生图/百度ernie+zit双采样_2045695437658656770.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_10

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/ernie+klein双采_2045055189861801985.json、图片生成/文生图/ernie+zit双采样_2045054582375587842.json、图片生成/文生图/zimage base 加速高质量lora最高20倍提速_2021771055412547585.json、图片生成/文生图/zimage base_电影级风格LORA测试_2059298671640010754.json、图片生成/文生图/百度ernie+zit双采样_2045695437658656770.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 4/5 个有
- `EmptyFlux2LatentImage` —— 3/5 个有
- `KSamplerAdvanced` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `KSampler` —— 2/5 个有
- `SDXLEmptyLatentSizePicker+` —— 2/5 个有
- `VAEEncode` —— 2/5 个有
- `AddLabel` —— 1/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `GetNode` —— 1/5 个有
- `INTConstant` —— 1/5 个有
- `SetNode` —— 1/5 个有
- `easy imageConcat` —— 1/5 个有
- `easy promptLine` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 60% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 5 | 34% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 5 | 60% |
| 重绘幅度 | simple | - | 5 | 40% |
| 宽度 | 768x1344 (0.57) | - | 2 | 50% |
| 高度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，5 个样本，取值分散，一致性仅 34%
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 60%
- 重绘幅度 最常用 simple，5 个样本，一致性 40%
- 宽度 最常用 768x1344 (0.57)，2 个样本，一致性 50%
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/5 个样本）：Steps较低可能导致细节不足
