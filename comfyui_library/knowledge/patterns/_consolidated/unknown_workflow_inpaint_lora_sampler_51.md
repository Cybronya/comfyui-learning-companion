---
name: unknown_workflow_inpaint_lora_sampler_51
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.811
common_nodes: [CLIPTextEncodeFlux, ConditioningZeroOut, DF_Float, DF_Image_scale_to_side, DF_Integer, DualCLIPLoader, Image Comparer (rgthree), ImageResizeKJ, ImageToMask, InpaintModelConditioning, KSampler, LayerMask: MaskGrow, LayerUtility: CropByMask, LayerUtility: RestoreCropBox, LoadImage, LoraLoaderModelOnly, MaskToImage, ResizeMask, SaveImage, Text Concatenate, Text _O, UNETLoader, VAEDecode, VAELoader, easy imageSize]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux 一键去水印极速工作流_1983738390074073090.json, 图片生成/图生图/Flux 局部重绘加速版_1982583858916925441.json, 平台全量/Flux 局部重绘，一键在线运行，全场景通用_1929875766522101761.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_51

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/Flux 一键去水印极速工作流_1983738390074073090.json、图片生成/图生图/Flux 局部重绘加速版_1982583858916925441.json、平台全量/Flux 局部重绘，一键在线运行，全场景通用_1929875766522101761.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncodeFlux`
- `ConditioningZeroOut`
- `DF_Float`
- `DF_Image_scale_to_side`
- `DF_Integer`
- `DualCLIPLoader`
- `Image Comparer (rgthree)`
- `ImageResizeKJ`
- `ImageToMask`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerUtility: CropByMask`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ResizeMask`
- `SaveImage`
- `Text Concatenate`
- `Text _O`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy imageSize`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 0.65 | 0.65 - 0.65 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 0.65，观测区间 0.65 - 0.65，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
