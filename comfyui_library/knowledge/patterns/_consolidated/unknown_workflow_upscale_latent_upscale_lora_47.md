---
name: unknown_workflow_upscale_latent_upscale_lora_47
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.7215
common_nodes: [CFGGuider, CLIPTextEncode, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2 I2V 完整版图像转视频工作流，拆分子图-调试可运行RH在线工作流_2008987818990772225.json, 视频生成/图生视频/LTX-2 图生视频 ComfyUI官方流_2008519432749981698.json, 视频生成/图生视频/LTX-2 图生视频-音画同步-支持中英文_2008792079337529345.json, 视频生成/图生视频/LTX-2 图生视频_2009447921246281729.json, 视频生成/图生视频/LTX-2.5-图生视频-数字人唱歌_对口型-可上传音频_2087430857970769922.json, 视频生成/图生视频/LTX-2.5-图生视频-数字人唱歌_对口型-可上传音频_2096779577384329217.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_47

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/LTX-2 I2V 完整版图像转视频工作流，拆分子图-调试可运行RH在线工作流_2008987818990772225.json、视频生成/图生视频/LTX-2 图生视频 ComfyUI官方流_2008519432749981698.json、视频生成/图生视频/LTX-2 图生视频-音画同步-支持中英文_2008792079337529345.json、视频生成/图生视频/LTX-2 图生视频_2009447921246281729.json、视频生成/图生视频/LTX-2.5-图生视频-数字人唱歌_对口型-可上传音频_2087430857970769922.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 5/6 个有
- `ImageResizeKJv2` —— 5/6 个有
- `ImpactExecutionOrderController` —— 5/6 个有
- `LTXVGemmaEnhancePrompt` —— 5/6 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 5/6 个有
- `PrimitiveFloat` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `SaveVideo` —— 5/6 个有
- `CheckpointLoaderSimple` —— 4/6 个有
- `LTXAVTextEncoderLoader` —— 4/6 个有
- `LTXVAudioVAELoader` —— 4/6 个有
- `DF_Int_to_Float` —— 3/6 个有
- `GetNode` —— 3/6 个有
- `MathExpression|pysssss` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `WanVideoImageResizeToClosest` —— 3/6 个有
- `easy float` —— 3/6 个有
- `easy int` —— 3/6 个有
- `Audio Duration (mtb)` —— 2/6 个有
- `CLIPLoader` —— 2/6 个有
- `LTXVAudioVAEEncode` —— 2/6 个有
- `LTXVDualCFGGuider` —— 2/6 个有
- `LTXVGemmaCLIPModelLoader` —— 2/6 个有
- `LoadAudio` —— 2/6 个有
- `MelBandRoFormerModelLoader` —— 2/6 个有
- `MelBandRoFormerSampler` —— 2/6 个有
- `SetLatentNoiseMask` —— 2/6 个有
- `SolidMask` —— 2/6 个有
- `TrimAudioDuration` —— 2/6 个有
- `UNETLoader` —— 2/6 个有
- `VAELoader` —— 2/6 个有
- `easy boolean` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `easy ifElse` —— 2/6 个有
- `CM_FloatToInt` —— 1/6 个有
- `CR Float To Integer` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `LTXVCropGuides` —— 1/6 个有
- `VAEDecode` —— 1/6 个有
- `VHS_VideoCombine` —— 1/6 个有
- `easy clearCacheAll` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 97 - 121 | 6 | 92% |
| 高度 | 25 | 25 - 25 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 97 - 121，6 个样本，取值集中（一致性 92%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
