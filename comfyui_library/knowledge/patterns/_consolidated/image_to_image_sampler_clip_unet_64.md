---
name: image_to_image_sampler_clip_unet_64
type: Image To Image
frequency: 8
level: strong
coverage: 0.91275
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FastCanvas, FastCanvasTool, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux-kontext-产品+背景-自动合成溶图_1950960132547084289.json, 图片生成/图生图/KONTEXT 溶图 V3_1985552455687720962.json, 图片生成/图生图/KONTEXT+溶图+V3+，+最高效稳定万物迁移工作流_2013144975940263938.json, 图片生成/图生图/Kontext Dev多图融合技巧（更可控）_1939332448016637954.json, 图片生成/图生图/kontext超强溶图_1987866800891301889.json, 图片生成/图生图/🦚【大炮精选】Kontext 溶图工作流【产品溶图_场景融合】💐_1947855170459811842.json, 平台全量/kontextFC贴图局部重绘_1951235374687416322.json, 平台全量/合成海报-kontext-2.0_1953083282318684161.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_64

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Flux-kontext-产品+背景-自动合成溶图_1950960132547084289.json、图片生成/图生图/KONTEXT 溶图 V3_1985552455687720962.json、图片生成/图生图/KONTEXT+溶图+V3+，+最高效稳定万物迁移工作流_2013144975940263938.json、图片生成/图生图/Kontext Dev多图融合技巧（更可控）_1939332448016637954.json、图片生成/图生图/kontext超强溶图_1987866800891301889.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FastCanvas`
- `FastCanvasTool`
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
- `LoraLoaderModelOnly` —— 7/8 个有
- `easy imageRemBg` —— 7/8 个有
- `CR Text` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `ImageConcanate` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `DeepTranslatorTextNode` —— 3/8 个有
- `ImageConcatMulti` —— 3/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `Seed (rgthree)` —— 3/8 个有
- `StringFunction|pysssss` —— 3/8 个有
- `ChinesePrompt_Mix` —— 2/8 个有
- `ImageScaleToMegapixels` —— 2/8 个有
- `RepeatLatentBatch` —— 2/8 个有
- `TextCombinerTwo` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `BiRefNet_Hugo` —— 1/8 个有
- `CR Latent Batch Size` —— 1/8 个有
- `RH_Translator` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
