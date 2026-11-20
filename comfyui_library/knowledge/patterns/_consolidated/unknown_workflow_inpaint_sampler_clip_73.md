---
name: unknown_workflow_inpaint_sampler_clip_73
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8695
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageToMask, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/FLUX换首饰衣服电商_1908051039432355842.json, 平台全量/【阡陌】FLUX万物精准迁移工作流_1902733507041603586.json, 平台全量/万物迁移Migration Of Everything (FLUX FILL+ Redux)_1865503155562692609.json, 平台全量/万物迁移goggogo_1910874271500173314.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_73

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/FLUX换首饰衣服电商_1908051039432355842.json、平台全量/【阡陌】FLUX万物精准迁移工作流_1902733507041603586.json、平台全量/万物迁移Migration Of Everything (FLUX FILL+ Redux)_1865503155562692609.json、平台全量/万物迁移goggogo_1910874271500173314.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

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
- `LayerUtility: ImageScaleByAspectRatio V2`
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
- `Image Blank` —— 3/4 个有
- `GrowMask` —— 2/4 个有
- `ImpactInt` —— 2/4 个有
- `SUPIR_Upscale` —— 2/4 个有
- `easy imageInsetCrop` —— 2/4 个有
- `DF_Image_scale_to_side` —— 1/4 个有
- `EmptyImage` —— 1/4 个有
- `ImageCrop+` —— 1/4 个有
- `ImageResize+` —— 1/4 个有
- `ImpactGaussianBlurMask` —— 1/4 个有
- `Int` —— 1/4 个有
- `LayerMask: SegformerB2ClothesUltra` —— 1/4 个有
- `MaskPreview+` —— 1/4 个有
- `PlaySound|pysssss` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy getNode` —— 1/4 个有
- `easy imageSize` —— 1/4 个有
- `easy setNode` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 4 | 80% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，4 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
