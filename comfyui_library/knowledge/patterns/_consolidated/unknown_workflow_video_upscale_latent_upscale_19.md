---
name: unknown_workflow_video_upscale_latent_upscale_19
type: Unknown Workflow
frequency: 15
level: strong
coverage: 0.8394
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/LTX2.0 文生视频_2008733695988994049.json, 视频生成/文生视频/LTX2.3 图生视频+全节点注释_2066555321589526529.json, 视频生成/文生视频/LTX2.3低显存文生图_图生图_首尾帧 视频生成ai漫剧短剧视频 保持人物一致性性价比超高LTX2_2031559977218875394.json, 视频生成/文生视频/LTX2.3全自动_手动提示词 图生视频  低消耗 人物一致 精准版_2057632019441602562.json, 视频生成/文生视频/LTX2.3全自动—图生_文生视频_2030257060473999361.json, 视频生成/文生视频/LTX2.3全自动图生+文生视频_2033000599163248642.json, 视频生成/文生视频/LTX2.3图生_ 文生视频_2033992306809905153.json, 视频生成/文生视频/LTX2.3图生_ 文生视频_2053005533375938562.json, 视频生成/文生视频/LTX2.3文生_图生视频-无字幕_2036254878376398850.json, 视频生成/文生视频/LTX2.3文生视频与图生视频-单_双人对话-唱歌_2033038147285688321.json, 视频生成/文生视频/LTX2.3文生视频与图生视频_2032329781139738626.json, 视频生成/文生视频/LTX2.3最强优化版_全自动-图生_ 文生视频_2049699781685063682.json, 视频生成/文生视频/LTX2.3高质量文生视频_2036689895091081218.json, 视频生成/文生视频/LTX2.3：图生、文生视频_2044341159635460098.json, 视频生成/文生视频/优化字幕版LTX2.3全自动图生_ 文生视频_2033796750112202753.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_19

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/文生视频/LTX2.0 文生视频_2008733695988994049.json、视频生成/文生视频/LTX2.3 图生视频+全节点注释_2066555321589526529.json、视频生成/文生视频/LTX2.3低显存文生图_图生图_首尾帧 视频生成ai漫剧短剧视频 保持人物一致性性价比超高LTX2_2031559977218875394.json、视频生成/文生视频/LTX2.3全自动_手动提示词 图生视频  低消耗 人物一致 精准版_2057632019441602562.json、视频生成/文生视频/LTX2.3全自动—图生_文生视频_2030257060473999361.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 15 个 workflow 都包含：
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
- `CR Text` —— 14/15 个有
- `INTConstant` —— 14/15 个有
- `LTXVImgToVideoConditionOnly` —— 14/15 个有
- `LTXVPreprocess` —— 14/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 14/15 个有
- `PrimitiveBoolean` —— 14/15 个有
- `LTXVChunkFeedForward` —— 13/15 个有
- `LTXVConditioning` —— 13/15 个有
- `ModelPatchTorchSettings` —— 13/15 个有
- `PathchSageAttentionKJ` —— 13/15 个有
- `CM_FloatToInt` —— 12/15 个有
- `PrimitiveFloat` —— 12/15 个有
- `RH_LLMAPI_Pro_Node` —— 11/15 个有
- `PrimitiveInt` —— 10/15 个有
- `PreviewAny` —— 9/15 个有
- `MathExpression|pysssss` —— 4/15 个有
- `GetNode` —— 3/15 个有
- `SetNode` —— 3/15 个有
- `SimpleMath+` —— 3/15 个有
- `Fast Groups Bypasser (rgthree)` —— 2/15 个有
- `Int` —— 2/15 个有
- `ShowText|pysssss` —— 2/15 个有
- `easy int` —— 2/15 个有
- `AILab_QwenVL` —— 1/15 个有
- `Bjornulf_IfElse` —— 1/15 个有
- `DF_Int_to_Float` —— 1/15 个有
- `FancyTimerNode` —— 1/15 个有
- `JWDatetimeString` —— 1/15 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/15 个有
- `Qwen2.5VL` —— 1/15 个有
- `Text` —— 1/15 个有
- `TextCombinerTwo` —— 1/15 个有
- `Textbox` —— 1/15 个有
- `intToFloat _O` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 15 | 94% |
| 高度 | 25 | 25 - 25 | 15 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，15 个样本，取值集中（一致性 94%）
- 高度 中位数 25，观测区间 25 - 25，15 个样本，取值集中（一致性 100%）
