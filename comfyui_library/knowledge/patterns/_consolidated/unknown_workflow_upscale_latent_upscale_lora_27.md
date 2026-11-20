---
name: unknown_workflow_upscale_latent_upscale_lora_27
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.845083
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SetLatentNoiseMask, SolidMask, TrimAudioDuration, easy cleanGpuUsed]
problems: []
missing: []
members: [数字人/数字人/LTX2.3数字人说话唱歌 精准对口型_2059893900621475841.json, 数字人/数字人/Ltx2.3指定音色+图片输入文案自动化配音生成数字人视频_2053381791427375106.json, 视频生成/图生视频/7-LTX 2.3（音频转视频）Image + Audio to Video_2053481289776414721.json, 视频生成/图生视频/ALTX2.3- 小寻唱歌·AI 对口型唱歌 MV 生成器_2089802778116972546.json, 视频生成/图生视频/LTX-2.3-Image Audio to Video-distilled-lora-1.1_2044225142284357633.json, 视频生成/图生视频/LTX2.3图生视频说话唱歌_骆驼版本_2037907809546805250.json, 视频生成/图生视频/LTX2.3数字人精准对口型，类型：说话、唱歌_2062387729098428417.json, 视频生成/图生视频/LTX2.3数字人说话唱歌 精准对口型_2087214680174583809.json, 视频生成/图生视频/LTX2.3数字人说话唱歌高精准对口型_2101198595667095554.json, 视频生成/图生视频/Ltx2.3+龙猫克隆+图片输入文案自动化配音生成数字人视频_2049792632808853506.json, 视频生成/图生视频/Ltx2.3指定音色+图片输入文案自动化配音生成数字人视频_2040420049630007297.json, 视频生成/文生视频/LTX2.3数字人说话唱歌-无字幕、提示词优化版_2034907055777124353.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_27

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（数字人/数字人/LTX2.3数字人说话唱歌 精准对口型_2059893900621475841.json、数字人/数字人/Ltx2.3指定音色+图片输入文案自动化配音生成数字人视频_2053381791427375106.json、视频生成/图生视频/7-LTX 2.3（音频转视频）Image + Audio to Video_2053481289776414721.json、视频生成/图生视频/ALTX2.3- 小寻唱歌·AI 对口型唱歌 MV 生成器_2089802778116972546.json、视频生成/图生视频/LTX-2.3-Image Audio to Video-distilled-lora-1.1_2044225142284357633.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 12 个 workflow 都包含：
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
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SolidMask`
- `TrimAudioDuration`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 11/12 个有
- `ResizeImageMaskNode` —— 11/12 个有
- `VAEDecodeTiled` —— 11/12 个有
- `Any Switch (rgthree)` —— 7/12 个有
- `CM_IntToFloat` —— 7/12 个有
- `LTXVEmptyLatentAudio` —— 7/12 个有
- `RHHiddenNodes` —— 7/12 个有
- `SimpleMath+` —— 7/12 个有
- `VHS_VideoCombine` —— 7/12 个有
- `PrimitiveFloat` —— 5/12 个有
- `SaveVideo` —— 5/12 个有
- `Fast Groups Bypasser (rgthree)` —— 4/12 个有
- `PreviewAny` —— 4/12 个有
- `Apply Whisper` —— 3/12 个有
- `LongCatVoiceCloneTTS` —— 3/12 个有
- `MelBandRoFormerModelLoader` —— 3/12 个有
- `MelBandRoFormerSampler` —— 3/12 个有
- `PreviewImage` —— 3/12 个有
- `RH_LLMAPI_Pro_Node` —— 3/12 个有
- `SoundFlow_GetLength` —— 3/12 个有
- `Text` —— 3/12 个有
- `LoraLoader` —— 2/12 个有
- `TextGenerateLTX2Prompt` —— 2/12 个有
- `ConditioningConcat` —— 1/12 个有
- `GetImageSize` —— 1/12 个有
- `IAMCCS_VRAMCleanup` —— 1/12 个有
- `Int` —— 1/12 个有
- `Label (rgthree)` —— 1/12 个有
- `NormalizeAudioLoudness` —— 1/12 个有
- `SaveImage` —— 1/12 个有
- `TT_img_enc_v2` —— 1/12 个有
- `VAEDecode` —— 1/12 个有
- `easy clearCacheAll` —— 1/12 个有

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
