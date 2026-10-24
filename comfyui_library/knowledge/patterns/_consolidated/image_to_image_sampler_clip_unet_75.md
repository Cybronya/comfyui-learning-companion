---
name: image_to_image_sampler_clip_unet_75
type: Image To Image
frequency: 6
level: weak
coverage: 0.796
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/YJ-APP-z-image-图生图_2031308137252265985.json, 图片生成/图生图/Z-Image-De洗图图生图_1997877980846260226.json, 图片生成/图生图/Z-image Base 洗图_2016353054697725954.json, 图片生成/图生图/Z-image+千问VL反推图生图洗图增强真实感_1993893012516306946.json, 图片生成/图生图/Z-image图生图-真实感洗图_1996077315346087937.json, 图片生成/图生图/Z-image洗图图生图_1995800646467072001.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_75

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/YJ-APP-z-image-图生图_2031308137252265985.json、图片生成/图生图/Z-Image-De洗图图生图_1997877980846260226.json、图片生成/图生图/Z-image Base 洗图_2016353054697725954.json、图片生成/图生图/Z-image+千问VL反推图生图洗图增强真实感_1993893012516306946.json、图片生成/图生图/Z-image图生图-真实感洗图_1996077315346087937.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 5/6 个有
- `ConditioningZeroOut` —— 5/6 个有
- `ShowText|pysssss` —— 4/6 个有
- `PrimitiveInt` —— 3/6 个有
- `Float` —— 2/6 个有
- `Image Comparer (rgthree)` —— 1/6 个有
- `ImageScaleToTotalPixels` —— 1/6 个有
- `Int` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `RH_Captioner` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 25 | 6 | 57% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 6 | 57% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 0.4 | 0.3 - 1 | 6 | 47% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 25，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.3 - 1，6 个样本，取值分散，一致性仅 47%
