---
name: image_to_image_controlnet_lora_sampler_3
type: Image To Image
frequency: 14
level: strong
coverage: 0.854714
common_nodes: [CFGNorm, DepthAnythingPreprocessor, Image Comparer (rgthree), ImagePadForOutpaint, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, Mask Fill Holes, MaskPreview+, ModelPatchLoader, ModelSamplingAuraFlow, OpenposePreprocessor, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Image-Edit 2511 工作流_2005512879656894466.json, 图片生成/图生图/史上最强多角度切换_1986738140855660546.json, 图片生成/图生图/多人物生成（最新）_1985591139195662338.json, 图片生成/图生图/多角度切换_1993455227615510529.json, 图片生成/图生图/生成特效_2001941830977634306.json, 图片生成/图生图/电商设计 白底图转场景 Qwen-Edit-2509_1987693018406916097.json, 图片生成/图生图/白底商品物品图生成场景白底图添加背景_2020531895754297346.json, 图片生成/图生图/白底生场景_2006309862233350146.json, 图片生成/图生图/草稿转海报图 （本地解码版本） 很好用_1997203326477484034.json, 图片生成/图生图/草稿转海报图_1996990126343536642.json, 图片生成/图生图/转漫画_2009566925705187330.json, 图片生成/文生图/产品线稿特效渲染_2003156643368042497.json, 图片生成/文生图/白底图生产品使用场景2509_2006431579106709505.json, 数字人/数字人/多人物生成（最新）_2093650694959099906.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/Qwen-Image-Edit 2511 工作流_2005512879656894466.json、图片生成/图生图/史上最强多角度切换_1986738140855660546.json、图片生成/图生图/多人物生成（最新）_1985591139195662338.json、图片生成/图生图/多角度切换_1993455227615510529.json、图片生成/图生图/生成特效_2001941830977634306.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGNorm`
- `DepthAnythingPreprocessor`
- `Image Comparer (rgthree)`
- `ImagePadForOutpaint`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `Mask Fill Holes`
- `MaskPreview+`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `OpenposePreprocessor`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `CannyEdgePreprocessor` —— 12/14 个有
- `ImageScaleBy` —— 10/14 个有
- `LoadDiffusionModelShared //Inspire` —— 8/14 个有
- `LoadTextEncoderShared //Inspire` —— 8/14 个有
- `SeedVR2LoadDiTModel` —— 8/14 个有
- `SeedVR2LoadVAEModel` —— 8/14 个有
- `SeedVR2VideoUpscaler` —— 8/14 个有
- `CLIPLoader` —— 6/14 个有
- `UNETLoader` —— 6/14 个有
- `Canny` —— 2/14 个有
- `ImageUpscaleWithModel` —— 2/14 个有
- `UpscaleModelLoader` —— 2/14 个有
- `easy imageColorMatch` —— 2/14 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/14 个有
- `NunchakuQwenImageDiTLoader` —— 1/14 个有
- `TT_img_enc` —— 1/14 个有
- `Text Concatenate` —— 1/14 个有
- `Text Multiline` —— 1/14 个有
- `TextEncodeQwenImageEditPlusAdvance_lrzjason` —— 1/14 个有
- `easy cleanGpuUsed` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 14 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 14 | 100% |
| 采样算法 | euler | - | 14 | 79% |
| 调度器 | simple | - | 14 | 79% |
| 重绘幅度 | 1 | 0.15 - 1 | 14 | 66% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 17/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，14 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，14 个样本，一致性 79%
- 调度器 最常用 simple，14 个样本，一致性 79%
- 重绘幅度 中位数 1，观测区间 0.15 - 1，14 个样本
- 高发问题（17/14 个样本）：Steps较低可能导致细节不足
