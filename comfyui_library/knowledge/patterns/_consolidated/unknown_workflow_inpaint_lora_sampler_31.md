---
name: unknown_workflow_inpaint_lora_sampler_31
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.38925
common_nodes: [BiRefNet_Hugo, CLIPLoader, CR Text, ConditioningZeroOut, Fast Groups Bypasser (rgthree), FastCanvas, FastCanvasTool, GetImageSize+, GetNode, ImagePadForOutpaint, InpaintModelConditioning, KSampler (Efficient), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PainterFluxImageEdit, PreviewImage, QwenMultiangleCameraNode, SaveImage, SetNode, UNETLoader, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Klein_9B文生图、单图编辑、多图编辑、局部重绘、扩图_2055930510144221186.json, 图片生成/文生图/flux-2-klein-9b-fp8  全套 全家福 文生 编辑 溶图 扩图 洗图 修图 多角度_2020325725206745089.json, 图片生成/文生图/klein全套+全家福+文生+编辑+溶图+扩图+洗图+修图+多角度+_2084459615470841857.json, 图片生成/文生图/一键运行 klein 9B TRUE-V2 微调模型  文生图、单图编辑、多图编辑、局部重绘、扩图_2055864120817266690.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_31

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Klein_9B文生图、单图编辑、多图编辑、局部重绘、扩图_2055930510144221186.json、图片生成/文生图/flux-2-klein-9b-fp8  全套 全家福 文生 编辑 溶图 扩图 洗图 修图 多角度_2020325725206745089.json、图片生成/文生图/klein全套+全家福+文生+编辑+溶图+扩图+洗图+修图+多角度+_2084459615470841857.json、图片生成/文生图/一键运行 klein 9B TRUE-V2 微调模型  文生图、单图编辑、多图编辑、局部重绘、扩图_2055864120817266690.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：39%

## 共有节点

全部 4 个 workflow 都包含：
- `BiRefNet_Hugo`
- `CLIPLoader`
- `CR Text`
- `ConditioningZeroOut`
- `Fast Groups Bypasser (rgthree)`
- `FastCanvas`
- `FastCanvasTool`
- `GetImageSize+`
- `GetNode`
- `ImagePadForOutpaint`
- `InpaintModelConditioning`
- `KSampler (Efficient)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PainterFluxImageEdit`
- `PreviewImage`
- `QwenMultiangleCameraNode`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageCaptionNode` —— 3/4 个有
- `VAEEncode` —— 3/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 16.5 | 8 - 25 | 4 | 48% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 16.5，观测区间 8 - 25，4 个样本，取值分散，一致性仅 48%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
