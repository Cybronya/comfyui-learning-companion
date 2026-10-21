---
name: unknown_workflow_sampler_vae_9
type: Unknown Workflow
frequency: 27
level: moderate
coverage: 0.957556
common_nodes: [BasicScheduler, CFGGuider, ConditioningZeroOut, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced]
problems: []
missing: []
members: [视频生成/图生视频/2068690343561879554.json, 视频生成/图生视频/2068939406005854210.json, 视频生成/图生视频/2068922121077747714.json, 视频生成/图生视频/2074134750515777537.json, 视频生成/图生视频/2074150490602033154.json, 视频生成/图生视频/2074307854646996994.json, 视频生成/图生视频/2069677041460539394.json, 视频生成/图生视频/LTX导演台2.0剪辑台LTX Director_2069021020295618562.json, 视频生成/图生视频/2076638289418870785.json, 视频生成/图生视频/2082428035797708802.json, 视频生成/图生视频/2074291321979891714.json, 视频生成/图生视频/2074299424884477953.json, 视频生成/图生视频/2059276164383985666.json, 视频生成/图生视频/2057350661624393729.json, 视频生成/图生视频/2064886980097429505.json, 视频生成/图生视频/2073289175195205632.json, 视频生成/图生视频/2059132036383858689.json, 视频生成/图生视频/2058003640417349634.json, 视频生成/图生视频/2075476336205983745.json, 视频生成/图生视频/2055095279413669890.json, 视频生成/图生视频/2067766430577287169.json, 视频生成/图生视频/2072669818989404161.json, 视频生成/图生视频/2069660528036892673.json, 视频生成/图生视频/2056028640659427329.json, 视频生成/文生视频/LTX Director 2.0：全能视频编辑与导演时间线_2068936813363941377.json, 视频生成/文生视频/LTX2.3-LTX Director 2.0-导演分镜工作流-文生视频_2075921500900782081.json, 视频生成/文生视频/LTX2.3导演台V2+图生视频工作流_2072015806417956866.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_9

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（视频生成/图生视频/2068690343561879554.json、视频生成/图生视频/2068939406005854210.json、视频生成/图生视频/2068922121077747714.json、视频生成/图生视频/2074134750515777537.json、视频生成/图生视频/2074150490602033154.json…）

- **类型**：Unknown Workflow
- **样本数**：27
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 27 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `VAELoaderKJ` —— 26/27 个有
- `CreateVideo` —— 25/27 个有
- `LTXVLatentUpsampler` —— 23/27 个有
- `LatentUpscaleModelLoader` —— 23/27 个有
- `VAEDecode` —— 23/27 个有
- `UNETLoader` —— 21/27 个有
- `SaveVideo` —— 20/27 个有
- `ModelPreviewOverrideKJ` —— 18/27 个有
- `VAELoader` —— 18/27 个有
- `LTXDirectorCropGuides` —— 16/27 个有
- `LoraLoaderModelOnly` —— 12/27 个有
- `LTX2SamplingPreviewOverride` —— 9/27 个有
- `LTXVCropGuides` —— 9/27 个有
- `VHS_VideoCombine` —— 9/27 个有
- `CheckpointLoaderSimple` —— 6/27 个有
- `GetVideoComponents` —— 6/27 个有
- `VAEDecodeTiled` —— 4/27 个有
- `PathchSageAttentionKJ` —— 2/27 个有
- `LTXVAudioVAELoader` —— 1/27 个有
- `LoadImage` —— 1/27 个有
- `TTResolutionSelector` —— 1/27 个有
- `Text` —— 1/27 个有
- `孤海注释` —— 1/27 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
