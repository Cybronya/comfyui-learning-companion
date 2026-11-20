---
name: unknown_workflow_inpaint_sampler_unet_2
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.927545
common_nodes: [CLIPVisionEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, ImageConcanate, ImageCrop+, ImageToMask, InpaintModelConditioning, KSampler, LoadImage, MaskToImage, SaveImage, StyleModelApply, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/FLUX redux+ACE++ 一键换装 模特精准迁移_1920305054073421826.json, 图片生成/图生图/FLXU换装_1915651643583696898.json, 图片生成/图生图/万物迁移-电商2.0版本2.0版本_1935874200882044930.json, 图片生成/图生图/模特迁移_1905997505379897345.json, 图片生成/图生图/电商模特换装工作流-mazh_1993858356211286018.json, 平台全量/万物迁移V7更新版本_1916338940234629121.json, 平台全量/万物迁移_2018639188786159617.json, 平台全量/万物迁移丨换背景2.0版本_1867976147337363457.json, 平台全量/万物迁移优化（电商版）_1921770107897331714.json, 平台全量/专业级鞋子迁移1.0版本_1910868719550300161.json, 平台全量/换鞋_1920415811209461762.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_unet_2

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/FLUX redux+ACE++ 一键换装 模特精准迁移_1920305054073421826.json、图片生成/图生图/FLXU换装_1915651643583696898.json、图片生成/图生图/万物迁移-电商2.0版本2.0版本_1935874200882044930.json、图片生成/图生图/模特迁移_1905997505379897345.json、图片生成/图生图/电商模特换装工作流-mazh_1993858356211286018.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 11 个 workflow 都包含：
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
- `CLIPTextEncode` —— 8/11 个有
- `FluxGuidance` —— 8/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/11 个有
- `CLIPTextEncodeFlux` —— 7/11 个有
- `ConditioningZeroOut` —— 7/11 个有
- `Image Blank` —— 7/11 个有
- `ImageResize+` —— 7/11 个有
- `ImageScale` —— 7/11 个有
- `ImpactInt` —— 7/11 个有
- `Int` —— 7/11 个有
- `LayerUtility: ColorImage V2` —— 7/11 个有
- `LayerUtility: CropByMask V2` —— 7/11 个有
- `LayerUtility: RestoreCropBox` —— 7/11 个有
- `LoraLoaderModelOnly` —— 7/11 个有
- `PreviewImage` —— 7/11 个有
- `ResizeMask` —— 7/11 个有
- `CR Latent Batch Size` —— 5/11 个有
- `ReduxAdvanced` —— 5/11 个有
- `Fast Groups Bypasser (rgthree)` —— 3/11 个有
- `LoraLoader` —— 3/11 个有
- `Image Rotate` —— 2/11 个有
- `LayerMask: BiRefNetUltraV2` —— 2/11 个有
- `LayerMask: LoadBiRefNetModel` —— 2/11 个有
- `LayerUtility: ImageRemoveAlpha` —— 2/11 个有
- `MirroredImage` —— 2/11 个有
- `ArgosTranslateTextNode` —— 1/11 个有
- `BaiduTranslateNode` —— 1/11 个有
- `CR Simple Image Compare` —— 1/11 个有
- `Mask Fill Holes` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 25 - 30 | 11 | 96% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | normal | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| LoRA 模型强度 | 0.8 | 0.8 - 0.8 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 25 - 30，11 个样本，取值集中（一致性 96%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 normal，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 0.8，观测区间 0.8 - 0.8，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
