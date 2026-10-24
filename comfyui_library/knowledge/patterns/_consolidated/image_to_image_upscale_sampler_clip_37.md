---
name: image_to_image_upscale_sampler_clip_37
type: Image To Image
frequency: 2
level: weak
coverage: 0.85
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, Fast Groups Bypasser (rgthree), FluxGuidance, Image Comparer (rgthree), ImageStitch, ImageUpscaleWithModel, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, ReferenceLatent, SaveImage, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux-kontext-dev+nunchaku 图像编辑极速版_1939984148310454273.json, 图片生成/图生图/flux-kontext 人物完美换衣(先脱后穿)_1940310513765011458.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_37

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flux-kontext-dev+nunchaku 图像编辑极速版_1939984148310454273.json、图片生成/图生图/flux-kontext 人物完美换衣(先脱后穿)_1940310513765011458.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageStitch`
- `ImageUpscaleWithModel`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `Fast Bypasser (rgthree)` —— 1/2 个有
- `GoogleTranslateTextNode` —— 1/2 个有
- `ImagePadForOutpaint` —— 1/2 个有
- `LoadImageOutput` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `NunchakuFluxDiTLoader` —— 1/2 个有
- `NunchakuFluxLoraLoader` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 14 | - | 2 | 57% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 14，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
