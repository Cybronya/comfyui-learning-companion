---
name: unknown_workflow_sampler_unet_vae_97
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.9795
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/2063503218805665793.json, 视频生成/图生视频/2056642345248055297.json, 视频生成/图生视频/2064317651400347649.json, 视频生成/图生视频/2057141350105178114.json, 视频生成/图生视频/2060889846209662978.json, 视频生成/图生视频/2068599191001190402.json, 视频生成/图生视频/2056302595207159810.json, 视频生成/图生视频/2068702491201593346.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_97

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2063503218805665793.json、视频生成/图生视频/2056642345248055297.json、视频生成/图生视频/2064317651400347649.json、视频生成/图生视频/2057141350105178114.json、视频生成/图生视频/2060889846209662978.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LTXVLatentUpsampler` —— 7/8 个有
- `LatentUpscaleModelLoader` —— 7/8 个有
- `LTX2SamplingPreviewOverride` —— 6/8 个有
- `CreateVideo` —— 5/8 个有
- `LoraLoaderModelOnly` —— 5/8 个有
- `SaveVideo` —— 5/8 个有
- `VHS_VideoCombine` —— 3/8 个有
- `ManualSigmas` —— 2/8 个有
- `SaveImage` —— 2/8 个有
- `CR Prompt Text` —— 1/8 个有
- `DapaoImageSplitNode` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `GuHaiAutoImageSplit` —— 1/8 个有
- `Int` —— 1/8 个有
- `LoadImage` —— 1/8 个有
- `LoadVideo` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `RH_LLMAPI_Pro_Node` —— 1/8 个有
- `TT_img_enc` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
