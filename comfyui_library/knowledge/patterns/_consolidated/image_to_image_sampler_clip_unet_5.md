---
name: image_to_image_sampler_clip_unet_5
type: Image To Image
frequency: 29
level: strong
coverage: 0.906483
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/人像精修_2076044034824564738.json, 图片生成/图生图/人像精修工作流_2048591215414747137.json, 图片生成/图生图/全能视频S真人前置-素描Kontext_1974104968892387330.json, 图片生成/图生图/动漫线稿上色｜多彩活力插画_1942398408399204354.json, 图片生成/图生图/单纯图像编辑_1993235777899479041.json, 图片生成/图生图/印花提取-商业级 Flux.1 Kontext_2103519336425156610.json, 图片生成/图生图/印花提取-商业级 Flux.1 Kontext_2104433739911745537.json, 图片生成/图生图/印花提取-商业级_Flux.1_Kontext_2108385501811142658.json, 图片生成/图生图/印花提取-商业级_Flux.1_Kontext_2109826006751203329.json, 图片生成/图生图/取衣去人_Kontext-DEV-LORA_1940461645275754497.json, 图片生成/图生图/图像局部修改_服装_家具_人物Kontext-DEV开源官方版_1938894823174950914.json, 图片生成/图生图/图像局部修改_服装编辑_Kontext-DEV开源ComfyUI官方版_1938389852155215873.json, 图片生成/图生图/家具布置迁移_Kontext溶图V4_1947327031031779330.json, 图片生成/图生图/手持商品迁移-加强版_Kontext溶图V4_1947477043904663554.json, 图片生成/图生图/手镯万物穿戴迁移_Kontext溶图V4_1947266108937113602.json, 图片生成/图生图/换头_1950809310471331842.json, 图片生成/图生图/换头kontext1_1957067763853266946.json, 图片生成/图生图/服装迁移迁移_Kontext溶图V4_1947332767635886082.json, 图片生成/图生图/电商商品演示_Kontext-DEV稳定多图编辑_1939373760153624578.json, 图片生成/图生图/电商手持商品-无需PS无痕溶图_1970991890646634498.json, 图片生成/图生图/电商手持商品-无需PS无痕溶图_Kontext-LORA_1945709848204025858.json, 图片生成/图生图/电商手持商品-溶图_Kontext-LORA_1946852736198406146.json, 平台全量/3图融合家具展示_Kontext-DEV稳定多图编辑_1940204811709009921.json, 平台全量/Kontext手镯戒指万物迁移_1947876325638975490.json, 平台全量/Kontext手镯戒指万物迁移_1948685524516110337.json, 平台全量/Kontext稳定融图工作流_1946395516546768898.json, 平台全量/Kontext耳环耳钉耳坠迁移_1947873743159865346.json, 平台全量/Kontext耳环耳钉耳坠迁移_1948685482994610177.json, 平台全量/Y-Overlay-人物换头Kontext-Lora_1946161470738755585.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_5

> 由 `engine/knowledge_consolidation` 从 29 个 workflow 归纳得出（图片生成/图生图/人像精修_2076044034824564738.json、图片生成/图生图/人像精修工作流_2048591215414747137.json、图片生成/图生图/全能视频S真人前置-素描Kontext_1974104968892387330.json、图片生成/图生图/动漫线稿上色｜多彩活力插画_1942398408399204354.json、图片生成/图生图/单纯图像编辑_1993235777899479041.json…）

- **类型**：Image To Image
- **样本数**：29
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 29 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
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
- `FluxKontextImageScale` —— 28/29 个有
- `LoraLoaderModelOnly` —— 26/29 个有
- `ImageStitch` —— 22/29 个有
- `PreviewImage` —— 22/29 个有
- `RepeatLatentBatch` —— 19/29 个有
- `Text Multiline` —— 19/29 个有
- `ShowText|pysssss` —— 18/29 个有
- `FastCanvas` —— 17/29 个有
- `FastCanvasTool` —— 17/29 个有
- `GoogleTranslateTextNode` —— 17/29 个有
- `ImageScaleDownToSize` —— 15/29 个有
- `Image Rembg (Remove Background)` —— 9/29 个有
- `RMBG` —— 7/29 个有
- `Image Comparer (rgthree)` —— 4/29 个有
- `LayerUtility: CropByMask V2` —— 4/29 个有
- `ImageConcatMulti` —— 3/29 个有
- `Fast Groups Bypasser (rgthree)` —— 2/29 个有
- `ImageResize+` —— 2/29 个有
- `LayerMask: PersonMaskUltra V2` —— 2/29 个有
- `easy cleanGpuUsed` —— 2/29 个有
- `BiRefNetRMBG` —— 1/29 个有
- `Images to RGB` —— 1/29 个有
- `LayerMask: PersonMaskUltra` —— 1/29 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/29 个有
- `LoaderGGUF` —— 1/29 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 29 | 94% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 29 | 100% |
| 采样算法 | euler | - | 29 | 100% |
| 调度器 | simple | - | 29 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 29 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，29 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，29 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，29 个样本，一致性 100%
- 调度器 最常用 simple，29 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，29 个样本，取值集中（一致性 100%）
