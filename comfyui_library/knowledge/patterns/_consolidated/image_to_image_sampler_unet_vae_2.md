---
name: image_to_image_sampler_unet_vae_2
type: Image To Image
frequency: 5
level: strong
coverage: 0.8756
common_nodes: [CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, PrimitiveStringMultiline, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/2096603719419912194.json, 图片生成/图生图/2096603788789510146.json, 图片生成/图生图/2096613161687408642.json, 图片生成/图生图/2098372807368470529.json, 图片生成/图生图/2103056580613857281.json]
source: knowledge_consolidation
---

# image_to_image_sampler_unet_vae_2

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2096603719419912194.json、图片生成/图生图/2096603788789510146.json、图片生成/图生图/2096613161687408642.json、图片生成/图生图/2098372807368470529.json、图片生成/图生图/2103056580613857281.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 4/5 个有
- `ComfyMathExpression` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `ImagePadForOutpaint` —— 1/5 个有
- `PrimitiveInt` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 24 | 24 - 24 | 5 | 100% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 2.5 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 24，观测区间 24 - 24，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 2.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
