---
name: image_to_image_lora_sampler_clip_66
type: Image To Image
frequency: 6
level: strong
coverage: 0.861667
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, ImpactInt, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/展示胸部_1996194183381762050.json, 图片生成/图生图/展示脚_1996210912619020289.json, 图片生成/文生图/【ComfyUI教程】Kontext透视纠正2.0，产品合成不再一眼假，节点逐一注释_2060600000048091137.json, 平台全量/F.1Kontext产品背景纠正透视溶图打光_2061801451910946818.json, 平台全量/F.1Kontext光影融合产品溶图打光场景海报合成阴影生成细节迁移尺寸不变_2019020038992306177.json, 平台全量/Kontext光影融合+放大（可选）_2046468687506444289.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_66

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/展示胸部_1996194183381762050.json、图片生成/图生图/展示脚_1996210912619020289.json、图片生成/文生图/【ComfyUI教程】Kontext透视纠正2.0，产品合成不再一眼假，节点逐一注释_2060600000048091137.json、平台全量/F.1Kontext产品背景纠正透视溶图打光_2061801451910946818.json、平台全量/F.1Kontext光影融合产品溶图打光场景海报合成阴影生成细节迁移尺寸不变_2019020038992306177.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImpactInt`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `Label (rgthree)` —— 5/6 个有
- `ConditioningZeroOut` —— 3/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `LayerUtility: ImageMaskScaleAs` —— 3/6 个有
- `HAIGC_SaveImagesToZip` —— 2/6 个有
- `InspyrenetRembg` —— 2/6 个有
- `LayerMask: MaskGrow` —— 2/6 个有
- `LayerUtility: HLFrequencyDetailRestore` —— 2/6 个有
- `LayerUtility: PurgeVRAM V2` —— 2/6 个有
- `RHUploadZip_V2` —— 2/6 个有
- `Text _O` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `ImageScaleBy` —— 1/6 个有
- `SeedVR2LoadDiTModel` —— 1/6 个有
- `SeedVR2LoadVAEModel` —— 1/6 个有
- `SeedVR2VideoUpscaler` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 6 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，6 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
