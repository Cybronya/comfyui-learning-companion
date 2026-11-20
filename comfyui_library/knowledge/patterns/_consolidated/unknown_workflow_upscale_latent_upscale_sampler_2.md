---
name: unknown_workflow_upscale_latent_upscale_sampler_2
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.8422
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, RandomNoise, SamplerCustomAdvanced, VAELoaderKJ]
problems: []
missing: []
members: [数字人/数字人/LTX2.3导演台分镜数字人V2_2073127023752601601.json, 数字人/数字人/LTX2.3导演台分镜数字人（新版导演台）_2063554511314186242.json, 视频生成/图生视频/LTX Director-i2v-prompt_replay-fixed_2057141350105178114.json, 视频生成/图生视频/LTX Director_2060889846209662978.json, 视频生成/图生视频/LTX2.3 Director图生视频_2058931295174086657.json, 视频生成/图生视频/LTX2.3 director v2.0 IC lora编辑视频_2071771328843173890.json, 视频生成/图生视频/LTX2.3 director v2.0复刻视频视频_2073210554319200257.json, 视频生成/图生视频/LTX2.3 director v2.0常规生视频_2072568558659391490.json, 视频生成/图生视频/LTX2.3 director_2056571721142071298.json, 视频生成/图生视频/LTX2.3 director导演剪辑版_2061086858423136258.json, 视频生成/图生视频/LTX2.3 创新导演剪辑流，创意无限！二创神器！_2055482875381862402.json, 视频生成/图生视频/LTX2.3 数字人 导演台分镜（最新版）_2078085536597757954.json, 视频生成/图生视频/LTX2.3--导演运镜--自定义分镜_2055900601728421889.json, 视频生成/图生视频/LTX2.3-Director 导演台节点-多图慢剧视频_2057459285617102849.json, 视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-华强买瓜版_2056974345699942402.json, 视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-华强买瓜版_2059911251098165250.json, 视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-大话西游版_2059273921228263425.json, 视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-歌曲《再见》_2060383965181202433.json, 视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-电商带货_2057720205580783618.json, 视频生成/图生视频/LTX2.3导演台功能_vbvr提示词优化_2055094635088891905.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_2

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（数字人/数字人/LTX2.3导演台分镜数字人V2_2073127023752601601.json、数字人/数字人/LTX2.3导演台分镜数字人（新版导演台）_2063554511314186242.json、视频生成/图生视频/LTX Director-i2v-prompt_replay-fixed_2057141350105178114.json、视频生成/图生视频/LTX Director_2060889846209662978.json、视频生成/图生视频/LTX2.3 Director图生视频_2058931295174086657.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：84%

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
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LTXVAudioVAEDecode` —— 17/20 个有
- `LoraLoaderModelOnly` —— 17/20 个有
- `VHS_VideoCombine` —— 16/20 个有
- `UNETLoader` —— 11/20 个有
- `VAEDecodeTiled` —— 11/20 个有
- `CreateVideo` —— 10/20 个有
- `LTX2SamplingPreviewOverride` —— 9/20 个有
- `VAEDecode` —— 9/20 个有
- `ManualSigmas` —— 8/20 个有
- `CheckpointLoaderSimple` —— 7/20 个有
- `GetNode` —— 6/20 个有
- `SetNode` —— 6/20 个有
- `GetVideoComponents` —— 5/20 个有
- `PrimitiveFloat` —— 4/20 个有
- `SaveVideo` —— 4/20 个有
- `SimpleMath+` —— 4/20 个有
- `DiffusionModelLoaderKJ` —— 2/20 个有
- `ModelPreviewOverrideKJ` —— 2/20 个有
- `孤海注释` —— 2/20 个有
- `Label (rgthree)` —— 1/20 个有
- `ModelPatchTorchSettings` —— 1/20 个有
- `PathchSageAttentionKJ` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
