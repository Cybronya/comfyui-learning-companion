---
name: image_to_image_upscale_lora_sampler_38
type: Image To Image
frequency: 5
level: weak
coverage: 0.8746
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, ImageUpscaleWithModel, KSampler, LoadImage, LoraLoaderModelOnly, PainterFluxImageEdit, PreviewImage, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Moss商业级真实感放大_2115257037499228162.json, 图片生成/图生图/Z-image+SeedVR2 +moss真实感放大商业级细节放大_2112449892311461890.json, "图片生成/图生图/去除塑料感,回归手机原相机 _无损放大细节炸裂_2043514967671971841.json", "图片生成/图生图/去除塑料感,还原相机原图_无损放大细节炸裂_2043518070223802369.json", "图片生成/图生图/告别塑料感,图秒变手机原相机_1962798780913463297.json"]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_38

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Moss商业级真实感放大_2115257037499228162.json、图片生成/图生图/Z-image+SeedVR2 +moss真实感放大商业级细节放大_2112449892311461890.json、图片生成/图生图/去除塑料感,回归手机原相机 _无损放大细节炸裂_2043514967671971841.json、图片生成/图生图/去除塑料感,还原相机原图_无损放大细节炸裂_2043518070223802369.json、图片生成/图生图/告别塑料感,图秒变手机原相机_1962798780913463297.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PainterFluxImageEdit`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `Image Lucy Sharpen` —— 3/5 个有
- `Int` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `UltimateSDUpscaleNoUpscale` —— 3/5 个有
- `DF_Integer` —— 2/5 个有
- `LG_Color_Match_V2` —— 2/5 个有
- `PrimitiveFloat` —— 2/5 个有
- `RHHiddenNodes` —— 2/5 个有
- `SkipLayerGuidanceDiTSimple` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 25 | 5 | 25% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 5 | 46% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | kl_optimal | - | 5 | 60% |
| 重绘幅度 | 0.5 | 0.3 - 0.5 | 5 | 77% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 25，5 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，5 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 kl_optimal，5 个样本，一致性 60%
- 重绘幅度 中位数 0.5，观测区间 0.3 - 0.5，5 个样本
- 高发问题（10/5 个样本）：Steps较低可能导致细节不足
