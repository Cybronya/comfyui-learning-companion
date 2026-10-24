---
name: image_to_image_sampler_vae_3
type: Image To Image
frequency: 31
level: strong
coverage: 0.460032
common_nodes: [Any Switch (rgthree), CFGNorm, CLIPLoader, EmptyLatentImage, GetNode, ImageScaleToTotalPixels, KSampler, LoadImage, ModelPatchTorchSettings, ModelSamplingAuraFlow, PrimitiveInt, PrimitiveStringMultiline, SaveImage, SetNode, StringConcatenate, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/yj多角度_1991683574254485506.json, 图片生成/图生图/z-image多视角_2002236887446220802.json, 图片生成/图生图/一图生成人物的全角度_1981620515842473985.json, 图片生成/图生图/一张图出人物全角度-人物一致性（支持真人_动漫）_1983704766868037634.json, 图片生成/图生图/一张图出人物全角度V2-人物一致性-加速版_2011065826538954753.json, 图片生成/图生图/一张图出人物全角度V2-人物一致性-加速版_2011432776901332993.json, 图片生成/图生图/一张图出人物全角度V2-人物一致性-加速版_2016220775275040770.json, 图片生成/图生图/一张图出人物全角度V2-人物一致性-加速版_阿硕_2089697946785894401.json, 图片生成/图生图/一张图出人物全角度V2-人物一致性_1981196994767126530.json, 图片生成/图生图/一张图出人物全角度V2-人物一致性_1984142155717476354.json, 图片生成/图生图/一张图出人物全角度V2-人物一致性_1993714548070957058.json, 图片生成/图生图/一张图出人物全角度V2-人物替换必备工作流_2026924486397792258.json, 图片生成/图生图/一张图出人物全角度V2_1994769377599873026.json, 图片生成/图生图/一张图出全角度_2008736255999217666.json, 图片生成/图生图/一张图出多角度图(包含全身、半身) 可选择出图数量_1983428632158904322.json, 图片生成/图生图/一张图片生成角色IP多镜头，V2-人物一致性（加速版）_2009266921132269569.json, 图片生成/图生图/一键生成人物全角度_2030893471090876417.json, 图片生成/图生图/人物全角度V3-人物一致性-极速版-MARS专用_2020735967652483073.json, 图片生成/图生图/人物全角度V3-人物一致性-极速版-不像你打S我_2001152207812689922.json, 图片生成/图生图/人物全角度V3-人物一致性-极速版-最短路径_2001500414749077505.json, 图片生成/图生图/人物全角度——人物一致性_1986762890776670209.json, 图片生成/图生图/图生图一九宫格 快速生成_2051836082001596418.json, 图片生成/图生图/图生图一九宫格 快速生成_2051916860920221697.json, 图片生成/图生图/图生图一九宫格+快速生成 (1)_2054384617259585537.json, 图片生成/图生图/图生图一九宫格+快速生成_2053715110807523329.json, 图片生成/图生图/多角度丨人物角色一致性丨一张图出全角度丨高度一致性丨一致性衍生训练集丨开源稳定！！_1980921439090032642.json, 图片生成/图生图/多角度人物角色一致性丨一张图出全角度丨高度一致性丨一致性衍生lora训练集丨_2006170421481181186.json, 图片生成/图生图/影视二创-人物角色多角度丨一张图出全角度丨一次16张视角_2004500679655911426.json, 图片生成/图生图/影视二创-人物角色多角度丨一张图出全角度丨一次16张视角_2008565004580163585.json, 图片生成/图生图/模特无限姿势丨人物一致性不同姿势_1994611400838422530.json, 图片生成/图生图/🌈老许：千问2511-人物镜头多角度展示 （OpenPose版）_2003704689671716866.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_3

> 由 `engine/knowledge_consolidation` 从 31 个 workflow 归纳得出（图片生成/图生图/yj多角度_1991683574254485506.json、图片生成/图生图/z-image多视角_2002236887446220802.json、图片生成/图生图/一图生成人物的全角度_1981620515842473985.json、图片生成/图生图/一张图出人物全角度-人物一致性（支持真人_动漫）_1983704766868037634.json、图片生成/图生图/一张图出人物全角度V2-人物一致性-加速版_2011065826538954753.json…）

- **类型**：Image To Image
- **样本数**：31
- **可信度**：强结论
- **平均知识覆盖**：46%

## 共有节点

全部 31 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `EmptyLatentImage`
- `GetNode`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `SaveImage`
- `SetNode`
- `StringConcatenate`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Mute / Bypass Relay (rgthree)` —— 30/31 个有
- `Mute / Bypass Repeater (rgthree)` —— 30/31 个有
- `PathchSageAttentionKJ` —— 30/31 个有
- `PrimitiveString` —— 30/31 个有
- `easy bookmark` —— 26/31 个有
- `RHHiddenNodes` —— 25/31 个有
- `ImageFlip` —— 23/31 个有
- `Label (rgthree)` —— 18/31 个有
- `LoraLoaderModelOnly` —— 7/31 个有
- `UNETLoader` —— 6/31 个有
- `Fast Groups Muter (rgthree)` —— 2/31 个有
- `DiffusionModelLoaderKJ` —— 1/31 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/31 个有
- `GeminiImageNode` —— 1/31 个有
- `ImageResizeKJv2` —— 1/31 个有
- `ImageScaleBy` —— 1/31 个有
- `ImageUpscaleWithModel` —— 1/31 个有
- `PreviewImage` —— 1/31 个有
- `UpscaleModelLoader` —— 1/31 个有
- `VAEDecodeTiled` —— 1/31 个有
- `VAEEncodeTiled` —— 1/31 个有
- `easy showAnything` —— 1/31 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 31 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 31 | 100% |
| 采样算法 | euler | - | 31 | 97% |
| 调度器 | simple | - | 31 | 97% |
| 重绘幅度 | 1 | 0.4 - 1 | 31 | 89% |
| 宽度 | 960 | 624 - 960 | 31 | 92% |
| 高度 | 1304 | 880 - 1344 | 31 | 94% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 479/31 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，31 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，31 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，31 个样本，一致性 97%
- 调度器 最常用 simple，31 个样本，一致性 97%
- 重绘幅度 中位数 1，观测区间 0.4 - 1，31 个样本，取值集中（一致性 89%）
- 宽度 中位数 960，观测区间 624 - 960，31 个样本，取值集中（一致性 92%）
- 高度 中位数 1304，观测区间 880 - 1344，31 个样本，取值集中（一致性 94%）
- 高发问题（479/31 个样本）：Steps较低可能导致细节不足
