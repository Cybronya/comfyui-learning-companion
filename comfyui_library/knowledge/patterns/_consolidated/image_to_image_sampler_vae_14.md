---
name: image_to_image_sampler_vae_14
type: Image To Image
frequency: 11
level: strong
coverage: 0.451
common_nodes: [Any Switch (rgthree), CFGNorm, CLIPLoader, EmptyLatentImage, GetNode, ImageScaleToTotalPixels, KSampler, LoadImage, ModelSamplingAuraFlow, PathchSageAttentionKJ, PrimitiveInt, PrimitiveStringMultiline, SaveImage, SetNode, StringConcatenate, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/动作模仿-人物一致性-10S出图_2001928140073103361.json, 图片生成/图生图/多角度-人物一致性_1997274319640268802.json, 图片生成/图生图/超级360°姿态生成生成各种朝向_1979064149919567874.json, 图片生成/文生图/一张图出人物全角度V2-人物一致性-加速版 阿硕_1980485872774762497.json, 图片生成/文生图/一张图出人物全角度V2-人物一致性-加速版一次性出15张人物一致性图片_2095333742851223554.json, 图片生成/文生图/一张图生成人物全角度_2011206036333535234.json, 图片生成/文生图/人物全角度一致性-加速版 -邻家AI大女孩_2043564088546041858.json, 平台全量/【CQ808】一张图出人物全角度V2-人物一致性-加速版_2016096544012902401.json, 平台全量/一张图出人物三视图 阿飞_2019795327984869378.json, 平台全量/多角度丨人物角色一致性丨一张图出全角度丨高度一致性丨一致性衍生训练集丨开源稳定！！_1983506467233931265.json, 平台全量/模特套图裂变丨高一致性多姿生成  一图生成人物全角度视图图片_1992766162484391938.json]
source: knowledge_consolidation
---

# image_to_image_sampler_vae_14

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/动作模仿-人物一致性-10S出图_2001928140073103361.json、图片生成/图生图/多角度-人物一致性_1997274319640268802.json、图片生成/图生图/超级360°姿态生成生成各种朝向_1979064149919567874.json、图片生成/文生图/一张图出人物全角度V2-人物一致性-加速版 阿硕_1980485872774762497.json、图片生成/文生图/一张图出人物全角度V2-人物一致性-加速版一次性出15张人物一致性图片_2095333742851223554.json…）

- **类型**：Image To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：45%

## 共有节点

全部 11 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGNorm`
- `CLIPLoader`
- `EmptyLatentImage`
- `GetNode`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `PathchSageAttentionKJ`
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
- `ModelPatchTorchSettings` —— 10/11 个有
- `PrimitiveString` —— 10/11 个有
- `RHHiddenNodes` —— 10/11 个有
- `Mute / Bypass Repeater (rgthree)` —— 9/11 个有
- `Mute / Bypass Relay (rgthree)` —— 8/11 个有
- `easy bookmark` —— 8/11 个有
- `ImageFlip` —— 7/11 个有
- `Label (rgthree)` —— 7/11 个有
- `Anything Everywhere` —— 1/11 个有
- `DWPreprocessor` —— 1/11 个有
- `GroundingDinoModelLoader (segment anything2)` —— 1/11 个有
- `NunchakuQwenImageDiTLoader` —— 1/11 个有
- `NunchakuQwenImageLoraLoader` —— 1/11 个有
- `SDPoseOODLoader` —— 1/11 个有
- `SDPoseOODProcessor` —— 1/11 个有
- `YOLOModelLoader` —— 1/11 个有
- `孤海注释` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 960 | 720 - 960 | 11 | 93% |
| 高度 | 1304 | 1024 - 1304 | 11 | 94% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 140/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 960，观测区间 720 - 960，11 个样本，取值集中（一致性 93%）
- 高度 中位数 1304，观测区间 1024 - 1304，11 个样本，取值集中（一致性 94%）
- 高发问题（140/11 个样本）：Steps较低可能导致细节不足
