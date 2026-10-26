---
name: image_to_image_sampler_clip_unet_175
type: Image To Image
frequency: 2
level: weak
coverage: 0.9075
common_nodes: [CLIPTextEncode, DualCLIPLoader, FluxGuidance, GetImageSizeAndCount, ImageConcatMulti, ImageScaleDownToSize, ImageStitch, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键三视图+骨骼图参考_Kontext-DEV_1948706378098122753.json, 图片生成/文生图/Kontext_Canny  参考线稿引导，图像一致编辑：目前最稳定图像质量最好的控制lLORA_1962350864377823234.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_175

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键三视图+骨骼图参考_Kontext-DEV_1948706378098122753.json、图片生成/文生图/Kontext_Canny  参考线稿引导，图像一致编辑：目前最稳定图像质量最好的控制lLORA_1962350864377823234.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `ImageScaleDownToSize`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `CR SDXL Aspect Ratio` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `FluxKontextImageScale` —— 1/2 个有
- `ImageCrop` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `TeaCache` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22.5 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22.5，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
