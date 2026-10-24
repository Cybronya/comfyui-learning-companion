---
name: image_to_image_sampler_clip_unet_33
type: Image To Image
frequency: 10
level: strong
coverage: 0.8914
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, ImageStitch, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图像融合换姿势_1962450517467205633.json, 图片生成/图生图/手绘风格3视图_Kontext-DEV-LORA_1940464345698693121.json, 图片生成/图生图/拍立得照片_Kontext-dev TeaCache加速方案_1944531646655942658.json, 图片生成/图生图/新海诚动漫风格转绘_Kontext-DEV-LORA_1946936172776185857.json, 图片生成/图生图/最新Kontext图片人物姿势 迁移_1961060397623263234.json, 图片生成/图生图/生成她或他的一生面相_1993846683480031233.json, 图片生成/图生图/看尽她或他的一生面相_Kontext-DEV-LORA_1946474284820914177.json, 图片生成/图生图/看尽她或他的一生面相_Kontext-DEV-LORA，遇见未来~_2034811200768319490.json, 图片生成/文生图/KONTEXT【合集 】参考预处理图引导，图像一致编辑： LORA_1962546980700467202.json, 图片生成/文生图/Kontext_Canny  参考线稿引导，图像一致编辑：目前最稳定图像质量最好的控制lLORA_1962350864377823234.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_33

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/图像融合换姿势_1962450517467205633.json、图片生成/图生图/手绘风格3视图_Kontext-DEV-LORA_1940464345698693121.json、图片生成/图生图/拍立得照片_Kontext-dev TeaCache加速方案_1944531646655942658.json、图片生成/图生图/新海诚动漫风格转绘_Kontext-DEV-LORA_1946936172776185857.json、图片生成/图生图/最新Kontext图片人物姿势 迁移_1961060397623263234.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 9/10 个有
- `Text Multiline` —— 9/10 个有
- `ShowText|pysssss` —— 7/10 个有
- `FluxKontextImageScale` —— 6/10 个有
- `ImageConcatMulti` —— 6/10 个有
- `TeaCache` —— 6/10 个有
- `GetImageSizeAndCount` —— 5/10 个有
- `ImageScaleDownToSize` —— 5/10 个有
- `AIO_Preprocessor` —— 4/10 个有
- `Image Padding` —— 4/10 个有
- `ImageCrop` —— 4/10 个有
- `CR Simple Image Compare` —— 3/10 个有
- `JWIntegerToString` —— 3/10 个有
- `JWStringReplace` —— 3/10 个有
- `Primitive integer [Crystools]` —— 3/10 个有
- `PrimitiveString` —— 3/10 个有
- `CR Latent Batch Size` —— 1/10 个有
- `EmptySD3LatentImage` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
