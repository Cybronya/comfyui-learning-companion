---
name: unknown_workflow_inpaint_lora_unet
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.857833
common_nodes: [CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, GrowMask, ImageConcanate, ImageResize+, ImageScale, ImageToMask, InpaintModelConditioning, InpaintStitch, InspyrenetRembg, LayerUtility: ColorImage, LayerUtility: ImageRemoveAlpha, LoadImage, LoraLoaderModelOnly, MaskToImage, PreviewImage, ReduxAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/AI模特手持产品生成_1902360459163643905.json, 图片生成/图生图/FLUX.产品背景工作流_1901616716240293889.json, 图片生成/图生图/FLUX.产品背景工作流_1919764475774173185.json, 图片生成/图生图/电商模特一致性生成，服装保持不变_1900143787912458241.json, 平台全量/FLUX.电商产品指定场景背景工作流_1899382074204405762.json, 平台全量/自动化万物迁移_1921183563977523202.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_unet

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/AI模特手持产品生成_1902360459163643905.json、图片生成/图生图/FLUX.产品背景工作流_1901616716240293889.json、图片生成/图生图/FLUX.产品背景工作流_1919764475774173185.json、图片生成/图生图/电商模特一致性生成，服装保持不变_1900143787912458241.json、平台全量/FLUX.电商产品指定场景背景工作流_1899382074204405762.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPVisionLoader`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `GrowMask`
- `ImageConcanate`
- `ImageResize+`
- `ImageScale`
- `ImageToMask`
- `InpaintModelConditioning`
- `InpaintStitch`
- `InspyrenetRembg`
- `LayerUtility: ColorImage`
- `LayerUtility: ImageRemoveAlpha`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 5/6 个有
- `ImageCrop+` —— 5/6 个有
- `InpaintCrop` —— 5/6 个有
- `LayerMask: SegmentAnythingUltra V2` —— 5/6 个有
- `MaskPreview+` —— 5/6 个有
- `RHHiddenNodes` —— 4/6 个有
- `KSampler` —— 3/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 35 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 35，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
