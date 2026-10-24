---
name: unknown_workflow_sampler_vae_34
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.928429
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3-图生视频+导演分镜节点2.0_2070497842334097410.json, 视频生成/图生视频/LTX2.3-图生视频+导演分镜节点_2055988767751720962.json, 视频生成/图生视频/LTX2.3-图生视频+导演分镜节点（自定义音频版）_2056019458614931458.json, 视频生成/图生视频/LTX2.3全流程导演台！_2056659960074956802.json, 视频生成/图生视频/LTX2.3导演台分镜数字人_2086131734063702018.json, 视频生成/图生视频/LTX2.3脱口秀导演台_2080600442291183617.json, 视频生成/图生视频/ltx2.3导演台_2061378483611328514.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_34

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-图生视频+导演分镜节点2.0_2070497842334097410.json、视频生成/图生视频/LTX2.3-图生视频+导演分镜节点_2055988767751720962.json、视频生成/图生视频/LTX2.3-图生视频+导演分镜节点（自定义音频版）_2056019458614931458.json、视频生成/图生视频/LTX2.3全流程导演台！_2056659960074956802.json、视频生成/图生视频/LTX2.3导演台分镜数字人_2086131734063702018.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 6/7 个有
- `LTXVAudioVAEDecode` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `PathchSageAttentionKJ` —— 5/7 个有
- `CreateVideo` —— 4/7 个有
- `SaveVideo` —— 4/7 个有
- `VHS_VideoCombine` —— 3/7 个有
- `ComfySwitchNode` —— 2/7 个有
- `DiffusionModelLoaderKJ` —— 2/7 个有
- `LTXVLatentUpsampler` —— 2/7 个有
- `LatentUpscaleModelLoader` —— 2/7 个有
- `ModelPatchTorchSettings` —— 2/7 个有
- `TTResolutionSelector` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `GetNode` —— 1/7 个有
- `ModelPreviewOverrideKJ` —— 1/7 个有
- `SetNode` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
