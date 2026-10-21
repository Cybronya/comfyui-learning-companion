---
name: unknown_workflow_video_lora_sampler_42
type: Unknown Workflow
frequency: 23
level: strong
coverage: 0.916565
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2039916059230216193.json, 视频生成/图生视频/2050558938583707649.json, 视频生成/图生视频/2030554473583611905.json, 视频生成/图生视频/2030803826088873986.json, 视频生成/图生视频/2031218465863897089.json, 视频生成/图生视频/2033196066207703042.json, 视频生成/图生视频/2036786729985777666.json, 视频生成/图生视频/2038212622302056450.json, 视频生成/图生视频/2038574000934227969.json, 视频生成/图生视频/2047146472457637889.json, 视频生成/图生视频/2049309806019743746.json, 视频生成/图生视频/2055254996790333442.json, 视频生成/图生视频/2060523387025444866.json, 视频生成/图生视频/LTX2.3+单人_双人对话-图生视频_2082722092436512769.json, 视频生成/图生视频/2072475992752484353.json, 视频生成/图生视频/2065067084408774657.json, 视频生成/图生视频/2037103853568528385.json, 视频生成/图生视频/2032374399482994689.json, 视频生成/图生视频/2032672959206264833.json, 视频生成/图生视频/2044340240424374273.json, 视频生成/图生视频/2043549529819062274.json, 视频生成/图生视频/2055624170523906050.json, 视频生成/图生视频/2056038472141549569.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_42

> 由 `engine/knowledge_consolidation` 从 23 个 workflow 归纳得出（视频生成/图生视频/2039916059230216193.json、视频生成/图生视频/2050558938583707649.json、视频生成/图生视频/2030554473583611905.json、视频生成/图生视频/2030803826088873986.json、视频生成/图生视频/2031218465863897089.json…）

- **类型**：Unknown Workflow
- **样本数**：23
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 23 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 21/23 个有
- `RH_LLMAPI_Pro_Node` —— 20/23 个有
- `SimpleMath+` —— 17/23 个有
- `easy cleanGpuUsed` —— 17/23 个有
- `Seed (rgthree)` —— 16/23 个有
- `easy int` —— 16/23 个有
- `DapaoImageAspectRatioResizeNode` —— 15/23 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/23 个有
- `LTXVLatentUpsampler` —— 7/23 个有
- `LatentUpscaleModelLoader` —— 7/23 个有
- `PrimitiveInt` —— 7/23 个有
- `INTConstant` —— 5/23 个有
- `PreviewAny` —— 4/23 个有
- `Label (rgthree)` —— 3/23 个有
- `llama_cpp_instruct_adv` —— 3/23 个有
- `llama_cpp_model_loader` —— 3/23 个有
- `Int` —— 2/23 个有
- `ShowText|pysssss` —— 2/23 个有
- `Switch` —— 2/23 个有
- `CR Prompt Text` —— 1/23 个有
- `CustomAddLabel` —— 1/23 个有
- `Fast Groups Bypasser (rgthree)` —— 1/23 个有
- `GetNode` —— 1/23 个有
- `LayerUtility: PurgeVRAM V2` —— 1/23 个有
- `PrimitiveStringMultiline` —— 1/23 个有
- `SetNode` —— 1/23 个有
- `TTResolutionSelector` —— 1/23 个有
- `llama_cpp_parameters` —— 1/23 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 23 | 100% |
| 高度 | 25 | 25 - 25 | 23 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，23 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，23 个样本，取值集中（一致性 100%）
