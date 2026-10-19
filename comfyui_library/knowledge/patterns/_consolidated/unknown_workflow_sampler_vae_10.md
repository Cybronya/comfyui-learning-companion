---
name: unknown_workflow_sampler_vae_10
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.96905
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVConcatAVLatent, LTXVConditioning, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/2073044076907294721.json, 视频生成/图生视频/2070497842334097410.json, 视频生成/图生视频/2055988767751720962.json, 视频生成/图生视频/2056019458614931458.json, 视频生成/图生视频/2056659960074956802.json, 视频生成/图生视频/2055283011867947010.json, 视频生成/图生视频/2055157039688634370.json, 视频生成/图生视频/2059896575970861058.json, 视频生成/图生视频/LTX2.3导演台分镜数字人_2086131734063702018.json, 视频生成/图生视频/2057726231881281537.json, 视频生成/图生视频/2080600442291183617.json, 视频生成/图生视频/2058649918318923777.json, 视频生成/图生视频/2055635483195133953.json, 视频生成/图生视频/2061446032973713410.json, 视频生成/图生视频/2075476336205983745.json, 视频生成/图生视频/2072669818989404161.json, 视频生成/图生视频/2069660528036892673.json, 视频生成/文生视频/LTX Director 2.0：全能视频编辑与导演时间线_2068936813363941377.json, 视频生成/文生视频/LTX Director导演台工作流_2066167001793515521.json, 视频生成/文生视频/LTX2.3导演分镜_2055938221086912513.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_10

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/2073044076907294721.json、视频生成/图生视频/2070497842334097410.json、视频生成/图生视频/2055988767751720962.json、视频生成/图生视频/2056019458614931458.json、视频生成/图生视频/2056659960074956802.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 20 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LTXVAudioVAEDecode` —— 18/20 个有
- `LTXVCropGuides` —— 16/20 个有
- `LTXVLatentUpsampler` —— 16/20 个有
- `LatentUpscaleModelLoader` —— 16/20 个有
- `LoraLoaderModelOnly` —— 16/20 个有
- `CreateVideo` —— 14/20 个有
- `SaveVideo` —— 14/20 个有
- `UNETLoader` —— 13/20 个有
- `VAEDecodeTiled` —— 12/20 个有
- `LTX2SamplingPreviewOverride` —— 10/20 个有
- `PathchSageAttentionKJ` —— 10/20 个有
- `CheckpointLoaderSimple` —— 9/20 个有
- `VAEDecode` —— 8/20 个有
- `VHS_VideoCombine` —— 7/20 个有
- `ModelPreviewOverrideKJ` —— 5/20 个有
- `Fast Groups Bypasser (rgthree)` —— 4/20 个有
- `LTXDirectorCropGuides` —— 4/20 个有
- `VAELoader` —— 4/20 个有
- `ComfySwitchNode` —— 2/20 个有
- `ModelPatchTorchSettings` —— 2/20 个有
- `TTResolutionSelector` —— 2/20 个有
- `DiffusionModelLoaderKJ` —— 1/20 个有
- `ImpactSwitch` —— 1/20 个有
- `LoadImage` —— 1/20 个有
- `Text` —— 1/20 个有
- `easy cleanGpuUsed` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
