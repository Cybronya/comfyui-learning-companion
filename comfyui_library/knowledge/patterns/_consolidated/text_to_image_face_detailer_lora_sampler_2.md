---
name: text_to_image_face_detailer_lora_sampler_2
type: Text To Image
frequency: 4
level: strong
coverage: 0.813
common_nodes: [CFGZeroStar, CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, CompressImages, DetailerForEach, DifferentialDiffusion, EditDetailerPipe, EmptyLatentImage, Epsilon Scaling, FaceDetailerPipe, Fast Groups Bypasser (rgthree), ImageListToBatch_, ImpactSwitch, KSampler, Lora Loader Stack (rgthree), Mahiro, MaskToSEGS, ModelSamplingDiscrete, PrimitiveBoolean, PrimitiveFloat, PrimitiveInt, SAMLoader, SDXL Empty Latent Image (rgthree), SaveImage, Seed (rgthree), SolidMask, ToDetailerPipe, UltralyticsDetectorProvider, VAEDecode, VAELoader, easy int]
problems: []
missing: []
members: [图片生成/文生图/3D_2055958447262322690.json, 图片生成/文生图/Ri-mix_2055715028027887618.json, 图片生成/文生图/miao_2056398342451712001.json, 图片生成/文生图/wai170_2055541155709898753.json]
source: knowledge_consolidation
---

# text_to_image_face_detailer_lora_sampler_2

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/3D_2055958447262322690.json、图片生成/文生图/Ri-mix_2055715028027887618.json、图片生成/文生图/miao_2056398342451712001.json、图片生成/文生图/wai170_2055541155709898753.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGZeroStar`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CompressImages`
- `DetailerForEach`
- `DifferentialDiffusion`
- `EditDetailerPipe`
- `EmptyLatentImage`
- `Epsilon Scaling`
- `FaceDetailerPipe`
- `Fast Groups Bypasser (rgthree)`
- `ImageListToBatch_`
- `ImpactSwitch`
- `KSampler`
- `Lora Loader Stack (rgthree)`
- `Mahiro`
- `MaskToSEGS`
- `ModelSamplingDiscrete`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SAMLoader`
- `SDXL Empty Latent Image (rgthree)`
- `SaveImage`
- `Seed (rgthree)`
- `SolidMask`
- `ToDetailerPipe`
- `UltralyticsDetectorProvider`
- `VAEDecode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/4 个有
- `ColorCorrect` —— 1/4 个有
- `ColorMatchV2` —— 1/4 个有
- `LatentUpscaleBy` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 4 | 81% |
| Prompt 约束强度(CFG) | 8 | 5 - 8 | 4 | 82% |
| 采样算法 | euler_ancestral | - | 4 | 100% |
| 调度器 | karras | - | 4 | 50% |
| 重绘幅度 | 1 | 0.5 - 1 | 4 | 75% |
| 宽度 | 512 | 512 - 512 | 4 | 100% |
| 高度 | 512 | 512 - 512 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，4 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 5 - 8，4 个样本，取值集中（一致性 82%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 100%
- 调度器 最常用 karras，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，4 个样本
- 宽度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，4 个样本，取值集中（一致性 100%）
