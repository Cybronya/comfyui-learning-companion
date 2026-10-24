---
name: image_to_image_sampler_clip_unet_60
type: Image To Image
frequency: 7
level: moderate
coverage: 0.777857
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, Flux2Scheduler, GetNode, KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein图生图+洗图+线稿+线稿上色_2031931837576122370.json, 图片生成/图生图/Klein图生图+洗图+线稿+线稿上色_2044302454275186690.json, 图片生成/图生图/Klein图生图+洗图+线稿=B站艾橘溪_2028089884472254465.json, 图片生成/图生图/WH-AI-Studio电商产品海报自动生成器_2022617947113529346.json, 图片生成/图生图/指定人脸+Flux2 klein图生图工作流_2038164410010705921.json, 图片生成/图生图/指定人脸+Klein图生图=B站艾橘溪_2012373696018653186.json, 图片生成/图生图/最新指定人脸换脸高清补光影+Klein图生图＋高清写实 2_2099689034640617474.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_60

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Klein图生图+洗图+线稿+线稿上色_2031931837576122370.json、图片生成/图生图/Klein图生图+洗图+线稿+线稿上色_2044302454275186690.json、图片生成/图生图/Klein图生图+洗图+线稿=B站艾橘溪_2028089884472254465.json、图片生成/图生图/WH-AI-Studio电商产品海报自动生成器_2022617947113529346.json、图片生成/图生图/指定人脸+Flux2 klein图生图工作流_2038164410010705921.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetNode`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageScaleDownToSize` —— 6/7 个有
- `Int` —— 6/7 个有
- `PainterFluxImageEdit` —— 6/7 个有
- `Qwen3_VQA` —— 6/7 个有
- `ShowText|pysssss` —— 6/7 个有
- `LayerMask: PersonMaskUltra V2` —— 3/7 个有
- `LayerUtility: CropBoxResolve` —— 3/7 个有
- `LayerUtility: CropByMask V2` —— 3/7 个有
- `SolidMask` —— 3/7 个有
- `easy mathInt` —— 3/7 个有
- `RHHiddenNodes` —— 2/7 个有
- `easy imageConcat` —— 2/7 个有
- `Anything Everywhere` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `ImageScale` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `LoraLoaderModelOnly` —— 1/7 个有
- `ModelSamplingAuraFlow` —— 1/7 个有
- `PhotoShakeNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 5 - 8 | 7 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 0.3 - 1 | 7 | 73% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 5 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，7 个样本
- 高发问题（10/7 个样本）：Steps较低可能导致细节不足
