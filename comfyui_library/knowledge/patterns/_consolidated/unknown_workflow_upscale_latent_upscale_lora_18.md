---
name: unknown_workflow_upscale_latent_upscale_lora_18
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.844818
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, TrimAudioDuration]
problems: []
missing: []
members: [数字人/数字人/DaNotebook LTX2.3 Digital_2093191068970999809.json, 数字人/数字人/LTX2.3数字人说话唱歌 精准对口型_2059893900621475841.json, 视频生成/图生视频/2053481289776414721.json, 视频生成/图生视频/ALTX2.3- 小寻唱歌·AI 对口型唱歌 MV 生成器_2089802778116972546.json, 视频生成/图生视频/2044225142284357633.json, 视频生成/图生视频/2035291558307700737.json, 视频生成/图生视频/2037907809546805250.json, 视频生成/图生视频/2062387729098428417.json, 视频生成/图生视频/LTX2.3数字人说话唱歌 精准对口型_2087214680174583809.json, 视频生成/图生视频/LTX2.3数字人说话唱歌高精准对口型_2101198595667095554.json, 视频生成/文生视频/LTX2.3数字人说话唱歌-无字幕、提示词优化版_2034907055777124353.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_18

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（数字人/数字人/DaNotebook LTX2.3 Digital_2093191068970999809.json、数字人/数字人/LTX2.3数字人说话唱歌 精准对口型_2059893900621475841.json、视频生成/图生视频/2053481289776414721.json、视频生成/图生视频/ALTX2.3- 小寻唱歌·AI 对口型唱歌 MV 生成器_2089802778116972546.json、视频生成/图生视频/2044225142284357633.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
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
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SolidMask`
- `TrimAudioDuration`

**可变部分**（部分 workflow 才有）：
- `LoadAudio` —— 10/11 个有
- `LoadImage` —— 10/11 个有
- `PrimitiveBoolean` —— 10/11 个有
- `ResizeImageMaskNode` —— 10/11 个有
- `VAEDecodeTiled` —— 10/11 个有
- `PrimitiveStringMultiline` —— 9/11 个有
- `easy cleanGpuUsed` —— 9/11 个有
- `Any Switch (rgthree)` —— 7/11 个有
- `CM_IntToFloat` —— 7/11 个有
- `LTXVEmptyLatentAudio` —— 7/11 个有
- `RHHiddenNodes` —— 7/11 个有
- `SimpleMath+` —— 7/11 个有
- `VHS_VideoCombine` —— 7/11 个有
- `PreviewAny` —— 4/11 个有
- `PrimitiveFloat` —— 4/11 个有
- `SaveVideo` —— 4/11 个有
- `PreviewImage` —— 3/11 个有
- `RH_LLMAPI_Pro_Node` —— 3/11 个有
- `Fast Groups Bypasser (rgthree)` —— 2/11 个有
- `LoraLoader` —— 2/11 个有
- `TextGenerateLTX2Prompt` —— 2/11 个有
- `ConditioningConcat` —— 1/11 个有
- `DA_LoadMedia` —— 1/11 个有
- `DA_Nag` —— 1/11 个有
- `GetImageSize` —— 1/11 个有
- `Int` —— 1/11 个有
- `Label (rgthree)` —— 1/11 个有
- `ResolutionSelector` —— 1/11 个有
- `SaveImage` —— 1/11 个有
- `TT_img_enc_v2` —— 1/11 个有
- `VAEDecode` —— 1/11 个有
- `easy clearCacheAll` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 25 - 25 | 7 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
