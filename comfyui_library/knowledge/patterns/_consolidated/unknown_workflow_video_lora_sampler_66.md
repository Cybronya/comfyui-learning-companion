---
name: unknown_workflow_video_lora_sampler_66
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.941
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX-2.3-图生视频-音画同步-人物一致性优化版_2039916059230216193.json, 视频生成/图生视频/LTX2.3 双人对话-图生视频_2050558938583707649.json, 视频生成/图生视频/LTX2.3 图生视频 人物一致性优化版_2030554473583611905.json, 视频生成/图生视频/LTX2.3 图生视频 人物一致性优化版_2030803826088873986.json, 视频生成/图生视频/LTX2.3 图生视频 人物一致性优化版_2031218465863897089.json, 视频生成/图生视频/LTX2.3 图生视频 人物一致性优化版_2033196066207703042.json, 视频生成/图生视频/LTX2.3 图生视频 人物一致性优化版_2036786729985777666.json, 视频生成/图生视频/LTX2.3 图生视频 人物一致性优化版工作流_2038212622302056450.json, 视频生成/图生视频/LTX2.3 图生视频 人物一致性优化版工作流_2038574000934227969.json, 视频生成/图生视频/LTX2.3 图生视频（提示词自动优化版）_2047146472457637889.json, 视频生成/图生视频/LTX2.3 图生视频（提示词自动优化版）_2049309806019743746.json, 视频生成/图生视频/LTX2.3 图生视频（提示词自动优化版）_2055254996790333442.json, 视频生成/图生视频/LTX2.3 图生视频（提示词自动优化版）_2060523387025444866.json, 视频生成/图生视频/LTX2.3+单人_双人对话-图生视频_2082722092436512769.json, 视频生成/图生视频/LTX2.3+图生视频+提示词扩写自动优化版+数字人说话唱歌+_2072475992752484353.json, 视频生成/图生视频/LTX2.3+图生视频自动 提示词自动 数字人_2065067084408774657.json, 视频生成/图生视频/LTX2.3_2037103853568528385.json, 视频生成/图生视频/LTX2.3服装模特手机自拍-图生视频_2056038472141549569.json, 视频生成/图生视频/aidir-LTX2.3 首帧图生视频 人物一致性优化版💃_2069596918434590721.json, 视频生成/文生视频/LTX2.3-图生+文生视频_2034105239082635265.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_66

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/LTX-2.3-图生视频-音画同步-人物一致性优化版_2039916059230216193.json、视频生成/图生视频/LTX2.3 双人对话-图生视频_2050558938583707649.json、视频生成/图生视频/LTX2.3 图生视频 人物一致性优化版_2030554473583611905.json、视频生成/图生视频/LTX2.3 图生视频 人物一致性优化版_2030803826088873986.json、视频生成/图生视频/LTX2.3 图生视频 人物一致性优化版_2031218465863897089.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 20 个 workflow 都包含：
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
- `easy cleanGpuUsed` —— 19/20 个有
- `CR Text` —— 18/20 个有
- `Seed (rgthree)` —— 17/20 个有
- `easy int` —— 17/20 个有
- `DapaoImageAspectRatioResizeNode` —— 16/20 个有
- `RH_LLMAPI_Pro_Node` —— 16/20 个有
- `SimpleMath+` —— 16/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/20 个有
- `llama_cpp_instruct_adv` —— 4/20 个有
- `llama_cpp_model_loader` —— 4/20 个有
- `INTConstant` —— 3/20 个有
- `LTXVLatentUpsampler` —— 3/20 个有
- `Label (rgthree)` —— 3/20 个有
- `LatentUpscaleModelLoader` —— 3/20 个有
- `PrimitiveInt` —— 3/20 个有
- `ShowText|pysssss` —— 3/20 个有
- `Switch` —— 2/20 个有
- `CR Prompt Text` —— 1/20 个有
- `CustomAddLabel` —— 1/20 个有
- `Fast Groups Bypasser (rgthree)` —— 1/20 个有
- `GetNode` —— 1/20 个有
- `LayerUtility: PurgeVRAM V2` —— 1/20 个有
- `Note Plus (mtb)` —— 1/20 个有
- `PreviewAny` —— 1/20 个有
- `PrimitiveStringMultiline` —— 1/20 个有
- `SetNode` —— 1/20 个有
- `TTResolutionSelector` —— 1/20 个有
- `llama_cpp_parameters` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 20 | 100% |
| 高度 | 25 | 25 - 25 | 20 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，20 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，20 个样本，取值集中（一致性 100%）
