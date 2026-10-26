---
name: text_to_image_sampler_clip_unet_22
type: Text To Image
frequency: 18
level: moderate
coverage: 0.820278
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Red-Z image Distilled Base加速版文生图V1_2018000841084506113.json, 图片生成/文生图/Red-Z-Image-Distilled-Base-加速版 文生图V1_2018292840656281602.json, 图片生成/文生图/Super Z-image 3.0文生图_2018000830837825538.json, 图片生成/文生图/Super Z-image 3.0文生图批量跑 浮云2.6_2019676814746066946.json, 图片生成/文生图/Super Z-image 文生图_2018521699486015489.json, 图片生成/文生图/Z Image BF16&FP8对比 + 4K超清放大_2005803927591415810.json, 图片生成/文生图/Z Image BF16&FP8对比 + 4K超清放大【AI小王子】_1995339494473785345.json, 图片生成/文生图/Z Image出图 + 4K超清放大_2005868847062286337.json, 图片生成/文生图/Z image文生图_2048404891235786754.json, 图片生成/文生图/Z-IMAGE：4K超清放大工作流+BF16-FP8效果对比_1996194432674414594.json, 图片生成/文生图/Z-IMAGE：小而美图像模型：文生图_1993913992611643394.json, 图片生成/文生图/Z-IMAGE：小而美图像模型：文生图_2035264157662060546.json, 图片生成/文生图/Z-IMAGE：文生图【无ai感】_1994210417830461442.json, 图片生成/文生图/Z-IMAGE：新王登基  文生图_1995696465139863553.json, 图片生成/文生图/Z-IMAGE：新王登基  文生图_2009258918182129665.json, 图片生成/文生图/Z-image-Super 3.0 文生图_2018286243913670658.json, 图片生成/文生图/图像修复放大 - Zimage_2009636078482886658.json, 图片生成/文生图/图像修复放大+Zimage双模_2020336239643205634.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_22

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/Red-Z image Distilled Base加速版文生图V1_2018000841084506113.json、图片生成/文生图/Red-Z-Image-Distilled-Base-加速版 文生图V1_2018292840656281602.json、图片生成/文生图/Super Z-image 3.0文生图_2018000830837825538.json、图片生成/文生图/Super Z-image 3.0文生图批量跑 浮云2.6_2019676814746066946.json、图片生成/文生图/Super Z-image 文生图_2018521699486015489.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 14/18 个有
- `ImageScaleBy` —— 14/18 个有
- `SeedVR2LoadDiTModel` —— 14/18 个有
- `SeedVR2LoadVAEModel` —— 14/18 个有
- `SeedVR2VideoUpscaler` —— 14/18 个有
- `ConditioningZeroOut` —— 12/18 个有
- `Fast Groups Bypasser (rgthree)` —— 12/18 个有
- `CR Prompt Text` —— 6/18 个有
- `PrimitiveInt` —— 6/18 个有
- `ImpactInt` —— 5/18 个有
- `LayerUtility: PurgeVRAM` —— 5/18 个有
- `easy promptList` —— 5/18 个有
- `Text` —— 4/18 个有
- `Int` —— 1/18 个有
- `LoraLoader` —— 1/18 个有
- `LoraLoaderModelOnly` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 9 - 15 | 18 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |
| 宽度 | 1080 | 720 - 1920 | 18 | 69% |
| 高度 | 1920 | 1080 - 1920 | 18 | 77% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 9 - 15，18 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 720 - 1920，18 个样本
- 高度 中位数 1920，观测区间 1080 - 1920，18 个样本
- 高发问题（12/18 个样本）：Steps较低可能导致细节不足
