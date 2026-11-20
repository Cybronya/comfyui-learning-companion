---
name: image_to_image_sampler_clip_unet_69
type: Image To Image
frequency: 8
level: strong
coverage: 0.78
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, Flux2Scheduler, GetNode, ImageScaleToTotalPixels, KSampler, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/WH-AI-Studio电商产品海报自动生成器_2022617947113529346.json, 图片生成/图生图/klein多图编辑+高清修复_2035621289964081153.json, 图片生成/图生图/klien-多图编辑_2077583346317746178.json, 图片生成/图生图/图像仿色-光影色调迁移_flux2 klein_2050495157325320194.json, 图片生成/图生图/模特换装 替换人物与服装  精准版_2085542352353062914.json, 图片生成/图生图/模特换装 替换人物与服装  精准版_2089594684371988481.json, 平台全量/全自动海报生成_洗海报_2013126637335875585.json, 平台全量/换脸换装 Flux2 klein  5图编辑 多图编辑+高清修复_2054441759832330242.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_69

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/WH-AI-Studio电商产品海报自动生成器_2022617947113529346.json、图片生成/图生图/klein多图编辑+高清修复_2035621289964081153.json、图片生成/图生图/klien-多图编辑_2077583346317746178.json、图片生成/图生图/图像仿色-光影色调迁移_flux2 klein_2050495157325320194.json、图片生成/图生图/模特换装 替换人物与服装  精准版_2085542352353062914.json…）

- **类型**：Image To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 8 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `Flux2Scheduler`
- `GetNode`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerSelect`
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
- `EmptyFlux2LatentImage` —— 7/8 个有
- `GetImageSize` —— 7/8 个有
- `ConditioningZeroOut` —— 6/8 个有
- `Image Comparer (rgthree)` —— 6/8 个有
- `LoraLoaderModelOnly` —— 6/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `LoaderGGUF` —— 5/8 个有
- `easy imageColorMatch` —— 5/8 个有
- `AIO_Preprocessor` —— 4/8 个有
- `Image Padding` —— 4/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/8 个有
- `Anything Everywhere` —— 2/8 个有
- `ModelSamplingAuraFlow` —— 2/8 个有
- `RHHiddenNodes` —— 2/8 个有
- `AILab_QwenVL` —— 1/8 个有
- `ImitationHueNode` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `easy imageConcat` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 8 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 75% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，8 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 75%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
