---
name: text_to_image_inpaint_lora_sampler_2
type: Text To Image
frequency: 4
level: strong
coverage: 0.86125
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, INTConstant, Image Comparer (rgthree), InpaintCropImproved, InpaintStitchImproved, JjkText, KSampler, KSamplerAdvanced, LoraLoaderModelOnly, PreviewImage, SaveImage, SetLatentNoiseMask, SimpleMath+, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAEEncode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2.1美食摄影局部重绘 产品图一键精修处理工具_2114122651714281474.json, 图片生成/图生图/qwen2.1美食摄影局部重绘，物品摄影产品图一键精修_2110469161540472833.json, 图片生成/图生图/qwen2.1美食摄影局部重绘，物品摄影产品图一键精修_2113456098777853954.json, 图片生成/图生图/自动COS原图直出版，局部重绘妆容精修图生图_2111893662941667329.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen2.1美食摄影局部重绘 产品图一键精修处理工具_2114122651714281474.json、图片生成/图生图/qwen2.1美食摄影局部重绘，物品摄影产品图一键精修_2110469161540472833.json、图片生成/图生图/qwen2.1美食摄影局部重绘，物品摄影产品图一键精修_2113456098777853954.json、图片生成/图生图/自动COS原图直出版，局部重绘妆容精修图生图_2111893662941667329.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `INTConstant`
- `Image Comparer (rgthree)`
- `InpaintCropImproved`
- `InpaintStitchImproved`
- `JjkText`
- `KSampler`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SetLatentNoiseMask`
- `SimpleMath+`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `孤海注释` —— 3/4 个有
- `EmptyImage` —— 2/4 个有
- `ComfySwitchNode` —— 1/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `DrawMaskOnImage` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ImageResizeKJv2` —— 1/4 个有
- `Node Collector (rgthree)` —— 1/4 个有
- `PrimitiveStringMultiline` —— 1/4 个有
- `QwenImage21Cache` —— 1/4 个有
- `RH_RhartImageG25FlareImageToImage` —— 1/4 个有
- `ReferenceLatent` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
