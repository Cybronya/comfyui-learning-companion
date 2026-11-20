---
name: unknown_workflow_inpaint_sampler_clip_65
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.88575
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageToMask, InpaintModelConditioning, KSampler, LoadImage, MaskToImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/万物迁移最佳版（可以迁移，服装，物品。电商产品，家居）_1910728197359529985.json, 图片生成/图生图/产品生成背景图V4，可带遮挡，带光影融合，效果出色_1899427116880973826.json, 图片生成/图生图/产品迁移重绘工作流_万物迁移_1936402456697819137.json, 平台全量/【V2】FLUX_Fill + ACE++ + Redux _ 万物迁移 _ 目前最能打组合_1950798305649426434.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_65

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/万物迁移最佳版（可以迁移，服装，物品。电商产品，家居）_1910728197359529985.json、图片生成/图生图/产品生成背景图V4，可带遮挡，带光影融合，效果出色_1899427116880973826.json、图片生成/图生图/产品迁移重绘工作流_万物迁移_1936402456697819137.json、平台全量/【V2】FLUX_Fill + ACE++ + Redux _ 万物迁移 _ 目前最能打组合_1950798305649426434.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
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
- `EmptyImage` —— 3/4 个有
- `ImageCrop+` —— 3/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `ImageResize+` —— 2/4 个有
- `Label (rgthree)` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `CR Latent Batch Size` —— 1/4 个有
- `Get resolution [Crystools]` —— 1/4 个有
- `Image Blank` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `LayerMask: MaskPreview` —— 1/4 个有
- `LayerMask: SegmentAnythingUltra V2` —— 1/4 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有
- `easy getNode` —— 1/4 个有
- `easy setNode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 20 - 30 | 4 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 30，观测区间 20 - 30，4 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
