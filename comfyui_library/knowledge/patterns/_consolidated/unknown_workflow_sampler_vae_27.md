---
name: unknown_workflow_sampler_vae_27
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.952167
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LTXDirectorGuide, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, VAELoaderKJ]
problems: []
missing: []
members: [数字人/数字人/AI脱口秀_2064723957512757249.json, 数字人/数字人/AI脱口秀_2066018894162255874.json, 视频生成/图生视频/LTX2.3 数字人 导演台分镜（最新版）_2078085536597757954.json, 视频生成/图生视频/LTX2.3--导演运镜--自定义分镜_2055900601728421889.json, 视频生成/图生视频/LTX2.3-Director 导演台节点-多图慢剧视频_2057459285617102849.json, 视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-华强买瓜版_2056974345699942402.json, 视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-华强买瓜版_2059911251098165250.json, 视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-大话西游版_2059273921228263425.json, 视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-歌曲《再见》_2060383965181202433.json, 视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-电商带货_2057720205580783618.json, 视频生成/图生视频/LTX2.3导演AI版的剪映版全能控制台-运镜分镜一网打进_2055283011867947010.json, 视频生成/图生视频/LTX导演工作流_2059458319999397889.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_27

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（数字人/数字人/AI脱口秀_2064723957512757249.json、数字人/数字人/AI脱口秀_2066018894162255874.json、视频生成/图生视频/LTX2.3 数字人 导演台分镜（最新版）_2078085536597757954.json、视频生成/图生视频/LTX2.3--导演运镜--自定义分镜_2055900601728421889.json、视频生成/图生视频/LTX2.3-Director 导演台节点-多图慢剧视频_2057459285617102849.json…）

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
- `LTXDirectorGuide`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 11/12 个有
- `LTXVAudioVAEDecode` —— 11/12 个有
- `LoraLoaderModelOnly` —— 11/12 个有
- `VAEDecodeTiled` —— 11/12 个有
- `LTXDirector` —— 10/12 个有
- `LTXVLatentUpsampler` —— 10/12 个有
- `LatentUpscaleModelLoader` —— 10/12 个有
- `LTX2SamplingPreviewOverride` —— 9/12 个有
- `CheckpointLoaderSimple` —— 8/12 个有
- `VHS_VideoCombine` —— 7/12 个有
- `SaveVideo` —— 6/12 个有
- `GetVideoComponents` —— 5/12 个有
- `PrimitiveFloat` —— 5/12 个有
- `SimpleMath+` —— 4/12 个有
- `DiffusionModelLoaderKJ` —— 3/12 个有
- `ModelPreviewOverrideKJ` —— 2/12 个有
- `TTResolutionSelector` —— 2/12 个有
- `UNETLoader` —— 2/12 个有
- `Yusu-LTXDirector` —— 2/12 个有
- `孤海注释` —— 2/12 个有
- `LTXFloatToInt` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有
- `LayerUtility: ColorImage` —— 1/12 个有
- `SaveAudio` —— 1/12 个有
- `VAEDecode` —— 1/12 个有
- `easy imageSize` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
