---
name: image_to_image_lora_sampler_unet_79
type: Image To Image
frequency: 8
level: strong
coverage: 0.9065
common_nodes: [CLIPLoader, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit 2511 极简工作流_2003712655913304065.json, 图片生成/图生图/Qwen-edit-2511-图像不偏移版_2004541985673412609.json, 图片生成/图生图/Qwen-eidt-2511-人物表情精准编辑(不偏移版)_2039330373867409410.json, 图片生成/图生图/Qwen-eidt-2511-人物表情精准编辑(不偏移版)_2076485352134631425.json, 图片生成/图生图/Qwen-eidt-2511-人物表情精准编辑(不偏移版)_2094969204024897537.json, 图片生成/图生图/Qwen-eidt-2511-人物表情精细编辑_2039326002383429633.json, 图片生成/图生图/Qwen2511场景加模特（真实去AI感）_2013203484270665729.json, 图片生成/图生图/Qwen场景加模特（真实去AI感）_2028289977292951554.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_79

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit 2511 极简工作流_2003712655913304065.json、图片生成/图生图/Qwen-edit-2511-图像不偏移版_2004541985673412609.json、图片生成/图生图/Qwen-eidt-2511-人物表情精准编辑(不偏移版)_2039330373867409410.json、图片生成/图生图/Qwen-eidt-2511-人物表情精准编辑(不偏移版)_2076485352134631425.json、图片生成/图生图/Qwen-eidt-2511-人物表情精准编辑(不偏移版)_2094969204024897537.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
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
- `CFGNorm` —— 7/8 个有
- `ModelSamplingAuraFlow` —— 7/8 个有
- `ConditioningZeroOut` —— 6/8 个有
- `PixelSmileConditioning` —— 4/8 个有
- `FluxKontextMultiReferenceLatentMethod` —— 3/8 个有
- `ReferenceLatent` —— 3/8 个有
- `GetImageSize+` —— 2/8 个有
- `ImageResize+` —— 2/8 个有
- `LayerUtility: CropByMask V2` —— 2/8 个有
- `LayerUtility: RestoreCropBox` —— 2/8 个有
- `PrimitiveFloat` —— 2/8 个有
- `SetLatentNoiseMask` —— 2/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `ImageConcanate` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 8 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，8 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（9/8 个样本）：Steps较低可能导致细节不足
