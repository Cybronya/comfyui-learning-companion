---
name: image_to_image_lora_sampler_unet_69
type: Image To Image
frequency: 10
level: strong
coverage: 0.9252
common_nodes: [CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit 2511 极简工作流_2003712655913304065.json, 图片生成/图生图/Qwen-edit-2511-图像不偏移版_2004541985673412609.json, 图片生成/图生图/Qwen-eidt-2511-人物表情精准编辑(不偏移版)_2039330373867409410.json, 图片生成/图生图/Qwen-eidt-2511-人物表情精准编辑(不偏移版)_2076485352134631425.json, 图片生成/图生图/Qwen-eidt-2511-人物表情精准编辑(不偏移版)_2094969204024897537.json, 图片生成/图生图/Qwen-eidt-2511-人物表情精细编辑_2039326002383429633.json, 图片生成/图生图/Qwen-image-edit2511三图融合--标准版--（必收藏）_2049911848614543361.json, 图片生成/图生图/Qwen-image-edit2511双图编辑--标准版--（必收藏）_2049875414901903362.json, 图片生成/图生图/Qwen2511场景加模特（真实去AI感）_2013203484270665729.json, 图片生成/图生图/Qwen场景加模特（真实去AI感）_2028289977292951554.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_69

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit 2511 极简工作流_2003712655913304065.json、图片生成/图生图/Qwen-edit-2511-图像不偏移版_2004541985673412609.json、图片生成/图生图/Qwen-eidt-2511-人物表情精准编辑(不偏移版)_2039330373867409410.json、图片生成/图生图/Qwen-eidt-2511-人物表情精准编辑(不偏移版)_2076485352134631425.json、图片生成/图生图/Qwen-eidt-2511-人物表情精准编辑(不偏移版)_2094969204024897537.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 9/10 个有
- `CFGNorm` —— 8/10 个有
- `Image Comparer (rgthree)` —— 8/10 个有
- `ConditioningZeroOut` —— 6/10 个有
- `FluxKontextMultiReferenceLatentMethod` —— 5/10 个有
- `PixelSmileConditioning` —— 4/10 个有
- `ReferenceLatent` —— 3/10 个有
- `GetImageSize+` —— 2/10 个有
- `ImageResize+` —— 2/10 个有
- `LayerUtility: CropByMask V2` —— 2/10 个有
- `LayerUtility: RestoreCropBox` —— 2/10 个有
- `PrimitiveFloat` —— 2/10 个有
- `SetLatentNoiseMask` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `ImageConcanate` —— 1/10 个有
- `ImageScaleToTotalPixels` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 10 | 76% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（11/10 个样本）：Steps较低可能导致细节不足
