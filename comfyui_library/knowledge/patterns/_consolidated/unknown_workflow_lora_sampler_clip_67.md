---
name: unknown_workflow_lora_sampler_clip_67
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.862857
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/LTX 2.3-IA2V-国风 MV_2038201954467323905.json, 视频生成/图生视频/LTX2.3音频图片生成视频_2051636070026096642.json, 视频生成/图生视频/LTX2_3_image_and_audio_to_video_ia2v_2083484804493955073.json, 视频生成/图生视频/LTX_2_3_I2V_Basic_2081391586033889281.json, 视频生成/图生视频/Ltx2.3 _mv数字人_2044558768721108993.json, 视频生成/图生视频/Ltx2.3+龙猫克隆+图片输入文案自动化配音生成数字人视频_2049792632808853506.json, 视频生成/图生视频/Ltx2.3指定音色+图片输入文案自动化配音生成数字人视频_2040420049630007297.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_67

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/LTX 2.3-IA2V-国风 MV_2038201954467323905.json、视频生成/图生视频/LTX2.3音频图片生成视频_2051636070026096642.json、视频生成/图生视频/LTX2_3_image_and_audio_to_video_ia2v_2083484804493955073.json、视频生成/图生视频/LTX_2_3_I2V_Basic_2081391586033889281.json、视频生成/图生视频/Ltx2.3 _mv数字人_2044558768721108993.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 6/7 个有
- `CreateVideo` —— 6/7 个有
- `LTXAVTextEncoderLoader` —— 6/7 个有
- `LTXVAudioVAEEncode` —— 6/7 个有
- `LTXVLatentUpsampler` —— 6/7 个有
- `LatentUpscaleModelLoader` —— 6/7 个有
- `LoadAudio` —— 6/7 个有
- `PrimitiveBoolean` —— 6/7 个有
- `PrimitiveFloat` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `SaveVideo` —— 6/7 个有
- `SetLatentNoiseMask` —— 6/7 个有
- `SolidMask` —— 6/7 个有
- `TrimAudioDuration` —— 6/7 个有
- `RecordAudio` —— 3/7 个有
- `SoundFlow_GetLength` —— 3/7 个有
- `Text` —— 3/7 个有
- `easy cleanGpuUsed` —— 3/7 个有
- `Apply Whisper` —— 2/7 个有
- `ComfySwitchNode` —— 2/7 个有
- `LongCatVoiceCloneTTS` —— 2/7 个有
- `LoraLoader` —— 2/7 个有
- `MelBandRoFormerModelLoader` —— 2/7 个有
- `MelBandRoFormerSampler` —— 2/7 个有
- `PreviewAny` —— 2/7 个有
- `TextGenerateLTX2Prompt` —— 2/7 个有
- `Anything Everywhere` —— 1/7 个有
- `DiffusionModelLoaderKJ` —— 1/7 个有
- `DualCLIPLoaderGGUF` —— 1/7 个有
- `Fast Groups Bypasser (rgthree)` —— 1/7 个有
- `IAMCCS_VRAMCleanup` —— 1/7 个有
- `LTXVEmptyLatentAudio` —— 1/7 个有
- `NormalizeAudioLoudness` —— 1/7 个有
- `Text Concatenate` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有
- `VAELoaderKJ` —— 1/7 个有
- `VHS_VideoCombine` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 97 | - | 1 | 100% |
| 高度 | 25 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
