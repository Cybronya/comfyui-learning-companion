---
name: unknown_workflow_video_lora_sampler_161
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.494857
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, INTConstant, ImageResizeKJv2, JoinStrings, KSamplerSelect, LTX2AttentionTunerPatch, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEEncode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplaceKJ, LTXVPreprocess, LTXVSeparateAVLatent, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SolidMask, TrimAudioDuration, UNETLoader, VAEDecode, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/LTX2.3数字人说话唱歌对口型+全节点注释_2054546076002209794.json, 数字人/数字人/Ltx2.3数字人说话-极速参数优化-202606_2068623008067051522.json, 数字人/数字人/ltx+tts_2077270862549577730.json, 数字人/数字人/数字人视频生成：LTX2.3 BGM+TTS优化版_2083187553284476929.json, 视频生成/图生视频/LTX2.3+音频驱动_2084104031198343170.json, 视频生成/图生视频/LTX2.3图片转数字人kj版_说话唱歌对口型_2043611581572976641.json, 视频生成/图生视频/LTX2.3图片转数字人kj版_说话唱歌对口型_2043656293486956545.json, 视频生成/图生视频/LTX2.3数字人_2044745216434900994.json, 视频生成/图生视频/LTX2.3数字人说话唱歌对口型！优化升级kj版！_2044045789097369601.json, 视频生成/图生视频/数字人带货视频LTX2.3_2083076708705587201.json, 视频生成/图生视频/数字人说话唱歌LTV2.0_图片对口型_2082357953612566530.json, 视频生成/图生视频/数字人说话唱歌LTV2.0_图片对口型_2083114579193843713.json, 视频生成/图生视频/数字人说话带货视频-文本驱动-升级版_2082813113300250626.json, 视频生成/图生视频/最新LTX2.3数字人1.1模型 数字人唱歌对口型极速版_2046477938211692546.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_161

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（数字人/数字人/LTX2.3数字人说话唱歌对口型+全节点注释_2054546076002209794.json、数字人/数字人/Ltx2.3数字人说话-极速参数优化-202606_2068623008067051522.json、数字人/数字人/ltx+tts_2077270862549577730.json、数字人/数字人/数字人视频生成：LTX2.3 BGM+TTS优化版_2083187553284476929.json、视频生成/图生视频/LTX2.3+音频驱动_2084104031198343170.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 14 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `ImageResizeKJv2`
- `JoinStrings`
- `KSamplerSelect`
- `LTX2AttentionTunerPatch`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEEncode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVImgToVideoInplaceKJ`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SolidMask`
- `TrimAudioDuration`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 13/14 个有
- `LatentUpscaleModelLoader` —— 13/14 个有
- `LayerUtility: PurgeVRAM` —— 13/14 个有
- `SimpleCalculatorKJ` —— 13/14 个有
- `ComfySwitchNode` —— 12/14 个有
- `GetImageSize` —— 12/14 个有
- `LTXVCropGuides` —— 12/14 个有
- `MelBandRoFormerModelLoader` —— 12/14 个有
- `MelBandRoFormerSampler` —— 12/14 个有
- `ResizeImageMaskNode` —— 12/14 个有
- `SimpleMath+` —— 7/14 个有
- `Compare` —— 6/14 个有
- `InversionDemoLazySwitch` —— 6/14 个有
- `easy showAnything` —— 6/14 个有
- `Int` —— 5/14 个有
- `IndexTTS2_Basic` —— 3/14 个有
- `JjkText` —— 3/14 个有
- `SaveAudio` —— 3/14 个有
- `GetAudioDurationFromAudio` —— 2/14 个有
- `1hew_AudioDuration` —— 1/14 个有
- `AudioTrim` —— 1/14 个有
- `ColorMatchV2` —— 1/14 个有
- `PreviewAudio` —— 1/14 个有
- `PreviewImage` —— 1/14 个有
- `Qwen3_VQA` —— 1/14 个有
- `RH_GetAudioDuration` —— 1/14 个有
- `RH_LLMAPI_NODE` —— 1/14 个有
- `SoundFlow_Mixer` —— 1/14 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/14 个有
- `easy indexTTSGenerateSimple` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
