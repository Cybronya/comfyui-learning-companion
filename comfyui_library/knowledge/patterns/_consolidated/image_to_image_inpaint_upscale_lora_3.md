---
name: image_to_image_inpaint_upscale_lora_3
type: Image To Image
frequency: 4
level: strong
coverage: 0.86075
common_nodes: [CheckpointLoaderSimple, CreateShapeMask, GrowMaskWithBlur, ImageBlend, ImageConcanate, ImagePadForOutpaint, ImageResizeKJv2, ImageScaleToTotalPixels, InpaintModelConditioning, KSampler, LoadImage, LoraLoaderModelOnly, MaskToImage, SaveImage, TextEncodeQwenImageEditPlus, VAEDecode, VAEEncode, WujiCleaner, WujiSampler, WujiUpscaler]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/（漫剧）360VR全景图+分镜图_2046989246132654081.json, 图片生成/文生图/360VR全景HDR图片生成 文生图+图生图   Qwen-image2511+自动扩写专用提示词_2047159797614649345.json, 图片生成/文生图/360VR全景Qwen-image2511+自动扩写专用提示词_2044278146651922434.json, 图片生成/文生图/360VR全景Qwen-image2511+自动扩写专用提示词_2044735074934988801.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_upscale_lora_3

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/（漫剧）360VR全景图+分镜图_2046989246132654081.json、图片生成/文生图/360VR全景HDR图片生成 文生图+图生图   Qwen-image2511+自动扩写专用提示词_2047159797614649345.json、图片生成/文生图/360VR全景Qwen-image2511+自动扩写专用提示词_2044278146651922434.json、图片生成/文生图/360VR全景Qwen-image2511+自动扩写专用提示词_2044735074934988801.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `CreateShapeMask`
- `GrowMaskWithBlur`
- `ImageBlend`
- `ImageConcanate`
- `ImagePadForOutpaint`
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `VAEDecode`
- `VAEEncode`
- `WujiCleaner`
- `WujiSampler`
- `WujiUpscaler`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 3/4 个有
- `Fast Groups Muter (rgthree)` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `RHHiddenNodes` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `Wuji360Panorama` —— 3/4 个有
- `WujiEditor` —— 3/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `SetNode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
