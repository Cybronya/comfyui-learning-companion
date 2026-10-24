---
name: image_to_image_lora_sampler_unet_58
type: Image To Image
frequency: 10
level: strong
coverage: 0.8536
common_nodes: [CFGNorm, CLIPLoader, FluxKontextMultiReferenceLatentMethod, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-2511图像编辑_2013521690571051010.json, 图片生成/图生图/Qwen-Edit-2511 单图、多图编辑工作流_2091504533078888449.json, 图片生成/图生图/Qwen-Edit-2511 溶图打光工作流_2091511848628740097.json, 图片生成/图生图/Qwen-Edit-2511_单图、多图编辑工作流_2096512805334769666.json, 图片生成/图生图/Qwen-Edit-2511_单图、多图编辑工作流_2096870533769027586.json, 图片生成/图生图/Qwen-image-edit-2511图像编辑（单图、双图、三图）_2025752704462626817.json, 图片生成/图生图/QwenEdit2511多图编辑工作流_2062019518045708289.json, 图片生成/图生图/Qwen_Edit_2511 多图编辑工作流_2049747436729536513.json, 图片生成/图生图/Qwen_Edit_2511 零偏移多图编辑工作流_2019645832496160769.json, 图片生成/图生图/Qwen_Edit_2511-无偏移增强版单图编辑工作流_2005187774271680514.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_58

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen-2511图像编辑_2013521690571051010.json、图片生成/图生图/Qwen-Edit-2511 单图、多图编辑工作流_2091504533078888449.json、图片生成/图生图/Qwen-Edit-2511 溶图打光工作流_2091511848628740097.json、图片生成/图生图/Qwen-Edit-2511_单图、多图编辑工作流_2096512805334769666.json、图片生成/图生图/Qwen-Edit-2511_单图、多图编辑工作流_2096870533769027586.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `FluxKontextMultiReferenceLatentMethod`
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
- `FluxKontextImageScale` —— 9/10 个有
- `Image Comparer (rgthree)` —— 9/10 个有
- `PreviewImage` —— 9/10 个有
- `EmptySD3LatentImage` —— 4/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `CR Prompt Text` —— 1/10 个有
- `EmptyImage` —— 1/10 个有
- `Fast Bypasser (rgthree)` —— 1/10 个有
- `GetImageSize` —— 1/10 个有
- `GetImageSize+` —— 1/10 个有
- `GetImageSizeAndCount` —— 1/10 个有
- `ImageCompositeMasked` —— 1/10 个有
- `ImageStitch` —— 1/10 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/10 个有
- `OlmDragCrop` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 5 - 8 | 10 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 5 - 8，10 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（14/10 个样本）：Steps较低可能导致细节不足
