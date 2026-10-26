---
name: text_to_image_upscale_sampler_clip_35
type: Text To Image
frequency: 3
level: strong
coverage: 0.910667
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-image-Turbo+丰胸Lora+提示词优化+高清放大_2008872315525795841.json, 图片生成/文生图/Z-image-Turbo-优化美女身材Lora_2007421350499061761.json, 图片生成/文生图/自-z image turbo文生图_2080539022929260546.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_35

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-image-Turbo+丰胸Lora+提示词优化+高清放大_2008872315525795841.json、图片生成/文生图/Z-image-Turbo-优化美女身材Lora_2007421350499061761.json、图片生成/文生图/自-z image turbo文生图_2080539022929260546.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `AddLabel` —— 1/3 个有
- `Int` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `easy showAnything` —— 1/3 个有
- `easy stylesSelector` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1024 - 1080 | 3 | 98% |
| 高度 | 1920 | 1536 - 1920 | 3 | 90% |
| 采样步数 | 9 | 9 - 9 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1024 - 1080，3 个样本，取值集中（一致性 98%）
- 高度 中位数 1920，观测区间 1536 - 1920，3 个样本，取值集中（一致性 90%）
- 采样步数 中位数 9，观测区间 9 - 9，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
