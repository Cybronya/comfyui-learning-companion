---
name: unknown_workflow_video_upscale_latent_upscale_73
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.693333
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.0 文生视频_2008733695988994049.json, 视频生成/文生视频/LTX2.3 图生视频+全节点注释_2066555321589526529.json, 视频生成/文生视频/LTX2.3高质量文生视频_2036689895091081218.json, 视频生成/文生视频/LTX2.3：图生、文生视频_2044341159635460098.json, 视频生成/文生视频/优化字幕版LTX2.3全自动图生_ 文生视频_2033796750112202753.json, 视频生成/文生视频/图&文生视频-LTX2.3-自动提示词-稳定优化版_2030497638990225409.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_73

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/LTX2.0 文生视频_2008733695988994049.json、视频生成/文生视频/LTX2.3 图生视频+全节点注释_2066555321589526529.json、视频生成/文生视频/LTX2.3高质量文生视频_2036689895091081218.json、视频生成/文生视频/LTX2.3：图生、文生视频_2044341159635460098.json、视频生成/文生视频/优化字幕版LTX2.3全自动图生_ 文生视频_2033796750112202753.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：69%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
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
- `INTConstant` —— 5/6 个有
- `LTXVImgToVideoConditionOnly` —— 5/6 个有
- `LTXVPreprocess` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `PrimitiveBoolean` —— 5/6 个有
- `CR Text` —— 4/6 个有
- `LTXVChunkFeedForward` —— 4/6 个有
- `MathExpression|pysssss` —— 4/6 个有
- `ModelPatchTorchSettings` —— 4/6 个有
- `PathchSageAttentionKJ` —— 4/6 个有
- `GetNode` —— 3/6 个有
- `PrimitiveInt` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `AILab_QwenVL` —— 2/6 个有
- `CM_FloatToInt` —— 2/6 个有
- `Int` —— 2/6 个有
- `PreviewAny` —— 2/6 个有
- `PrimitiveFloat` —— 2/6 个有
- `RH_LLMAPI_Pro_Node` —— 2/6 个有
- `Bjornulf_IfElse` —— 1/6 个有
- `CM_IntToFloat` —— 1/6 个有
- `DF_Int_to_Float` —— 1/6 个有
- `FancyTimerNode` —— 1/6 个有
- `JWDatetimeString` —— 1/6 个有
- `JoinStrings` —— 1/6 个有
- `Qwen2.5VL` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `Text` —— 1/6 个有
- `Text Multiline` —— 1/6 个有
- `TextCombinerTwo` —— 1/6 个有
- `Textbox` —— 1/6 个有
- `VRAMReserver` —— 1/6 个有
- `easy showAnything` —— 1/6 个有
- `intToFloat _O` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 6 | 91% |
| 高度 | 25 | 25 - 25 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，6 个样本，取值集中（一致性 91%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
