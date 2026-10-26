---
name: unknown_workflow_sampler_unet_vae_175
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.8785
common_nodes: [CLIPLoader, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PainterFluxImageEdit, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Klein-9B-图像各种风格转换_2022484805551661058.json, 图片生成/图生图/Klein-9B-图像风格、灯光迁移（lora）_2065039831608156161.json, 图片生成/图生图/Klein-9B-点状插图风格_2043666470843981826.json, 图片生成/图生图/Klein-9b VS Klein-9B-KV-图像编辑对比_2032988026435018754.json, 图片生成/图生图/Klein-BFS-黑兽换脸_2048205881640226818.json, 图片生成/图生图/Klien-9B-图像转电影风格图像_2043669674784727041.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_175

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Klein-9B-图像各种风格转换_2022484805551661058.json、图片生成/图生图/Klein-9B-图像风格、灯光迁移（lora）_2065039831608156161.json、图片生成/图生图/Klein-9B-点状插图风格_2043666470843981826.json、图片生成/图生图/Klein-9b VS Klein-9B-KV-图像编辑对比_2032988026435018754.json、图片生成/图生图/Klein-BFS-黑兽换脸_2048205881640226818.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PainterFluxImageEdit`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 4/6 个有
- `Image Comparer (rgthree)` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `PreviewImage` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `AddLabel` —— 1/6 个有
- `CropFace` —— 1/6 个有
- `ImageConcatMulti` —— 1/6 个有
- `PrimitiveFloat` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 5 - 10 | 6 | 79% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 5 - 10，6 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
