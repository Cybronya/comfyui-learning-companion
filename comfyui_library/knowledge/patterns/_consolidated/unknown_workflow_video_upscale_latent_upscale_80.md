---
name: unknown_workflow_video_upscale_latent_upscale_80
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8294
common_nodes: [CFGGuider, CLIPTextEncode, CR Prompt Text, CR Text, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, SimpleMath+, VAEDecodeTiled, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3-图生对口型数字人-自动扩写-强化口型_2057753722972889090.json, 视频生成/图生视频/对口型说话唱歌--LTX2.3图生数字人--自动扩写-模块优化-无字幕_2038618856104665090.json, 视频生成/图生视频/超快速高清版LTX2.3图生视频，自动提示词。三阶采样_2044928269383897089.json, 视频生成/图生视频/超快速高清版LTX2.3图生视频，自动提示词。三阶采样_2046030109836054530.json, 视频生成/文生视频/文生对口型视频--说话唱歌--LTX2.3文生数字人--无字幕-模块优化_2038618886479814658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_80

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-图生对口型数字人-自动扩写-强化口型_2057753722972889090.json、视频生成/图生视频/对口型说话唱歌--LTX2.3图生数字人--自动扩写-模块优化-无字幕_2038618856104665090.json、视频生成/图生视频/超快速高清版LTX2.3图生视频，自动提示词。三阶采样_2044928269383897089.json、视频生成/图生视频/超快速高清版LTX2.3图生视频，自动提示词。三阶采样_2046030109836054530.json、视频生成/文生视频/文生对口型视频--说话唱歌--LTX2.3文生数字人--无字幕-模块优化_2038618886479814658.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LTXVChunkFeedForward` —— 4/5 个有
- `LTXVImgToVideoInplace` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `ModelPatchTorchSettings` —— 4/5 个有
- `PathchSageAttentionKJ` —— 4/5 个有
- `easy int` —— 4/5 个有
- `AudioCrop` —— 3/5 个有
- `BasicScheduler` —— 3/5 个有
- `CM_FloatToInt` —— 3/5 个有
- `CM_IntToFloat` —— 3/5 个有
- `INTConstant` —— 3/5 个有
- `LTXVAudioVAEEncode` —— 3/5 个有
- `LTXVPreprocess` —— 3/5 个有
- `LoadAudio` —— 3/5 个有
- `PreviewAudio` —— 3/5 个有
- `SetLatentNoiseMask` —— 3/5 个有
- `ShowAnything|Mie` —— 3/5 个有
- `SolidMask` —— 3/5 个有
- `SoundFlow_GetLength` —— 3/5 个有
- `ConcatTextOfUtils` —— 2/5 个有
- `LTXVAudioVAEDecode` —— 2/5 个有
- `LTXVEmptyLatentAudio` —— 2/5 个有
- `LTXVScheduler` —— 2/5 个有
- `easy float` —— 2/5 个有
- `GetImageSize` —— 1/5 个有
- `Int` —— 1/5 个有
- `MelBandRoFormerModelLoader` —— 1/5 个有
- `MelBandRoFormerSampler` —— 1/5 个有
- `ResizeImageMaskNode` —— 1/5 个有
- `ResizeImagesByLongerEdge` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
