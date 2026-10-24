---
name: unknown_workflow_video_upscale_latent_upscale_43
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.755556
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.0 文生视频_2008733695988994049.json, 视频生成/文生视频/LTX2.3 图生视频+全节点注释_2066555321589526529.json, 视频生成/文生视频/LTX2.3文生_图生视频-无字幕_2036254878376398850.json, 视频生成/文生视频/LTX2.3文生视频+图生视频_2034150036669472770.json, 视频生成/文生视频/LTX2.3文生视频与图生视频-单_双人对话-唱歌_2033038147285688321.json, 视频生成/文生视频/LTX2.3文生视频与图生视频_2032329781139738626.json, 视频生成/文生视频/LTX2.3最强优化版_全自动-图生_ 文生视频_2049699781685063682.json, 视频生成/文生视频/LTX2.3高质量文生视频_2036689895091081218.json, 视频生成/文生视频/优化字幕版LTX2.3全自动图生_ 文生视频_2033796750112202753.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_43

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/文生视频/LTX2.0 文生视频_2008733695988994049.json、视频生成/文生视频/LTX2.3 图生视频+全节点注释_2066555321589526529.json、视频生成/文生视频/LTX2.3文生_图生视频-无字幕_2036254878376398850.json、视频生成/文生视频/LTX2.3文生视频+图生视频_2034150036669472770.json、视频生成/文生视频/LTX2.3文生视频与图生视频-单_双人对话-唱歌_2033038147285688321.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideoConditionOnly` —— 8/9 个有
- `LTXVPreprocess` —— 8/9 个有
- `CR Text` —— 7/9 个有
- `INTConstant` —— 7/9 个有
- `LTXVChunkFeedForward` —— 7/9 个有
- `LTXVConditioning` —— 7/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/9 个有
- `ModelPatchTorchSettings` —— 7/9 个有
- `PathchSageAttentionKJ` —— 7/9 个有
- `PrimitiveBoolean` —— 7/9 个有
- `CM_FloatToInt` —— 6/9 个有
- `PrimitiveFloat` —— 5/9 个有
- `RH_LLMAPI_Pro_Node` —— 5/9 个有
- `GetNode` —— 4/9 个有
- `MathExpression|pysssss` —— 4/9 个有
- `SetNode` —— 4/9 个有
- `Int` —— 3/9 个有
- `PreviewAny` —— 3/9 个有
- `PrimitiveInt` —— 3/9 个有
- `SimpleMath+` —— 3/9 个有
- `ShowText|pysssss` —— 2/9 个有
- `Text` —— 2/9 个有
- `easy int` —— 2/9 个有
- `AILab_QwenVL` —— 1/9 个有
- `Bjornulf_IfElse` —— 1/9 个有
- `Bool` —— 1/9 个有
- `DF_Int_to_Float` —— 1/9 个有
- `FancyTimerNode` —— 1/9 个有
- `Float` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `JWDatetimeString` —— 1/9 个有
- `Qwen2.5VL` —— 1/9 个有
- `TextCombinerTwo` —— 1/9 个有
- `Textbox` —— 1/9 个有
- `intToFloat _O` —— 1/9 个有
- `math_calculate` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 9 | 92% |
| 高度 | 25 | 25 - 25 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，9 个样本，取值集中（一致性 92%）
- 高度 中位数 25，观测区间 25 - 25，9 个样本，取值集中（一致性 100%）
