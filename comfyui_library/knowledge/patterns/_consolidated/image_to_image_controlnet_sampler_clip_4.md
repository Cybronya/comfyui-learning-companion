---
name: image_to_image_controlnet_sampler_clip_4
type: Image To Image
frequency: 8
level: moderate
coverage: 0.803375
common_nodes: [AIO_Preprocessor, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, FloatConstant, GetImageSize+, Image Comparer (rgthree), ImageAddNoise, ImageBlend, ImageSharpen, KSampler, LoadImage, MathExpression|pysssss, ModelPatchLoader, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy convertAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Z-image 增加真实感_细节_纹理_2000242586008907778.json, 图片生成/图生图/Z-image 真实感模特_2001124938759237634.json, 图片生成/图生图/Z-image+增加真实感_细节_纹理_2001123346911723522.json, 图片生成/图生图/Zimage+增加真实感细节纹理_2045136330379759618.json, 图片生成/图生图/Zimage增加真实感细节纹理_2054148049051635714.json, 图片生成/图生图/Zimage增加真实感细节纹理_2057640412038385665.json, 图片生成/图生图/人像摄影-增加细节-Zimage_2003395244379049985.json, 图片生成/图生图/人物变胖工作流_2001332037065863169.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/Z-image 增加真实感_细节_纹理_2000242586008907778.json、图片生成/图生图/Z-image 真实感模特_2001124938759237634.json、图片生成/图生图/Z-image+增加真实感_细节_纹理_2001123346911723522.json、图片生成/图生图/Zimage+增加真实感细节纹理_2045136330379759618.json、图片生成/图生图/Zimage增加真实感细节纹理_2054148049051635714.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 8 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `FloatConstant`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageAddNoise`
- `ImageBlend`
- `ImageSharpen`
- `KSampler`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelPatchLoader`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy convertAnything`

**可变部分**（部分 workflow 才有）：
- `ImageScaleBy` —— 4/8 个有
- `SeedVR2LoadDiTModel` —— 4/8 个有
- `SeedVR2LoadVAEModel` —— 4/8 个有
- `SeedVR2VideoUpscaler` —— 4/8 个有
- `CFGNorm` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有
- `ModelSamplingAuraFlow` —— 1/8 个有
- `TextEncodeQwenImageEditPlus` —— 1/8 个有
- `easy imageSize` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 8 | 93% |
| Prompt 约束强度(CFG) | 0.7 | 0.7 - 1 | 8 | 83% |
| 采样算法 | euler | - | 8 | 88% |
| 调度器 | sgm_uniform | - | 8 | 75% |
| 重绘幅度 | 0.25 | 0.2 - 1 | 8 | 26% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，8 个样本，取值集中（一致性 93%）
- Prompt 约束强度(CFG) 中位数 0.7，观测区间 0.7 - 1，8 个样本，取值集中（一致性 83%）
- 采样算法 最常用 euler，8 个样本，一致性 88%
- 调度器 最常用 sgm_uniform，8 个样本，一致性 75%
- 重绘幅度 中位数 0.25，观测区间 0.2 - 1，8 个样本，取值分散，一致性仅 26%
- 风险：Prompt 约束强度(CFG) 观测到 0.7，低于常用下限 1（CFG 过低可能导致 Prompt 约束不足、结果偏离描述）
