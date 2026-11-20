---
name: unknown_workflow_inpaint_sampler_clip_85
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.693667
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GrowMask, Image Blend by Mask, Image Blending Mode, Image Filter Adjustments, Image Levels Adjustment, ImageBlur, ImageCompositeMasked, ImageInvert, ImageRemoveBackground+, ImageResizeKJv2, ImpactGaussianBlurMask, InpaintModelConditioning, KSampler, LBMSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadLBMModel, MaskToImage, PreviewImage, SaveImage, TransparentBGSession+, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/云影Ai_relighting人物摄影打光工作流_2080641269767958529.json, 平台全量/CG迷-LBM_relighting人物摄影打光工作流_1926977738828075010.json, 平台全量/阿清的真实感提升打光工作流_2089219806254952449.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_85

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/云影Ai_relighting人物摄影打光工作流_2080641269767958529.json、平台全量/CG迷-LBM_relighting人物摄影打光工作流_1926977738828075010.json、平台全量/阿清的真实感提升打光工作流_2089219806254952449.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GrowMask`
- `Image Blend by Mask`
- `Image Blending Mode`
- `Image Filter Adjustments`
- `Image Levels Adjustment`
- `ImageBlur`
- `ImageCompositeMasked`
- `ImageInvert`
- `ImageRemoveBackground+`
- `ImageResizeKJv2`
- `ImpactGaussianBlurMask`
- `InpaintModelConditioning`
- `KSampler`
- `LBMSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadLBMModel`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`
- `TransparentBGSession+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
