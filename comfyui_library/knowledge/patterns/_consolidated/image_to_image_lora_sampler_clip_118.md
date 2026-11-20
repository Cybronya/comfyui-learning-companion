---
name: image_to_image_lora_sampler_clip_118
type: Image To Image
frequency: 3
level: strong
coverage: 0.937
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, Text Multiline, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/真人变假模_1980925614649724929.json, 数字人/数字人/kontext 真实人物照片转动漫卡通风格_1943493630646493185.json, 视频生成/图生视频/Flux 去除马赛克_1994289242960576513.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_118

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/真人变假模_1980925614649724929.json、数字人/数字人/kontext 真实人物照片转动漫卡通风格_1943493630646493185.json、视频生成/图生视频/Flux 去除马赛克_1994289242960576513.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/3 个有
- `GetImageSizeAndCount` —— 2/3 个有
- `ImageConcatMulti` —— 2/3 个有
- `ImageStitch` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `ConstrainImage|pysssss` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/3 个有
- `LayerUtility: CropByMask` —— 1/3 个有
- `LayerUtility: ImageAutoCrop V2` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 3 | 89% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
