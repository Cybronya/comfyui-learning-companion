---
name: unknown_workflow_controlnet_inpaint_sampler_12
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.905
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CheckpointLoader|pysssss, ControlNetApplyAdvanced, ControlNetLoader, CropMask, GrowMask, ImageColorMatch+, ImageResize+, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, MaskBlur+, RepeatLatentBatch, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/超自然高精度换脸，没有AI感_1908901262610604033.json, 图片生成/图生图/高精度换脸_1906320458168324097.json, 平台全量/高清换脸-新版本_1905614203665977346.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_sampler_12

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/超自然高精度换脸，没有AI感_1908901262610604033.json、图片生成/图生图/高精度换脸_1906320458168324097.json、平台全量/高清换脸-新版本_1905614203665977346.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CheckpointLoader|pysssss`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `CropMask`
- `GrowMask`
- `ImageColorMatch+`
- `ImageResize+`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `MaskBlur+`
- `RepeatLatentBatch`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 2/3 个有
- `ApplyInstantID` —— 2/3 个有
- `ColorMatch` —— 2/3 个有
- `Int` —— 2/3 个有
- `Prompts Everywhere` —— 2/3 个有
- `SUPIR_conditioner` —— 2/3 个有
- `SUPIR_encode` —— 2/3 个有
- `SUPIR_first_stage` —— 2/3 个有
- `SUPIR_model_loader_v2` —— 2/3 个有
- `SUPIR_sample` —— 2/3 个有
- `GetNode` —— 1/3 个有
- `MaskPreview+` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `SUPIR_decode` —— 1/3 个有
- `SetNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.5 | 0.5 - 0.5 | 3 | 100% |
| 采样步数 | 12 | 12 - 15 | 3 | 89% |
| Prompt 约束强度(CFG) | 2 | 1.5 - 2 | 3 | 87% |
| 采样算法 | euler_ancestral | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 67% |
| 重绘幅度 | 0.6 | 0.6 - 0.6 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.5，观测区间 0.5 - 0.5，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 12，观测区间 12 - 15，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 2，观测区间 1.5 - 2，3 个样本，取值集中（一致性 87%）
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 67%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 0.6，3 个样本，取值集中（一致性 100%）
