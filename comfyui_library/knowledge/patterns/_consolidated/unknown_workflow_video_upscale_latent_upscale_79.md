---
name: unknown_workflow_video_upscale_latent_upscale_79
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.723
common_nodes: [BasicScheduler, CFGGuider, DualCLIPLoader, KSamplerSelect, LTXDirector, LTXDirectorGuide, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/工作流基础系列29-LTX 2.3+Director导演台_2085570972542922754.json, 视频生成/图生视频/电商图片音频提示词生成视频 LtxDirector_2059242196313919490.json, 视频生成/文生视频/LTX2.3导演台2.0工作流_2081613434218700801.json, 视频生成/文生视频/LTX2.3导演台V2_2081573363293708290.json, 视频生成/文生视频/工作流基础系列29-LTX 2.3+Director导演台_2064315632790892545.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_79

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/工作流基础系列29-LTX 2.3+Director导演台_2085570972542922754.json、视频生成/图生视频/电商图片音频提示词生成视频 LtxDirector_2059242196313919490.json、视频生成/文生视频/LTX2.3导演台2.0工作流_2081613434218700801.json、视频生成/文生视频/LTX2.3导演台V2_2081573363293708290.json、视频生成/文生视频/工作流基础系列29-LTX 2.3+Director导演台_2064315632790892545.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `DualCLIPLoader`
- `KSamplerSelect`
- `LTXDirector`
- `LTXDirectorGuide`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `CLIPTextEncode` —— 3/5 个有
- `GetNode` —— 3/5 个有
- `LTX2_NAG` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `ConditioningZeroOut` —— 2/5 个有
- `Label (rgthree)` —— 2/5 个有
- `LoadImage` —— 2/5 个有
- `ManualSigmas` —— 2/5 个有
- `PreviewAudio` —— 2/5 个有
- `BatchCount+` —— 1/5 个有
- `DNode_CameraShakeLissajous` —— 1/5 个有
- `ImageFromBatch` —— 1/5 个有
- `LTX2SamplingPreviewOverride` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
