---
name: text_to_image_upscale_sampler_clip_33
type: Text To Image
frequency: 3
level: strong
coverage: 0.808
common_nodes: [CLIPLoaderGGUF, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), GetImageSize+, Image Comparer (rgthree), ImageScaleBy, KSampler, LayerUtility: PurgeVRAM V2, ModelSamplingAuraFlow, PreviewImage, PrimitiveFloat, SaveImage, Seed (rgthree), SimpleMathDual+, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Anime-漫画专用_文生图_效果绝佳_2049096542295953409.json, 图片生成/文生图/Z-Anime-漫画专用_文生图_效果绝佳_高清放大_2049062082934480898.json, 图片生成/文生图/Z-Anime-漫画流整合+漫画高清放大_2048382191738036225.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_33

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-Anime-漫画专用_文生图_效果绝佳_2049096542295953409.json、图片生成/文生图/Z-Anime-漫画专用_文生图_效果绝佳_高清放大_2049062082934480898.json、图片生成/文生图/Z-Anime-漫画流整合+漫画高清放大_2048382191738036225.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoaderGGUF`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveFloat`
- `SaveImage`
- `Seed (rgthree)`
- `SimpleMathDual+`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 2/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `ProcessString` —— 1/3 个有
- `easy promptLine` —— 1/3 个有
- `easy promptList` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.4 | 0.4 - 1 | 3 | 53% |
| 宽度 | 832 | 832 - 832 | 3 | 100% |
| 高度 | 1216 | 1216 - 1216 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 1，3 个样本
- 宽度 中位数 832，观测区间 832 - 832，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1216，观测区间 1216 - 1216，3 个样本，取值集中（一致性 100%）
- 高发问题（8/3 个样本）：Steps较低可能导致细节不足
