---
name: text_to_image_sampler_clip_unet_146
type: Text To Image
frequency: 5
level: moderate
coverage: 0.8308
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/MossImage文生分镜图生成工作流V1.0_2112470399945625601.json, 图片生成/文生图/Super Z-image 3.0文生图批量跑 浮云2.6_2019676814746066946.json, 图片生成/文生图/Super Z-image 文生图_2018521699486015489.json, 图片生成/文生图/Z-Image-Turbo 浮云2.3_2018528654661263361.json, 图片生成/文生图/贞贞lora多重z-image版本对比_2018006131871846401.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_146

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/MossImage文生分镜图生成工作流V1.0_2112470399945625601.json、图片生成/文生图/Super Z-image 3.0文生图批量跑 浮云2.6_2019676814746066946.json、图片生成/文生图/Super Z-image 文生图_2018521699486015489.json、图片生成/文生图/Z-Image-Turbo 浮云2.3_2018528654661263361.json、图片生成/文生图/贞贞lora多重z-image版本对比_2018006131871846401.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 4/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `ImageStitch` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `MOSSImagePromptEnhancerT8` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `ResolutionSelector` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1024 - 1080 | 5 | 98% |
| 高度 | 1920 | 1024 - 1920 | 5 | 79% |
| 采样步数 | 15 | 8 - 16 | 5 | 79% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 5 | 33% |
| 采样算法 | euler | - | 5 | 80% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1024 - 1080，5 个样本，取值集中（一致性 98%）
- 高度 中位数 1920，观测区间 1024 - 1920，5 个样本
- 采样步数 中位数 15，观测区间 8 - 16，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，5 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（7/5 个样本）：Steps较低可能导致细节不足
