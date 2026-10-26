---
name: unknown_workflow_upscale_latent_upscale_sampler_5
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.905214
common_nodes: [BasicScheduler, CFGGuider, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3-漫剧导演工作台工作流_2078873049419571202.json, 视频生成/图生视频/LTX_2.3_Director_2.0_多功能导演台7.11优化版工作流_2088158819493961729.json, 视频生成/图生视频/LTX_Director_2-修复版_2073922895696453634.json, 视频生成/图生视频/LTX_Director_2_Workflow_FL_frame首尾帧_2072254537259372546.json, 视频生成/图生视频/LTX_Director_2_Workflow_extend_video视频延长_2072252924708872193.json, 视频生成/图生视频/LTX_Director_2_Workflow_iclora_edit_video视频编辑_2072255653216874498.json, 视频生成/图生视频/LTX_Director_2_多参_2074755278909820930.json, 视频生成/图生视频/LTX_Director_2_视频编辑_2072931950360350721.json, 视频生成/图生视频/LTX_Director_2_视频编辑_2073226755028119553.json, 视频生成/图生视频/LTX_Director_V2.0升级版导演台节点工作流_2068939406005854210.json, 视频生成/图生视频/LTX导演台2.0+3DREAK-白模驱动视频工作流_2074134750515777537.json, 视频生成/图生视频/LTX导演台2.0+3DREAK-白模驱动视频工作流_2074150490602033154.json, 视频生成/图生视频/LTX导演台2.0+3DREAK-白模驱动视频工作流_2074307854646996994.json, 视频生成/图生视频/工作流基础系列29-LTX 2.3+Director导演台_2085570972542922754.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_5

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-漫剧导演工作台工作流_2078873049419571202.json、视频生成/图生视频/LTX_2.3_Director_2.0_多功能导演台7.11优化版工作流_2088158819493961729.json、视频生成/图生视频/LTX_Director_2-修复版_2073922895696453634.json、视频生成/图生视频/LTX_Director_2_Workflow_FL_frame首尾帧_2072254537259372546.json、视频生成/图生视频/LTX_Director_2_Workflow_extend_video视频延长_2072252924708872193.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LTXDirectorCropGuides` —— 13/14 个有
- `LTXVConditioning` —— 13/14 个有
- `VAEDecode` —— 13/14 个有
- `ConditioningZeroOut` —— 12/14 个有
- `CreateVideo` —— 12/14 个有
- `ModelPreviewOverrideKJ` —— 11/14 个有
- `VAELoader` —— 11/14 个有
- `SaveVideo` —— 10/14 个有
- `VHS_VideoCombine` —— 6/14 个有
- `LoadImage` —— 4/14 个有
- `LoraLoaderModelOnly` —— 4/14 个有
- `CLIPTextEncode` —— 3/14 个有
- `GetNode` —— 3/14 个有
- `GetVideoComponents` —— 3/14 个有
- `SetNode` —— 3/14 个有
- `VRAM_Debug` —— 3/14 个有
- `LTX2_NAG` —— 2/14 个有
- `TTResolutionSelector` —— 2/14 个有
- `LTXVCropGuides` —— 1/14 个有
- `Label (rgthree)` —— 1/14 个有
- `LiconMSR` —— 1/14 个有
- `PreviewAudio` —— 1/14 个有
- `VAEDecodeTiled` —— 1/14 个有
- `easy cleanGpuUsed` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
