---
name: unknown_workflow_video_upscale_latent_upscale_6
type: Unknown Workflow
frequency: 25
level: strong
coverage: 0.81032
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetNode, INTConstant, KSampler, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, PathchSageAttentionKJ, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, VAEDecodeTiled, VHS_VideoCombine, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/LTX2.3数字人=首尾帧+台本+参考音频_2050868438406582274.json, 图片生成/文生图/LTX2.3数字人（唱歌）_2046955390981644289.json, 平台全量/音频生视频 LTX2.3文生MV_2053017927036751874.json, 数字人/数字人/A-6 最佳口播数字人 LTX2.3 _ 音频驱动 _ 嘴型精准 _ 高清输出_2083957412322701313.json, 数字人/数字人/LTX2.3 数字人 文图生双模式 v1.1+VBVR_2031652480672604161.json, 数字人/数字人/LTX2.3-数字人-上传图片和音频生成电商带货数字人_2033156191248977921.json, 数字人/数字人/LTX2.3图生_文生数字人_2034265668933132290.json, 数字人/数字人/LTX2.3数字人=图片+台本+参考音频_2031237333273546754.json, 数字人/数字人/LTX2.3数字人=首尾帧+台本+参考音频_2031911940234153985.json, 数字人/数字人/LTX2.3数字人=首尾帧+台本+参考音频_2046018270754508801.json, 数字人/数字人/数字人 LTX2.3 (图片+台本+参考音频) 上手简单效果好_2032385532776423426.json, 视频生成/图生视频/005.LTX2.3音视融合002.LTX2.3图或文+音生视频_2035354663842746370.json, 视频生成/图生视频/LTX LTX2.3 文生视频 文生MV_2041707361903058945.json, 视频生成/图生视频/LTX2.3图生视频mv文生视频长视频制作文本生成视频mv制作口播视频生成两个模式切换_2037757708098609154.json, 视频生成/图生视频/LTX2.3多参数字人 口播带货生视频（图片+参考音频+台词）_2094365968310034434.json, 视频生成/图生视频/LTX2.3多参数字人 口播带货生视频（图片+参考音频+台词）_2094393909978943489.json, 视频生成/图生视频/LTX2.3多参数字人（图片+参考音频+台词）_2031937428285562881.json, 视频生成/图生视频/LTX2.3数字人 图片+台本+参考音频（48G）_2036273171539693570.json, 视频生成/图生视频/LTX2.3数字人=首尾帧+台本+参考音频_2037170336013225986.json, 视频生成/图生视频/LTX2.3数字人_2031988132572303362.json, 视频生成/图生视频/LTX2.3数字人口播短视频_2031504476846170114.json, 视频生成/图生视频/LTX2.3数字人口播短视频横板_2031510568200310786.json, 视频生成/图生视频/LTX2.3数字人对口型_2031512055987052545.json, 视频生成/图生视频/LTX2.3数字人文生图版_2037908498046001153.json, 视频生成/图生视频/LTX2.3数字人，图生视频+音色克隆+自定义台词_2079391615793328130.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_6

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/文生图/LTX2.3数字人=首尾帧+台本+参考音频_2050868438406582274.json、图片生成/文生图/LTX2.3数字人（唱歌）_2046955390981644289.json、平台全量/音频生视频 LTX2.3文生MV_2053017927036751874.json、数字人/数字人/A-6 最佳口播数字人 LTX2.3 _ 音频驱动 _ 嘴型精准 _ 高清输出_2083957412322701313.json、数字人/数字人/LTX2.3 数字人 文图生双模式 v1.1+VBVR_2031652480672604161.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 25 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `KSampler`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CM_FloatToInt` —— 24/25 个有
- `LoraLoaderModelOnly` —— 24/25 个有
- `easy showAnything` —— 24/25 个有
- `ImageSharpen` —— 23/25 个有
- `LoadImage` —— 23/25 个有
- `LTX2_NAG` —— 22/25 个有
- `PrimitiveBoolean` —— 21/25 个有
- `ResizeImageMaskNode` —— 21/25 个有
- `LoadAudio` —— 19/25 个有
- `GetImageSize` —— 15/25 个有
- `PrimitiveStringMultiline` —— 15/25 个有
- `AudioDuration_wan` —— 14/25 个有
- `AudioPad` —— 14/25 个有
- `IndexTTS2Run` —— 14/25 个有
- `PreviewAudio` —— 14/25 个有
- `SaveAudio` —— 10/25 个有
- `Int` —— 8/25 个有
- `ImageResizeKJv2` —— 6/25 个有
- `VHS_LoadAudioUpload` —— 6/25 个有
- `GetImageSizeAndCount` —— 5/25 个有
- `LTXVFirstLastFrameControl_TTP` —— 5/25 个有
- `MelBandRoFormerModelLoader` —— 3/25 个有
- `MelBandRoFormerSampler` —— 3/25 个有
- `SoundFlow_GetLength` —— 3/25 个有
- `TrimAudioDuration` —— 3/25 个有
- `RH_GetAudioDuration` —— 2/25 个有
- `AudioSeparation` —— 1/25 个有
- `ComfyMathExpression` —— 1/25 个有
- `CustomAddLabel` —— 1/25 个有
- `Divide [DVB]` —— 1/25 个有
- `FlashVSRNode` —— 1/25 个有
- `HeartMuLa_Transcribe` —— 1/25 个有
- `JWInteger` —— 1/25 个有
- `OmniVoiceVoiceCloneTTS` —— 1/25 个有
- `OmniVoiceWhisperLoader` —— 1/25 个有
- `ShowText` —— 1/25 个有
- `VRAMReserver` —— 1/25 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 25 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 25 | 100% |
| 采样算法 | euler | - | 25 | 100% |
| 调度器 | simple | - | 25 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 25 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 25/25 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 25/25 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，25 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，25 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，25 个样本，一致性 100%
- 调度器 最常用 simple，25 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，25 个样本，取值集中（一致性 100%）
- 高发问题（25/25 个样本）：Steps较低可能导致细节不足
- 高发问题（25/25 个样本）：发现KSampler但没有VAEDecode
