---
name: unknown_workflow_video_upscale_latent_upscale_12
type: Unknown Workflow
frequency: 18
level: strong
coverage: 0.8135
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSampler, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, ResizeImagesByLongerEdge, SetLatentNoiseMask, SimpleMath+, SolidMask, VAEDecodeTiled, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/2033775410789486594.json, 视频生成/图生视频/LTX2.3多参数字人 口播带货生视频（图片+参考音频+台词）_2094365968310034434.json, 视频生成/图生视频/LTX2.3多参数字人 口播带货生视频（图片+参考音频+台词）_2094393909978943489.json, 视频生成/图生视频/LTX2.3多参数字人（图片+参考音频+台词）_2031937428285562881.json, 视频生成/图生视频/2036273171539693570.json, 视频生成/图生视频/2037170336013225986.json, 视频生成/图生视频/2031988132572303362.json, 视频生成/图生视频/2031504476846170114.json, 视频生成/图生视频/2031510568200310786.json, 视频生成/图生视频/2031512055987052545.json, 视频生成/图生视频/2037908498046001153.json, 视频生成/图生视频/2079391615793328130.json, 视频生成/图生视频/2079391881473122306.json, 视频生成/图生视频/2031742502574755842.json, 视频生成/图生视频/2073004728237256705.json, 视频生成/图生视频/2071813613165309953.json, 视频生成/图生视频/2046398543711182850.json, 视频生成/文生视频/LTX2.3数字人 图片+台本+参考音频_2032085252935524354.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_12

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/2033775410789486594.json、视频生成/图生视频/LTX2.3多参数字人 口播带货生视频（图片+参考音频+台词）_2094365968310034434.json、视频生成/图生视频/LTX2.3多参数字人 口播带货生视频（图片+参考音频+台词）_2094393909978943489.json、视频生成/图生视频/LTX2.3多参数字人（图片+参考音频+台词）_2031937428285562881.json、视频生成/图生视频/2036273171539693570.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSampler`
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
- `LoadImage`
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `ResizeImagesByLongerEdge`
- `SetLatentNoiseMask`
- `SimpleMath+`
- `SolidMask`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 17/18 个有
- `CFGGuider` —— 17/18 个有
- `CM_FloatToInt` —— 17/18 个有
- `GetNode` —— 17/18 个有
- `INTConstant` —— 17/18 个有
- `KSamplerSelect` —— 17/18 个有
- `LTX2_NAG` —— 17/18 个有
- `RandomNoise` —— 17/18 个有
- `ResizeImageMaskNode` —— 17/18 个有
- `SamplerCustomAdvanced` —— 17/18 个有
- `SetNode` —— 17/18 个有
- `easy cleanGpuUsed` —— 17/18 个有
- `easy showAnything` —— 17/18 个有
- `LoadAudio` —— 16/18 个有
- `PrimitiveBoolean` —— 16/18 个有
- `ImageSharpen` —— 13/18 个有
- `PrimitiveStringMultiline` —— 13/18 个有
- `AudioDuration_wan` —— 12/18 个有
- `AudioPad` —— 12/18 个有
- `GetImageSize` —— 12/18 个有
- `IndexTTS2Run` —— 12/18 个有
- `SaveAudio` —— 9/18 个有
- `PreviewAudio` —— 8/18 个有
- `Int` —— 4/18 个有
- `RH_GetAudioDuration` —— 4/18 个有
- `ImageResizeKJv2` —— 3/18 个有
- `RTXVideoSuperResolution` —— 3/18 个有
- `GetImageSizeAndCount` —— 2/18 个有
- `LTXVFirstLastFrameControl_TTP` —— 2/18 个有
- `PreviewAny` —— 2/18 个有
- `RHLLMChatNode` —— 2/18 个有
- `Textbox` —— 2/18 个有
- `VHS_LoadAudioUpload` —— 2/18 个有
- `ComfyMathExpression` —— 1/18 个有
- `Divide [DVB]` —— 1/18 个有
- `FlashVSRNode` —— 1/18 个有
- `JWInteger` —— 1/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/18 个有
- `LayerUtility: PurgeVRAM V2` —— 1/18 个有
- `OmniVoiceVoiceCloneTTS` —— 1/18 个有
- `OmniVoiceWhisperLoader` —— 1/18 个有
- `Text` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 18 | 100% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 18/18 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，18 个样本，取值集中（一致性 100%）
- 高发问题（19/18 个样本）：Steps较低可能导致细节不足
- 高发问题（18/18 个样本）：发现KSampler但没有VAEDecode
