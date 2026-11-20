---
name: unknown_workflow_inpaint_sampler_clip_79
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.757667
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FeatherMask, FluxGuidance, GetNode, ImageConcanate, ImageCrop, ImageToMask, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerUtility: ColorPicker, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, PreviewImage, SaveImage, SetNode, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/Flii+redux 万物迁移工作流_1921718199556177921.json, 图片生成/图生图/万物洗稿工作流_1920707930499518465.json, 平台全量/万物洗稿工作流_1921416014062616578.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_79

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flii+redux 万物迁移工作流_1921718199556177921.json、图片生成/图生图/万物洗稿工作流_1920707930499518465.json、平台全量/万物洗稿工作流_1921416014062616578.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `FeatherMask`
- `FluxGuidance`
- `GetNode`
- `ImageConcanate`
- `ImageCrop`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `InspyrenetRembg` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `BiRefNet_ModelLoader_Zho` —— 1/3 个有
- `BiRefNet_Zho` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
