---
name: unknown_workflow_controlnet_inpaint_sampler
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.855667
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetLoader, CropMask, GrowMask, ImageResize+, InpaintModelConditioning, InstantIDFaceAnalysis, InstantIDModelLoader, KSampler, LayerMask: MaskPreview, LayerMask: PersonMaskUltra V2, LayerUtility: CropBoxResolve, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, MaskBlur+, RepeatLatentBatch, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/AI摄影_人像图超强换脸V2.6_1955536036283781121.json, 图片生成/图生图/Instant-id换face工作流_2017135341706153986.json, 图片生成/图生图/Instantid 精准换脸工作流_2087382545582350338.json, 图片生成/图生图/Instantid精准换脸工作流_1990349959331500034.json, 图片生成/图生图/Instantid精准换脸工作流_2009976152181448705.json, 图片生成/图生图/SDXL INSTANTID260816_2088833184023801857.json, 图片生成/图生图/inshant-ID换脸工作流_2106574825912365057.json, 图片生成/图生图/instant id 换脸 _ 一键在线运行4.0_1991136198989053954.json, 图片生成/图生图/instant id 换脸很不错_2044791626463191041.json, 图片生成/图生图/【CQ808】换脸-v3_2037473796621340673.json, 图片生成/图生图/一键换脸工作流_1980791470967930882.json, 图片生成/图生图/单人-Instantid精准换脸工作流_2036763462029811713.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_inpaint_sampler

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/AI摄影_人像图超强换脸V2.6_1955536036283781121.json、图片生成/图生图/Instant-id换face工作流_2017135341706153986.json、图片生成/图生图/Instantid 精准换脸工作流_2087382545582350338.json、图片生成/图生图/Instantid精准换脸工作流_1990349959331500034.json、图片生成/图生图/Instantid精准换脸工作流_2009976152181448705.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `CropMask`
- `GrowMask`
- `ImageResize+`
- `InpaintModelConditioning`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `KSampler`
- `LayerMask: MaskPreview`
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
- `ApplyInstantID` —— 11/12 个有
- `ColorMatch` —— 11/12 个有
- `Image Comparer (rgthree)` —— 11/12 个有
- `FaceAnalysisModels` —— 10/12 个有
- `FaceBoundingBox` —— 10/12 个有
- `PreviewImage` —— 10/12 个有
- `SUPIR_Upscale` —— 10/12 个有
- `AIO_Preprocessor` —— 4/12 个有
- `ControlNetApplyAdvanced` —— 4/12 个有
- `ImageColorMatch+` —— 2/12 个有
- `ApplyInstantIDAdvanced` —— 1/12 个有
- `FeatheredMask` —— 1/12 个有
- `GetNode` —— 1/12 个有
- `ImageConcatMulti` —— 1/12 个有
- `ImpactInt` —— 1/12 个有
- `SUPIR_conditioner` —— 1/12 个有
- `SUPIR_decode` —— 1/12 个有
- `SUPIR_encode` —— 1/12 个有
- `SUPIR_first_stage` —— 1/12 个有
- `SUPIR_model_loader_v2` —— 1/12 个有
- `SUPIR_sample` —— 1/12 个有
- `Seed_` —— 1/12 个有
- `SetNode` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.45 | 0.45 - 0.45 | 4 | 100% |
| 采样步数 | 20 | 15 - 41 | 12 | 68% |
| Prompt 约束强度(CFG) | 2 | 1.5 - 2 | 12 | 87% |
| 采样算法 | euler_ancestral | - | 12 | 100% |
| 调度器 | sgm_uniform | - | 12 | 92% |
| 重绘幅度 | 0.5 | 0.36 - 0.6 | 12 | 88% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.45，观测区间 0.45 - 0.45，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 15 - 41，12 个样本
- Prompt 约束强度(CFG) 中位数 2，观测区间 1.5 - 2，12 个样本，取值集中（一致性 87%）
- 采样算法 最常用 euler_ancestral，12 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，12 个样本，一致性 92%
- 重绘幅度 中位数 0.5，观测区间 0.36 - 0.6，12 个样本，取值集中（一致性 88%）
