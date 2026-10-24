---
name: unknown_workflow_video_upscale_latent_upscale_33
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8022
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetNode, INTConstant, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewAudio, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, VAEDecodeTiled, VHS_VideoCombine, easy showAnything]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/LTX2.3动漫图生MV-30秒分段_2043299201156653058.json, 视频生成/图生视频/LTX2.3图生视频mv文生视频长视频制作文本生成视频mv制作口播视频生成两个模式切换_2037757708098609154.json, 视频生成/图生视频/数字人直播+虚拟美女模特+LTX2.3数字人++图生视频极速版LTX2.3+数字人话+唱歌_2046755636465115137.json, 视频生成/文生视频/LTX2.3数字人 数字人直播+虚拟美女模特 图生视频极速版LTX2.3+数字人话+唱歌_2049691978417352705.json, 视频生成/文生视频/LTX2.3数字人文生图生自由切换_2039937365250154497.json, 视频生成/文生视频/LTX2.3数字人文生视频和图生视频自由切换，纵享丝滑！_2031393544925089793.json, 视频生成/文生视频/LTX2.3数字人文生视频图生视频自由切换版工作流_2031222373810180098.json, 视频生成/文生视频/LTX2.3数字人无字幕版 数字人直播 虚拟美女模特   图生视频极速版LTX2.3 数字人话 唱歌_2044970741254332418.json, 视频生成/文生视频/「Supermate」LTX2.3-数字人说话&唱歌-最佳版_2042879991003750402.json, 视频生成/文生视频/数字人直播 虚拟美女模特 LTX2.3数字人无字幕版  图生视频极速版LTX2.3 数字人话 唱歌对_2044685431765213185.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_33

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/LTX2.3动漫图生MV-30秒分段_2043299201156653058.json、视频生成/图生视频/LTX2.3图生视频mv文生视频长视频制作文本生成视频mv制作口播视频生成两个模式切换_2037757708098609154.json、视频生成/图生视频/数字人直播+虚拟美女模特+LTX2.3数字人++图生视频极速版LTX2.3+数字人话+唱歌_2046755636465115137.json、视频生成/文生视频/LTX2.3数字人 数字人直播+虚拟美女模特 图生视频极速版LTX2.3+数字人话+唱歌_2049691978417352705.json、视频生成/文生视频/LTX2.3数字人文生图生自由切换_2039937365250154497.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
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
- `LoraLoaderModelOnly`
- `PathchSageAttentionKJ`
- `PreviewAudio`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 9/10 个有
- `KSampler` —— 9/10 个有
- `PrimitiveBoolean` —— 9/10 个有
- `ResizeImageMaskNode` —— 9/10 个有
- `ImageSharpen` —— 6/10 个有
- `VHS_LoadAudioUpload` —— 6/10 个有
- `easy cleanGpuUsed` —— 6/10 个有
- `LoadAudio` —— 5/10 个有
- `SoundFlow_GetLength` —— 5/10 个有
- `AudioCrop` —— 4/10 个有
- `ImageCASharpening+` —— 4/10 个有
- `NormalizeAudioLoudness` —— 4/10 个有
- `RunningHub Deepcleaner` —— 4/10 个有
- `AudioEvenSplitNode` —— 1/10 个有
- `AudioSelectNode` —— 1/10 个有
- `FloatConstant` —— 1/10 个有
- `ImageBatchGet` —— 1/10 个有
- `ImageBatchOneOrMore` —— 1/10 个有
- `ImageResizeKJv2` —— 1/10 个有
- `LTXVAddGuide` —— 1/10 个有
- `LTXVImgToVideoInplaceKJ` —— 1/10 个有
- `Label (rgthree)` —— 1/10 个有
- `ManualSigmas` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `ShowText` —— 1/10 个有
- `TextGenerateLTX2Prompt` —— 1/10 个有
- `TrimAudioDuration` —— 1/10 个有
- `VAELoader` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 9/10 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，9 个样本，取值集中（一致性 100%）
- 高发问题（9/10 个样本）：Steps较低可能导致细节不足
- 高发问题（9/10 个样本）：发现KSampler但没有VAEDecode
