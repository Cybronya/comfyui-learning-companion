---
name: unknown_workflow_inpaint_sampler_clip_63
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.8485
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GroundingDinoModelLoader (segment anything), GroundingDinoSAMSegment (segment anything), Image Comparer (rgthree), InpaintModelConditioning, KSampler, LoadImage, PreviewImage, SAMModelLoader (segment anything), SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/一键换衣-提示词方式_1901607291534065665.json, 图片生成/图生图/一键消除水印_1926110099427790849.json, 图片生成/图生图/消除水印_1937873398519500802.json, 平台全量/消除水印_1937705800100155393.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_63

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键换衣-提示词方式_1901607291534065665.json、图片生成/图生图/一键消除水印_1926110099427790849.json、图片生成/图生图/消除水印_1937873398519500802.json、平台全量/消除水印_1937705800100155393.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GroundingDinoModelLoader (segment anything)`
- `GroundingDinoSAMSegment (segment anything)`
- `Image Comparer (rgthree)`
- `InpaintModelConditioning`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SAMModelLoader (segment anything)`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `GrowMaskWithBlur` —— 3/4 个有
- `Image Overlay` —— 3/4 个有
- `LayerMask: MaskPreview` —— 3/4 个有
- `DeepTranslatorTextNode` —— 2/4 个有
- `GrowMask` —— 1/4 个有
- `LoraLoaderModelOnly` —— 1/4 个有
- `MaskToImage` —— 1/4 个有
- `Masks Combine Regions` —— 1/4 个有
- `VAEEncodeForInpaint` —— 1/4 个有
- `easy imageScaleDownBy` —— 1/4 个有

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
