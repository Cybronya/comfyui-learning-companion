---
name: unknown_workflow_upscale_latent_upscale_lora_33
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.866636
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3首尾帧视频生成_2030927886542180353.json, 视频生成/图生视频/LTX-2.3高动态MV无限时长，一张图一段音频一键生成。_2037366573874290689.json, 视频生成/图生视频/LTX-2.3：把”白狐酱板鸭_装进OpenClaw！_2058356490804752385.json, 视频生成/图生视频/LTX2.3 图 + 音频数字人对口型_2043593704170070018.json, 视频生成/图生视频/LTX2.3 图生视频_2043581288925372417.json, 视频生成/图生视频/LTX2.3 多图参考_2031341831253925890.json, 视频生成/图生视频/LTX2.3 多图参考_2032121353918226434.json, 视频生成/图生视频/LTX2.3 数字人艾希&李小小《我们都是数字人》播客生产工作流 V3.00331_2038794251055669250.json, 视频生成/图生视频/LTX2.3-图像音频生视频，口型同步_2031297244112101377.json, 视频生成/图生视频/LTX2.3-数字人（支持双人对话）_2031346405217935361.json, 视频生成/图生视频/LTX2_3_image_and_audio_to_video_ia2v_2083484804493955073.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_33

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3首尾帧视频生成_2030927886542180353.json、视频生成/图生视频/LTX-2.3高动态MV无限时长，一张图一段音频一键生成。_2037366573874290689.json、视频生成/图生视频/LTX-2.3：把”白狐酱板鸭_装进OpenClaw！_2058356490804752385.json、视频生成/图生视频/LTX2.3 图 + 音频数字人对口型_2043593704170070018.json、视频生成/图生视频/LTX2.3 图生视频_2043581288925372417.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
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
- `ComfyMathExpression` —— 10/11 个有
- `LTXVImgToVideoInplace` —— 10/11 个有
- `ResizeImagesByLongerEdge` —— 10/11 个有
- `PrimitiveStringMultiline` —— 9/11 个有
- `ResizeImageMaskNode` —— 7/11 个有
- `LTXVEmptyLatentAudio` —— 6/11 个有
- `LTXVAudioVAEEncode` —— 5/11 个有
- `LoadAudio` —— 5/11 个有
- `PrimitiveBoolean` —— 5/11 个有
- `PrimitiveFloat` —— 5/11 个有
- `SetLatentNoiseMask` —— 5/11 个有
- `SolidMask` —— 5/11 个有
- `TrimAudioDuration` —— 4/11 个有
- `ImageResizeKJv2` —— 3/11 个有
- `LTXVImgToVideoInplaceKJ` —— 3/11 个有
- `PreviewAny` —— 3/11 个有
- `LTX2_NAG` —— 2/11 个有
- `LoraLoader` —— 2/11 个有
- `SimpleMath+` —— 2/11 个有
- `TextGenerateLTX2Prompt` —— 2/11 个有
- `AudioCrop` —— 1/11 个有
- `ComfySwitchNode` —— 1/11 个有
- `FloatConstant` —— 1/11 个有
- `GetImageSize` —— 1/11 个有
- `ImageResize+` —— 1/11 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/11 个有
- `MathExpression|pysssss` —— 1/11 个有
- `RH_LLMAPI_Pro_Node` —— 1/11 个有
- `RecordAudio` —— 1/11 个有
- `Resize` —— 1/11 个有
- `StringReplace` —— 1/11 个有
- `easy showAnything` —— 1/11 个有
- `string_util_StrConcat` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 24 - 25 | 6 | 98% |
| LoRA 模型强度 | 1 | - | 2 | 100% |
| LoRA 文本强度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，6 个样本，取值集中（一致性 98%）
- LoRA 模型强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
