---
name: unknown_workflow_inpaint_sampler_unet_3
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.937
common_nodes: [CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, ImageConcanate, ImageCrop+, ImageToMask, InpaintModelConditioning, KSampler, LoadImage, MaskToImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/FLUX redux+ACE++ 一键换装 模特精准迁移_1920305054073421826.json, 图片生成/图生图/FLXU换装_1915651643583696898.json, 图片生成/图生图/万物迁移-电商2.0版本2.0版本_1935874200882044930.json, 图片生成/图生图/模特迁移_1905997505379897345.json, 图片生成/图生图/电商模特换装工作流-mazh_1993858356211286018.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_unet_3

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/FLUX redux+ACE++ 一键换装 模特精准迁移_1920305054073421826.json、图片生成/图生图/FLXU换装_1915651643583696898.json、图片生成/图生图/万物迁移-电商2.0版本2.0版本_1935874200882044930.json、图片生成/图生图/模特迁移_1905997505379897345.json、图片生成/图生图/电商模特换装工作流-mazh_1993858356211286018.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `ImageConcanate`
- `ImageCrop+`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
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
- `CLIPTextEncode` —— 4/5 个有
- `FluxGuidance` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `CLIPTextEncodeFlux` —— 3/5 个有
- `CR Latent Batch Size` —— 3/5 个有
- `ConditioningZeroOut` —— 3/5 个有
- `Image Blank` —— 3/5 个有
- `ImageResize+` —— 3/5 个有
- `ImageScale` —— 3/5 个有
- `ImpactInt` —— 3/5 个有
- `Int` —— 3/5 个有
- `LayerUtility: ColorImage V2` —— 3/5 个有
- `LayerUtility: CropByMask V2` —— 3/5 个有
- `LayerUtility: RestoreCropBox` —— 3/5 个有
- `LoraLoaderModelOnly` —— 3/5 个有
- `PreviewImage` —— 3/5 个有
- `ResizeMask` —— 3/5 个有
- `BaiduTranslateNode` —— 1/5 个有
- `CR Simple Image Compare` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `Mask Fill Holes` —— 1/5 个有
- `ReduxAdvanced` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 25 - 28 | 5 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 0.8 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 25 - 28，5 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
