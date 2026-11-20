---
name: image_to_image_controlnet_sampler_clip_14
type: Image To Image
frequency: 4
level: strong
coverage: 0.87075
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningClamp, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio, LoadImage, ModelPatchLoader, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Zimage-线稿-控制出图_2042821461584384001.json, 平台全量/Zimage姿势控制出图_2020069586825121794.json, 平台全量/Zimage姿势控制反推提示词出图_2020063583417147394.json, 平台全量/Zimage高清tile放大_2020409872084377601.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_sampler_clip_14

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Zimage-线稿-控制出图_2042821461584384001.json、平台全量/Zimage姿势控制出图_2020069586825121794.json、平台全量/Zimage姿势控制反推提示词出图_2020063583417147394.json、平台全量/Zimage高清tile放大_2020409872084377601.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningClamp`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio`
- `LoadImage`
- `ModelPatchLoader`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 2/4 个有
- `AnimeLineArtPreprocessor` —— 1/4 个有
- `PIP_图像联结` —— 1/4 个有
- `PreviewAny` —— 1/4 个有
- `RH_Captioner` —— 1/4 个有
- `TilePreprocessor` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | 8 - 9 | 4 | 94% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 0.3 - 1 | 4 | 63% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，观测区间 8 - 9，4 个样本，取值集中（一致性 94%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，4 个样本
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
