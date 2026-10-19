---
name: image_to_image_sampler_clip_vae_2
type: Image To Image
frequency: 7
level: strong
coverage: 0.885143
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, GoogleTranslateTextNode, ImageStitch, KSampler, LoadImage, LoadImageOutput, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: [CR Prompt Text]
members: [图片生成/文生图/1942757866497617921.json, 图片生成/文生图/1944642913160843265.json, 图片生成/文生图/1956530025573044225.json, 图片生成/文生图/1968134912584876033.json, 视频生成/图生视频/1941888370622754818.json, 视频生成/图生视频/1944641439055925249.json, 视频生成/图生视频/1944590384733540353.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_2

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1942757866497617921.json、图片生成/文生图/1944642913160843265.json、图片生成/文生图/1956530025573044225.json、图片生成/文生图/1968134912584876033.json、视频生成/图生视频/1941888370622754818.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `GoogleTranslateTextNode`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `LoadImageOutput`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 6/7 个有
- `ImageConcanate` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `NunchakuFluxDiTLoader` —— 3/7 个有
- `NunchakuFluxLoraLoader` —— 3/7 个有
- `TeaCache` —— 3/7 个有
- `UnetLoaderGGUF` —— 3/7 个有
- `EmptySD3LatentImage` —— 2/7 个有
- `JWInteger` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `PDIMAGE_LongerSize` —— 2/7 个有
- `RHHiddenNodes` —— 2/7 个有
- `UNETLoader` —— 2/7 个有
- `VHS_VideoCombine` —— 2/7 个有
- `LayerColor: BrightnessContrastV2` —— 1/7 个有
- `LayerFilter: Sharp & Soft` —— 1/7 个有
- `MagCache` —— 1/7 个有
- `Text` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text
