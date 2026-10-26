---
name: image_to_image_lora_sampler_clip_63
type: Image To Image
frequency: 4
level: strong
coverage: 0.9305
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, GetImageSize_, ImageCrop, ImageStitch, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, PreviewImage, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Kontext深度图角色一致性迁移工作流V1_1957723229132783618.json, 图片生成/图生图/人物kontext深度编辑_1958375720730968066.json, 图片生成/文生图/Kontext深度控制ControlNet  让图像编辑更可控_1957626065449578497.json, 图片生成/文生图/Kontext深度控制ControlNet  让图像编辑更可控_2049318030034870273.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_63

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux Kontext深度图角色一致性迁移工作流V1_1957723229132783618.json、图片生成/图生图/人物kontext深度编辑_1958375720730968066.json、图片生成/文生图/Kontext深度控制ControlNet  让图像编辑更可控_1957626065449578497.json、图片生成/文生图/Kontext深度控制ControlNet  让图像编辑更可控_2049318030034870273.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GetImageSize_`
- `ImageCrop`
- `ImageStitch`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `CR Prompt Text` —— 1/4 个有
- `DepthAnything_V2` —— 1/4 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `PDIMAGE_LongerSize` —— 1/4 个有
- `SeedVR2` —— 1/4 个有
- `TeaCache` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
