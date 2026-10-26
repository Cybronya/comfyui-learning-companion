---
name: text_to_image_sampler_clip_unet_211
type: Text To Image
frequency: 2
level: weak
coverage: 0.9535
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, EmptyLatentImage, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Boogu edit图像编辑+图像放大_2070355925101268993.json, 图片生成/图生图/F2_klein多图_2056028041498898434.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_211

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Boogu edit图像编辑+图像放大_2070355925101268993.json、图片生成/图生图/F2_klein多图_2056028041498898434.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `ConditioningZeroOut` —— 1/2 个有
- `DF_Get_image_size` —— 1/2 个有
- `ImageSharpen` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `ModelSamplingAuraFlow` —— 1/2 个有
- `TextEncodeBooguEdit` —— 1/2 个有
- `ZML_PreviewImage` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `workflow>自定义采样` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | - | 2 | 67% |
| 高度 | 768 | - | 2 | 67% |
| 采样步数 | 15.5 | - | 2 | 39% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 50% |
| 采样算法 | dpmpp_2m | - | 2 | 50% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，样本不足，未给区间，2 个样本
- 高度 中位数 768，样本不足，未给区间，2 个样本
- 采样步数 中位数 15.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 50%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
