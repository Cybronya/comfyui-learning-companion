---
name: image_to_image_sampler_clip_unet_73
type: Image To Image
frequency: 8
level: strong
coverage: 0.92175
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/开源版Kontext [dev]，一句话精准改图，省算力！_1938559267488063489.json, 图片生成/图生图/手办盲盒超火模型——图片转3D手办模型_2046143930944720898.json, 图片生成/图生图/换背景kontext_1989633808280506369.json, 图片生成/图生图/电商产品溶图_2026942543119785985.json, 图片生成/图生图/白膜上色器_1947606569657819137.json, 图片生成/图生图/老照片修复+上色kontext dev_1946791542956941313.json, 图片生成/图生图/老照片修复及上色-kontext dev开源_1939192628053229569.json, 图片生成/文生图/KONTEXT 溶图 —  最高效稳定 & 最简单的万物迁移工作流_1962762684775182338.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_73

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/开源版Kontext [dev]，一句话精准改图，省算力！_1938559267488063489.json、图片生成/图生图/手办盲盒超火模型——图片转3D手办模型_2046143930944720898.json、图片生成/图生图/换背景kontext_1989633808280506369.json、图片生成/图生图/电商产品溶图_2026942543119785985.json、图片生成/图生图/白膜上色器_1947606569657819137.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 6/8 个有
- `RH_Translator` —— 6/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `ConditioningZeroOut` —— 4/8 个有
- `RHHiddenNodes` —— 4/8 个有
- `PreviewImage` —— 3/8 个有
- `easy imageConcat` —— 3/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `Preview from image [Crystools]` —— 2/8 个有
- `ConditioningConcat` —— 1/8 个有
- `ImageResizeKJv2` —— 1/8 个有
- `ImageScaleDownToSize` —— 1/8 个有
- `JjkText` —— 1/8 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/8 个有
- `LayerUtility: ImageBlendAdvance V2` —— 1/8 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/8 个有
- `RepeatLatentBatch` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 30 | 8 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 30，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
