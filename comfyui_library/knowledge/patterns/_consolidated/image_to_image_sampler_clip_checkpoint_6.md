---
name: image_to_image_sampler_clip_checkpoint_6
type: Image To Image
frequency: 4
level: moderate
coverage: 0.90225
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/IL局部重绘-sfw_2020811288871444481.json, 图片生成/图生图/一键真人转动漫_1925339421200293890.json, 图片生成/图生图/一键转绘动漫二次元女生插画_1925336007384965121.json, 图片生成/图生图/一键转绘动漫绘本女生插画_1925328701666340865.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_checkpoint_6

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/IL局部重绘-sfw_2020811288871444481.json、图片生成/图生图/一键真人转动漫_1925339421200293890.json、图片生成/图生图/一键转绘动漫二次元女生插画_1925336007384965121.json、图片生成/图生图/一键转绘动漫绘本女生插画_1925328701666340865.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 3/4 个有
- `ImageConcanate` —— 2/4 个有
- `CLIPSetLastLayer` —— 1/4 个有
- `Image Compare (mtb)` —— 1/4 个有
- `ImageBlend` —— 1/4 个有
- `InpaintModelConditioning` —— 1/4 个有
- `Latent Noise Injection` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 28 | 4 | 84% |
| Prompt 约束强度(CFG) | 8 | 6 - 8 | 4 | 88% |
| 采样算法 | euler_ancestral | - | 4 | 100% |
| 调度器 | normal | - | 4 | 75% |
| 重绘幅度 | 0.3 | 0.3 - 0.5 | 4 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 28，4 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 8，4 个样本，取值集中（一致性 88%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 75%
- 重绘幅度 中位数 0.3，观测区间 0.3 - 0.5，4 个样本
