---
name: unknown_workflow_inpaint_lora_unet
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.85
common_nodes: [CLIPVisionLoader, ConditioningZeroOut, DualCLIPLoader, GrowMask, ImageConcanate, ImageResize+, ImageScale, ImageToMask, InpaintModelConditioning, InpaintStitch, InspyrenetRembg, LayerUtility: ColorImage, LayerUtility: ImageRemoveAlpha, LoadImage, LoraLoaderModelOnly, MaskToImage, PreviewImage, RHHiddenNodes, ReduxAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/AI模特手持产品生成_1902360459163643905.json, 图片生成/图生图/FLUX.产品背景工作流_1901616716240293889.json, 图片生成/图生图/FLUX.产品背景工作流_1919764475774173185.json, 图片生成/图生图/电商模特一致性生成，服装保持不变_1900143787912458241.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_unet

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/AI模特手持产品生成_1902360459163643905.json、图片生成/图生图/FLUX.产品背景工作流_1901616716240293889.json、图片生成/图生图/FLUX.产品背景工作流_1919764475774173185.json、图片生成/图生图/电商模特一致性生成，服装保持不变_1900143787912458241.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
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
- `RHHiddenNodes`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 3/4 个有
- `ImageCrop+` —— 3/4 个有
- `InpaintCrop` —— 3/4 个有
- `LayerMask: SegmentAnythingUltra V2` —— 3/4 个有
- `MaskPreview+` —— 3/4 个有
- `KSampler` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 35 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | normal | - | 1 | 100% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
