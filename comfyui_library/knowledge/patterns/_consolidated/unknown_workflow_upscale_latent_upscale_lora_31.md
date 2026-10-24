---
name: unknown_workflow_upscale_latent_upscale_lora_31
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8441
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/ltx2.3参考图+参考音色_2041020461265457154.json, 视频生成/图生视频/ltx2.3图生视频-官方版_2057789192654123010.json, 视频生成/图生视频/【图+文→生视频】飞灵AI高质量版_2067639353119174658.json, 视频生成/图生视频/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）_2033190788460453889.json, 视频生成/图生视频/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）自动横屏竖屏_2033053099966865410.json, 视频生成/图生视频/🐱video_ITX2.3_I2V图像首尾帧生视频_2031942296714878977.json, 视频生成/文生视频/AI真人短剧工作流+文生_图生视频_2035632455331356674.json, 视频生成/文生视频/LTX-Video (2.3) IC-LoRA_ 双人分镜头对话_2038235232167534593.json, 视频生成/文生视频/LTX2.3文生_图生视频 AI真人短剧工作流_2053318411618398209.json, 视频生成/文生视频/LTX2.3文生_图生视频 AI真人短剧工作流_2054136644139266049.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_31

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/ltx2.3参考图+参考音色_2041020461265457154.json、视频生成/图生视频/ltx2.3图生视频-官方版_2057789192654123010.json、视频生成/图生视频/【图+文→生视频】飞灵AI高质量版_2067639353119174658.json、视频生成/图生视频/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）_2033190788460453889.json、视频生成/图生视频/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）自动横屏竖屏_2033053099966865410.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `PrimitiveStringMultiline` —— 9/10 个有
- `ResizeImageMaskNode` —— 9/10 个有
- `CreateVideo` —— 8/10 个有
- `SaveVideo` —— 8/10 个有
- `RH_LLMAPI_Pro_Node` —— 6/10 个有
- `easy showAnything` —— 5/10 个有
- `GetNode` —— 4/10 个有
- `SetNode` —— 4/10 个有
- `DeepTranslatorTextNode` —— 3/10 个有
- `LoraLoader` —— 3/10 个有
- `PreviewAny` —— 3/10 个有
- `TextGenerateLTX2Prompt` —— 3/10 个有
- `ImageSharpen` —— 2/10 个有
- `LTX2SamplingPreviewOverride` —— 2/10 个有
- `LTXVEnhanceAVideoKJ` —— 2/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/10 个有
- `VHS_VideoCombine` —— 2/10 个有
- `CR Text` —— 1/10 个有
- `ComfySwitchNode` —— 1/10 个有
- `ConditioningZeroOut` —— 1/10 个有
- `Fast Groups Muter (rgthree)` —— 1/10 个有
- `FastFilmGrain` —— 1/10 个有
- `LTX2_NAG` —— 1/10 个有
- `LTXVImgToVideoInplaceKJ` —— 1/10 个有
- `LTXVReferenceAudio` —— 1/10 个有
- `PrimitiveFloat` —— 1/10 个有
- `VHS_LoadAudioUpload` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 25 - 25 | 10 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
