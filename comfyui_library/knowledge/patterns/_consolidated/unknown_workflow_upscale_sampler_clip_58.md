---
name: unknown_workflow_upscale_sampler_clip_58
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.919333
common_nodes: [CLIPTextEncode, ConditioningZeroOut, Image Comparer (rgthree), ImageUpscaleWithModel, KSampler, LoadImage, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UpscaleModelLoader, VAEDecodeTiled, VAEEncodeTiled, VAELoader, easy imageBatchToImageList, easy imageListToImageBatch]
problems: [发现KSampler但没有VAEDecode, Steps较低可能导致细节不足]
missing: []
members: [平台全量/Z-Image-Turbo-TTP高清放大（速度真快）_1994203448077991938.json, 平台全量/Z-image图片放大_2018196096618598401.json, 平台全量/flux-TTP高清放大工作流_1936780216553361410.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_58

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/Z-Image-Turbo-TTP高清放大（速度真快）_1994203448077991938.json、平台全量/Z-image图片放大_2018196096618598401.json、平台全量/flux-TTP高清放大工作流_1936780216553361410.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Image Comparer (rgthree)`
- `ImageUpscaleWithModel`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UpscaleModelLoader`
- `VAEDecodeTiled`
- `VAEEncodeTiled`
- `VAELoader`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `DualCLIPLoader` —— 1/3 个有
- `FluxGuidance` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `ModelSamplingAuraFlow` —— 1/3 个有
- `ModelSamplingFlux` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `UnetLoaderGGUF` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 25 | 3 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 0.25 | 0.25 - 0.3 | 3 | 91% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 3/3 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 25，3 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 0.25，观测区间 0.25 - 0.3，3 个样本，取值集中（一致性 91%）
- 高发问题（3/3 个样本）：发现KSampler但没有VAEDecode
