---
name: image_to_image_lora_sampler_unet_236
type: Image To Image
frequency: 3
level: strong
coverage: 0.941
common_nodes: [CLIPLoader, ConditioningZeroOut, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/Qwen2511-图像编辑极简工作流_2083740236118581249.json, 平台全量/去除全能图片G image 2噪点工作流_2058735501527568385.json, 平台全量/造光 _ Qwen-Image-Edit-2511_1943285184441556993.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_236

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Qwen2511-图像编辑极简工作流_2083740236118581249.json、平台全量/去除全能图片G image 2噪点工作流_2058735501527568385.json、平台全量/造光 _ Qwen-Image-Edit-2511_1943285184441556993.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/3 个有
- `ModelSamplingAuraFlow` —— 2/3 个有
- `ConstrainImage|pysssss` —— 1/3 个有
- `EmptySD3LatentImage` —— 1/3 个有
- `MuyeTextEditOutput` —— 1/3 个有
- `ResizeImageMaskNode` —— 1/3 个有
- `Switch any [Crystools]` —— 1/3 个有
- `TTResolutionSelector` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler_ancestral | - | 3 | 67% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 67%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
