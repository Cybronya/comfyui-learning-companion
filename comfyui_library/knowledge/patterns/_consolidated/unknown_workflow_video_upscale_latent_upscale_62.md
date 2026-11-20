---
name: unknown_workflow_video_upscale_latent_upscale_62
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.805714
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetNode, INTConstant, KSampler, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, PathchSageAttentionKJ, PreviewAudio, PrimitiveBoolean, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, VHS_VideoCombine, easy showAnything]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/文生视频/LTX2.3 图生_文生 数字人整合优化版_2044956920242507777.json, 视频生成/文生视频/LTX2.3 图生_文生 数字人整合优化版_2045020959014395906.json, 视频生成/文生视频/LTX2.3数字人 开源最强数字人（人文生图生自由切换版）_2031464133991862273.json, 视频生成/文生视频/LTX2.3数字人 数字人直播+虚拟美女模特 图生视频极速版LTX2.3+数字人话+唱歌_2049691978417352705.json, 视频生成/文生视频/LTX2.3数字人 音频驱动_2082129889662160897.json, 视频生成/文生视频/LTX2.3数字人_文生图生自由切换版_2031165124689534978.json, 视频生成/文生视频/LTX2.3数字人文生图生+高清放大_2039963424049860609.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_62

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/文生视频/LTX2.3 图生_文生 数字人整合优化版_2044956920242507777.json、视频生成/文生视频/LTX2.3 图生_文生 数字人整合优化版_2045020959014395906.json、视频生成/文生视频/LTX2.3数字人 开源最强数字人（人文生图生自由切换版）_2031464133991862273.json、视频生成/文生视频/LTX2.3数字人 数字人直播+虚拟美女模特 图生视频极速版LTX2.3+数字人话+唱歌_2049691978417352705.json、视频生成/文生视频/LTX2.3数字人 音频驱动_2082129889662160897.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：81%

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
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `PathchSageAttentionKJ`
- `PreviewAudio`
- `PrimitiveBoolean`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/7 个有
- `ResizeImagesByLongerEdge` —— 5/7 个有
- `VAEDecodeTiled` —— 5/7 个有
- `VHS_LoadAudioUpload` —— 5/7 个有
- `ResizeImageMaskNode` —— 4/7 个有
- `easy cleanGpuUsed` —— 4/7 个有
- `ImageSharpen` —— 3/7 个有
- `ImageResizeKJv2` —— 2/7 个有
- `LoadAudio` —— 2/7 个有
- `VAEDecode` —— 2/7 个有
- `AudioCrop` —— 1/7 个有
- `CR Text` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `GetImageSize` —— 1/7 个有
- `ImageCASharpening+` —— 1/7 个有
- `ImageScaleToTotalPixels` —— 1/7 个有
- `MemoryCleaner` —— 1/7 个有
- `NormalizeAudioLoudness` —— 1/7 个有
- `RH_GetAudioDuration` —— 1/7 个有
- `RTXVideoSuperResolution` —— 1/7 个有
- `RunningHub Deepcleaner` —— 1/7 个有
- `SeedVR2LoadDiTModel` —— 1/7 个有
- `SeedVR2LoadVAEModel` —— 1/7 个有
- `SeedVR2VideoUpscaler` —— 1/7 个有
- `SoundFlow_GetLength` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `VHS_VideoInfo` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.5 | 7 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 5/7 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.5，7 个样本，取值集中（一致性 89%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
- 高发问题（5/7 个样本）：发现KSampler但没有VAEDecode
