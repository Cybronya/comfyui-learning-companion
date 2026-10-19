---
name: unknown_workflow_video_sampler_clip_69
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.77325
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CM_FloatToInt, EmptyLTXVLatentVideo, GetNode, INTConstant, KSamplerSelect, LTX2_NAG, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVSeparateAVLatent, LoadImage, PreviewAudio, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, VHS_VideoCombine, easy showAnything]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/2061333260944367617.json, 视频生成/图生视频/2061445369535483905.json, 视频生成/文生视频/LTX2.3 图生_文生 数字人整合优化版_2044956920242507777.json, 视频生成/文生视频/LTX2.3 图生_文生 数字人整合优化版_2045020959014395906.json, 视频生成/文生视频/LTX2.3数字人 开源最强数字人（人文生图生自由切换版）_2031464133991862273.json, 视频生成/文生视频/LTX2.3数字人 音频驱动_2082129889662160897.json, 视频生成/文生视频/LTX2.3数字人_文生图生自由切换版_2031165124689534978.json, 视频生成/文生视频/LTX2.3数字人文生图生+高清放大_2039963424049860609.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_69

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2061333260944367617.json、视频生成/图生视频/2061445369535483905.json、视频生成/文生视频/LTX2.3 图生_文生 数字人整合优化版_2044956920242507777.json、视频生成/文生视频/LTX2.3 图生_文生 数字人整合优化版_2045020959014395906.json、视频生成/文生视频/LTX2.3数字人 开源最强数字人（人文生图生自由切换版）_2031464133991862273.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `PreviewAudio`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LTXVCropGuides` —— 7/8 个有
- `LTXVImgToVideoInplace` —— 7/8 个有
- `LoraLoaderModelOnly` —— 7/8 个有
- `PrimitiveBoolean` —— 7/8 个有
- `VHS_LoadAudioUpload` —— 7/8 个有
- `CheckpointLoaderSimple` —— 6/8 个有
- `KSampler` —— 6/8 个有
- `LTX2SamplingPreviewOverride` —— 6/8 个有
- `LTXAVTextEncoderLoader` —— 6/8 个有
- `LTXVAudioVAELoader` —— 6/8 个有
- `LTXVLatentUpsampler` —— 6/8 个有
- `LTXVPreprocess` —— 6/8 个有
- `LatentUpscaleModelLoader` —— 6/8 个有
- `PathchSageAttentionKJ` —— 6/8 个有
- `VAEDecodeTiled` —— 6/8 个有
- `ImageResizeKJv2` —— 4/8 个有
- `ResizeImagesByLongerEdge` —— 4/8 个有
- `easy cleanGpuUsed` —— 4/8 个有
- `ImageSharpen` —— 3/8 个有
- `ResizeImageMaskNode` —— 3/8 个有
- `DiffusionModelLoaderKJ` —— 2/8 个有
- `DualCLIPLoaderGGUF` —— 2/8 个有
- `Float` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `VAEDecode` —— 2/8 个有
- `VAELoaderKJ` —— 2/8 个有
- `VisualizeSigmasKJ` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `GetImageSize` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `LTXVAddGuideMulti` —— 1/8 个有
- `LoadAudio` —— 1/8 个有
- `MemoryCleaner` —— 1/8 个有
- `RH_GetAudioDuration` —— 1/8 个有
- `RTXVideoSuperResolution` —— 1/8 个有
- `SeedVR2LoadDiTModel` —— 1/8 个有
- `SeedVR2LoadVAEModel` —— 1/8 个有
- `SeedVR2VideoUpscaler` —— 1/8 个有
- `VHS_LoadVideo` —— 1/8 个有
- `VHS_SelectImages` —— 1/8 个有
- `VHS_VideoInfo` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 67% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.5 | 6 | 89% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 4/8 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 67%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.5，6 个样本，取值集中（一致性 89%）
- 高发问题（6/8 个样本）：Steps较低可能导致细节不足
- 高发问题（4/8 个样本）：发现KSampler但没有VAEDecode
