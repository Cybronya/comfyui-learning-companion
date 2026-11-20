---
name: unknown_workflow_video_upscale_latent_upscale_105
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.829333
common_nodes: [Any Switch (rgthree), CFGGuider, CLIPTextEncode, CR Text, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadAudio, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SetLatentNoiseMask, SimpleMath+, SolidMask, TrimAudioDuration, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [数字人/数字人/短视频鸡汤文案-口播数字人_2033773182313832449.json, 数字人/数字人/短视频鸡汤文案-口播数字人_2033799108900691969.json, 视频生成/文生视频/LTX2.3 - 多功能可独立音频数字人_2047017723305140225.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_105

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（数字人/数字人/短视频鸡汤文案-口播数字人_2033773182313832449.json、数字人/数字人/短视频鸡汤文案-口播数字人_2033799108900691969.json、视频生成/文生视频/LTX2.3 - 多功能可独立音频数字人_2047017723305140225.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
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
- `SamplerCustomAdvanced`
- `SetLatentNoiseMask`
- `SimpleMath+`
- `SolidMask`
- `TrimAudioDuration`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `AudioToFPS` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `ImageSharpen` —— 2/3 个有
- `IndexTTS2Run` —— 2/3 个有
- `Qwen3ASRLoader` —— 2/3 个有
- `Qwen3ASRTranscribe` —— 2/3 个有
- `Qwen3TTSCustomVoice` —— 2/3 个有
- `Qwen3TTSModelLoader` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `RunningHub Deepcleaner` —— 2/3 个有
- `SaveAudio` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `AudioCrop` —— 1/3 个有
- `CM_IntToFloat` —— 1/3 个有
- `CreateVideo` —— 1/3 个有
- `LTXVEmptyLatentAudio` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `ResizeImagesByLongerEdge` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 1 | 100% |
| 高度 | 25 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
