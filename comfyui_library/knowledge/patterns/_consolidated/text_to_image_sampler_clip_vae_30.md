---
name: text_to_image_sampler_clip_vae_30
type: Text To Image
frequency: 3
level: weak
coverage: 0.881667
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DeepTranslatorTextNode, EmptyLatentImage, GetImageSize+, ImageConcanate, KSampler, LayerUtility: JoyCaptionBeta1, LayerUtility: LoadJoyCaptionBeta1Model, LoadImage, SaveImage, ShowText|pysssss, VAEDecode, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/反推提示词/joycaption3反推新王_1928065677561577474.json, 图片生成/反推提示词/反推JoyCaption3+Z image工作流_2039279837541572609.json, 图片生成/图生图/批量打标最新反推｜JoyCaption3海报制作利器_2091223214956568578.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_vae_30

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/反推提示词/joycaption3反推新王_1928065677561577474.json、图片生成/反推提示词/反推JoyCaption3+Z image工作流_2039279837541572609.json、图片生成/图生图/批量打标最新反推｜JoyCaption3海报制作利器_2091223214956568578.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DeepTranslatorTextNode`
- `EmptyLatentImage`
- `GetImageSize+`
- `ImageConcanate`
- `KSampler`
- `LayerUtility: JoyCaptionBeta1`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LoadImage`
- `SaveImage`
- `ShowText|pysssss`
- `VAEDecode`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `CheckpointLoaderSimple` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `VAELoader` —— 2/3 个有
- `JjkText` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoadImagesFromFolderKJ` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `Note _O` —— 1/3 个有
- `Save Text File` —— 1/3 个有
- `SeedVarianceEnhancer` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有
- `solarL_SaveImagesToZip` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 80 - 512 | 3 | 45% |
| 高度 | 512 | 80 - 512 | 3 | 45% |
| 采样步数 | 5 | 4 - 20 | 3 | 24% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 3 | 24% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 80 - 512，3 个样本，取值分散，一致性仅 45%
- 高度 中位数 512，观测区间 80 - 512，3 个样本，取值分散，一致性仅 45%
- 采样步数 中位数 5，观测区间 4 - 20，3 个样本，取值分散，一致性仅 24%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，3 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
