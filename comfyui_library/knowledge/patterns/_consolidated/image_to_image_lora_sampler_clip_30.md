---
name: image_to_image_lora_sampler_clip_30
type: Image To Image
frequency: 8
level: strong
coverage: 0.949
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, InspyrenetRembg, KSampler, LayerMask: MaskGrow, LayerUtility: HLFrequencyDetailRestore, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Product Integration into Background電商工作流(Kontext)_2087376665625321473.json, 图片生成/图生图/kontext 光影融合_2044313699082571778.json, 图片生成/图生图/产品溶图 色彩变动小_2073969942722076673.json, 图片生成/图生图/光影融合工作流出.4.0_皮肤质感不变_2054854751262650369.json, 图片生成/图生图/文字去除_2056744378412130306.json, 图片生成/图生图/文字去除_2084124655224451073.json, 图片生成/图生图/融图 方式2_1960990249864368130.json, 图片生成/图生图/零偏移加投影-光影融合-文字细节图片尺寸不变_2075857386061000706.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_30

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Product Integration into Background電商工作流(Kontext)_2087376665625321473.json、图片生成/图生图/kontext 光影融合_2044313699082571778.json、图片生成/图生图/产品溶图 色彩变动小_2073969942722076673.json、图片生成/图生图/光影融合工作流出.4.0_皮肤质感不变_2054854751262650369.json、图片生成/图生图/文字去除_2056744378412130306.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `InspyrenetRembg`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: HLFrequencyDetailRestore`
- `LayerUtility: ImageMaskScaleAs`
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
- `Image Comparer (rgthree)` —— 6/8 个有
- `ImpactInt` —— 6/8 个有
- `FastCanvas` —— 2/8 个有
- `FastCanvasTool` —— 2/8 个有
- `Label (rgthree)` —— 2/8 个有
- `LayerUtility: AnyRerouter` —— 2/8 个有
- `LayerUtility: FluxKontextImageScale` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `HAIGC_SaveImagesToZip` —— 1/8 个有
- `PMRF` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `RBGImageStitchPlus` —— 1/8 个有
- `RHUploadZip_V2` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 27.5 | 20 - 30 | 8 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 27.5，观测区间 20 - 30，8 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
