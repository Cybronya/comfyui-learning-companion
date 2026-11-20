---
name: image_to_image_lora_sampler_unet_41
type: Image To Image
frequency: 14
level: moderate
coverage: 0.919
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问三图编辑_2015629342180642817.json, 图片生成/图生图/千问图像编辑2511  单图编辑_2003720550470066177.json, 图片生成/图生图/千问图像编辑2511  双图编辑_2003696896738770946.json, 图片生成/图生图/千问多角度调整 拍摄角度切换_2009814695871516673.json, 图片生成/图生图/双图编辑Qwen edit 2511 千问改图_2013884239669895170.json, 图片生成/图生图/商品照片生成模特图-电商专用-image_qwen_image_edit_2509_1988199854688133122.json, 图片生成/图生图/图片转色块 Qwen Image Edit 2511_2052014658105692161.json, 图片生成/图生图/图片镜头切换_2016419512840626178.json, 图片生成/图生图/多图万能处理（QWEN EDIT 2511）_2015346327189725186.json, 图片生成/图生图/多角度_2038826670580310017.json, 图片生成/图生图/多角度工作流_2038655919210369025.json, 图片生成/图生图/手动控制镜头3d camera qwen 2511人物场景多角度镜头控制镜头选择10秒出图_2011705037017325569.json, 图片生成/图生图/手动控制镜头3d camera qwen 2511人物场景多角度镜头控制镜头选择（柯基大佬版）_2010169381770240002.json, 图片生成/图生图/手动控制镜头3d camera qwen 2511人物场景多角度镜头控制镜头选择（柯基大佬版）_2037411672662478850.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_41

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/千问三图编辑_2015629342180642817.json、图片生成/图生图/千问图像编辑2511  单图编辑_2003720550470066177.json、图片生成/图生图/千问图像编辑2511  双图编辑_2003696896738770946.json、图片生成/图生图/千问多角度调整 拍摄角度切换_2009814695871516673.json、图片生成/图生图/双图编辑Qwen edit 2511 千问改图_2013884239669895170.json…）

- **类型**：Image To Image
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
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
- `FluxKontextMultiReferenceLatentMethod` —— 13/14 个有
- `EmptySD3LatentImage` —— 12/14 个有
- `ImageScaleToTotalPixels` —— 9/14 个有
- `QwenMultiangleCameraNode` —— 7/14 个有
- `Int` —— 5/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/14 个有
- `easy showAnything` —— 4/14 个有
- `PreviewImage` —— 3/14 个有
- `TextInput_` —— 3/14 个有
- `ZML_LimitImageAspect` —— 3/14 个有
- `Bookmark (rgthree)` —— 1/14 个有
- `CR Text` —— 1/14 个有
- `KepStringList` —— 1/14 个有
- `MuyeTextEditOutput` —— 1/14 个有
- `TT_img_enc` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4.5 | 4 - 20 | 14 | 34% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 14 | 65% |
| 采样算法 | euler | - | 14 | 100% |
| 调度器 | simple | - | 14 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4.5，观测区间 4 - 20，14 个样本，取值分散，一致性仅 34%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，14 个样本
- 采样算法 最常用 euler，14 个样本，一致性 100%
- 调度器 最常用 simple，14 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（13/14 个样本）：Steps较低可能导致细节不足
