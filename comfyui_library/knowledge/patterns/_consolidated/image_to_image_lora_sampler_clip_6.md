---
name: image_to_image_lora_sampler_clip_6
type: Image To Image
frequency: 15
level: strong
coverage: 0.896333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, RepeatLatentBatch, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Kontext Canva_一致性双图融合(电商神器)_Borges_1951582446481518594.json, 图片生成/图生图/Flux Kontext Canva_一致性双图融合(电商神器)_Borges_1970704107847774209.json, 图片生成/图生图/Flux kontext 老照片高清修复上色_1942218462028828674.json, 图片生成/图生图/Kontext Dev Fuse it｜多图溶图_1946409936961040386.json, 图片生成/图生图/Kontext-DEV【先去除后替换产品】换场景_1945660410626285569.json, 图片生成/图生图/Kontext-DEV【先去除后替换产品】换场景_1969909066803933185.json, 图片生成/图生图/Kontext-DEV模特换衣_1940636003080056834.json, 图片生成/图生图/Kontext-DEV模特换衣_1948210585455460353.json, 图片生成/图生图/Kontext-电商可用万物迁移（融图）_1946483138434621441.json, 图片生成/图生图/人物换头写真_无需PS深度溶图Kontext-LORA_1945817066031247361.json, 图片生成/图生图/人物换头换脸_深度溶图Kontext-LORA_1946849452919545857.json, 图片生成/图生图/家具布置迁移_Kontext溶图V4_1947327031031779330.json, 图片生成/图生图/手持商品迁移-加强版_Kontext溶图V4_1947477043904663554.json, 图片生成/图生图/手镯万物穿戴迁移_Kontext溶图V4_1947266108937113602.json, 图片生成/图生图/换头_1950809310471331842.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/图生图/Flux Kontext Canva_一致性双图融合(电商神器)_Borges_1951582446481518594.json、图片生成/图生图/Flux Kontext Canva_一致性双图融合(电商神器)_Borges_1970704107847774209.json、图片生成/图生图/Flux kontext 老照片高清修复上色_1942218462028828674.json、图片生成/图生图/Kontext Dev Fuse it｜多图溶图_1946409936961040386.json、图片生成/图生图/Kontext-DEV【先去除后替换产品】换场景_1945660410626285569.json…）

- **类型**：Image To Image
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `RepeatLatentBatch`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 14/15 个有
- `GoogleTranslateTextNode` —— 14/15 个有
- `PreviewImage` —— 14/15 个有
- `ShowText|pysssss` —— 14/15 个有
- `Text Multiline` —— 13/15 个有
- `ImageStitch` —— 12/15 个有
- `FastCanvas` —— 10/15 个有
- `FastCanvasTool` —— 10/15 个有
- `ImageScaleDownToSize` —— 10/15 个有
- `RMBG` —— 9/15 个有
- `Image Rembg (Remove Background)` —— 5/15 个有
- `EmptySD3LatentImage` —— 4/15 个有
- `GetImageSizeAndCount` —— 4/15 个有
- `SaveLatent` —— 4/15 个有
- `LayerMask: PersonMaskUltra V2` —— 3/15 个有
- `LayerUtility: CropByMask V2` —— 3/15 个有
- `Note Plus (mtb)` —— 3/15 个有
- `CR Text` —— 1/15 个有
- `ConditioningCombine` —— 1/15 个有
- `Image Comparer (rgthree)` —— 1/15 个有
- `Images to RGB` —— 1/15 个有
- `LoadImageFromUrl` —— 1/15 个有
- `RH_Translator` —— 1/15 个有
- `TeaCache` —— 1/15 个有
- `Text _O` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 15 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 15 | 100% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，15 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
