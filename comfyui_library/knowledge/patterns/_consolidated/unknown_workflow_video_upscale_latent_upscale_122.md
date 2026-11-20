---
name: unknown_workflow_video_upscale_latent_upscale_122
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.971667
common_nodes: [AudioCrop, BasicScheduler, CFGGuider, CLIPTextEncode, CM_FloatToInt, CM_IntToFloat, CR Prompt Text, CR Text, CheckpointLoaderSimple, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoraLoaderModelOnly, ManualSigmas, PreviewAudio, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, ShowAnything|Mie, SimpleMath+, SolidMask, SoundFlow_GetLength, VAEDecodeTiled, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3-图生对口型数字人-自动扩写-强化口型_2057753722972889090.json, 视频生成/图生视频/对口型说话唱歌--LTX2.3图生数字人--自动扩写-模块优化-无字幕_2038618856104665090.json, 视频生成/文生视频/文生对口型视频--说话唱歌--LTX2.3文生数字人--无字幕-模块优化_2038618886479814658.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_122

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/LTX2.3-图生对口型数字人-自动扩写-强化口型_2057753722972889090.json、视频生成/图生视频/对口型说话唱歌--LTX2.3图生数字人--自动扩写-模块优化-无字幕_2038618856104665090.json、视频生成/文生视频/文生对口型视频--说话唱歌--LTX2.3文生数字人--无字幕-模块优化_2038618886479814658.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `AudioCrop`
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CM_IntToFloat`
- `CR Prompt Text`
- `CR Text`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PreviewAudio`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `ShowAnything|Mie`
- `SimpleMath+`
- `SolidMask`
- `SoundFlow_GetLength`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LTXVChunkFeedForward` —— 2/3 个有
- `LTXVImgToVideoInplace` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `ModelPatchTorchSettings` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `easy int` —— 2/3 个有
- `GetImageSize` —— 1/3 个有
- `Int` —— 1/3 个有
- `LTXVPreprocess` —— 1/3 个有
- `MelBandRoFormerModelLoader` —— 1/3 个有
- `MelBandRoFormerSampler` —— 1/3 个有
- `ResizeImageMaskNode` —— 1/3 个有
- `ResizeImagesByLongerEdge` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
