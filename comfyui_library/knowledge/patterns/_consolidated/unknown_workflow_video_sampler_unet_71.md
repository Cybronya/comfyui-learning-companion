---
name: unknown_workflow_video_sampler_unet_71
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6818
common_nodes: [BasicScheduler, CFGGuider, DualCLIPLoader, GetNode, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVSeparateAVLatent, RandomNoise, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/AI代码侠土豆-LTX2.3导演台_2056245217631756289.json, 视频生成/图生视频/LTX+2.3 Director 单图关键帧工作流-用于集成_2064373452538208258.json, 视频生成/图生视频/LTX2.3-漫剧导演工作台工作流_2078873049419571202.json, 视频生成/图生视频/ltx2.3导演台_2061378483611328514.json, 视频生成/图生视频/图生视频-LTX2.3_2057271107857768450.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_71

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/AI代码侠土豆-LTX2.3导演台_2056245217631756289.json、视频生成/图生视频/LTX+2.3 Director 单图关键帧工作流-用于集成_2064373452538208258.json、视频生成/图生视频/LTX2.3-漫剧导演工作台工作流_2078873049419571202.json、视频生成/图生视频/ltx2.3导演台_2061378483611328514.json、视频生成/图生视频/图生视频-LTX2.3_2057271107857768450.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `DualCLIPLoader`
- `GetNode`
- `KSamplerSelect`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `LTXVCropGuides` —— 4/5 个有
- `TTResolutionSelector` —— 4/5 个有
- `DiffusionModelLoaderKJ` —— 3/5 个有
- `RHSettingsNode` —— 2/5 个有
- `RH_RhartImageG2TextToImage` —— 2/5 个有
- `SaveImage` —— 2/5 个有
- `Text` —— 2/5 个有
- `AppParams` —— 1/5 个有
- `CLIPTextEncode` —— 1/5 个有
- `LTXDirectorCropGuides` —— 1/5 个有
- `LTXVLatentUpsampler` —— 1/5 个有
- `LatentUpscaleModelLoader` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
