---
name: unknown_workflow_upscale_latent_upscale_lora_52
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.832143
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/【LTX2.3官方工作流优化】数字人支持唱歌 音频+图片=超自然数字人 含提示词扩写模板_2034460297049677825.json, 视频生成/图生视频/【LTX2.3官方工作流优化】首尾帧控制 _含提示词扩写模板_2033785787984125953.json, 视频生成/图生视频/【图+文→生视频】飞灵AI高质量版_2067639353119174658.json, 视频生成/图生视频/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）_2033190788460453889.json, 视频生成/图生视频/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）自动横屏竖屏_2033053099966865410.json, 视频生成/图生视频/图生视频一镜到底_已修复_2078421854469050370.json, 视频生成/图生视频/🐱video_ITX2.3_I2V图像首尾帧生视频_2031942296714878977.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_52

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/【LTX2.3官方工作流优化】数字人支持唱歌 音频+图片=超自然数字人 含提示词扩写模板_2034460297049677825.json、视频生成/图生视频/【LTX2.3官方工作流优化】首尾帧控制 _含提示词扩写模板_2033785787984125953.json、视频生成/图生视频/【图+文→生视频】飞灵AI高质量版_2067639353119174658.json、视频生成/图生视频/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）_2033190788460453889.json、视频生成/图生视频/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）自动横屏竖屏_2033053099966865410.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LTXVEmptyLatentAudio` —— 6/7 个有
- `PrimitiveBoolean` —— 6/7 个有
- `PrimitiveStringMultiline` —— 6/7 个有
- `RH_LLMAPI_Pro_Node` —— 6/7 个有
- `ResizeImageMaskNode` —— 5/7 个有
- `easy showAnything` —— 5/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `CR Text` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `LTXVImgToVideoInplaceKJ` —— 2/7 个有
- `LoadAudio` —— 2/7 个有
- `LoraLoader` —— 2/7 个有
- `PlaySound|pysssss` —— 2/7 个有
- `PreviewAny` —— 2/7 个有
- `Text` —— 2/7 个有
- `TextGenerateLTX2Prompt` —— 2/7 个有
- `CR Integer To String` —— 1/7 个有
- `Float` —— 1/7 个有
- `GetAudioDurationFromAudio` —— 1/7 个有
- `ImageResizeKJv2` —— 1/7 个有
- `Int` —— 1/7 个有
- `LTXVAudioVAEEncode` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `RH_LLMAPI_NODE` —— 1/7 个有
- `SetLatentNoiseMask` —— 1/7 个有
- `SolidMask` —— 1/7 个有
- `TrimAudioDuration` —— 1/7 个有
- `easy promptReplace` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 25 - 25 | 6 | 100% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
