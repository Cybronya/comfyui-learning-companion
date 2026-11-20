---
name: image_to_image_sampler_clip_unet_88
type: Image To Image
frequency: 7
level: strong
coverage: 0.867286
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/模型图生成效果图+_1969336789913772033.json, 图片生成/图生图/溶图 色彩变动小_Kontext_2064292965186621441.json, 图片生成/图生图/美漫手绘故事_Kontext-LORA_1955150925189058561.json, 图片生成/图生图/马克笔风格风格转绘_1943325807521505281.json, 平台全量/Kontext-一键精修婚纱摄影_1950220264686706689.json, 平台全量/kontext可爱扁平动漫风格转绘_1942014172815376386.json, 平台全量/【婚纱摄影精修】-kontext_1967223131414913026.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_88

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/模型图生成效果图+_1969336789913772033.json、图片生成/图生图/溶图 色彩变动小_Kontext_2064292965186621441.json、图片生成/图生图/美漫手绘故事_Kontext-LORA_1955150925189058561.json、图片生成/图生图/马克笔风格风格转绘_1943325807521505281.json、平台全量/Kontext-一键精修婚纱摄影_1950220264686706689.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `ShowText|pysssss` —— 5/7 个有
- `Text Multiline` —— 5/7 个有
- `UpscaleModelLoader` —— 5/7 个有
- `EmptySD3LatentImage` —— 4/7 个有
- `ImageConcatMulti` —— 4/7 个有
- `ImageUpscaleWithModel` —— 4/7 个有
- `GetImageSizeAndCount` —— 3/7 个有
- `Image Comparer (rgthree)` —— 2/7 个有
- `LoraLoader` —— 2/7 个有
- `CR Latent Batch Size` —— 1/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `Image Resize Factor (mtb)` —— 1/7 个有
- `ImageScaleBy` —— 1/7 个有
- `ImageUpscaleWithModelBatched` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 7 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 0.75 | - | 2 | 67% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，7 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.75，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
