---
name: image_to_image_lora_sampler_unet_60
type: Image To Image
frequency: 9
level: strong
coverage: 0.841778
common_nodes: [CFGNorm, CLIPLoader, FluxKontextImageScale, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/2511多图编辑（4步极速）_2006636022146273282.json, 图片生成/图生图/Comfyui教学第四期-千问编辑模型_2009830377501757442.json, 图片生成/图生图/FireRed-Image-edit1.1 跨次元换装_2029765859891224577.json, 图片生成/图生图/FireRed-Image-edit1.1--单图编辑_2029763824429047809.json, 图片生成/图生图/FireRed-Image-edit1.1--模特换姿势_2029768783438553089.json, 图片生成/图生图/FireRed-Image-edit1.1--模特换脸_2029771574110326786.json, 图片生成/图生图/FireRed-Image-edit1.1--模特换装_2029765744128434177.json, 图片生成/图生图/FireRed-一键换装 自用版_2029920597647564802.json, 图片生成/图生图/小红书FireRed-Image-edit 单图双图多图编辑 换装迁移_2031243779381923842.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_60

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/2511多图编辑（4步极速）_2006636022146273282.json、图片生成/图生图/Comfyui教学第四期-千问编辑模型_2009830377501757442.json、图片生成/图生图/FireRed-Image-edit1.1 跨次元换装_2029765859891224577.json、图片生成/图生图/FireRed-Image-edit1.1--单图编辑_2029763824429047809.json、图片生成/图生图/FireRed-Image-edit1.1--模特换姿势_2029768783438553089.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 7/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/9 个有
- `easy cleanGpuUsed` —— 7/9 个有
- `easy int` —— 7/9 个有
- `CR Prompt Text` —— 6/9 个有
- `Anything Everywhere` —— 1/9 个有
- `CLIPTextEncode` —— 1/9 个有
- `Fast Groups Bypasser (rgthree)` —— 1/9 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/9 个有
- `OpenposePreprocessor` —— 1/9 个有
- `ReferenceLatent` —— 1/9 个有
- `SaveImageWebsocket` —— 1/9 个有
- `Text` —— 1/9 个有
- `VRAM_Debug` —— 1/9 个有
- `easy positive` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 5 - 8 | 9 | 86% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 5 - 8，9 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
