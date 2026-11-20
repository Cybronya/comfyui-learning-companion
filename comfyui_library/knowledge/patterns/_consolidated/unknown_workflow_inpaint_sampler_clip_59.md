---
name: unknown_workflow_inpaint_sampler_clip_59
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.79575
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, EmptyImage, FluxGuidance, GrowMaskWithBlur, ImageConcanate, ImageCrop+, ImageResizeKJ, ImageToMask, InpaintCrop, InpaintModelConditioning, InpaintStitch, Int, KSampler, LayerMask: SegformerB2ClothesUltra, LoadImage, MaskToImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/Flux一键换装_虚拟换装服装电商专用V3.6_1954412621770440706.json, 图片生成/图生图/手动涂鸦换装V2+加强版=艾橘溪_1913191183433068545.json, 图片生成/图生图/虚拟换装服装电商一键换装_2045738971988238337.json, 平台全量/模特换装 服饰替换 高清放大 虚拟换装服装电商一键换装_2069238337650651137.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_59

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux一键换装_虚拟换装服装电商专用V3.6_1954412621770440706.json、图片生成/图生图/手动涂鸦换装V2+加强版=艾橘溪_1913191183433068545.json、图片生成/图生图/虚拟换装服装电商一键换装_2045738971988238337.json、平台全量/模特换装 服饰替换 高清放大 虚拟换装服装电商一键换装_2069238337650651137.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `FluxGuidance`
- `GrowMaskWithBlur`
- `ImageConcanate`
- `ImageCrop+`
- `ImageResizeKJ`
- `ImageToMask`
- `InpaintCrop`
- `InpaintModelConditioning`
- `InpaintStitch`
- `Int`
- `KSampler`
- `LayerMask: SegformerB2ClothesUltra`
- `LoadImage`
- `MaskToImage`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `AddMask` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `FeatheredMask` —— 3/4 个有
- `Image Filter Adjustments` —— 3/4 个有
- `ImageCompositeMasked` —— 3/4 个有
- `ImageCrop` —— 3/4 个有
- `InspyrenetRembgAdvanced` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `LoraLoader` —— 3/4 个有
- `MathExpression|pysssss` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `easy imageIndexSwitch` —— 2/4 个有
- `ImageResize+` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `Robust Video Matting` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.7 | 0.7 - 0.7 | 3 | 100% |
| LoRA 文本强度 | 0.8 | 0.8 - 0.8 | 3 | 100% |
| 采样步数 | 25 | 25 - 50 | 4 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.7，观测区间 0.7 - 0.7，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 50，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
