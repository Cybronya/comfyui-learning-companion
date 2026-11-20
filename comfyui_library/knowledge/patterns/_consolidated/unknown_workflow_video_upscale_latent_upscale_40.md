---
name: unknown_workflow_video_upscale_latent_upscale_40
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8073
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, GetNode, KSampler, KSamplerSelect, LTX2SamplingPreviewOverride, LTXVAudioVAEEncode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, VAEDecodeTiled, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/文生视频/LTX-2.3-文生视频数字人_2031035980697837569.json, 视频生成/文生视频/LTX2.3文生视频-汉服古风版-MV短视频_2046587712806850562.json, 视频生成/文生视频/LTX2.3文生视频MV工作流：AI文字生成音乐视频创作_2030846649316151298.json, 视频生成/文生视频/LTX2.3文生视频长视频制作文本生成视频mv制作口播视频生成工作流_2051504924906795009.json, 视频生成/文生视频/LTX2.3文生视频长视频制作文本生成视频mv制作口播视频生成工作流_2055853295931011073.json, 视频生成/文生视频/最新LTX2.3文生MV工作流_2030889486191693825.json, 视频生成/文生视频/音频生视频 LTX2.3文生MV KJ优化版_2034134213573746690.json, 音频生成/音频生成/LTX2.3数字人_2031246027176546305.json, 音频生成/音频生成/最佳口播数字人_LTX2.3_音频驱动_嘴型精准_高清输出_2102687764545363970.json, 音频生成/音频生成/最佳口播数字人_LTX2.3_音频驱动_嘴型精准_高清输出_2104392823285051394.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_40

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/LTX-2.3-文生视频数字人_2031035980697837569.json、视频生成/文生视频/LTX2.3文生视频-汉服古风版-MV短视频_2046587712806850562.json、视频生成/文生视频/LTX2.3文生视频MV工作流：AI文字生成音乐视频创作_2030846649316151298.json、视频生成/文生视频/LTX2.3文生视频长视频制作文本生成视频mv制作口播视频生成工作流_2051504924906795009.json、视频生成/文生视频/LTX2.3文生视频长视频制作文本生成视频mv制作口播视频生成工作流_2055853295931011073.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 10 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `KSampler`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTXVAudioVAEEncode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
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
- `CM_FloatToInt` —— 9/10 个有
- `CheckpointLoaderSimple` —— 9/10 个有
- `INTConstant` —— 9/10 个有
- `LTXAVTextEncoderLoader` —— 9/10 个有
- `LTXVAudioVAELoader` —— 9/10 个有
- `LoadAudio` —— 9/10 个有
- `PathchSageAttentionKJ` —— 9/10 个有
- `PreviewAudio` —— 9/10 个有
- `ImageSharpen` —— 8/10 个有
- `LTXVImgToVideoInplace` —— 8/10 个有
- `LTXVPreprocess` —— 8/10 个有
- `LoraLoaderModelOnly` —— 8/10 个有
- `ResizeImagesByLongerEdge` —— 8/10 个有
- `Int` —— 7/10 个有
- `MelBandRoFormerModelLoader` —— 7/10 个有
- `MelBandRoFormerSampler` —— 7/10 个有
- `SoundFlow_GetLength` —— 7/10 个有
- `TrimAudioDuration` —— 7/10 个有
- `LoadImage` —— 3/10 个有
- `GetImageSize` —— 2/10 个有
- `LTX2_NAG` —— 2/10 个有
- `RH_GetAudioDuration` —— 2/10 个有
- `CR Float To Integer` —— 1/10 个有
- `CR Prompt Text` —— 1/10 个有
- `DiffusionModelLoaderKJ` —— 1/10 个有
- `DualCLIPLoader` —— 1/10 个有
- `FloatConstant` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `PrimitiveFloat` —— 1/10 个有
- `ResizeImageMaskNode` —— 1/10 个有
- `SigmasPreview` —— 1/10 个有
- `TextGenerateLTX2Prompt` —— 1/10 个有
- `TextInputNode` —— 1/10 个有
- `VAELoaderKJ` —— 1/10 个有
- `VHS_LoadAudioUpload` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 10 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 90% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 10/10 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，10 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 90%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，10 个样本，取值集中（一致性 100%）
- 高发问题（10/10 个样本）：Steps较低可能导致细节不足
- 高发问题（10/10 个样本）：发现KSampler但没有VAEDecode
