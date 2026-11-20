---
name: unknown_workflow_lora_sampler_clip_93
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.852
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/LTX 2.3-IA2V-国风 MV_2038201954467323905.json, 视频生成/图生视频/LTX2.3音频图片生成视频_2051636070026096642.json, 视频生成/图生视频/LTX2_3_image_and_audio_to_video_ia2v_2083484804493955073.json, 视频生成/图生视频/LTX_2_3_I2V_Basic_2081391586033889281.json, 视频生成/图生视频/Ltx2.3 _mv数字人_2044558768721108993.json, 视频生成/图生视频/OpenClaw + Fish Audio：一键复现“不要怕”名场面！_2039165345923080193.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_93

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/LTX 2.3-IA2V-国风 MV_2038201954467323905.json、视频生成/图生视频/LTX2.3音频图片生成视频_2051636070026096642.json、视频生成/图生视频/LTX2_3_image_and_audio_to_video_ia2v_2083484804493955073.json、视频生成/图生视频/LTX_2_3_I2V_Basic_2081391586033889281.json、视频生成/图生视频/Ltx2.3 _mv数字人_2044558768721108993.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 6 个 workflow 都包含：
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
- `CheckpointLoaderSimple` —— 5/6 个有
- `CreateVideo` —— 5/6 个有
- `LTXAVTextEncoderLoader` —— 5/6 个有
- `LTXVAudioVAEEncode` —— 5/6 个有
- `LTXVLatentUpsampler` —— 5/6 个有
- `LatentUpscaleModelLoader` —— 5/6 个有
- `LoadAudio` —— 5/6 个有
- `PrimitiveBoolean` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `SaveVideo` —— 5/6 个有
- `SetLatentNoiseMask` —— 5/6 个有
- `SolidMask` —— 5/6 个有
- `TrimAudioDuration` —— 5/6 个有
- `PrimitiveFloat` —— 4/6 个有
- `LoraLoader` —— 3/6 个有
- `PreviewAny` —— 3/6 个有
- `RecordAudio` —— 3/6 个有
- `TextGenerateLTX2Prompt` —— 3/6 个有
- `ComfySwitchNode` —— 2/6 个有
- `Anything Everywhere` —— 1/6 个有
- `AudioInfo` —— 1/6 个有
- `Bjornulf_ShowInt` —— 1/6 个有
- `DiffusionModelLoaderKJ` —— 1/6 个有
- `DualCLIPLoaderGGUF` —— 1/6 个有
- `FishS2VoiceCloneTTS` —— 1/6 个有
- `LTXVEmptyLatentAudio` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `PreviewAudio` —— 1/6 个有
- `SoundFlow_GetLength` —— 1/6 个有
- `StringReplace` —— 1/6 个有
- `Text` —— 1/6 个有
- `Text Concatenate` —— 1/6 个有
- `UnetLoaderGGUF` —— 1/6 个有
- `VAELoaderKJ` —— 1/6 个有
- `VHS_VideoCombine` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 97 | - | 1 | 100% |
| 高度 | 25 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
