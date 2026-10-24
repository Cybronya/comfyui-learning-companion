---
name: image_to_image_sampler_clip_unet_119
type: Image To Image
frequency: 4
level: moderate
coverage: 0.8625
common_nodes: [CLIPTextEncode, Image Comparer (rgthree), KSampler, LoadImage, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/WAN2.1图生图_1949144078248812546.json, 图片生成/图生图/Wan2.1图生图（洗图增强真实感）_1949495116142125057.json, 图片生成/图生图/Z-image 图生图工作流_2046980983332806658.json, 图片生成/文生图/Flux-Krea图生图（降低AI感的大模型）_1950930994167742465.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_119

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/WAN2.1图生图_1949144078248812546.json、图片生成/图生图/Wan2.1图生图（洗图增强真实感）_1949495116142125057.json、图片生成/图生图/Z-image 图生图工作流_2046980983332806658.json、图片生成/文生图/Flux-Krea图生图（降低AI感的大模型）_1950930994167742465.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `RH_Captioner` —— 3/4 个有
- `FilmGrain` —— 2/4 个有
- `ImageScale` —— 2/4 个有
- `easy cleanGpuUsed` —— 2/4 个有
- `ConditioningZeroOut` —— 1/4 个有
- `DualCLIPLoader` —— 1/4 个有
- `LayerColor: Brightness & Contrast` —— 1/4 个有
- `LoraLoader` —— 1/4 个有
- `Primitive float [Crystools]` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 4 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 4 | 81% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 0.4 | 0.1 - 0.5 | 4 | 53% |
| LoRA 模型强度 | 0.45 | - | 1 | 100% |
| LoRA 文本强度 | 0.45 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，4 个样本，取值集中（一致性 81%）
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 0.4，观测区间 0.1 - 0.5，4 个样本
