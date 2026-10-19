---
name: unknown_workflow_video_upscale_latent_upscale_53
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.791
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetNode, INTConstant, KSampler, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, PathchSageAttentionKJ, PreviewAudio, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, VAEDecodeTiled, VHS_VideoCombine, easy showAnything]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/2047993632803786754.json, 视频生成/图生视频/2047229271873163265.json, 视频生成/图生视频/最佳口播数字人_LTX2.3_音频驱动_嘴型精准_高清输出_2104490779896016898.json, 视频生成/图生视频/2074873407807778817.json, 视频生成/文生视频/LTX2.3【雄舟天文馆高清直出版】首尾帧+音色克隆_2046116731281739777.json, 视频生成/文生视频/LTX2.3数字人文生图生自由切换版_2031035696881864705.json, 音频生成/音频生成/最佳口播数字人_LTX2.3_音频驱动_嘴型精准_高清输出_2102687764545363970.json, 音频生成/音频生成/最佳口播数字人_LTX2.3_音频驱动_嘴型精准_高清输出_2104392823285051394.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_53

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2047993632803786754.json、视频生成/图生视频/2047229271873163265.json、视频生成/图生视频/最佳口播数字人_LTX2.3_音频驱动_嘴型精准_高清输出_2104490779896016898.json、视频生成/图生视频/2074873407807778817.json、视频生成/文生视频/LTX2.3【雄舟天文馆高清直出版】首尾帧+音色克隆_2046116731281739777.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 8 个 workflow 都包含：
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
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadAudio`
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
- `GetImageSize` —— 7/8 个有
- `LTXVPreprocess` —— 5/8 个有
- `PrimitiveBoolean` —— 5/8 个有
- `easy cleanGpuUsed` —— 5/8 个有
- `LoraLoaderModelOnly` —— 4/8 个有
- `RH_GetAudioDuration` —— 4/8 个有
- `ResizeImagesByLongerEdge` —— 4/8 个有
- `Apply Whisper` —— 3/8 个有
- `AudioDuration_wan` —— 3/8 个有
- `AudioPad` —— 3/8 个有
- `ImageResizeKJv2` —— 3/8 个有
- `InversionDemoLazySwitch` —— 3/8 个有
- `LTXVFirstLastFrameControl_TTP` —— 3/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `Qwen3TTSModelLoader` —— 3/8 个有
- `Qwen3TTSVoiceClone` —— 3/8 个有
- `SaveAudio` —— 3/8 个有
- `ShowText|pysssss` —— 3/8 个有
- `Text Concatenate` —— 3/8 个有
- `llama_cpp_instruct_adv` —— 3/8 个有
- `llama_cpp_model_loader` —— 3/8 个有
- `llama_cpp_parameters` —— 3/8 个有
- `GetImageSizeAndCount` —— 2/8 个有
- `ImageBatchMulti` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `GetImageSize+` —— 1/8 个有
- `PainterAudioLength` —— 1/8 个有
- `RTXVideoSuperResolution` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | simple | - | 8 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 8/8 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 simple，8 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
- 高发问题（8/8 个样本）：发现KSampler但没有VAEDecode
