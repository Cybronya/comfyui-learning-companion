---
name: image_to_image_lora_sampler_unet_68
type: Image To Image
frequency: 9
level: moderate
coverage: 0.784333
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit-多图角度生成器_1990322262794530817.json, 图片生成/图生图/Qwen-Image-Edit-InScene-Annotate_1984575376770940930.json, 图片生成/图生图/Qwen-Image-Edit-InScene_1984569830982500353.json, 图片生成/图生图/Qwen-Image-Edit-InStyle_1984563047832436738.json, 图片生成/图生图/Qwen-Image-Edit-InSubject_1984566159439708162.json, 图片生成/图生图/Qwen-Image-Edit-多角度_1984584360991014913.json, 图片生成/图生图/Qwen-image-Edit图像编辑用法【基础流】_1958688533957525505.json, 图片生成/图生图/Qwen-多角度切换_1994398890684190721.json, 图片生成/图生图/图像多角度转换——一张角色图生成多角度视角_1984598564712103937.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_68

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit-多图角度生成器_1990322262794530817.json、图片生成/图生图/Qwen-Image-Edit-InScene-Annotate_1984575376770940930.json、图片生成/图生图/Qwen-Image-Edit-InScene_1984569830982500353.json、图片生成/图生图/Qwen-Image-Edit-InStyle_1984563047832436738.json、图片生成/图生图/Qwen-Image-Edit-InSubject_1984566159439708162.json…）

- **类型**：Image To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
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
- `TextEncodeQwenImageEditPlus` —— 8/9 个有
- `easy imageSize` —— 8/9 个有
- `Image Comparer (rgthree)` —— 7/9 个有
- `PreviewImage` —— 7/9 个有
- `PrimitiveStringMultiline` —— 7/9 个有
- `ShowText|pysssss` —— 2/9 个有
- `Text Multiline` —— 2/9 个有
- `easy promptLine` —— 2/9 个有
- `Any Switch (rgthree)` —— 1/9 个有
- `Anything Everywhere3` —— 1/9 个有
- `ImageConcatFromBatch` —— 1/9 个有
- `ImageListToImageBatch` —— 1/9 个有
- `TextEncodeQwenImageEditEnhanced` —— 1/9 个有
- `VHS_SelectImages` —— 1/9 个有
- `easy imageListToImageBatch` —— 1/9 个有
- `easy promptList` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 20 | 9 | 60% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 9 | 60% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（8/9 个样本）：Steps较低可能导致细节不足
