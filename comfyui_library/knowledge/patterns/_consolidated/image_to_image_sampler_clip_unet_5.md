---
name: image_to_image_sampler_clip_unet_5
type: Image To Image
frequency: 24
level: strong
coverage: 0.887583
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, ImageStitch, KSampler, LoadImage, PreviewImage, ReferenceLatent, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext最新姿势参考改图_1960974269314469890.json, 图片生成/图生图/Kontext最新姿势参考改图_1961618107724926977.json, 图片生成/图生图/Kontext最新姿势迁移_1961618061616988161.json, 图片生成/图生图/Kontext深度Depth引导图像编辑_1957761851306209281.json, 图片生成/图生图/Kontext线稿lineart 引导图像编辑_1961994378770366466.json, 图片生成/图生图/Line线稿提取_Kontext-DEV-LORA_1948603383413374977.json, 图片生成/图生图/MinimalSketchStyle线稿提取_Kontext-DEV-LORA_1948602505090478081.json, 图片生成/图生图/PS1游戏风格_Kontext-DEV-LORA_1945035820526133249.json, 图片生成/图生图/Sketch手绘风格_Kontext-DEV-LORA_1948604464042246145.json, 图片生成/图生图/万物大理石雕塑_Kontext-DEV-LORA_1946494072476299266.json, 图片生成/图生图/万物折纸风格_Kontext-DEV-LORA_1946488692631302145.json, 图片生成/图生图/万物玩偶_Kontext-DEV-LORA_1946577691345580034.json, 图片生成/图生图/图像融合换姿势_1962450517467205633.json, 图片生成/图生图/夜景到白天变化_Kontext-DEV-LORA_1947252443596886018.json, 图片生成/图生图/拍立得手持风格_Kontext-DEV-LORA_1947997286562430978.json, 图片生成/图生图/新海诚动漫风格转绘_Kontext-DEV-LORA_1946936172776185857.json, 图片生成/图生图/最新Kontext图片人物姿势 迁移_1961060397623263234.json, 图片生成/图生图/生成她或他的一生面相_1993846683480031233.json, 图片生成/图生图/看尽她或他的一生面相_Kontext-DEV-LORA_1946474284820914177.json, 图片生成/图生图/看尽她或他的一生面相_Kontext-DEV-LORA，遇见未来~_2034811200768319490.json, 图片生成/图生图/青铜雕塑_Kontext-DEV-LORA_1946225600609546241.json, 图片生成/图生图/高清扩图_Kontext-DEV-LORA_1944993249007427586.json, 图片生成/图生图/高清扩图_Kontext-DEV-LORA_1945760609537290241.json, 图片生成/文生图/KONTEXT【合集 】参考预处理图引导，图像一致编辑： LORA_1962546980700467202.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_5

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（图片生成/图生图/Kontext最新姿势参考改图_1960974269314469890.json、图片生成/图生图/Kontext最新姿势参考改图_1961618107724926977.json、图片生成/图生图/Kontext最新姿势迁移_1961618061616988161.json、图片生成/图生图/Kontext深度Depth引导图像编辑_1957761851306209281.json、图片生成/图生图/Kontext线稿lineart 引导图像编辑_1961994378770366466.json…）

- **类型**：Image To Image
- **样本数**：24
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 24 个 workflow 都包含：
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
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ShowText|pysssss` —— 22/24 个有
- `TeaCache` —— 22/24 个有
- `LoraLoaderModelOnly` —— 20/24 个有
- `FluxKontextImageScale` —— 16/24 个有
- `Image Padding` —— 16/24 个有
- `ImageConcatMulti` —— 11/24 个有
- `AIO_Preprocessor` —— 8/24 个有
- `GetImageSizeAndCount` —— 8/24 个有
- `ImageCrop` —— 8/24 个有
- `ImageScaleDownToSize` —— 8/24 个有
- `CR Simple Image Compare` —— 7/24 个有
- `ImagePadKJ` —— 4/24 个有
- `RHHiddenNodes` —— 4/24 个有
- `JWIntegerToString` —— 3/24 个有
- `JWStringReplace` —— 3/24 个有
- `Primitive integer [Crystools]` —— 3/24 个有
- `PrimitiveString` —— 3/24 个有
- `CR Latent Batch Size` —— 1/24 个有
- `easy imageRemBg` —— 1/24 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 24 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 24 | 100% |
| 采样算法 | euler | - | 24 | 100% |
| 调度器 | simple | - | 24 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 24 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，24 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，24 个样本，一致性 100%
- 调度器 最常用 simple，24 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，24 个样本，取值集中（一致性 100%）
