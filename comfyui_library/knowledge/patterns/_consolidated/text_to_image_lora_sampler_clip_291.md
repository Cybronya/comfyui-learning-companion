---
name: text_to_image_lora_sampler_clip_291
type: Text To Image
frequency: 6
level: strong
coverage: 0.826
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveImage, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux 3_Image_Klein开源版多图参考生图｜局部重绘也拿捏_2111302012662018049.json, 图片生成/图生图/Flux3 Image Klein distill加速，t2i图生图双用_2111564003540557826.json, 图片生成/图生图/Flux3 Klein图生图，场景加人物与商品换背景双能力_2112277741444886529.json, 图片生成/图生图/Flux3_Klein_i2i图生图｜场景添加人物商品换背景｜一键智能编辑出图_2112044474250653697.json, 图片生成/文生图/Flux3 Klein文生图，人像写真海报制作全能出图_2112279255878033409.json, 图片生成/文生图/Flux3_Klein_t2i文生图｜人像写真海报制作全能｜文本直出高质量图片_2112046112122171393.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_291

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux 3_Image_Klein开源版多图参考生图｜局部重绘也拿捏_2111302012662018049.json、图片生成/图生图/Flux3 Image Klein distill加速，t2i图生图双用_2111564003540557826.json、图片生成/图生图/Flux3 Klein图生图，场景加人物与商品换背景双能力_2112277741444886529.json、图片生成/图生图/Flux3_Klein_i2i图生图｜场景添加人物商品换背景｜一键智能编辑出图_2112044474250653697.json、图片生成/文生图/Flux3 Klein文生图，人像写真海报制作全能出图_2112279255878033409.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 5/6 个有
- `PreviewAny` —— 5/6 个有
- `ResolutionSelector` —— 5/6 个有
- `TextGenerate` —— 5/6 个有
- `ComfyMathExpression` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `LoadImage` —— 4/6 个有
- `ModelSamplingFlux` —— 4/6 个有
- `PrimitiveFloat` —— 4/6 个有
- `ReferenceMultiLatent` —— 4/6 个有
- `Seed (rgthree)` —— 4/6 个有
- `BatchImagesNode` —— 3/6 个有
- `GetImageSize` —— 2/6 个有
- `ImageScaleToTotalPixels` —— 2/6 个有
- `RepeatLatentBatch` —— 2/6 个有
- `StringFormat` —— 2/6 个有
- `PreviewImage` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高发问题（8/6 个样本）：Steps较低可能导致细节不足
