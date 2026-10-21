---
name: unknown_workflow_video_upscale_latent_upscale_3
type: Unknown Workflow
frequency: 36
level: strong
coverage: 0.773111
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetNode, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, PrimitiveBoolean, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, VAEDecodeTiled, VHS_VideoCombine]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/2082459555551858689.json, 视频生成/图生视频/2068287878093955073.json, 视频生成/图生视频/2069026282452639746.json, 视频生成/图生视频/LTX2.3 Org版 图片说话唱歌精确对口型_2103431205076168706.json, 视频生成/图生视频/LTX2.3 Org版 图片说话唱歌精确对口型_2103455782971990018.json, 视频生成/图生视频/2081696395232370690.json, 视频生成/图生视频/2068218768014274561.json, 视频生成/图生视频/2068294782593626113.json, 视频生成/图生视频/2068288834533675009.json, 视频生成/图生视频/2036255760610496514.json, 视频生成/图生视频/2035160184418471938.json, 视频生成/图生视频/2052644596936650754.json, 视频生成/图生视频/2052992002366689281.json, 视频生成/图生视频/2055189140328722433.json, 视频生成/图生视频/2058724589433352194.json, 视频生成/图生视频/2059186368546430977.json, 视频生成/图生视频/2059884088110174209.json, 视频生成/图生视频/2062789190563225602.json, 视频生成/图生视频/LTX2.3+Org 加长图生视频High-Quality Image-to-Video_2093890735903956994.json, 视频生成/图生视频/2071781935793393665.json, 视频生成/图生视频/2040333916862685186.json, 视频生成/图生视频/2042076729832906754.json, 视频生成/图生视频/2040953875372445698.json, 视频生成/图生视频/2039930544166805506.json, 视频生成/图生视频/2065027141875621889.json, 视频生成/图生视频/2046755636465115137.json, 视频生成/图生视频/2042466020870332417.json, 视频生成/图生视频/2071796898314407937.json, 视频生成/图生视频/2076471205808394241.json, 视频生成/文生视频/LTX2.3 数字人唱歌说话 对口型 图生视频 智能极速版  图片音频双驱动_2035153850771968001.json, 视频生成/文生视频/LTX2.3数字人 数字人直播+虚拟美女模特 图生视频极速版LTX2.3+数字人话+唱歌_2049691978417352705.json, 视频生成/文生视频/LTX2.3数字人无字幕版 数字人直播 虚拟美女模特   图生视频极速版LTX2.3 数字人话 唱歌_2044970741254332418.json, 视频生成/文生视频/【最新加速版】数字人话 LTX2.3唱歌对口型_2043952711799934977.json, 视频生成/文生视频/数字人直播 虚拟美女模特 LTX2.3数字人无字幕版  图生视频极速版LTX2.3 数字人话 唱歌对_2044685431765213185.json, 视频生成/文生视频/数字人话 LTX2.3唱歌对口型【最新加速版】_2042470118726311937.json, 音频生成/音频生成/LTX2.3 数字人说话唱歌对口型_2043490102965440514.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_3

> 由 `engine/knowledge_consolidation` 从 36 个 workflow 归纳得出（视频生成/图生视频/2082459555551858689.json、视频生成/图生视频/2068287878093955073.json、视频生成/图生视频/2069026282452639746.json、视频生成/图生视频/LTX2.3 Org版 图片说话唱歌精确对口型_2103431205076168706.json、视频生成/图生视频/LTX2.3 Org版 图片说话唱歌精确对口型_2103455782971990018.json…）

- **类型**：Unknown Workflow
- **样本数**：36
- **可信度**：强结论
- **平均知识覆盖**：77%

## 共有节点

全部 36 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveBoolean`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SetNode`
- `SimpleMath+`
- `SolidMask`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 33/36 个有
- `KSampler` —— 33/36 个有
- `LTX2SamplingPreviewOverride` —— 33/36 个有
- `LTX2_NAG` —— 33/36 个有
- `LTXVPreprocess` —— 33/36 个有
- `DF_Int_to_Float` —— 32/36 个有
- `ImageResizeKJv2` —— 32/36 个有
- `Int` —— 32/36 个有
- `MelBandRoFormerModelLoader` —— 32/36 个有
- `MelBandRoFormerSampler` —— 32/36 个有
- `PrimitiveInt` —— 32/36 个有
- `PrimitiveStringMultiline` —— 32/36 个有
- `JoinStrings` —— 29/36 个有
- `SoundFlow_GetLength` —— 22/36 个有
- `CM_FloatToInt` —— 21/36 个有
- `ComfyMathExpression` —— 18/36 个有
- `LTXVAudioVAEDecode` —— 18/36 个有
- `ManualSigmas` —— 18/36 个有
- `NormalizeAudioLoudness` —— 18/36 个有
- `ResizeImagesByLongerEdge` —— 18/36 个有
- `TrimAudioDuration` —— 18/36 个有
- `PreviewAudio` —— 17/36 个有
- `ImageAndMaskResizeNode` —— 15/36 个有
- `LayerUtility: PurgeVRAM` —— 14/36 个有
- `PrimitiveFloat` —— 13/36 个有
- `ResizeImageMaskNode` —— 7/36 个有
- `Compare` —— 5/36 个有
- `InversionDemoLazySwitch` —— 5/36 个有
- `AudioCrop` —— 4/36 个有
- `INTConstant` —— 4/36 个有
- `ImageCASharpening+` —— 4/36 个有
- `PathchSageAttentionKJ` —— 4/36 个有
- `RunningHub Deepcleaner` —— 4/36 个有
- `easy showAnything` —— 4/36 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 6 | 33 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 33 | 100% |
| 采样算法 | euler | - | 33 | 55% |
| 调度器 | simple | - | 33 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 33 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 33/36 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 33/36 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 6，33 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，33 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，33 个样本，一致性 55%
- 调度器 最常用 simple，33 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，33 个样本，取值集中（一致性 100%）
- 高发问题（33/36 个样本）：Steps较低可能导致细节不足
- 高发问题（33/36 个样本）：发现KSampler但没有VAEDecode
