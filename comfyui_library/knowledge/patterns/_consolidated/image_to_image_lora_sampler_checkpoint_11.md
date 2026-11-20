---
name: image_to_image_lora_sampler_checkpoint_11
type: Image To Image
frequency: 3
level: strong
coverage: 0.979333
common_nodes: [CheckpointLoaderSimple, Image Compare (mtb), KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Edit AIO 单图编辑_1980186635260301313.json, 图片生成/图生图/Qwen Edit AIO 双图编辑_1980186596010004482.json, 平台全量/【升级】全自动移除水印或文字_1997846078957531138.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_checkpoint_11

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Qwen Edit AIO 单图编辑_1980186635260301313.json、图片生成/图生图/Qwen Edit AIO 双图编辑_1980186596010004482.json、平台全量/【升级】全自动移除水印或文字_1997846078957531138.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 3 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `Image Compare (mtb)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `DWPreprocessor` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 4 - 12 | 3 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 67% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 12，观测区间 4 - 12，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
