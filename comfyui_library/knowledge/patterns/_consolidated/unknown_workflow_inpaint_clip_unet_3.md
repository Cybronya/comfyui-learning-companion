---
name: unknown_workflow_inpaint_clip_unet_3
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.867667
common_nodes: [CLIPTextEncode, DifferentialDiffusion, DualCLIPLoader, InpaintModelConditioning, LoadImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux_去水印局部重绘_1896135661734985730.json, 平台全量/FLUX局部重绘工作流（大全）_1946922468586975233.json, 平台全量/FLUX局部重绘工作流（大全）_2018505514463793153.json, 平台全量/FLUX局部重绘工作流（大全）_2070664376184557570.json, 平台全量/Flux Fill局部重绘_2061360095384129538.json, 平台全量/FluxRedux模特换装_1894287797715644418.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_clip_unet_3

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Flux_去水印局部重绘_1896135661734985730.json、平台全量/FLUX局部重绘工作流（大全）_1946922468586975233.json、平台全量/FLUX局部重绘工作流（大全）_2018505514463793153.json、平台全量/FLUX局部重绘工作流（大全）_2070664376184557570.json、平台全量/Flux Fill局部重绘_2061360095384129538.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `InpaintModelConditioning`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxGuidance` —— 5/6 个有
- `Image Comparer (rgthree)` —— 5/6 个有
- `ImpactGaussianBlurMask` —— 5/6 个有
- `KSampler` —— 5/6 个有
- `UnetLoaderGGUF` —— 3/6 个有
- `FluxSamplerParams+` —— 2/6 个有
- `LoadImageMask` —— 2/6 个有
- `CLIPVisionEncode` —— 1/6 个有
- `CLIPVisionLoader` —— 1/6 个有
- `GrowMaskWithBlur` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `StyleModelApplySimple` —— 1/6 个有
- `StyleModelLoader` —— 1/6 个有
- `VAEEncode` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 30 | 5 | 82% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 5 | 0% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 30，5 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
