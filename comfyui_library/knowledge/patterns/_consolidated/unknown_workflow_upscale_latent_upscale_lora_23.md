---
name: unknown_workflow_upscale_latent_upscale_lora_23
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.902154
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CR Text, CheckpointLoaderSimple, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/一张图片，简单台词，就能出片了_2039634307186171905.json, 视频生成/文生视频/LTX2.3 图生_ 文生视频【提示词自动优化】_2033527714837176322.json, 视频生成/文生视频/LTX2.3-图生+文生视频_2034105239082635265.json, 视频生成/文生视频/LTX2.3低显存文生图_图生图_首尾帧 视频生成ai漫剧短剧视频 保持人物一致性性价比超高LTX2_2031559977218875394.json, 视频生成/文生视频/LTX2.3全自动_手动提示词 图生视频  低消耗 人物一致 精准版_2057632019441602562.json, 视频生成/文生视频/LTX2.3全自动—图生_文生视频_2030257060473999361.json, 视频生成/文生视频/LTX2.3全自动图生+文生视频_2033000599163248642.json, 视频生成/文生视频/LTX2.3图生_ 文生视频_2033992306809905153.json, 视频生成/文生视频/LTX2.3图生_ 文生视频_2053005533375938562.json, 视频生成/文生视频/LTX2.3文生_图生视频-无字幕_2036254878376398850.json, 视频生成/文生视频/LTX2.3文生视频与图生视频-单_双人对话-唱歌_2033038147285688321.json, 视频生成/文生视频/LTX2.3文生视频与图生视频_2032329781139738626.json, 视频生成/文生视频/文生视频  开源（2）_2046762687073357825.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_23

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/一张图片，简单台词，就能出片了_2039634307186171905.json、视频生成/文生视频/LTX2.3 图生_ 文生视频【提示词自动优化】_2033527714837176322.json、视频生成/文生视频/LTX2.3-图生+文生视频_2034105239082635265.json、视频生成/文生视频/LTX2.3低显存文生图_图生图_首尾帧 视频生成ai漫剧短剧视频 保持人物一致性性价比超高LTX2_2031559977218875394.json、视频生成/文生视频/LTX2.3全自动_手动提示词 图生视频  低消耗 人物一致 精准版_2057632019441602562.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CR Text`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 12/13 个有
- `VHS_VideoCombine` —— 12/13 个有
- `LTXVConditioning` —— 11/13 个有
- `PrimitiveInt` —— 9/13 个有
- `RH_LLMAPI_Pro_Node` —— 9/13 个有
- `PreviewAny` —— 7/13 个有
- `ShowText|pysssss` —— 3/13 个有
- `Fast Groups Bypasser (rgthree)` —— 2/13 个有
- `GetNode` —— 2/13 个有
- `SetNode` —— 2/13 个有
- `SimpleMath+` —— 2/13 个有
- `easy int` —— 2/13 个有
- `llama_cpp_instruct_adv` —— 2/13 个有
- `llama_cpp_model_loader` —— 2/13 个有
- `CreateVideo` —— 1/13 个有
- `FancyTimerNode` —— 1/13 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/13 个有
- `MathExpression|pysssss` —— 1/13 个有
- `SaveVideo` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有
- `llama_cpp_parameters` —— 1/13 个有
- `数学运算_孤海` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 13 | 100% |
| 高度 | 25 | 25 - 25 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，13 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，13 个样本，取值集中（一致性 100%）
