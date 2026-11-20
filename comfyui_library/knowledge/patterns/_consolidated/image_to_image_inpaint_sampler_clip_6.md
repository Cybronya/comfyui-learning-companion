---
name: image_to_image_inpaint_sampler_clip_6
type: Image To Image
frequency: 3
level: strong
coverage: 0.835667
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, DifferentialDiffusion, DualCLIPLoader, FL_ColorPicker, FluxGuidance, HfImageToRGB, ImageComposite+, ImageResize+, ImageResizeKJ, ImpactInt, InpaintModelConditioning, Int, KSampler, LayerColor: AutoAdjustV2, LayerMask: SegformerClothesPipelineLoader, LayerMask: SegformerUltraV2, LayerUtility: RGB Value, LoadImage, MaskFastGrow, PreviewImage, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, Seed (rgthree), SimpleMath+, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/一键换发色_1897311883236429826.json, 图片生成/图生图/染发师工作流程_1909562659363090433.json, 图片生成/图生图/高级染发工作流 ｜一键生图系列_1918835878297272321.json]
source: knowledge_consolidation
---

# image_to_image_inpaint_sampler_clip_6

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/一键换发色_1897311883236429826.json、图片生成/图生图/染发师工作流程_1909562659363090433.json、图片生成/图生图/高级染发工作流 ｜一键生图系列_1918835878297272321.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FL_ColorPicker`
- `FluxGuidance`
- `HfImageToRGB`
- `ImageComposite+`
- `ImageResize+`
- `ImageResizeKJ`
- `ImpactInt`
- `InpaintModelConditioning`
- `Int`
- `KSampler`
- `LayerColor: AutoAdjustV2`
- `LayerMask: SegformerClothesPipelineLoader`
- `LayerMask: SegformerUltraV2`
- `LayerUtility: RGB Value`
- `LoadImage`
- `MaskFastGrow`
- `PreviewImage`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`
- `Seed (rgthree)`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `0246.Highway` —— 1/3 个有
- `AddLabel` —— 1/3 个有
- `Display Int (rgthree)` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LayerUtility: ImageReel` —— 1/3 个有
- `LayerUtility: ImageReelComposit` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 0.6 | 0.6 - 0.6 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 0.6，3 个样本，取值集中（一致性 100%）
