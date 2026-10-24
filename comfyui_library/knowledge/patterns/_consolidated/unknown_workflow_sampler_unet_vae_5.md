---
name: unknown_workflow_sampler_unet_vae_5
type: Unknown Workflow
frequency: 26
level: moderate
coverage: 0.936154
common_nodes: [BasicScheduler, CFGGuider, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3-漫剧导演工作台工作流_2078873049419571202.json, 视频生成/图生视频/LTX2.3导演台2.0Director_2072850432728326145.json, 视频生成/图生视频/LTX2.3导演台_音频驱动_修复版_2073964076115513345.json, 视频生成/图生视频/LTX_2.3_Director_2.0_多功能导演台7.11优化版工作流_2088158819493961729.json, 视频生成/图生视频/LTX_Director_2-修复版_2073922895696453634.json, 视频生成/图生视频/LTX_Director_2_Workflow_FL_frame首尾帧_2072254537259372546.json, 视频生成/图生视频/LTX_Director_2_Workflow_extend_video视频延长_2072252924708872193.json, 视频生成/图生视频/LTX_Director_2_Workflow_iclora_edit_video视频编辑_2072255653216874498.json, 视频生成/图生视频/LTX_Director_2_多参_2074755278909820930.json, 视频生成/图生视频/LTX_Director_2_视频编辑_2072931950360350721.json, 视频生成/图生视频/LTX_Director_2_视频编辑_2073226755028119553.json, 视频生成/图生视频/LTX_Director_V2.0升级版导演台节点工作流_2068690343561879554.json, 视频生成/图生视频/LTX_Director_V2.0升级版导演台节点工作流_2068939406005854210.json, 视频生成/图生视频/LTX_Director_V2.0升级版导演台节点工作流【加速版】_2068922121077747714.json, 视频生成/图生视频/LTX导演台2.0+3DREAK-白模驱动视频工作流_2074134750515777537.json, 视频生成/图生视频/LTX导演台2.0+3DREAK-白模驱动视频工作流_2074150490602033154.json, 视频生成/图生视频/LTX导演台2.0+3DREAK-白模驱动视频工作流_2074307854646996994.json, 视频生成/图生视频/LTX导演台2.0_2069677041460539394.json, 视频生成/图生视频/LTX导演台2.0剪辑台LTX Director_2069021020295618562.json, 视频生成/图生视频/LTX导演台2.0剪辑台LTX Director_2076638289418870785.json, 视频生成/图生视频/LTX导演台2.0剪辑台LTX Director_2082428035797708802.json, 视频生成/图生视频/LTX导演台2.0白模驱动视频工作流_2074291321979891714.json, 视频生成/图生视频/LTX导演台2.0白模驱动视频工作流_2074299424884477953.json, 视频生成/图生视频/人脸一致性-LTX导演台2.0+dasiwaV3_2075476336205983745.json, 视频生成/文生视频/LTX导演台2.0【Director】优化工作流已修复_2060326139540885505.json, 视频生成/文生视频/LTX导演台2.0【Director】视频延长+编辑_2069229270215516161.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_5

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-漫剧导演工作台工作流_2078873049419571202.json、视频生成/图生视频/LTX2.3导演台2.0Director_2072850432728326145.json、视频生成/图生视频/LTX2.3导演台_音频驱动_修复版_2073964076115513345.json、视频生成/图生视频/LTX_2.3_Director_2.0_多功能导演台7.11优化版工作流_2088158819493961729.json、视频生成/图生视频/LTX_Director_2-修复版_2073922895696453634.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 26 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 25/26 个有
- `LTXVConditioning` —— 25/26 个有
- `VAEDecode` —— 25/26 个有
- `LTXDirectorCropGuides` —— 24/26 个有
- `LTXVLatentUpsampler` —— 24/26 个有
- `LatentUpscaleModelLoader` —— 24/26 个有
- `ModelPreviewOverrideKJ` —— 24/26 个有
- `VAELoader` —— 24/26 个有
- `CreateVideo` —— 22/26 个有
- `SaveVideo` —— 19/26 个有
- `VHS_VideoCombine` —— 10/26 个有
- `LoraLoaderModelOnly` —— 9/26 个有
- `CLIPTextEncode` —— 6/26 个有
- `LoadImage` —— 6/26 个有
- `GetVideoComponents` —— 5/26 个有
- `LTX2_NAG` —— 5/26 个有
- `TTResolutionSelector` —— 3/26 个有
- `VRAM_Debug` —— 3/26 个有
- `GetNode` —— 2/26 个有
- `SetNode` —— 2/26 个有
- `LTX2SamplingPreviewOverride` —— 1/26 个有
- `LiconMSR` —— 1/26 个有
- `PathchSageAttentionKJ` —— 1/26 个有
- `VAEDecodeTiled` —— 1/26 个有
- `easy cleanGpuUsed` —— 1/26 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
