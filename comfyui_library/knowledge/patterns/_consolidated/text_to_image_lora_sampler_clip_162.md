---
name: text_to_image_lora_sampler_clip_162
type: Text To Image
frequency: 10
level: strong
coverage: 0.8469
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageScaleToTotalPixels, JjkText, JoinStrings, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, PreviewImage, Qwen3_VQA, SaveImage, ShowText|pysssss, TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, WD14Tagger|pysssss, easy showAnything, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键动漫转真人去AI感｜超真实漫画线稿转真人上色图生图_2091284153483485186.json, 图片生成/图生图/一键动漫转真人｜去AI感超真实线稿上色图生图_2096327040692740098.json, 图片生成/图生图/动漫漫画线稿一键转真人｜上色去AI感超写实出片_2103081870073356289.json, 图片生成/图生图/动漫漫画线稿一键转真人｜写实上色去AI感超真实出图_2110705708227457025.json, 图片生成/图生图/动漫漫画线稿转真人 上色去AI感超真实图生图_2098856374296989697.json, 图片生成/图生图/动漫线稿转真人上色｜去AI感超真实图生图写实_2095845675723476993.json, 图片生成/图生图/动漫转真人漫画转真人线稿转真人线稿上色去AI感超真实_2109430637001273345.json, 图片生成/图生图/去AI感超真实动漫转真人｜漫画线稿转真人上色图生图生成_2091300209572794370.json, 图片生成/图生图/去AI感超真实｜动漫漫画线稿转真人图生图上色_2090928740271484929.json, 图片生成/图生图/漫画线稿转真人｜动漫转写实 去AI感超真实 上色效果自然_2105521306086232065.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_162

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/一键动漫转真人去AI感｜超真实漫画线稿转真人上色图生图_2091284153483485186.json、图片生成/图生图/一键动漫转真人｜去AI感超真实线稿上色图生图_2096327040692740098.json、图片生成/图生图/动漫漫画线稿一键转真人｜上色去AI感超写实出片_2103081870073356289.json、图片生成/图生图/动漫漫画线稿一键转真人｜写实上色去AI感超真实出图_2110705708227457025.json、图片生成/图生图/动漫漫画线稿转真人 上色去AI感超真实图生图_2098856374296989697.json…）

- **类型**：Text To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `JjkText`
- `JoinStrings`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `Qwen3_VQA`
- `SaveImage`
- `ShowText|pysssss`
- `TextEncodeQwenImageEdit`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `WD14Tagger|pysssss`
- `easy showAnything`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PIP_图像联结` —— 5/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 10 | 100% |
| 采样算法 | er_sde | - | 10 | 100% |
| 调度器 | beta | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |
| 宽度 | 80 | 80 - 80 | 10 | 100% |
| 高度 | 80 | 80 - 80 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 30/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，10 个样本，一致性 100%
- 调度器 最常用 beta，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，10 个样本，取值集中（一致性 100%）
- 高发问题（30/10 个样本）：Steps较低可能导致细节不足
