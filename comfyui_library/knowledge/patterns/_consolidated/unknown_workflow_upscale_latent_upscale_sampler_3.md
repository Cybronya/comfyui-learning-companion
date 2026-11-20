---
name: unknown_workflow_upscale_latent_upscale_sampler_3
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.949583
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, RandomNoise, SamplerCustomAdvanced, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3导演台分镜数字人_2086131734063702018.json, 视频生成/图生视频/LTX2.3导演工作流【运镜&分镜编辑】_2059858506483847169.json, 视频生成/图生视频/LTX2.3导演工作流自定义分镜更随心_2057286566376202241.json, 视频生成/图生视频/LTX2.3导演工作流自定义分镜随心所欲_2058019383724830722.json, 视频生成/图生视频/LTX2.3脱口秀导演台_2080600442291183617.json, 视频生成/图生视频/LTX_2.3_Director_2.0_多功能导演台7.11优化版工作流_2088158819493961729.json, 视频生成/图生视频/LTX_Director_2_Workflow_FL_frame首尾帧_2072254537259372546.json, 视频生成/图生视频/LTX_Director_2_Workflow_extend_video视频延长_2072252924708872193.json, 视频生成/图生视频/LTX_Director_2_Workflow_iclora_edit_video视频编辑_2072255653216874498.json, 视频生成/图生视频/LTX_Director_2_多参_2074755278909820930.json, 视频生成/图生视频/LTX_Director_2_视频编辑_2072931950360350721.json, 视频生成/图生视频/LTX_Director_2_视频编辑_2073226755028119553.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_3

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/LTX2.3导演台分镜数字人_2086131734063702018.json、视频生成/图生视频/LTX2.3导演工作流【运镜&分镜编辑】_2059858506483847169.json、视频生成/图生视频/LTX2.3导演工作流自定义分镜更随心_2057286566376202241.json、视频生成/图生视频/LTX2.3导演工作流自定义分镜随心所欲_2058019383724830722.json、视频生成/图生视频/LTX2.3脱口秀导演台_2080600442291183617.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 12 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LTXVConditioning` —— 11/12 个有
- `CreateVideo` —— 10/12 个有
- `SaveVideo` —— 10/12 个有
- `UNETLoader` —— 9/12 个有
- `LTXVAudioVAEDecode` —— 8/12 个有
- `LoraLoaderModelOnly` —— 8/12 个有
- `LTXDirectorCropGuides` —— 7/12 个有
- `VAEDecode` —— 7/12 个有
- `ModelPreviewOverrideKJ` —— 6/12 个有
- `VAELoader` —— 6/12 个有
- `LTXVCropGuides` —— 5/12 个有
- `VAEDecodeTiled` —— 5/12 个有
- `CheckpointLoaderSimple` —— 3/12 个有
- `LTX2SamplingPreviewOverride` —— 3/12 个有
- `LoadImage` —— 3/12 个有
- `VHS_VideoCombine` —— 3/12 个有
- `VRAM_Debug` —— 3/12 个有
- `ModelPatchTorchSettings` —— 2/12 个有
- `PathchSageAttentionKJ` —— 2/12 个有
- `GetNode` —— 1/12 个有
- `LiconMSR` —— 1/12 个有
- `SetNode` —— 1/12 个有
- `TTResolutionSelector` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
