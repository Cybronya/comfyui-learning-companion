---
name: image_to_image_lora_sampler_unet_54
type: Image To Image
frequency: 10
level: moderate
coverage: 0.8081
common_nodes: [CFGNorm, CLIPLoader, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen edit 图像编辑_1970750998853677057.json, 图片生成/图生图/Qwen-Edit-2509 超多角度切换 LoRA_1990400053313507330.json, 图片生成/图生图/Qwen-Edit-2509-多角度切换_1990328940835336193.json, 图片生成/图生图/Qwen-Edit-2509-白底图转模特展示_1989690060327014401.json, 图片生成/图生图/Qwen-Edit-一键角度编辑器_1990319553639051265.json, 图片生成/图生图/Qwen-Image-Edit-InScene-Annotate_1984575376770940930.json, 图片生成/图生图/Qwen-Image-Edit-InScene_1984569830982500353.json, 图片生成/图生图/Qwen-Image-Edit-InStyle_1984563047832436738.json, 图片生成/图生图/Qwen-Image-Edit-InSubject_1984566159439708162.json, 图片生成/图生图/Qwen-Image-Edit-多角度_1984584360991014913.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_54

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen edit 图像编辑_1970750998853677057.json、图片生成/图生图/Qwen-Edit-2509 超多角度切换 LoRA_1990400053313507330.json、图片生成/图生图/Qwen-Edit-2509-多角度切换_1990328940835336193.json、图片生成/图生图/Qwen-Edit-2509-白底图转模特展示_1989690060327014401.json、图片生成/图生图/Qwen-Edit-一键角度编辑器_1990319553639051265.json…）

- **类型**：Image To Image
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `TextEncodeQwenImageEditPlus` —— 9/10 个有
- `ImageScaleToTotalPixels` —— 8/10 个有
- `PreviewImage` —— 8/10 个有
- `easy imageSize` —— 7/10 个有
- `PrimitiveStringMultiline` —— 6/10 个有
- `CameraControlPromptNode` —— 1/10 个有
- `Display Any (rgthree)` —— 1/10 个有
- `ImageResizeKJv2` —— 1/10 个有
- `JjkText` —— 1/10 个有
- `LoadImageFromUrl` —— 1/10 个有
- `Note Plus (mtb)` —— 1/10 个有
- `TextEncodeQwenImageEdit` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 10 | 61% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 10 | 61% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（21/10 个样本）：Steps较低可能导致细节不足
