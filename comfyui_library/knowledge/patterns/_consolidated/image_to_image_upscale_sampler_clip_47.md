---
name: image_to_image_upscale_sampler_clip_47
type: Image To Image
frequency: 3
level: strong
coverage: 0.961333
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ImageUpscaleWithModel, KSampler, LoadImage, SaveImage, UpscaleModelLoader, VAEDecode, VAEEncode]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/▶XL 2.5D 真人转动漫_2026303786460909569.json, 图片生成/图生图/▶真人转动漫流_2058933901715918849.json, 平台全量/图片改4k_1990408144151076865.json]
source: knowledge_consolidation
---

# image_to_image_upscale_sampler_clip_47

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/▶XL 2.5D 真人转动漫_2026303786460909569.json、图片生成/图生图/▶真人转动漫流_2058933901715918849.json、平台全量/图片改4k_1990408144151076865.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 2/3 个有
- `CR Text Concatenate` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `PreviewImage` —— 1/3 个有
- `WD14Tagger|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 25 | 3 | 90% |
| Prompt 约束强度(CFG) | 6 | 4.59 - 6 | 3 | 88% |
| 采样算法 | euler_ancestral | - | 3 | 67% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 0.4 | 0.4 - 0.5 | 3 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 25，3 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 4.59 - 6，3 个样本，取值集中（一致性 88%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 67%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.5，3 个样本，取值集中（一致性 89%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
