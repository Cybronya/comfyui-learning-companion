---
name: image_to_image_lora_sampler_unet_36
type: Image To Image
frequency: 13
level: moderate
coverage: 0.965
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen万能图片编辑图生图全能图片V1平替_2005434060799442945.json, 图片生成/图生图/三张图就编辑 ICEdit_LoRA_2015404467323146242.json, 图片生成/图生图/主体抠图与黑白蒙版生成_2052234697593368577.json, 图片生成/图生图/主体抠图与黑白蒙版生成_2061622051689033729.json, 图片生成/图生图/人物转3D手办Qwen-Image-Edit图像编辑_1998633582274994178.json, 图片生成/图生图/人物转3D手办Qwen-Image-Edit图像编辑_2013877879095955458.json, 图片生成/图生图/人物转3D手办Qwen-Image-Edit图像编辑_2070417457063485442.json, 图片生成/图生图/千问-3D转绘_1995785923046543362.json, 图片生成/图生图/千问图片编辑工作流_1986050948818751490.json, 图片生成/图生图/完美解决Qwen-edit-2511-图像质量下降、位移及色差_2004895752210055169.json, 图片生成/图生图/超强2D转3D-Qwen-Image-Edit_2020677263766855681.json, 图片生成/文生图/3D转绘-Qwen-Image-Edit图像编辑-Comfy官方_1986720327151595522.json, 图片生成/文生图/3D转绘-Qwen-Image-Edit图像编辑-Comfy官方_1986721390671949825.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_36

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/qwen万能图片编辑图生图全能图片V1平替_2005434060799442945.json、图片生成/图生图/三张图就编辑 ICEdit_LoRA_2015404467323146242.json、图片生成/图生图/主体抠图与黑白蒙版生成_2052234697593368577.json、图片生成/图生图/主体抠图与黑白蒙版生成_2061622051689033729.json、图片生成/图生图/人物转3D手办Qwen-Image-Edit图像编辑_1998633582274994178.json…）

- **类型**：Image To Image
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 12/13 个有
- `ConditioningZeroOut` —— 11/13 个有
- `ModelSamplingAuraFlow` —— 11/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/13 个有
- `Text Multiline` —— 8/13 个有
- `ImageStitch` —— 6/13 个有
- `FluxKontextImageScale` —— 5/13 个有
- `Image Comparer (rgthree)` —— 5/13 个有
- `DuckHideNode` —— 1/13 个有
- `InpaintCrop` —— 1/13 个有
- `InpaintStitch` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `YANC.MultilineString` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 25 | 13 | 46% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 13 | 59% |
| 采样算法 | euler | - | 13 | 85% |
| 调度器 | simple | - | 13 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 25，13 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，13 个样本
- 采样算法 最常用 euler，13 个样本，一致性 85%
- 调度器 最常用 simple，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
