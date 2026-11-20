---
name: image_to_image_sampler_clip_unet_9
type: Image To Image
frequency: 22
level: strong
coverage: 0.877955
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/图片一键去水印工具_1994723497270185986.json, 图片生成/图生图/图片去水印 一键消除水印_1991030181810872322.json, 图片生成/图生图/图片去除水印｜Flux Kontext_1965644146411192321.json, 图片生成/图生图/精修  产品精修  高清放大  高清修复_2067117890985349122.json, 图片生成/图生图/精修  产品精修  高清放大  高清修复_2067171835975913473.json, 图片生成/图生图/精修  产品精修  高清放大  高清修复_2067179157712359425.json, 图片生成/图生图/精修  产品精修  高清放大  高清修复_2067208635549310978.json, 图片生成/图生图/精修  产品精修  高清放大  高清修复_2067220096564682753.json, 图片生成/图生图/精修  产品精修  高清放大  高清修复_2067291955792539649.json, 图片生成/图生图/精修(全能)-kontext_1946789807444881409.json, 图片生成/图生图/精修(全能)-kontext_1978771739381485569.json, 图片生成/图生图/精修-3C电器类-kontxet_1959112427612876802.json, 图片生成/图生图/精修-人像类-kontxet_1959172035203248129.json, 图片生成/图生图/精修-美妆类-kontxet_1959132660998287362.json, 图片生成/图生图/精修-饰品类-kontxet_1959157765254098946.json, 图片生成/图生图/精修图像人物_商品_2054200148770729986.json, 图片生成/图生图/角色三视图_1946904422775709697.json, 图片生成/图生图/角色三视图_2034158201708486657.json, 图片生成/图生图/角色三视图_2049287384948281346.json, "图片生成/文生图/电商桌面产品换背景,产品不变_1977561433867210753.json", 图片生成/文生图/阮旭东aigc：仿 全能图片V1 3d渲染打印工作流（含supir放大+前后对比）_1961604160586190849.json, 视频生成/图生视频/精修(全能)-kontext_2048657663176740866.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_9

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/图生图/图片一键去水印工具_1994723497270185986.json、图片生成/图生图/图片去水印 一键消除水印_1991030181810872322.json、图片生成/图生图/图片去除水印｜Flux Kontext_1965644146411192321.json、图片生成/图生图/精修  产品精修  高清放大  高清修复_2067117890985349122.json、图片生成/图生图/精修  产品精修  高清放大  高清修复_2067171835975913473.json…）

- **类型**：Image To Image
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：88%

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
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 20/22 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 20/22 个有
- `LoraLoaderModelOnly` —— 19/22 个有
- `PreviewImage` —— 17/22 个有
- `FluxKontextImageScale` —— 9/22 个有
- `DetailTransfer` —— 4/22 个有
- `ImageScaleToTotalPixels` —— 1/22 个有
- `ImpactImageBatchToImageList` —— 1/22 个有
- `Int` —— 1/22 个有
- `SUPIR_Upscale` —— 1/22 个有
- `Text` —— 1/22 个有
- `workflow>HyperSpeed` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 22 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 22 | 100% |
| 采样算法 | euler | - | 22 | 100% |
| 调度器 | simple | - | 22 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，22 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，22 个样本，一致性 100%
- 调度器 最常用 simple，22 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
