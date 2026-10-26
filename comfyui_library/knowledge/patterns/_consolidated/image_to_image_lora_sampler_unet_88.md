---
name: image_to_image_lora_sampler_unet_88
type: Image To Image
frequency: 7
level: strong
coverage: 0.956286
common_nodes: [CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit-2511图像编辑多合一工作流_2003654587804467201.json, 图片生成/图生图/Qwen-Image-Edit-2509  万能图像编辑 完胜 全能图片V1 2  Pro_1997925023178457089.json, 图片生成/图生图/Qwen-Image-Edit-2511新版图像编辑（单图模式工作流）_2011577913421864962.json, 图片生成/图生图/comfyui图像转钢笔插画_1985699102325448705.json, 图片生成/图生图/image_qwen_image_edit_2509-双图参考+参考色调重打光_2011594156342255617.json, 图片生成/图生图/qwen Edit 2511 单图编辑+修改表情_2059458819733942274.json, 图片生成/图生图/▶千问Qwen漫画本子上色流2_2058936764278075393.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_88

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit-2511图像编辑多合一工作流_2003654587804467201.json、图片生成/图生图/Qwen-Image-Edit-2509  万能图像编辑 完胜 全能图片V1 2  Pro_1997925023178457089.json、图片生成/图生图/Qwen-Image-Edit-2511新版图像编辑（单图模式工作流）_2011577913421864962.json、图片生成/图生图/comfyui图像转钢笔插画_1985699102325448705.json、图片生成/图生图/image_qwen_image_edit_2509-双图参考+参考色调重打光_2011594156342255617.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `ImageScaleToTotalPixels`
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
- `CFGNorm` —— 6/7 个有
- `ConditioningZeroOut` —— 3/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `CLIPLoaderGGUF` —— 1/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/7 个有
- `InpaintModelConditioning` —— 1/7 个有
- `LayerUtility: ImageMaskScaleAs` —— 1/7 个有
- `MaskFillHoles` —— 1/7 个有
- `PixelSmileConditioning` —— 1/7 个有
- `Textbox` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 10 | 7 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 10，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（9/7 个样本）：Steps较低可能导致细节不足
