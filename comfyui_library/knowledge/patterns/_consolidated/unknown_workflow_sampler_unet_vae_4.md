---
name: unknown_workflow_sampler_unet_vae_4
type: Unknown Workflow
frequency: 24
level: moderate
coverage: 0.924208
common_nodes: [BasicScheduler, CFGGuider, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/2078873049419571202.json, 视频生成/图生视频/2072850432728326145.json, 视频生成/图生视频/2073964076115513345.json, 视频生成/图生视频/LTX_2.3_Director_2.0_多功能导演台7.11优化版工作流_2088158819493961729.json, 视频生成/图生视频/2073922895696453634.json, 视频生成/图生视频/2072254537259372546.json, 视频生成/图生视频/2072252924708872193.json, 视频生成/图生视频/2072255653216874498.json, 视频生成/图生视频/2074755278909820930.json, 视频生成/图生视频/2072931950360350721.json, 视频生成/图生视频/2073226755028119553.json, 视频生成/图生视频/2068690343561879554.json, 视频生成/图生视频/2068939406005854210.json, 视频生成/图生视频/2068922121077747714.json, 视频生成/图生视频/2074134750515777537.json, 视频生成/图生视频/2074150490602033154.json, 视频生成/图生视频/2074307854646996994.json, 视频生成/图生视频/2069677041460539394.json, 视频生成/图生视频/LTX导演台2.0剪辑台LTX Director_2069021020295618562.json, 视频生成/图生视频/2076638289418870785.json, 视频生成/图生视频/2082428035797708802.json, 视频生成/图生视频/2074291321979891714.json, 视频生成/图生视频/2074299424884477953.json, 视频生成/图生视频/工作流基础系列29-LTX 2.3+Director导演台_2085570972542922754.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_4

> 由 `engine/knowledge_consolidation` 从 24 个 workflow 归纳得出（视频生成/图生视频/2078873049419571202.json、视频生成/图生视频/2072850432728326145.json、视频生成/图生视频/2073964076115513345.json、视频生成/图生视频/LTX_2.3_Director_2.0_多功能导演台7.11优化版工作流_2088158819493961729.json、视频生成/图生视频/2073922895696453634.json…）

- **类型**：Unknown Workflow
- **样本数**：24
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 24 个 workflow 都包含：
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
- `LTXVConditioning` —— 23/24 个有
- `VAEDecode` —— 23/24 个有
- `ConditioningZeroOut` —— 22/24 个有
- `LTXVLatentUpsampler` —— 22/24 个有
- `LatentUpscaleModelLoader` —— 22/24 个有
- `CreateVideo` —— 21/24 个有
- `LTXDirectorCropGuides` —— 21/24 个有
- `ModelPreviewOverrideKJ` —— 21/24 个有
- `VAELoader` —— 21/24 个有
- `SaveVideo` —— 18/24 个有
- `VHS_VideoCombine` —— 9/24 个有
- `LoraLoaderModelOnly` —— 7/24 个有
- `CLIPTextEncode` —— 5/24 个有
- `GetVideoComponents` —— 5/24 个有
- `LoadImage` —— 5/24 个有
- `LTX2_NAG` —— 4/24 个有
- `GetNode` —— 3/24 个有
- `SetNode` —— 3/24 个有
- `VRAM_Debug` —— 3/24 个有
- `TTResolutionSelector` —— 2/24 个有
- `LTXVCropGuides` —— 1/24 个有
- `Label (rgthree)` —— 1/24 个有
- `LiconMSR` —— 1/24 个有
- `PreviewAudio` —— 1/24 个有
- `VAEDecodeTiled` —— 1/24 个有
- `easy cleanGpuUsed` —— 1/24 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
