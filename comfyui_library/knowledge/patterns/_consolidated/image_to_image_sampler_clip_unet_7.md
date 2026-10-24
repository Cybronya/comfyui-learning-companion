---
name: image_to_image_sampler_clip_unet_7
type: Image To Image
frequency: 22
level: strong
coverage: 0.896545
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, ShowText|pysssss, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一年前的老照片修复技术_1942854549231349761.json, 图片生成/图生图/一张图片生成 3D Chibi可爱风格_2027185278074494977.json, 图片生成/图生图/一键三视图_Kontext-DEV图像编辑_1939142169158410241.json, 图片生成/图生图/一键人像精修_Kontext-dev_1944091800334139394.json, 图片生成/图生图/万物国画风格转绘_Kontext-dev_1943327017553043458.json, 图片生成/图生图/万物大理石雕塑_Kontext-DEV-LORA_1946494072476299266.json, 图片生成/图生图/万物折纸风格_Kontext-DEV-LORA_1946488692631302145.json, 图片生成/图生图/万物擦除_Kontext-DEV图像编辑_1938902253212520450.json, 图片生成/图生图/万物擦除之Kontext-DEV精准区域编辑_1940637803657015297.json, 图片生成/图生图/万物玩偶_Kontext-DEV-LORA_1946577691345580034.json, 图片生成/图生图/人物换背景_Kontext-DEV图像编辑_1938939080438636546.json, 图片生成/图生图/图像局部修改_服装_家具_人物Kontext-DEV开源官方版_1938894823174950914.json, 图片生成/图生图/图像局部修改_服装编辑_Kontext-DEV开源ComfyUI官方版_1938389852155215873.json, 图片生成/图生图/夜景到白天变化_Kontext-DEV-LORA_1947252443596886018.json, 图片生成/图生图/家具布置迁移_Kontext溶图V4_1947327031031779330.json, 图片生成/图生图/手持商品迁移-加强版_Kontext溶图V4_1947477043904663554.json, 图片生成/图生图/手镯万物穿戴迁移_Kontext溶图V4_1947266108937113602.json, 图片生成/图生图/服装迁移迁移_Kontext溶图V4_1947332767635886082.json, 图片生成/图生图/电商商品演示_Kontext-DEV稳定多图编辑_1939373760153624578.json, 图片生成/图生图/电商手持商品-无需PS无痕溶图_1970991890646634498.json, 图片生成/图生图/电商手持商品-无需PS无痕溶图_Kontext-LORA_1945709848204025858.json, 图片生成/图生图/电商手持商品-溶图_Kontext-LORA_1946852736198406146.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_7

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/图生图/一年前的老照片修复技术_1942854549231349761.json、图片生成/图生图/一张图片生成 3D Chibi可爱风格_2027185278074494977.json、图片生成/图生图/一键三视图_Kontext-DEV图像编辑_1939142169158410241.json、图片生成/图生图/一键人像精修_Kontext-dev_1944091800334139394.json、图片生成/图生图/万物国画风格转绘_Kontext-dev_1943327017553043458.json…）

- **类型**：Image To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `ShowText|pysssss`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 21/22 个有
- `ImageStitch` —— 21/22 个有
- `PreviewImage` —— 21/22 个有
- `LoraLoaderModelOnly` —— 20/22 个有
- `GoogleTranslateTextNode` —— 14/22 个有
- `ImageConcatMulti` —— 14/22 个有
- `RepeatLatentBatch` —— 9/22 个有
- `FastCanvas` —— 8/22 个有
- `FastCanvasTool` —— 8/22 个有
- `ImageScaleDownToSize` —— 8/22 个有
- `Image Padding` —— 4/22 个有
- `Image Rembg (Remove Background)` —— 4/22 个有
- `RMBG` —— 4/22 个有
- `TeaCache` —— 4/22 个有
- `EmptySD3LatentImage` —— 3/22 个有
- `GetImageSizeAndCount` —— 3/22 个有
- `LoaderGGUF` —— 2/22 个有
- `ImageAndMaskPreview` —— 1/22 个有
- `ImagePadKJ` —— 1/22 个有
- `Images to RGB` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 22 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 22 | 100% |
| 采样算法 | euler | - | 22 | 100% |
| 调度器 | simple | - | 22 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，22 个样本，一致性 100%
- 调度器 最常用 simple，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
