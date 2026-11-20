---
name: unknown_workflow_inpaint_sampler_clip_59
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.75
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FeatherMask, FluxGuidance, GetNode, ImageConcanate, ImageCrop, ImageToMask, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerUtility: ColorPicker, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, PreviewImage, SaveImage, SetNode, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/Flii+redux 万物迁移工作流_1921718199556177921.json, 图片生成/图生图/万物洗稿工作流_1920707930499518465.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_59

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Flii+redux 万物迁移工作流_1921718199556177921.json、图片生成/图生图/万物洗稿工作流_1920707930499518465.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
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
- `BiRefNet_ModelLoader_Zho` —— 1/2 个有
- `BiRefNet_Zho` —— 1/2 个有
- `InspyrenetRembg` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
