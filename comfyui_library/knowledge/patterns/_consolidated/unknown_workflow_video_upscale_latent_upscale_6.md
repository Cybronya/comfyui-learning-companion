---
name: unknown_workflow_video_upscale_latent_upscale_6
type: Unknown Workflow
frequency: 22
level: strong
coverage: 0.810864
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetNode, INTConstant, KSampler, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVCropGuides, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, VAEDecodeTiled, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [图片生成/文生图/LTX2.3数字人=首尾帧+台本+参考音频_2050868438406582274.json, 图片生成/文生图/LTX2.3数字人（唱歌）_2046955390981644289.json, 数字人/数字人/A-6 最佳口播数字人 LTX2.3 _ 音频驱动 _ 嘴型精准 _ 高清输出_2083957412322701313.json, 数字人/数字人/LTX2.3 数字人 文图生双模式 v1.1+VBVR_2031652480672604161.json, 数字人/数字人/LTX2.3-数字人-上传图片和音频生成电商带货数字人_2033156191248977921.json, 数字人/数字人/LTX2.3图生_文生数字人_2034265668933132290.json, 数字人/数字人/LTX2.3多图参考MV_2032770671985565698.json, 数字人/数字人/LTX2.3数字人=图片+台本+参考音频_2031237333273546754.json, 数字人/数字人/LTX2.3数字人=首尾帧+台本+参考音频_2031911940234153985.json, 数字人/数字人/LTX2.3数字人=首尾帧+台本+参考音频_2046018270754508801.json, 数字人/数字人/LTX2.3数字人文生图生自由切换版_2031196262409703425.json, 数字人/数字人/LTX2.3数字人文生图生自由切换版_2036799959873363969.json, 数字人/数字人/LTX2.3数字人文生图生自由切换版_2037157839772323842.json, 数字人/数字人/LTX2.3数字人文生图生自由切换版_2080368015757107201.json, 数字人/数字人/数字人 LTX2.3 (图片+台本+参考音频) 上手简单效果好_2032385532776423426.json, 数字人/数字人/首尾帧数字人2.3ltx_2038810340254814210.json, 视频生成/图生视频/LTX2.3 最强数字人（语音口播）_2080251768956608514.json, 视频生成/图生视频/LTX2.3图生视频mv文生视频长视频制作文本生成视频mv制作口播视频生成两个模式切换_2037757708098609154.json, 视频生成/图生视频/LTX2.3多参数字人 口播带货生视频（图片+参考音频+台词）_2094365968310034434.json, 视频生成/图生视频/LTX2.3多参数字人 口播带货生视频（图片+参考音频+台词）_2094393909978943489.json, 视频生成/图生视频/LTX2.3多参数字人（图片+参考音频+台词）_2031937428285562881.json, 视频生成/图生视频/快速跨境电商数字人开口说话V1_2079391881473122306.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_6

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/文生图/LTX2.3数字人=首尾帧+台本+参考音频_2050868438406582274.json、图片生成/文生图/LTX2.3数字人（唱歌）_2046955390981644289.json、数字人/数字人/A-6 最佳口播数字人 LTX2.3 _ 音频驱动 _ 嘴型精准 _ 高清输出_2083957412322701313.json、数字人/数字人/LTX2.3 数字人 文图生双模式 v1.1+VBVR_2031652480672604161.json、数字人/数字人/LTX2.3-数字人-上传图片和音频生成电商带货数字人_2033156191248977921.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 22 个 workflow 都包含：
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
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LTXVConditioning` —— 21/22 个有
- `ResizeImagesByLongerEdge` —— 21/22 个有
- `LTXVImgToVideoInplace` —— 20/22 个有
- `LoraLoaderModelOnly` —— 20/22 个有
- `PrimitiveBoolean` —— 18/22 个有
- `ResizeImageMaskNode` —— 18/22 个有
- `ImageSharpen` —— 17/22 个有
- `PreviewAudio` —— 16/22 个有
- `LoadAudio` —— 13/22 个有
- `GetImageSize` —— 11/22 个有
- `AudioDuration_wan` —— 9/22 个有
- `AudioPad` —— 9/22 个有
- `IndexTTS2Run` —— 9/22 个有
- `PrimitiveStringMultiline` —— 9/22 个有
- `VHS_LoadAudioUpload` —— 9/22 个有
- `SaveAudio` —— 5/22 个有
- `GetImageSizeAndCount` —— 4/22 个有
- `ImageResizeKJv2` —— 4/22 个有
- `Int` —— 4/22 个有
- `RH_GetAudioDuration` —— 4/22 个有
- `LTXVFirstLastFrameControl_TTP` —— 3/22 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/22 个有
- `RTXVideoSuperResolution` —— 3/22 个有
- `LTXVImgToVideoInplaceKJ` —— 2/22 个有
- `AudioSeparation` —— 1/22 个有
- `CR Text` —— 1/22 个有
- `CustomAddLabel` —— 1/22 个有
- `GetImageSize+` —— 1/22 个有
- `HeartMuLa_Transcribe` —— 1/22 个有
- `PrimitiveInt` —— 1/22 个有
- `ShowText` —— 1/22 个有
- `Text` —— 1/22 个有
- `VRAMReserver` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 22 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 22 | 100% |
| 采样算法 | euler | - | 22 | 100% |
| 调度器 | simple | - | 22 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 22 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 22/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 22/22 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，22 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，22 个样本，一致性 100%
- 调度器 最常用 simple，22 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，22 个样本，取值集中（一致性 100%）
- 高发问题（22/22 个样本）：Steps较低可能导致细节不足
- 高发问题（22/22 个样本）：发现KSampler但没有VAEDecode
