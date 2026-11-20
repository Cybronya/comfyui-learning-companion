---
name: unknown_workflow_video_upscale_latent_upscale_55
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.824429
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetNode, INTConstant, KSampler, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, PathchSageAttentionKJ, PreviewAudio, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, VAEDecodeTiled, VHS_VideoCombine, easy showAnything]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [数字人/数字人/LTX2.3多图参考MV_2032770671985565698.json, 数字人/数字人/LTX2.3数字人文生图生自由切换版_2031196262409703425.json, 数字人/数字人/LTX2.3数字人文生图生自由切换版_2036799959873363969.json, 数字人/数字人/LTX2.3数字人文生图生自由切换版_2037157839772323842.json, 数字人/数字人/LTX2.3数字人文生图生自由切换版_2080368015757107201.json, 数字人/数字人/LTX2.3数字人无字幕版_2031615343537430529.json, 数字人/数字人/批量视频-测试_2080195859542798337.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_55

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（数字人/数字人/LTX2.3多图参考MV_2032770671985565698.json、数字人/数字人/LTX2.3数字人文生图生自由切换版_2031196262409703425.json、数字人/数字人/LTX2.3数字人文生图生自由切换版_2036799959873363969.json、数字人/数字人/LTX2.3数字人文生图生自由切换版_2037157839772323842.json、数字人/数字人/LTX2.3数字人文生图生自由切换版_2080368015757107201.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `KSampler`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `PathchSageAttentionKJ`
- `PreviewAudio`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideoInplace` —— 6/7 个有
- `LoraLoaderModelOnly` —— 6/7 个有
- `PrimitiveBoolean` —— 6/7 个有
- `ResizeImagesByLongerEdge` —— 6/7 个有
- `easy cleanGpuUsed` —— 6/7 个有
- `ResizeImageMaskNode` —— 5/7 个有
- `VHS_LoadAudioUpload` —— 4/7 个有
- `ImageSharpen` —— 3/7 个有
- `LoadAudio` —— 3/7 个有
- `AudioCrop` —— 2/7 个有
- `NormalizeAudioLoudness` —— 2/7 个有
- `RH_GetAudioDuration` —— 2/7 个有
- `RTXVideoSuperResolution` —— 2/7 个有
- `AudioBeforeAfterSilence` —— 1/7 个有
- `CR Prompt Text` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `GetImageSize+` —— 1/7 个有
- `GetImageSizeAndCount` —— 1/7 个有
- `HeartMuLa_Transcribe` —— 1/7 个有
- `ImageCASharpening+` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `LTXVImgToVideoInplaceKJ` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `LongCatVoiceCloneTTS` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `Qwen3ASRLoader` —— 1/7 个有
- `Qwen3ASRTranscribe` —— 1/7 个有
- `Qwen3TTSModelLoader` —— 1/7 个有
- `Qwen3TTSVoiceClone` —— 1/7 个有
- `RunningHub Deepcleaner` —— 1/7 个有
- `SoundFlow_GetLength` —— 1/7 个有
- `easy downloadIndexTTSAndLoadModel` —— 1/7 个有
- `easy indexTTSGenerateSimple` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 7/7 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
- 高发问题（7/7 个样本）：发现KSampler但没有VAEDecode
