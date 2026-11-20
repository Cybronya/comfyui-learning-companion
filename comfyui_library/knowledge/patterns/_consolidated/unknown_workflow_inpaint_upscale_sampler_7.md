---
name: unknown_workflow_inpaint_upscale_sampler_7
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.701
common_nodes: [CLIPTextEncodeFlux, CLIPVisionLoader, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, EmptyImage, Image Comparer (rgthree), ImageConcanate, ImageCrop+, ImageToMask, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, PreviewBridge, PreviewImage, ReduxAdvanced, SaveImage, StyleModelLoader, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/更好用的万物迁移Fill-OneReward_1967472909642031106.json, 平台全量/【超好用的万物迁移】Fill-OneReward 局部重绘  最新最好用的万物迁移_1986964949111123969.json, 平台全量/产品图商用工作流【全行业】_1896745402626711554.json, 平台全量/安-好用的万物迁移_1937080050640408577.json, 平台全量/更好用的万物迁移_1972125173342269442.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_sampler_7

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/更好用的万物迁移Fill-OneReward_1967472909642031106.json、平台全量/【超好用的万物迁移】Fill-OneReward 局部重绘  最新最好用的万物迁移_1986964949111123969.json、平台全量/产品图商用工作流【全行业】_1896745402626711554.json、平台全量/安-好用的万物迁移_1937080050640408577.json、平台全量/更好用的万物迁移_1972125173342269442.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `EmptyImage`
- `Image Comparer (rgthree)`
- `ImageConcanate`
- `ImageCrop+`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `PreviewBridge`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerMask: MaskPreview` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `GetImageSize` —— 3/5 个有
- `ImageRemoveBackground+` —— 1/5 个有
- `RemBGSession+` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | normal | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 normal，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
