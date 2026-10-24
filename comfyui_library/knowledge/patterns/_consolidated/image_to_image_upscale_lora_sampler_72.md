---
name: image_to_image_upscale_lora_sampler_72
type: Image To Image
frequency: 2
level: weak
coverage: 0.8965
common_nodes: [CLIPLoader, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, Krea2EditGroundedEncode, Krea2EditModelPatch, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Krea2 Edit 双图编辑工作流_2088249764218490881.json, 图片生成/图生图/Krea2 Turbo 双图编辑工作流 自带无损 4K 高清放大_2075834701444632578.json]
source: knowledge_consolidation
---

# image_to_image_upscale_lora_sampler_72

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Krea2 Edit 双图编辑工作流_2088249764218490881.json、图片生成/图生图/Krea2 Turbo 双图编辑工作流 自带无损 4K 高清放大_2075834701444632578.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `Krea2EditGroundedEncode`
- `Krea2EditModelPatch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `ImpactMinMax` —— 1/2 个有
- `PrimitiveBoolean` —— 1/2 个有
- `ResolutionSelector` —— 1/2 个有
- `TextInput_` —— 1/2 个有
- `ZML_SwitchOutput` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 11 | - | 2 | 91% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 1536 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
