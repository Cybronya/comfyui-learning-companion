---
name: unknown_workflow_inpaint_upscale_sampler_7
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.837333
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, ColorCorrectOfUtils, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, GetImageSize+, Image Comparer (rgthree), ImageCompositeMasked, ImagePadForOutpaintMasked, ImageResize+, ImageScaleBy, ImageUpscaleWithModel, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LoadImage, MultiplicationNode, PreviewImage, PrimitiveFloat, PrimitiveInt, SaveImage, StyleModelApply, StyleModelLoader, UpscaleModelLoader, VAEDecode, VAELoader, easy imageColorMatch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/FLUX 无痕扩图 (高清人像专用)_1935171756485189633.json, 图片生成/图生图/FLUX无痕扩图+ 细节自动修复_1975516517129433090.json, 图片生成/图生图/双截棍极速扩图-一分钟出图_1922314971554729985.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_sampler_7

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/FLUX 无痕扩图 (高清人像专用)_1935171756485189633.json、图片生成/图生图/FLUX无痕扩图+ 细节自动修复_1975516517129433090.json、图片生成/图生图/双截棍极速扩图-一分钟出图_1922314971554729985.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `ColorCorrectOfUtils`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `ImagePadForOutpaintMasked`
- `ImageResize+`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LoadImage`
- `MultiplicationNode`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `SaveImage`
- `StyleModelApply`
- `StyleModelLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageColorMatch`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 2/3 个有
- `MaskPreview+` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `Florence2ModelLoader` —— 1/3 个有
- `Florence2Run` —— 1/3 个有
- `NunchakuFluxDiTLoader` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `easy imageInsetCrop` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | sgm_uniform | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（6/3 个样本）：Steps较低可能导致细节不足
