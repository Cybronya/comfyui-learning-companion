---
name: image_to_image_sampler_clip_unet_37
type: Image To Image
frequency: 11
level: strong
coverage: 0.910818
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux-kontext 通用三视图v2_1939134527006822401.json, 图片生成/图生图/Flux-kontext 通用三视图v2_1956579410549854210.json, 图片生成/图生图/Flux-kontext完美去水印_2074376725714268161.json, 图片生成/图生图/Flux-终章_1938425347513716737.json, 图片生成/图生图/JC自用Kontext改图_1952574001413599234.json, 图片生成/图生图/Kontext  图像遮罩修改_1942399861767737346.json, 图片生成/图生图/Kontext Dev涂抹遮罩精准修图_1940228497220747266.json, 图片生成/图生图/Kontext Dev生成三视图-一句话改图时代开启_1949672728417718273.json, 图片生成/图生图/kontext 人物三视图_1942403251813945346.json, 平台全量/Kontext Dev涂抹遮罩精准修图-涂哪改哪_1939977597440671745.json, 平台全量/Kontext Dev生成三视图-一句话改图时代开启_1939585349809053697.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_37

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Flux-kontext 通用三视图v2_1939134527006822401.json、图片生成/图生图/Flux-kontext 通用三视图v2_1956579410549854210.json、图片生成/图生图/Flux-kontext完美去水印_2074376725714268161.json、图片生成/图生图/Flux-终章_1938425347513716737.json、图片生成/图生图/JC自用Kontext改图_1952574001413599234.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 11 个 workflow 都包含：
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
- `FluxKontextImageScale` —— 10/11 个有
- `PreviewImage` —— 6/11 个有
- `RH_Translator` —— 6/11 个有
- `ConstrainImage|pysssss` —— 5/11 个有
- `Image Blank` —— 3/11 个有
- `Image Comparer (rgthree)` —— 3/11 个有
- `ImageStitch` —— 3/11 个有
- `LayerUtility: ImageScaleRestore` —— 3/11 个有
- `MaskToImage` —— 3/11 个有
- `Mix Color By Mask` —— 3/11 个有
- `CR SDXL Aspect Ratio` —— 2/11 个有
- `RMBG` —— 2/11 个有
- `ResizeImageMixlab` —— 1/11 个有
- `Text Multiline` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 11 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，11 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
