---
name: unknown_workflow_video_upscale_latent_upscale_22
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.813286
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, EmptyLTXVLatentVideo, GetNode, INTConstant, ImageSharpen, KSamplerSelect, LTX2SamplingPreviewOverride, LTXAVTextEncoderLoader, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, PreviewAudio, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, SetNode, SimpleMath+, SolidMask, VAEDecodeTiled, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足, 发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/2043299201156653058.json, 视频生成/图生视频/2037757708098609154.json, 视频生成/图生视频/2030898825140899842.json, 视频生成/图生视频/2037756141316345857.json, 视频生成/文生视频/LTX LTX2.3 文生视频 文生MV_2041828761359880193.json, 视频生成/文生视频/LTX2.3 文生视频 文生MV_2037069470136541186.json, 视频生成/文生视频/LTX2.3数字人文生图生自由切换_2039937365250154497.json, 视频生成/文生视频/LTX2.3数字人文生视频和图生视频自由切换，纵享丝滑！_2031393544925089793.json, 视频生成/文生视频/LTX2.3数字人文生视频图生视频自由切换版工作流_2031222373810180098.json, 视频生成/文生视频/LTX2.3文生MV工作流_2030727534442188801.json, 视频生成/文生视频/LTX2.3文生MV工作流_2032463287467642882.json, 视频生成/文生视频/LTX2.3文生MV工作流_2034249600609034241.json, 视频生成/文生视频/LTX2.3文生MV工作流_2035257169087569922.json, 视频生成/文生视频/「Supermate」LTX2.3-数字人说话&唱歌-最佳版_2042879991003750402.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_22

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/2043299201156653058.json、视频生成/图生视频/2037757708098609154.json、视频生成/图生视频/2030898825140899842.json、视频生成/图生视频/2037756141316345857.json、视频生成/文生视频/LTX LTX2.3 文生视频 文生MV_2041828761359880193.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `INTConstant`
- `ImageSharpen`
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
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 13/14 个有
- `KSampler` —— 13/14 个有
- `LoadAudio` —— 9/14 个有
- `SoundFlow_GetLength` —— 9/14 个有
- `TrimAudioDuration` —— 9/14 个有
- `Int` —— 8/14 个有
- `MelBandRoFormerModelLoader` —— 8/14 个有
- `MelBandRoFormerSampler` —— 8/14 个有
- `LTX2_NAG` —— 6/14 个有
- `LoadImage` —— 6/14 个有
- `VHS_LoadAudioUpload` —— 6/14 个有
- `PrimitiveBoolean` —— 5/14 个有
- `ResizeImageMaskNode` —— 5/14 个有
- `AudioEvenSplitNode` —— 1/14 个有
- `AudioSelectNode` —— 1/14 个有
- `FloatConstant` —— 1/14 个有
- `ImageBatchGet` —— 1/14 个有
- `ImageBatchOneOrMore` —— 1/14 个有
- `ImageResizeKJv2` —— 1/14 个有
- `LTXVAddGuide` —— 1/14 个有
- `LTXVImgToVideoInplaceKJ` —— 1/14 个有
- `Label (rgthree)` —— 1/14 个有
- `ManualSigmas` —— 1/14 个有
- `MathExpression|pysssss` —— 1/14 个有
- `PreviewImage` —— 1/14 个有
- `ShowText` —— 1/14 个有
- `TextGenerateLTX2Prompt` —— 1/14 个有
- `VAELoader` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 0.4 | 0.4 - 0.4 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |
| 发现KSampler但没有VAEDecode | 13/14 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 0.4，观测区间 0.4 - 0.4，13 个样本，取值集中（一致性 100%）
- 高发问题（13/14 个样本）：Steps较低可能导致细节不足
- 高发问题（13/14 个样本）：发现KSampler但没有VAEDecode
