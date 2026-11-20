---
name: image_to_image_sampler_clip_unet_90
type: Image To Image
frequency: 7
level: strong
coverage: 0.875286
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/光影-斑驳_1947801930464641026.json, 平台全量/单张图片去水印_2032468628049760258.json, 平台全量/去掉马赛克_1954025157570678786.json, 平台全量/实拍产品一键精修_2011936535611969538.json, 平台全量/工作流实用推荐篇1-kontext图片完美去水印_2016848529863483394.json, 平台全量/电商服饰-真人服装变平面图-kontext_1972132599806291970.json, 平台全量/盒子Kontext 配色转换工作流_1956912159490805761.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_90

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/光影-斑驳_1947801930464641026.json、平台全量/单张图片去水印_2032468628049760258.json、平台全量/去掉马赛克_1954025157570678786.json、平台全量/实拍产品一键精修_2011936535611969538.json、平台全量/工作流实用推荐篇1-kontext图片完美去水印_2016848529863483394.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 7 个 workflow 都包含：
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
- `FluxKontextImageScale` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `LoraLoaderModelOnly` —— 4/7 个有
- `Image Comparer (rgthree)` —— 3/7 个有
- `Anything Everywhere3` —— 2/7 个有
- `easy imageConcat` —— 2/7 个有
- `CM_NearestSDXLResolution` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `Lora Loader` —— 1/7 个有
- `ModelSamplingFlux` —— 1/7 个有
- `PlaySound|pysssss` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 7 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，7 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
