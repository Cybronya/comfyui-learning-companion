---
name: unknown_workflow_inpaint_sampler_clip_47
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9078
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageResize+, InpaintCrop, InpaintModelConditioning, InpaintStitch, KSampler, LoadImage, MaskPreview+, MaskToImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键快速换装（100%精准度）_1915681331496288258.json, 平台全量/AI模特换装图【AI小王子】_1912360852794867713.json, 平台全量/flux模特换装_1977996980230180865.json, 平台全量/【AI小王子】56.换衣_2048557116666945537.json, 数字人/数字人/【极致精准换装】FLUX 一键快速迁移换装（适用服装、首饰、配件）_1927885747024740354.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_47

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/一键快速换装（100%精准度）_1915681331496288258.json、平台全量/AI模特换装图【AI小王子】_1912360852794867713.json、平台全量/flux模特换装_1977996980230180865.json、平台全量/【AI小王子】56.换衣_2048557116666945537.json、数字人/数字人/【极致精准换装】FLUX 一键快速迁移换装（适用服装、首饰、配件）_1927885747024740354.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageConcanate`
- `ImageResize+`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `KSampler`
- `LoadImage`
- `MaskPreview+`
- `MaskToImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `ImageToMask` —— 3/5 个有
- `InspyrenetRembg` —— 3/5 个有
- `LayerUtility: ColorImage` —— 3/5 个有
- `easy imageCropFromMask` —— 3/5 个有
- `GroundingDinoModelLoader (segment anything)` —— 2/5 个有
- `GroundingDinoSAMSegment (segment anything)` —— 2/5 个有
- `Image To Mask` —— 2/5 个有
- `LayerUtility: ColorImage V2` —— 2/5 个有
- `SAMModelLoader (segment anything)` —— 2/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | beta | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
