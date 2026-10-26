---
name: unknown_workflow_upscale_latent_upscale_sampler_4
type: Unknown Workflow
frequency: 17
level: moderate
coverage: 0.840176
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, RandomNoise, SamplerCustomAdvanced, VAELoaderKJ]
problems: []
missing: []
members: [数字人/数字人/LTX2.3导演台分镜数字人V2_2073127023752601601.json, 数字人/数字人/LTX2.3导演台分镜数字人（新版导演台）_2063554511314186242.json, 视频生成/图生视频/LTX Director-i2v-prompt_replay-fixed_2057141350105178114.json, 视频生成/图生视频/LTX Director_2060889846209662978.json, 视频生成/图生视频/LTX2.3 Director图生视频_2058931295174086657.json, 视频生成/图生视频/LTX2.3 director v2.0 IC lora编辑视频_2071771328843173890.json, 视频生成/图生视频/LTX2.3 director v2.0复刻视频视频_2073210554319200257.json, 视频生成/图生视频/LTX2.3 director v2.0常规生视频_2072568558659391490.json, 视频生成/图生视频/LTX2.3 director_2056571721142071298.json, 视频生成/图生视频/LTX2.3 director导演剪辑版_2061086858423136258.json, 视频生成/图生视频/LTX2.3 全能导演分镜-更强的控制性_2055524487839404034.json, 视频生成/图生视频/LTX2.3导演台分镜数字人_2086131734063702018.json, 视频生成/图生视频/LTX2.3脱口秀导演台_2080600442291183617.json, 视频生成/图生视频/ltx导演节点_2057350661624393729.json, 视频生成/图生视频/图片+音频多参生视频——Ltx2.3 All In One 导演级操控_2055531778017906689.json, 视频生成/图生视频/完美掌控LTX2.3-LTX Director-导演版分镜工作流-更强的控制性_2067766430577287169.json, 视频生成/图生视频/超好玩LTX2.3导演控制台-运镜分镜-不传音频版v2.0_2056028640659427329.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_4

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（数字人/数字人/LTX2.3导演台分镜数字人V2_2073127023752601601.json、数字人/数字人/LTX2.3导演台分镜数字人（新版导演台）_2063554511314186242.json、视频生成/图生视频/LTX Director-i2v-prompt_replay-fixed_2057141350105178114.json、视频生成/图生视频/LTX Director_2060889846209662978.json、视频生成/图生视频/LTX2.3 Director图生视频_2058931295174086657.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：中等可信
- **平均知识覆盖**：84%

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
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `VHS_VideoCombine` —— 16/17 个有
- `LoraLoaderModelOnly` —— 15/17 个有
- `LTXVAudioVAEDecode` —— 13/17 个有
- `UNETLoader` —— 11/17 个有
- `VAEDecode` —— 9/17 个有
- `ManualSigmas` —— 8/17 个有
- `VAEDecodeTiled` —— 8/17 个有
- `CheckpointLoaderSimple` —— 5/17 个有
- `GetNode` —— 5/17 个有
- `LTX2SamplingPreviewOverride` —— 5/17 个有
- `SetNode` —— 5/17 个有
- `CreateVideo` —— 4/17 个有
- `PathchSageAttentionKJ` —— 4/17 个有
- `LoadImage` —— 3/17 个有
- `ModelPatchTorchSettings` —— 3/17 个有
- `ImpactSwitch` —— 2/17 个有
- `Int` —— 2/17 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/17 个有
- `SaveVideo` —— 2/17 个有
- `DiffusionModelLoaderKJ` —— 1/17 个有
- `GetVideoComponents` —— 1/17 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
