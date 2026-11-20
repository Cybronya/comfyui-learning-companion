---
name: unknown_workflow_sampler_clip_vae_57
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.902
common_nodes: [ApplyPulidFlux, CLIPTextEncode, CLIPVisionLoader, CR Text, CR Text Concatenate, ConditioningZeroOut, DepthAnythingV2Preprocessor, DownloadAndLoadFlorence2Model, Florence2Run, FluxGuidance, ImageScaleToTotalPixels, InstructPixToPixConditioning, KSampler, LoadImage, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, ReduxAdvanced, SaveImage, ShowText|pysssss, StyleModelLoader, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/flux-蜡笔画_1909477759297400834.json, 图片生成/图生图/吉卜力风格_flux图生图_1907367695694589954.json, 平台全量/Ghibli Style(flux)_1878697274871291906.json, 平台全量/Portrait pencil sketch @datou_1875152528340901890.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_57

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/flux-蜡笔画_1909477759297400834.json、图片生成/图生图/吉卜力风格_flux图生图_1907367695694589954.json、平台全量/Ghibli Style(flux)_1878697274871291906.json、平台全量/Portrait pencil sketch @datou_1875152528340901890.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyPulidFlux`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `DepthAnythingV2Preprocessor`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `FluxGuidance`
- `ImageScaleToTotalPixels`
- `InstructPixToPixConditioning`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `ReduxAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StyleModelLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 3/4 个有
- `VAELoader` —— 3/4 个有
- `CheckpointLoaderSimple` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `Power Lora Loader (rgthree)` —— 2/4 个有
- `UNETLoader` —— 2/4 个有
- `ApplyFBCacheOnModel` —— 1/4 个有
- `ImageResize+` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 12 - 12 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | dpmpp_2m | - | 4 | 100% |
| 调度器 | beta | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12，观测区间 12 - 12，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
