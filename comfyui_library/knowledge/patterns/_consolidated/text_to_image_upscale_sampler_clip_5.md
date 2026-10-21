---
name: text_to_image_upscale_sampler_clip_5
type: Text To Image
frequency: 14
level: strong
coverage: 0.82
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Image Comparer (rgthree), ImageScaleBy, KSampler, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Red-Z-Image-Distilled-Base-加速版 文生图V1_2018292840656281602.json, 图片生成/文生图/Z Image BF16&FP8对比 + 4K超清放大_2005803927591415810.json, 图片生成/文生图/Z Image BF16&FP8对比 + 4K超清放大【AI小王子】_1995339494473785345.json, 图片生成/文生图/Z Image出图 + 4K超清放大_2005868847062286337.json, 图片生成/文生图/Z-IMAGE：4K超清放大工作流+BF16-FP8效果对比_1996194432674414594.json, 图片生成/文生图/Z-IMAGE：小而美图像模型：文生图_1993913992611643394.json, 图片生成/文生图/Z-IMAGE：文生图【无ai感】_1994210417830461442.json, 图片生成/文生图/Z-IMAGE：新王登基  文生图_1995696465139863553.json, 图片生成/文生图/Z-IMAGE：新王登基  文生图_2009258918182129665.json, 图片生成/文生图/Z-image-Art 文生图+高清放大_2017835536668434434.json, 图片生成/文生图/Z-image-Super 3.0 文生图_2018286243913670658.json, 图片生成/文生图/Z-image绝世美女人物一致性lora和工作流，高清美女图适合抖音、快手等自媒体平台_1995357519012880385.json, 图片生成/文生图/图像修复放大 - Zimage_2009636078482886658.json, 图片生成/文生图/图像修复放大+Zimage双模_2020336239643205634.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_5

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Red-Z-Image-Distilled-Base-加速版 文生图V1_2018292840656281602.json、图片生成/文生图/Z Image BF16&FP8对比 + 4K超清放大_2005803927591415810.json、图片生成/文生图/Z Image BF16&FP8对比 + 4K超清放大【AI小王子】_1995339494473785345.json、图片生成/文生图/Z Image出图 + 4K超清放大_2005868847062286337.json、图片生成/文生图/Z-IMAGE：4K超清放大工作流+BF16-FP8效果对比_1996194432674414594.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `KSampler`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 11/14 个有
- `Fast Groups Bypasser (rgthree)` —— 11/14 个有
- `ImpactInt` —— 5/14 个有
- `easy promptList` —— 5/14 个有
- `Text` —— 4/14 个有
- `PrimitiveInt` —— 3/14 个有
- `CR Prompt Text` —— 2/14 个有
- `LayerUtility: PurgeVRAM` —— 2/14 个有
- `Int` —— 1/14 个有
- `JoinStringMulti` —— 1/14 个有
- `KepStringLiteral` —— 1/14 个有
- `LoraLoaderModelOnly` —— 1/14 个有
- `PrimitiveStringMultiline` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1080 | 1080 - 1920 | 14 | 71% |
| 高度 | 1920 | 1080 - 1920 | 14 | 75% |
| 采样步数 | 9.5 | 8 - 15 | 14 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 93% |
| 调度器 | simple | - | 14 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 1080 - 1920，14 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，14 个样本
- 采样步数 中位数 9.5，观测区间 8 - 15，14 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 93%
- 调度器 最常用 simple，14 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（12/14 个样本）：Steps较低可能导致细节不足
