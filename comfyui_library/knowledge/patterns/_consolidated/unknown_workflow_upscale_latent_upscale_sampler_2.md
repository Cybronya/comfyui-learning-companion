---
name: unknown_workflow_upscale_latent_upscale_sampler_2
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.816059
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVConcatAVLatent, LTXVConditioning, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, RandomNoise, SamplerCustomAdvanced, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/2058931295174086657.json, 视频生成/图生视频/2071771328843173890.json, 视频生成/图生视频/2073210554319200257.json, 视频生成/图生视频/2072568558659391490.json, 视频生成/图生视频/2056571721142071298.json, 视频生成/图生视频/2061086858423136258.json, 视频生成/图生视频/2055482875381862402.json, 视频生成/图生视频/2078085536597757954.json, 视频生成/图生视频/2068969187762069506.json, 视频生成/图生视频/2055900601728421889.json, 视频生成/图生视频/2057459285617102849.json, 视频生成/图生视频/2056974345699942402.json, 视频生成/图生视频/2059911251098165250.json, 视频生成/图生视频/2059273921228263425.json, 视频生成/图生视频/2060383965181202433.json, 视频生成/图生视频/2057720205580783618.json, 视频生成/图生视频/2055094635088891905.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_2

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/2058931295174086657.json、视频生成/图生视频/2071771328843173890.json、视频生成/图生视频/2073210554319200257.json、视频生成/图生视频/2072568558659391490.json、视频生成/图生视频/2056571721142071298.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LTXVAudioVAEDecode` —— 16/17 个有
- `LTXVCropGuides` —— 16/17 个有
- `LoraLoaderModelOnly` —— 14/17 个有
- `VHS_VideoCombine` —— 12/17 个有
- `CreateVideo` —— 11/17 个有
- `LTX2SamplingPreviewOverride` —— 10/17 个有
- `UNETLoader` —— 9/17 个有
- `VAEDecodeTiled` —— 9/17 个有
- `VAEDecode` —— 8/17 个有
- `CheckpointLoaderSimple` —— 7/17 个有
- `GetNode` —— 6/17 个有
- `ManualSigmas` —— 6/17 个有
- `SetNode` —— 6/17 个有
- `GetVideoComponents` —— 5/17 个有
- `SaveVideo` —— 5/17 个有
- `PrimitiveFloat` —— 4/17 个有
- `SimpleMath+` —— 4/17 个有
- `Label (rgthree)` —— 2/17 个有
- `ModelPreviewOverrideKJ` —— 2/17 个有
- `孤海注释` —— 2/17 个有
- `DiffusionModelLoaderKJ` —— 1/17 个有
- `Fast Groups Bypasser (rgthree)` —— 1/17 个有
- `LTXDirectorCropGuides` —— 1/17 个有
- `VAELoader` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
