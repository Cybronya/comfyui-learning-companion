---
name: text_to_image_lora_sampler_clip_372
type: Text To Image
frequency: 5
level: strong
coverage: 0.867
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, Image Comparer (rgthree), JjkText, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MuyeTextEditOutput, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux 2 Kelin图片编辑PS专用 绿色遮罩重绘扩图工具_2113780878739595266.json, 图片生成/图生图/无痕扩图+图片编辑二合一｜Flux-2-Kelin图生图处理_2093255855188824066.json, 图片生成/图生图/无痕扩图图片编辑二合一｜Flux-2-Kelin图生图处理_2093097024676782082.json, 图片生成/图生图/无痕扩图图片编辑二合一｜Flux-2-Kelin图生图处理_2093499770567479298.json, 图片生成/图生图/无痕扩图图片编辑二合一｜Flux-2-Kelin图生图处理_2093540237699014658.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_372

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux 2 Kelin图片编辑PS专用 绿色遮罩重绘扩图工具_2113780878739595266.json、图片生成/图生图/无痕扩图+图片编辑二合一｜Flux-2-Kelin图生图处理_2093255855188824066.json、图片生成/图生图/无痕扩图图片编辑二合一｜Flux-2-Kelin图生图处理_2093097024676782082.json、图片生成/图生图/无痕扩图图片编辑二合一｜Flux-2-Kelin图生图处理_2093499770567479298.json、图片生成/图生图/无痕扩图图片编辑二合一｜Flux-2-Kelin图生图处理_2093540237699014658.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 5 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `JjkText`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MuyeTextEditOutput`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `DapaoImagePadDirectionNode` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `ImpactInt` —— 4/5 个有
- `孤海注释` —— 3/5 个有
- `GrowMask` —— 1/5 个有
- `ImageCompositeMasked` —— 1/5 个有
- `Int` —— 1/5 个有
- `InvertMask` —— 1/5 个有
- `LayerMask: MaskByColor` —— 1/5 个有
- `MaskBlur+` —— 1/5 个有
- `easy imageSizeByLongerSide` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高发问题（10/5 个样本）：Steps较低可能导致细节不足
