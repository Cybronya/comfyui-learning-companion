---
name: unknown_workflow_controlnet_upscale_lora_12
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.846
common_nodes: [AIO_Preprocessor, ApplyPulidFlux, CLIPTextEncode, CLIPVisionLoader, CR Text, ConditioningZeroOut, ControlNetApplyAdvanced, ControlNetLoader, DepthAnything_V2, DownloadAndLoadDepthAnythingV2Model, DualCLIPLoader, FluxGuidance, FusionText, Image Comparer (rgthree), InstructPixToPixConditioning, Joy_caption_two, Joy_caption_two_load, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, PulidEvaClipLoader, PulidFluxModelLoader, PulidInsightFaceLoader, ReduxAdvanced, RepeatLatentBatch, SUPIR_Upscale, SaveImage, StyleModelLoader, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/图片转绘油画风格，FLUX人物风景动物变成绘画_2015769332269195266.json, 平台全量/FLUX图片转绘油画风格工作流_1952752223114752002.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_upscale_lora_12

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图片转绘油画风格，FLUX人物风景动物变成绘画_2015769332269195266.json、平台全量/FLUX图片转绘油画风格工作流_1952752223114752002.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `ApplyPulidFlux`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Text`
- `ConditioningZeroOut`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DepthAnything_V2`
- `DownloadAndLoadDepthAnythingV2Model`
- `DualCLIPLoader`
- `FluxGuidance`
- `FusionText`
- `Image Comparer (rgthree)`
- `InstructPixToPixConditioning`
- `Joy_caption_two`
- `Joy_caption_two_load`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PulidEvaClipLoader`
- `PulidFluxModelLoader`
- `PulidInsightFaceLoader`
- `ReduxAdvanced`
- `RepeatLatentBatch`
- `SUPIR_Upscale`
- `SaveImage`
- `StyleModelLoader`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| ControlNet 权重 | 0.8 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- ControlNet 权重 中位数 0.8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
