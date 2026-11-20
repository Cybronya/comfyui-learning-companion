---
name: unknown_workflow_inpaint_sampler_clip_48
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.889333
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageToMask, InpaintModelConditioning, KSampler, LoadImage, MaskToImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/万物迁移最佳版（可以迁移，服装，物品。电商产品，家居）_1910728197359529985.json, 图片生成/图生图/产品生成背景图V4，可带遮挡，带光影融合，效果出色_1899427116880973826.json, 图片生成/图生图/产品迁移重绘工作流_万物迁移_1936402456697819137.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_48

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/万物迁移最佳版（可以迁移，服装，物品。电商产品，家居）_1910728197359529985.json、图片生成/图生图/产品生成背景图V4，可带遮挡，带光影融合，效果出色_1899427116880973826.json、图片生成/图生图/产品迁移重绘工作流_万物迁移_1936402456697819137.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageCrop+` —— 2/3 个有
- `CR Latent Batch Size` —— 1/3 个有
- `Get resolution [Crystools]` —— 1/3 个有
- `Image Blank` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `ImageScale` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `easy getNode` —— 1/3 个有
- `easy setNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 3 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
