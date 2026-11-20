---
name: unknown_workflow_video_upscale_latent_upscale_10
type: Unknown Workflow
frequency: 21
level: strong
coverage: 0.876381
common_nodes: [CFGGuider, CLIPTextEncode, CR Text, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 图生视频_2085391376946122754.json, 视频生成/图生视频/LTX2.3-22b-fp8低显存首尾帧快速生成ai视频保持人物一致性性价比LTX2.3-首尾帧视频_2030491852985606146.json, 视频生成/图生视频/LTX2.3-22b-fp8低显存首尾帧快速生成ai视频保持人物一致性性价比LTX2.3-首尾帧视频_2030519163785060353.json, 视频生成/图生视频/LTX2.3-多帧视频_2030546098619682817.json, 视频生成/图生视频/LTX2.3-首尾帧视频_2030921554300768258.json, 视频生成/图生视频/LTX2.3-首尾帧视频（优化版）一致性增强_2030280752230830082.json, 视频生成/图生视频/LTX2.3_自动图_文生视频工作流优化版_2032374399482994689.json, 视频生成/图生视频/LTX2.3_自动图_文生视频工作流优化版_2032672959206264833.json, 视频生成/图生视频/LTX2.3全自动—图生_ 文生视频_2044340240424374273.json, 视频生成/图生视频/LTX2.3全自动—图生视频.全节点注释_2043549529819062274.json, 视频生成/图生视频/LTX2.3全自动图生视频_2055624170523906050.json, 视频生成/文生视频/LTX2.3 图生_ 文生视频【提示词自动优化】_2033527714837176322.json, 视频生成/文生视频/LTX2.3低显存文生图_图生图_首尾帧 视频生成ai漫剧短剧视频 保持人物一致性性价比超高LTX2_2031559977218875394.json, 视频生成/文生视频/LTX2.3全自动_手动提示词 图生视频  低消耗 人物一致 精准版_2057632019441602562.json, 视频生成/文生视频/LTX2.3全自动—图生_文生视频_2030257060473999361.json, 视频生成/文生视频/LTX2.3全自动图生+文生视频_2033000599163248642.json, 视频生成/文生视频/LTX2.3图生_ 文生视频_2033992306809905153.json, 视频生成/文生视频/LTX2.3图生_ 文生视频_2053005533375938562.json, 视频生成/文生视频/LTX2.3：图生、文生视频_2044341159635460098.json, 视频生成/文生视频/图生视频 -LTX2.3 全自动   图生视频_ 文生视频_2030510007468429313.json, 视频生成/文生视频/图生视频 文生视频 -LTX2.3 一键生成_2030565382297227266.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_10

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 图生视频_2085391376946122754.json、视频生成/图生视频/LTX2.3-22b-fp8低显存首尾帧快速生成ai视频保持人物一致性性价比LTX2.3-首尾帧视频_2030491852985606146.json、视频生成/图生视频/LTX2.3-22b-fp8低显存首尾帧快速生成ai视频保持人物一致性性价比LTX2.3-首尾帧视频_2030519163785060353.json、视频生成/图生视频/LTX2.3-多帧视频_2030546098619682817.json、视频生成/图生视频/LTX2.3-首尾帧视频_2030921554300768258.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 21 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CM_FloatToInt` —— 20/21 个有
- `LTXVAudioVAELoader` —— 20/21 个有
- `LTXVChunkFeedForward` —— 20/21 个有
- `LTXVImgToVideoConditionOnly` —— 20/21 个有
- `ModelPatchTorchSettings` —— 20/21 个有
- `PathchSageAttentionKJ` —— 20/21 个有
- `PrimitiveFloat` —— 20/21 个有
- `PrimitiveInt` —— 20/21 个有
- `INTConstant` —— 19/21 个有
- `RH_LLMAPI_Pro_Node` —— 15/21 个有
- `PreviewAny` —— 12/21 个有
- `Fast Groups Bypasser (rgthree)` —— 7/21 个有
- `LTXVFirstLastFrameControl_TTP` —— 5/21 个有
- `SimpleMath+` —— 5/21 个有
- `easy showAnything` —— 4/21 个有
- `Int` —— 2/21 个有
- `SetNode` —— 2/21 个有
- `TextInputNode` —— 2/21 个有
- `DualCLIPLoader` —— 1/21 个有
- `GetImageSize+` —— 1/21 个有
- `LTXVImgToVideoInplaceKJ` —— 1/21 个有
- `MathExpression|pysssss` —— 1/21 个有
- `PromptRelayEncode` —— 1/21 个有
- `UNETLoader` —— 1/21 个有
- `VAELoaderKJ` —— 1/21 个有
- `easy getNode` —— 1/21 个有
- `easy setNode` —— 1/21 个有
- `孤海注释` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 21 | 100% |
| 高度 | 25 | 25 - 25 | 21 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，21 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，21 个样本，取值集中（一致性 100%）
