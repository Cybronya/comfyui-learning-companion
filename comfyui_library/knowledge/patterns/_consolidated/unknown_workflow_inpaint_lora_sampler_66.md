---
name: unknown_workflow_inpaint_lora_sampler_66
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.738
common_nodes: [CLIPTextEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, ImageCrop, InpaintModelConditioning, KSampler, LayerMask: PersonMaskUltra V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, ReduxAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy makeImageForICLora]
problems: []
missing: []
members: [图片生成/图生图/最强换装工作流  redux+fill+自动蒙版_1922298174697046018.json, 平台全量/flux redux人物一致生成_1948376634249359361.json, 平台全量/换脸  Redux+Fill+AcePlus_1920495723790667777.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_66

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/最强换装工作流  redux+fill+自动蒙版_1922298174697046018.json、平台全量/flux redux人物一致生成_1948376634249359361.json、平台全量/换脸  Redux+Fill+AcePlus_1920495723790667777.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImageCrop`
- `InpaintModelConditioning`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 2/3 个有
- `DifferentialDiffusion` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `GrowMaskWithBlur` —— 2/3 个有
- `LayerMask: MaskPreview` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `ClothesSegment` —— 1/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `FaceAnalysisModels` —— 1/3 个有
- `FaceBoundingBox` —— 1/3 个有
- `FastCanvas` —— 1/3 个有
- `FastCanvasTool` —— 1/3 个有
- `InvertMask` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 28 | 3 | 62% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | normal | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 28，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 normal，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
