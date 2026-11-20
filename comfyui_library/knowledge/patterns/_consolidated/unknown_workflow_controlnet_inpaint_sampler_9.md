---
name: unknown_workflow_controlnet_inpaint_sampler_9
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.974
common_nodes: [AIO_Preprocessor, Anything Everywhere3, CLIPTextEncode, CheckpointLoader|pysssss, ColorMatch, ControlNetApplyAdvanced, ControlNetLoader, CropMask, GrowMask, ImageColorMatch+, ImageResize+, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, Int, KSampler, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, MaskBlur+, Prompts Everywhere, RepeatLatentBatch, SUPIR_conditioner, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/超自然高精度换脸，没有AI感_1908901262610604033.json, 图片生成/图生图/高精度换脸_1906320458168324097.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_sampler_9

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/超自然高精度换脸，没有AI感_1908901262610604033.json、图片生成/图生图/高精度换脸_1906320458168324097.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `Anything Everywhere3`
- `CLIPTextEncode`
- `CheckpointLoader|pysssss`
- `ColorMatch`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `CropMask`
- `GrowMask`
- `ImageColorMatch+`
- `ImageResize+`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `Int`
- `KSampler`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: CropBoxResolve`
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `MaskBlur+`
- `Prompts Everywhere`
- `RepeatLatentBatch`
- `SUPIR_conditioner`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ApplyInstantID` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `SUPIR_decode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.5 | - | 2 | 100% |
| 采样步数 | 12 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 2 | - | 2 | 100% |
| 采样算法 | euler_ancestral | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 100% |
| 重绘幅度 | 0.6 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 12，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 100%
- 重绘幅度 中位数 0.6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
