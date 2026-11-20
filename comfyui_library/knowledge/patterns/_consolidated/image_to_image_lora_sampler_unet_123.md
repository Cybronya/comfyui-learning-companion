---
name: image_to_image_lora_sampler_unet_123
type: Image To Image
frequency: 6
level: weak
coverage: 0.847333
common_nodes: [CFGNorm, CLIPLoader, FluxKontextImageScale, GetImageSize, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/69.tonnie-2511扩图_2010311843973177346.json, 图片生成/图生图/73.tonnie-2511换脸（效果不好）_2010883623301419009.json, 图片生成/图生图/Qwen edit 2511无像素偏移_2004837793459306497.json, 图片生成/图生图/Qwen_Edit_2511-无偏移增强版单图编辑工作流_2005187774271680514.json, 平台全量/Qwen-edit-2511 换脸_2008019983095304193.json, 平台全量/QwenEdit2511高质量换脸换装万物迁移_2036001547536048129.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_123

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/69.tonnie-2511扩图_2010311843973177346.json、图片生成/图生图/73.tonnie-2511换脸（效果不好）_2010883623301419009.json、图片生成/图生图/Qwen edit 2511无像素偏移_2004837793459306497.json、图片生成/图生图/Qwen_Edit_2511-无偏移增强版单图编辑工作流_2005187774271680514.json、平台全量/Qwen-edit-2511 换脸_2008019983095304193.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextImageScale`
- `GetImageSize`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `Image Blank` —— 4/6 个有
- `Image Comparer (rgthree)` —— 4/6 个有
- `ImageCompositeMasked` —— 4/6 个有
- `JoinImageWithAlpha` —— 4/6 个有
- `CropFace` —— 3/6 个有
- `Mask Fill Holes` —— 3/6 个有
- `CLIPTextEncode` —— 2/6 个有
- `ConditioningZeroOut` —— 2/6 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `ReferenceLatent` —— 2/6 个有
- `CR Prompt Text` —— 1/6 个有
- `DifferentialDiffusion` —— 1/6 个有
- `GetImageSizeAndCount` —— 1/6 个有
- `ImageBlank` —— 1/6 个有
- `ImagePadForOutpaint` —— 1/6 个有
- `ImageStitch` —— 1/6 个有
- `MaskPreview` —— 1/6 个有
- `PrimitiveStringMultiline` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 1 - 10 | 6 | 51% |
| Prompt 约束强度(CFG) | 1 | 1 - 10 | 6 | 0% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 1 - 10，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 10，6 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（5/6 个样本）：Steps较低可能导致细节不足
