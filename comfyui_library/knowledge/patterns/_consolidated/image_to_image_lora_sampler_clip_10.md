---
name: image_to_image_lora_sampler_clip_10
type: Image To Image
frequency: 13
level: strong
coverage: 0.931154
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LayerUtility: HLFrequencyDetailRestore, LayerUtility: ImageMaskScaleAs, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Product Integration into Background電商工作流(Kontext)_2087376665625321473.json, 图片生成/图生图/kontext 光影融合_2044313699082571778.json, 图片生成/图生图/产品溶图 色彩变动小_2073969942722076673.json, 图片生成/图生图/光影融合工作流出.4.0_皮肤质感不变_2054854751262650369.json, 图片生成/图生图/文字去除_2056744378412130306.json, 图片生成/图生图/文字去除_2084124655224451073.json, 图片生成/图生图/融图 方式2_1960990249864368130.json, 图片生成/图生图/零偏移加投影-光影融合-文字细节图片尺寸不变_2075857386061000706.json, 平台全量/AI人像换背景_1971968703522926593.json, 平台全量/Kontext 产品迁移光影融合还原材质细节_1969044737183391746.json, 平台全量/Kontext 光影融合(自用)_1959529564726833154.json, 平台全量/Kontext 无损光影打光融合_1959204688077991938.json, 平台全量/kontexe-产品光影融合_1972139362794270722.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/Product Integration into Background電商工作流(Kontext)_2087376665625321473.json、图片生成/图生图/kontext 光影融合_2044313699082571778.json、图片生成/图生图/产品溶图 色彩变动小_2073969942722076673.json、图片生成/图生图/光影融合工作流出.4.0_皮肤质感不变_2054854751262650369.json、图片生成/图生图/文字去除_2056744378412130306.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LayerUtility: HLFrequencyDetailRestore`
- `LayerUtility: ImageMaskScaleAs`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `InspyrenetRembg` —— 12/13 个有
- `LayerMask: MaskGrow` —— 12/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 12/13 个有
- `Image Comparer (rgthree)` —— 10/13 个有
- `FastCanvas` —— 7/13 个有
- `FastCanvasTool` —— 7/13 个有
- `LayerUtility: FluxKontextImageScale` —— 7/13 个有
- `ImpactInt` —— 6/13 个有
- `PreviewImage` —— 6/13 个有
- `LayerUtility: AnyRerouter` —— 5/13 个有
- `Anything Everywhere` —— 2/13 个有
- `Label (rgthree)` —— 2/13 个有
- `RBGImageStitchPlus` —— 2/13 个有
- `easy cleanGpuUsed` —— 2/13 个有
- `ConstrainImage|pysssss` —— 1/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `HAIGC_SaveImagesToZip` —— 1/13 个有
- `PMRF` —— 1/13 个有
- `RHUploadZip_V2` —— 1/13 个有
- `easy imageRemBg` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 13 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | beta | - | 13 | 54% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，13 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 54%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
