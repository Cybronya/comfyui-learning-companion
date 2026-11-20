---
name: image_to_image_lora_sampler_clip_92
type: Image To Image
frequency: 5
level: strong
coverage: 0.9158
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DF_Text_Box, EmptyFlux2LatentImage, GetImageSize, Image Comparer (rgthree), KOOK_SaveJPGImage, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/人宠合影_2094488714394300417.json, 平台全量/人脸矫正-V1_2095426450949234689.json, 平台全量/宠物写真_2094450486249353217.json, 平台全量/宠物生日照_2094449620310122497.json, 平台全量/宠物证件照_2094451004325580802.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_92

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/人宠合影_2094488714394300417.json、平台全量/人脸矫正-V1_2095426450949234689.json、平台全量/宠物写真_2094450486249353217.json、平台全量/宠物生日照_2094449620310122497.json、平台全量/宠物证件照_2094451004325580802.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DF_Text_Box`
- `EmptyFlux2LatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `KOOK_SaveJPGImage`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConstrainImage|pysssss` —— 4/5 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `easy imageColorMatch` —— 4/5 个有
- `Any Switch (rgthree)` —— 3/5 个有
- `DF_Integer` —— 3/5 个有
- `LayerMask: BiRefNetUltraV2` —— 3/5 个有
- `LayerMask: LoadBiRefNetModel` —— 3/5 个有
- `LayerUtility: ColorImage V2` —— 3/5 个有
- `LayerUtility: CropByMask V2` —— 3/5 个有
- `LayerUtility: ImageBlendAdvance` —— 3/5 个有
- `CR SDXL Aspect Ratio` —— 2/5 个有
- `DF_Text` —— 2/5 个有
- `easy cleanGpuUsed` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `easy textIndexSwitch` —— 2/5 个有
- `LayerUtility: ImageScaleRestore` —— 1/5 个有
- `StringReplace` —— 1/5 个有
- `Text _O` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 5 | 100% |
| Prompt 约束强度(CFG) | 1.2 | 1 - 1.2 | 5 | 91% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1.2，观测区间 1 - 1.2，5 个样本，取值集中（一致性 91%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（10/5 个样本）：Steps较低可能导致细节不足
