---
name: unknown_workflow_upscale_latent_upscale_sampler_2
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.956375
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, RandomNoise, SamplerCustomAdvanced, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 数字人 导演台分镜（最新版）_2078085536597757954.json, 视频生成/图生视频/LTX2.3--导演运镜--自定义分镜_2055900601728421889.json, 视频生成/图生视频/LTX2.3-Director 导演台节点-多图慢剧视频_2057459285617102849.json, 视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-华强买瓜版_2056974345699942402.json, 视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-华强买瓜版_2059911251098165250.json, 视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-大话西游版_2059273921228263425.json, 视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-歌曲《再见》_2060383965181202433.json, 视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-电商带货_2057720205580783618.json, 视频生成/图生视频/LTX2.3导演AI版的剪映版全能控制台-运镜分镜一网打进_2055283011867947010.json, 视频生成/图生视频/LTX2.3导演分镜工作流（支持多图+多个音频）自由编辑_2055157039688634370.json, 视频生成/图生视频/LTX2.3导演台工作流、短剧多分镜编辑合并、多人对口型 、数字人唱歌_2057726231881281537.json, 视频生成/图生视频/LTX2.3导演工作流【运镜&分镜编辑】_2059858506483847169.json, 视频生成/图生视频/LTX2.3导演工作流自定义分镜更随心_2057286566376202241.json, 视频生成/图生视频/LTX2.3导演工作流自定义分镜随心所欲_2058019383724830722.json, 视频生成/图生视频/LTX导演台工作流_2055076989958139906.json, 视频生成/图生视频/完美掌控LTX2.3-LTX Director-导演版分镜工作流-更强的控制性_2067766430577287169.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_2

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 数字人 导演台分镜（最新版）_2078085536597757954.json、视频生成/图生视频/LTX2.3--导演运镜--自定义分镜_2055900601728421889.json、视频生成/图生视频/LTX2.3-Director 导演台节点-多图慢剧视频_2057459285617102849.json、视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-华强买瓜版_2056974345699942402.json、视频生成/图生视频/LTX2.3-LTX Director-导演分镜工作流-更强的控制性-华强买瓜版_2059911251098165250.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 16 个 workflow 都包含：
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
- `CreateVideo` —— 15/16 个有
- `LTX2SamplingPreviewOverride` —— 15/16 个有
- `LoraLoaderModelOnly` —— 15/16 个有
- `VAEDecodeTiled` —— 15/16 个有
- `CheckpointLoaderSimple` —— 14/16 个有
- `LTXVAudioVAEDecode` —— 13/16 个有
- `SaveVideo` —— 9/16 个有
- `VHS_VideoCombine` —— 8/16 个有
- `GetVideoComponents` —— 6/16 个有
- `PrimitiveFloat` —— 4/16 个有
- `SimpleMath+` —— 4/16 个有
- `ModelPreviewOverrideKJ` —— 2/16 个有
- `孤海注释` —— 2/16 个有
- `DiffusionModelLoaderKJ` —— 1/16 个有
- `ImpactSwitch` —— 1/16 个有
- `Int` —— 1/16 个有
- `Label (rgthree)` —— 1/16 个有
- `LoadImage` —— 1/16 个有
- `UNETLoader` —— 1/16 个有
- `VAEDecode` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
