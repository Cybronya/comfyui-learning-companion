---
name: text_to_image_lora_sampler_clip_252
type: Text To Image
frequency: 7
level: strong
coverage: 0.905
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), ImpactInt, JjkText, KSampler, LayerMask: MaskGrow, LayerUtility: HLFrequencyDetailRestore, LayerUtility: ImageMaskScaleAs, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/F.2 Klein产品溶图打光 电商场景合成光影融合海报_2098126474191654914.json, 图片生成/图生图/F.2_Klein产品溶图打光_电商场景合成光影融合海报_2098205867203186689.json, 图片生成/图生图/KONTX图像编辑工作流｜图生图一键高清生成_2094042285666299906.json, 图片生成/图生图/KONTX图像编辑工作流｜图生图局部重绘一键直出_2093832351976607745.json, 图片生成/图生图/Kontext产品溶图打光，图生图质感光影一步到位_2111209773038391298.json, 图片生成/图生图/Kontext产品溶图打光｜商品图质感升级出片利器_2111102942605570049.json, 图片生成/图生图/Kontext产品溶图打光｜图生图场景融合｜产品图氛围感直接拉满_2104785068794400770.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_252

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/F.2 Klein产品溶图打光 电商场景合成光影融合海报_2098126474191654914.json、图片生成/图生图/F.2_Klein产品溶图打光_电商场景合成光影融合海报_2098205867203186689.json、图片生成/图生图/KONTX图像编辑工作流｜图生图一键高清生成_2094042285666299906.json、图片生成/图生图/KONTX图像编辑工作流｜图生图局部重绘一键直出_2093832351976607745.json、图片生成/图生图/Kontext产品溶图打光，图生图质感光影一步到位_2111209773038391298.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `ImpactInt`
- `JjkText`
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
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 5/7 个有
- `FluxGuidance` —— 5/7 个有
- `InspyrenetRembg` —— 5/7 个有
- `LayerMask: BiRefNetUltraV2` —— 5/7 个有
- `LayerMask: LoadBiRefNetModelV2` —— 5/7 个有
- `GrowMask` —— 3/7 个有
- `ImageUpscaleWithModel` —— 3/7 个有
- `InvertMask` —— 3/7 个有
- `JoinImageWithAlpha` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `Upscale Model Loader` —— 3/7 个有
- `YUAN_TXTConvertAny` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `FastCanvas` —— 2/7 个有
- `FastCanvasTool` —— 2/7 个有
- `GLM_Translation_Text` —— 2/7 个有
- `ImageCropper` —— 2/7 个有
- `MultiTextConcatenate` —— 2/7 个有
- `MuyeTextEditOutput` —— 2/7 个有
- `easy imageRemBg` —— 2/7 个有
- `Label (rgthree)` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 7 | 100% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 80 | 7 | 100% |
| 高度 | 80 | 80 - 80 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，7 个样本，取值集中（一致性 100%）
- 高发问题（11/7 个样本）：Steps较低可能导致细节不足
