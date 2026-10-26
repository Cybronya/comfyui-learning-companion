---
name: unknown_workflow_inpaint_sampler_clip_47
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.87
common_nodes: [CLIPTextEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FluxGuidance, Image Comparer (rgthree), ImageConcanate, ImageToMask, InpaintModelConditioning, KSampler, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, PreviewImage, ReduxAdvanced, SaveImage, StyleModelLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/万物迁移升级版【OneReward】_1944223056828989442.json, 图片生成/图生图/背面工作流_1928736107893264385.json, 图片生成/图生图/连衣裙_api_1935916299509751809.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_47

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/万物迁移升级版【OneReward】_1944223056828989442.json、图片生成/图生图/背面工作流_1928736107893264385.json、图片生成/图生图/连衣裙_api_1935916299509751809.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `InspyrenetRembg` —— 2/3 个有
- `NunchakuFluxDiTLoader` —— 2/3 个有
- `easy imageInsetCrop` —— 2/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `ImageCrop` —— 1/3 个有
- `LayerMask: MaskGrow` —— 1/3 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/3 个有
- `LayerUtility: ImageScaleRestore V2` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `Mask Fill Holes` —— 1/3 个有
- `MaskPreview` —— 1/3 个有
- `NunchakuFluxLoraLoader` —— 1/3 个有
- `UNETLoader` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 35 | 3 | 52% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 35，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
