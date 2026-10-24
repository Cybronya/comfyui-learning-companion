---
name: unknown_workflow_upscale_latent_upscale_lora_19
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.867923
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3首尾帧视频生成_2030927886542180353.json, 视频生成/图生视频/LTX-2.3高动态MV无限时长，一张图一段音频一键生成。_2037366573874290689.json, 视频生成/图生视频/LTX-2.3：把”白狐酱板鸭_装进OpenClaw！_2058356490804752385.json, 视频生成/图生视频/LTX2.3 图 + 音频数字人对口型_2043593704170070018.json, 视频生成/图生视频/LTX2.3 图生视频_2043581288925372417.json, 视频生成/图生视频/LTX2.3 多图参考_2031341831253925890.json, 视频生成/图生视频/LTX2.3 多图参考_2032121353918226434.json, 视频生成/图生视频/LTX2.3-图像音频生视频，口型同步_2031297244112101377.json, 视频生成/图生视频/LTX2.3-数字人（支持双人对话）_2031346405217935361.json, 视频生成/图生视频/LTX2.3_数字人口播_v1.0_（mv数字人）_2054790441681342465.json, 视频生成/图生视频/LTX2.3_数字人口播_v1.1_（自定义音频_图像生视频）_2054484478025838593.json, 视频生成/图生视频/OpenClaw + Fish Audio：一键复现“不要怕”名场面！_2039165345923080193.json, 视频生成/图生视频/🐱video_LTX2.3_I2V自定义音频图像生视频_2031928367213187074.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_19

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3首尾帧视频生成_2030927886542180353.json、视频生成/图生视频/LTX-2.3高动态MV无限时长，一张图一段音频一键生成。_2037366573874290689.json、视频生成/图生视频/LTX-2.3：把”白狐酱板鸭_装进OpenClaw！_2058356490804752385.json、视频生成/图生视频/LTX2.3 图 + 音频数字人对口型_2043593704170070018.json、视频生成/图生视频/LTX2.3 图生视频_2043581288925372417.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 12/13 个有
- `LTXVImgToVideoInplace` —— 12/13 个有
- `ResizeImagesByLongerEdge` —— 12/13 个有
- `PrimitiveStringMultiline` —— 10/13 个有
- `LTXVAudioVAEEncode` —— 8/13 个有
- `LoadAudio` —— 8/13 个有
- `PrimitiveBoolean` —— 8/13 个有
- `SetLatentNoiseMask` —— 8/13 个有
- `SolidMask` —— 8/13 个有
- `PrimitiveFloat` —— 7/13 个有
- `ResizeImageMaskNode` —— 7/13 个有
- `TrimAudioDuration` —— 7/13 个有
- `LTXVEmptyLatentAudio` —— 5/13 个有
- `PreviewAny` —— 5/13 个有
- `ImageResizeKJv2` —— 3/13 个有
- `LoraLoader` —— 3/13 个有
- `TextGenerateLTX2Prompt` —— 3/13 个有
- `LTX2_NAG` —— 2/13 个有
- `LTXVImgToVideoInplaceKJ` —— 2/13 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/13 个有
- `Qwen3ASRLoader_DFT` —— 2/13 个有
- `Qwen3ASRTranscribe_DFT` —— 2/13 个有
- `SimpleMath+` —— 2/13 个有
- `SoundFlow_GetLength` —— 2/13 个有
- `StringReplace` —— 2/13 个有
- `AudioCrop` —— 1/13 个有
- `AudioInfo` —— 1/13 个有
- `Bjornulf_ShowInt` —— 1/13 个有
- `FishS2VoiceCloneTTS` —— 1/13 个有
- `GetImageSize` —— 1/13 个有
- `ImageResize+` —— 1/13 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/13 个有
- `Label (rgthree)` —— 1/13 个有
- `MathExpression|pysssss` —— 1/13 个有
- `PreviewAudio` —— 1/13 个有
- `RH_LLMAPI_Pro_Node` —— 1/13 个有
- `StringConcatenate` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有
- `string_util_StrConcat` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 24 - 25 | 5 | 98% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，5 个样本，取值集中（一致性 98%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
