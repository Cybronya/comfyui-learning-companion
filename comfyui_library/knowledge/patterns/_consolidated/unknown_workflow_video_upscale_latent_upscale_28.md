---
name: unknown_workflow_video_upscale_latent_upscale_28
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.811667
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine, easy int, easy showAnything]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.3-动漫风格-文生视频_2056725499799490562.json, 视频生成/文生视频/LTX2.3-古风仙侠-修仙风格-文生视频工作流_2043222692043689985.json, 视频生成/文生视频/LTX2.3-古风仙侠-修仙风格-文生视频工作流_2046668664065236993.json, 视频生成/文生视频/LTX2.3-文生视频+提示词把控时间轴分镜_2064245211223646210.json, 视频生成/文生视频/LTX2.3-文生视频工作流-官方版_2039703712691658754.json, 视频生成/文生视频/LTX2.3-文生视频工作流-官方版_2050760001458847745.json, 视频生成/文生视频/LTX2.3-文生视频工作流-官方版_2059990321597079554.json, 视频生成/文生视频/LTX2.3-文生视频工作流_2042126629517926402.json, 视频生成/文生视频/LTX2.3-文生视频工作流_2067565937770983426.json, 视频生成/文生视频/LTX2.3板块：首尾帧工作流_2050777299921973250.json, 视频生成/文生视频/加速版文生视频_2044733727841980418.json, 视频生成/文生视频/文生视频 加速版 LTX2.3 多角色对话 数字人说话唱歌_2043136851845844993.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_28

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/LTX2.3-动漫风格-文生视频_2056725499799490562.json、视频生成/文生视频/LTX2.3-古风仙侠-修仙风格-文生视频工作流_2043222692043689985.json、视频生成/文生视频/LTX2.3-古风仙侠-修仙风格-文生视频工作流_2046668664065236993.json、视频生成/文生视频/LTX2.3-文生视频+提示词把控时间轴分镜_2064245211223646210.json、视频生成/文生视频/LTX2.3-文生视频工作流-官方版_2039703712691658754.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LTXVScheduler` —— 11/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/12 个有
- `SimpleMath+` —— 7/12 个有
- `EmptyImage` —— 6/12 个有
- `easy float` —— 6/12 个有
- `PrimitiveInt` —— 5/12 个有
- `GetNode` —— 1/12 个有
- `ImageResize+` —— 1/12 个有
- `LTX2_NAG` —— 1/12 个有
- `LTXVAddGuide` —— 1/12 个有
- `LTXVImgToVideoInplace` —— 1/12 个有
- `LTXVPreprocess` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有
- `LoadImage` —— 1/12 个有
- `SetNode` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 12 | 100% |
| 高度 | 24 | 24 - 25 | 12 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，12 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 25，12 个样本，取值集中（一致性 99%）
