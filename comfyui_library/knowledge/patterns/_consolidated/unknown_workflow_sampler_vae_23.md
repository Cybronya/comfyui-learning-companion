---
name: unknown_workflow_sampler_vae_23
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.966818
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/2063503218805665793.json, 视频生成/图生视频/2055655934248144898.json, 视频生成/图生视频/2059487866354495489.json, 视频生成/图生视频/2056642345248055297.json, 视频生成/图生视频/2064317651400347649.json, 视频生成/图生视频/2057141350105178114.json, 视频生成/图生视频/2060889846209662978.json, 视频生成/图生视频/2068599191001190402.json, 视频生成/图生视频/2056302595207159810.json, 视频生成/图生视频/2055524487839404034.json, 视频生成/图生视频/2055531778017906689.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_23

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2063503218805665793.json、视频生成/图生视频/2055655934248144898.json、视频生成/图生视频/2059487866354495489.json、视频生成/图生视频/2056642345248055297.json、视频生成/图生视频/2064317651400347649.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 11 个 workflow 都包含：
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
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LTXVLatentUpsampler` —— 10/11 个有
- `LatentUpscaleModelLoader` —— 10/11 个有
- `LTX2SamplingPreviewOverride` —— 9/11 个有
- `LoraLoaderModelOnly` —— 9/11 个有
- `VAEDecode` —— 8/11 个有
- `CreateVideo` —— 7/11 个有
- `SaveVideo` —— 7/11 个有
- `UNETLoader` —— 7/11 个有
- `VHS_VideoCombine` —— 5/11 个有
- `CheckpointLoaderSimple` —— 4/11 个有
- `Int` —— 3/11 个有
- `LoadImage` —— 3/11 个有
- `VAEDecodeTiled` —— 3/11 个有
- `ImpactSwitch` —— 2/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/11 个有
- `ManualSigmas` —— 2/11 个有
- `CR Prompt Text` —— 1/11 个有
- `DapaoImageSplitNode` —— 1/11 个有
- `Fast Groups Bypasser (rgthree)` —— 1/11 个有
- `GuHaiAutoImageSplit` —— 1/11 个有
- `LoadVideo` —— 1/11 个有
- `PreviewAny` —— 1/11 个有
- `RH_LLMAPI_Pro_Node` —— 1/11 个有
- `SaveImage` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
