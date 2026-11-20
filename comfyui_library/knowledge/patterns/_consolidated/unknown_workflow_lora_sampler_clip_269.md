---
name: unknown_workflow_lora_sampler_clip_269
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.915
common_nodes: [ApplyPulidFlux, CLIPTextEncode, CLIPVisionLoader, CR Text, CR Text Concatenate, ConditioningZeroOut, DepthAnythingV2Preprocessor, DownloadAndLoadFlorence2Model, DualCLIPLoader, Florence2Run, FluxGuidance, ImageScaleToTotalPixels, InstructPixToPixConditioning, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, PulidFluxEvaClipLoader, PulidFluxInsightFaceLoader, PulidFluxModelLoader, ReduxAdvanced, SaveImage, ShowText|pysssss, StyleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux-蜡笔画_1909477759297400834.json, 图片生成/图生图/吉卜力风格_flux图生图_1907367695694589954.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_269

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/flux-蜡笔画_1909477759297400834.json、图片生成/图生图/吉卜力风格_flux图生图_1907367695694589954.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyPulidFlux`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `DepthAnythingV2Preprocessor`
- `DownloadAndLoadFlorence2Model`
- `DualCLIPLoader`
- `Florence2Run`
- `FluxGuidance`
- `ImageScaleToTotalPixels`
- `InstructPixToPixConditioning`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `PulidFluxEvaClipLoader`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `ReduxAdvanced`
- `SaveImage`
- `ShowText|pysssss`
- `StyleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplyFBCacheOnModel` —— 1/2 个有
- `CheckpointLoaderSimple` —— 1/2 个有
- `ImageResize+` —— 1/2 个有
- `UNETLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | sgm_uniform | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
