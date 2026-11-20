---
name: unknown_workflow_inpaint_sampler_clip_69
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7855
common_nodes: [BaiduTranslateNode, CLIPTextEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageCrop+, ImageToMask, ImpactInt, InpaintCrop, InpaintModelConditioning, InpaintStitch, InspyrenetRembg, KSampler, LayerMask: SegmentAnythingUltra V2, LayerUtility: GetImageSize, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, MaskToImage, Parabolize, PreviewImage, ReduxAdvanced, SaveImage, SetNode, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/【精准一键换衣】 FLUX模特人物换装_1919586611879673857.json, 图片生成/文生图/一键换装FLUX重绘_1924659553831407618.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_69

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【精准一键换衣】 FLUX模特人物换装_1919586611879673857.json、图片生成/文生图/一键换装FLUX重绘_1924659553831407618.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `BaiduTranslateNode`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `ImageCrop+`
- `ImageToMask`
- `ImpactInt`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `InspyrenetRembg`
- `KSampler`
- `LayerMask: SegmentAnythingUltra V2`
- `LayerUtility: GetImageSize`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `MaskToImage`
- `Parabolize`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `SetNode`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
