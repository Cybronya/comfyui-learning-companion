---
name: unknown_workflow_inpaint_lora_sampler_33
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.820667
common_nodes: [CLIPTextEncode, CLIPVisionLoader, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, InpaintModelConditioning, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ReduxAdvanced, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy makeImageForICLora]
problems: []
missing: []
members: [图片生成/图生图/6.tonnie-flux-fill万物迁移（换装）_1992523737929150466.json, 图片生成/图生图/F1 FILL+REDUX（产品换背景）_2089147272247463938.json, 图片生成/图生图/FLUX FILL超细节局部重绘万物迁移_2027602800858894337.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_33

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/6.tonnie-flux-fill万物迁移（换装）_1992523737929150466.json、图片生成/图生图/F1 FILL+REDUX（产品换背景）_2089147272247463938.json、图片生成/图生图/FLUX FILL超细节局部重绘万物迁移_2027602800858894337.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `InpaintModelConditioning`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ReduxAdvanced`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy makeImageForICLora`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `Image Comparer (rgthree)` —— 2/3 个有
- `ImageCrop+` —— 2/3 个有
- `LayerUtility: ImageRemoveAlpha` —— 2/3 个有
- `Mask Fill Holes` —— 2/3 个有
- `MaskPreview+` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `ImageCrop` —— 1/3 个有
- `InpaintCrop` —— 1/3 个有
- `InpaintStitch` —— 1/3 个有
- `LayerMask: LoadSegmentAnythingModels` —— 1/3 个有
- `LayerMask: SegmentAnythingUltra V3` —— 1/3 个有
- `LayerUtility: CropByMask V2` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `RembgNode_Mix` —— 1/3 个有
- `easy pipeEdit` —— 1/3 个有
- `easy pipeOut` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 3 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，3 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
