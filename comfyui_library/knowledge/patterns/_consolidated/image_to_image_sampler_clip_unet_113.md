---
name: image_to_image_sampler_clip_unet_113
type: Image To Image
frequency: 4
level: strong
coverage: 0.95725
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, ImageScaleToTotalPixels, KSampler, LoadImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2-Klein-9b图像编辑工作流_2022269747924049922.json, 图片生成/图生图/Flux2-Klein-图片编辑 (单图)_2028867735513468929.json, 图片生成/图生图/Flux2_Klein_9B印花提取V8_2104445424978452481.json, 图片生成/图生图/Klein-单图编辑_2064942255387013122.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_113

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux2-Klein-9b图像编辑工作流_2022269747924049922.json、图片生成/图生图/Flux2-Klein-图片编辑 (单图)_2028867735513468929.json、图片生成/图生图/Flux2_Klein_9B印花提取V8_2104445424978452481.json、图片生成/图生图/Klein-单图编辑_2064942255387013122.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 3/4 个有
- `Image Comparer (rgthree)` —— 3/4 个有
- `LoraLoader` —— 3/4 个有
- `Flux2KleinEnhancer` —— 1/4 个有
- `FluxResolutionNode` —— 1/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `RTXVideoSuperResolution` —— 1/4 个有
- `Seed (rgthree)` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5 | 4 - 6 | 4 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5，观测区间 4 - 6，4 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
