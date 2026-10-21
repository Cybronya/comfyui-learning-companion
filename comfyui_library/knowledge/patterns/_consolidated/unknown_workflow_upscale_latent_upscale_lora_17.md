---
name: unknown_workflow_upscale_latent_upscale_lora_17
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.955846
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/2078085536597757954.json, 视频生成/图生视频/2056974345699942402.json, 视频生成/图生视频/2059911251098165250.json, 视频生成/图生视频/2059273921228263425.json, 视频生成/图生视频/2060383965181202433.json, 视频生成/图生视频/2057720205580783618.json, 视频生成/图生视频/2055283011867947010.json, 视频生成/图生视频/2055157039688634370.json, 视频生成/图生视频/2059858506483847169.json, 视频生成/图生视频/2057286566376202241.json, 视频生成/图生视频/2058019383724830722.json, 视频生成/图生视频/2055639215265861633.json, 视频生成/图生视频/2059458319999397889.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_17

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/2078085536597757954.json、视频生成/图生视频/2056974345699942402.json、视频生成/图生视频/2059911251098165250.json、视频生成/图生视频/2059273921228263425.json、视频生成/图生视频/2060383965181202433.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 12/13 个有
- `CreateVideo` —— 12/13 个有
- `LTX2SamplingPreviewOverride` —— 12/13 个有
- `LTXVAudioVAEDecode` —— 10/13 个有
- `SaveVideo` —— 7/13 个有
- `VHS_VideoCombine` —— 7/13 个有
- `GetVideoComponents` —— 5/13 个有
- `PrimitiveFloat` —— 5/13 个有
- `SimpleMath+` —— 4/13 个有
- `ModelPreviewOverrideKJ` —— 2/13 个有
- `孤海注释` —— 2/13 个有
- `DiffusionModelLoaderKJ` —— 1/13 个有
- `LTXFloatToInt` —— 1/13 个有
- `Label (rgthree)` —— 1/13 个有
- `LayerUtility: ColorImage` —— 1/13 个有
- `SaveAudio` —— 1/13 个有
- `UNETLoader` —— 1/13 个有
- `easy imageSize` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
