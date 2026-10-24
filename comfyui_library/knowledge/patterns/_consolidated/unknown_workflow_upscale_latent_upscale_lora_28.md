---
name: unknown_workflow_upscale_latent_upscale_lora_28
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7619
common_nodes: [Bjornulf_ShowInt, CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAEEncode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PainterAudioLength, PathchSageAttentionKJ, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, SetLatentNoiseMask, SimpleMath+, SolidMask, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/LTX2.3 高质量单图音频数字人MV（效果好）_2045105546377826305.json, 视频生成/图生视频/LTX2.3 _ 三图-首中尾帧 音频克隆(附带音色设计) 优化版_2033197165668999170.json, 视频生成/图生视频/LTX2.3 _音频数字人MV_2037904151203549186.json, 视频生成/图生视频/LTX2.3 _音频数字人MV_2039705616616263681.json, 视频生成/图生视频/LTX2.3 ai2v 高质量超自然图+克隆音频生数字人_2032689684190597122.json, 视频生成/图生视频/LTX2.3 高质量超自然图+音频数字人MV_2033038433718898690.json, 视频生成/图生视频/三图首尾帧自定义文案视频生成-LTX2.3-电商、广告、口播_2033180233595097089.json, 视频生成/图生视频/音频数字人MVLTX2.3 _ 上传音频+图片即可_2044840720346910722.json, 视频生成/图生视频/首尾帧视频数字人-无字幕-音频克隆版-LTX2.3-优化版~（支持手自动提示词）_2033020049098805250.json, 视频生成/文生视频/LTX2.3-高质量超自然图+克隆音频生数字人_2032834292765696002.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_28

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/LTX2.3 高质量单图音频数字人MV（效果好）_2045105546377826305.json、视频生成/图生视频/LTX2.3 _ 三图-首中尾帧 音频克隆(附带音色设计) 优化版_2033197165668999170.json、视频生成/图生视频/LTX2.3 _音频数字人MV_2037904151203549186.json、视频生成/图生视频/LTX2.3 _音频数字人MV_2039705616616263681.json、视频生成/图生视频/LTX2.3 ai2v 高质量超自然图+克隆音频生数字人_2032689684190597122.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 10 个 workflow 都包含：
- `Bjornulf_ShowInt`
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAEEncode`
- `LTXVAudioVAELoader`
- `LTXVChunkFeedForward`
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
- `ModelPatchTorchSettings`
- `PainterAudioLength`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `SetLatentNoiseMask`
- `SimpleMath+`
- `SolidMask`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 9/10 个有
- `GetImageSize` —— 9/10 个有
- `ImageScaleBy` —— 9/10 个有
- `ImpactInt` —— 9/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/10 个有
- `LoadAudio` —— 9/10 个有
- `PreviewAudio` —— 9/10 个有
- `VAEDecode` —— 9/10 个有
- `AudioCrop` —— 5/10 个有
- `CR Prompt Text` —— 5/10 个有
- `CR Text` —— 5/10 个有
- `RH_LLMAPI_Pro_Node` —— 5/10 个有
- `FB_Qwen3TTSVoiceClone` —— 4/10 个有
- `SetNode` —— 4/10 个有
- `WhisperSTT` —— 4/10 个有
- `easy seed` —— 3/10 个有
- `ComfyMathExpression` —— 2/10 个有
- `FloatConstant` —— 2/10 个有
- `LTXVEmptyLatentAudio` —— 2/10 个有
- `LTXVImgToVideoInplaceKJ` —— 2/10 个有
- `PreviewAny` —— 2/10 个有
- `ShowAnything|Mie` —— 2/10 个有
- `AudioConcatenate` —— 1/10 个有
- `DualCLIPLoader` —— 1/10 个有
- `FB_Qwen3TTSVoiceDesign` —— 1/10 个有
- `Float` —— 1/10 个有
- `ImpactConditionalBranch` —— 1/10 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/10 个有
- `PlaySound|pysssss` —— 1/10 个有
- `PreviewImage` —— 1/10 个有
- `PrimitiveInt` —— 1/10 个有
- `PrimitiveStringMultiline` —— 1/10 个有
- `Resize` —— 1/10 个有
- `ResizeImageMaskNode` —— 1/10 个有
- `SaveAudio` —— 1/10 个有
- `Switch any [Crystools]` —— 1/10 个有
- `Text` —— 1/10 个有
- `TextGenerateLTX2Prompt` —— 1/10 个有
- `VAEDecodeTiled` —— 1/10 个有
- `easy imageConcat` —— 1/10 个有
- `easy int` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
