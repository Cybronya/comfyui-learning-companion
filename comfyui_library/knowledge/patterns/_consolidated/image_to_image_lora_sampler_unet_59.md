---
name: image_to_image_lora_sampler_unet_59
type: Image To Image
frequency: 10
level: moderate
coverage: 0.9359
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问三图编辑_2015629342180642817.json, 图片生成/图生图/千问图像编辑2511  单图编辑_2003720550470066177.json, 图片生成/图生图/千问图像编辑2511  双图编辑_2003696896738770946.json, 图片生成/图生图/千问多角度调整 拍摄角度切换_2009814695871516673.json, 图片生成/图生图/双图编辑Qwen edit 2511 千问改图_2013884239669895170.json, 图片生成/图生图/商品照片生成模特图-电商专用-image_qwen_image_edit_2509_1988199854688133122.json, 图片生成/图生图/图像多角度编辑手动控制更精准_2017089045016350722.json, 图片生成/图生图/多角度工作流_2038655919210369025.json, 图片生成/图生图/自由调节镜头视角无极选择器Qwen2511+image+edit_2034454761310785538.json, 图片生成/文生图/Qwen2511多角度可视化控制流可调节_2010509977156329474.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_59

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/千问三图编辑_2015629342180642817.json、图片生成/图生图/千问图像编辑2511  单图编辑_2003720550470066177.json、图片生成/图生图/千问图像编辑2511  双图编辑_2003696896738770946.json、图片生成/图生图/千问多角度调整 拍摄角度切换_2009814695871516673.json、图片生成/图生图/双图编辑Qwen edit 2511 千问改图_2013884239669895170.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 10 个 workflow 都包含：
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
- `FluxKontextMultiReferenceLatentMethod` —— 9/10 个有
- `EmptySD3LatentImage` —— 8/10 个有
- `ImageScaleToTotalPixels` —— 5/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/10 个有
- `QwenMultiangleCameraNode` —— 5/10 个有
- `Int` —— 4/10 个有
- `TextInput_` —— 3/10 个有
- `ZML_LimitImageAspect` —— 3/10 个有
- `easy showAnything` —— 3/10 个有
- `Fast Groups Bypasser (rgthree)` —— 2/10 个有
- `KepStringList` —— 2/10 个有
- `easy promptList` —— 2/10 个有
- `MuyeTextEditOutput` —— 1/10 个有
- `RH_Nano_Banana2_Image2Image` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 20 | 10 | 25% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 10 | 61% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 90% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 20，10 个样本，取值分散，一致性仅 25%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 90%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（9/10 个样本）：Steps较低可能导致细节不足
