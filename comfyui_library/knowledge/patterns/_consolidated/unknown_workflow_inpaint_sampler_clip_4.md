---
name: unknown_workflow_inpaint_sampler_clip_4
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.888125
common_nodes: [CLIPTextEncode, CLIPVisionEncode, DualCLIPLoader, FluxGuidance, ImageConcanate, ImageToMask, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, PreviewImage, SaveImage, StyleModelApply, StyleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [平台全量/512万物迁移修罗9号_1946863438452940802.json, 平台全量/CG迷-ACE++人物指定轮廓迁移工作流_1927314967697973249.json, 平台全量/CG迷-ACE++物体指定控制生成工作流_1927309854770368514.json, 平台全量/CG迷-Flux  512版本万物迁移工作流_1927355519273426946.json, 平台全量/Comfyui + FLUX 模特角色一键换装工作流_1901164939678228482.json, 平台全量/FLUX Redux 万物迁移_1925463022809042945.json, 平台全量/FLUX.1_fill+redux万物迁移工作流_1881348712072114178.json, 平台全量/FLUX万物迁移工作流-一键全自动流程_1930080830574727170.json, 平台全量/FLUX万物迁移工作流-全自动流程FLUX万物迁移工作流_1961689722097745922.json, 平台全量/FLUX万物迁移工作流_1896448618712924161.json, 平台全量/Flux_物件遷移換裝_1893943766074458114.json, 平台全量/Flux产品迁移工作流_1969764327609802754.json, 平台全量/Flux的Fill+Redux万物迁移工作流，可换装、换产品_1902896962012884994.json, 平台全量/Redux Fill万物迁移(M）_1904107318798094337.json, 平台全量/nunchakuFLUX万物迁移工作流_1910921368362516481.json, 平台全量/万物迁服装双融合工作_1916343454522081281.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_sampler_clip_4

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（平台全量/512万物迁移修罗9号_1946863438452940802.json、平台全量/CG迷-ACE++人物指定轮廓迁移工作流_1927314967697973249.json、平台全量/CG迷-ACE++物体指定控制生成工作流_1927309854770368514.json、平台全量/CG迷-Flux  512版本万物迁移工作流_1927355519273426946.json、平台全量/Comfyui + FLUX 模特角色一键换装工作流_1901164939678228482.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 16 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
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
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 15/16 个有
- `UNETLoader` —— 15/16 个有
- `DifferentialDiffusion` —— 14/16 个有
- `EmptyImage` —— 11/16 个有
- `ImageCrop` —— 7/16 个有
- `ImageResize+` —— 7/16 个有
- `Image Blank` —— 5/16 个有
- `easy int` —— 5/16 个有
- `GetImageSize+` —— 4/16 个有
- `ImpactInt` —— 4/16 个有
- `RMBG` —— 4/16 个有
- `LoraLoaderModelOnly` —— 3/16 个有
- `ConditioningZeroOut` —— 2/16 个有
- `Fast Groups Bypasser (rgthree)` —— 2/16 个有
- `AdvancedVisionLoader` —— 1/16 个有
- `AutoDownloadBiRefNetModel` —— 1/16 个有
- `DF_Image_scale_to_side` —— 1/16 个有
- `ImpactGaussianBlurMask` —— 1/16 个有
- `LayerUtility: ImageRemoveAlpha` —— 1/16 个有
- `NunchakuFluxDiTLoader` —— 1/16 个有
- `RembgByBiRefNet` —— 1/16 个有
- `SUPIR_Upscale` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 28 | 20 - 30 | 16 | 81% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 16 | 100% |
| 采样算法 | euler | - | 16 | 100% |
| 调度器 | normal | - | 16 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 16 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 28，观测区间 20 - 30，16 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，16 个样本，一致性 100%
- 调度器 最常用 normal，16 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，16 个样本，取值集中（一致性 100%）
