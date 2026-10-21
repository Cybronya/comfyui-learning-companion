---
name: unknown_workflow_video_upscale_latent_upscale_16
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.93175
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CR Text, EmptyLTXVLatentVideo, JWInteger, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveFloat, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2043952648432394241.json, 视频生成/图生视频/2046122180257255425.json, 视频生成/图生视频/2051571267114938370.json, 视频生成/图生视频/2053658888255356930.json, 视频生成/图生视频/2036142607784484866.json, 视频生成/图生视频/2070413012745412609.json, 视频生成/图生视频/2070799952854474753.json, 视频生成/图生视频/2051501055195791361.json, 视频生成/图生视频/2053052230592409601.json, 视频生成/图生视频/2051614845358886913.json, 视频生成/图生视频/2052714455703801858.json, 视频生成/图生视频/2074073783828307970.json, 视频生成/图生视频/2075903253178572801.json, 视频生成/图生视频/2043901634517929985.json, 视频生成/图生视频/2051956185665949698.json, 视频生成/文生视频/（贞贞lora-13000步）Ltxv 2.3文生视频自动提示词版+顶级放大V1_2036316995154616322.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_16

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/2043952648432394241.json、视频生成/图生视频/2046122180257255425.json、视频生成/图生视频/2051571267114938370.json、视频生成/图生视频/2053658888255356930.json、视频生成/图生视频/2036142607784484866.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 16 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CR Text`
- `EmptyLTXVLatentVideo`
- `JWInteger`
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
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 14/16 个有
- `ConcatTextOfUtils` —— 14/16 个有
- `FlashVSR_SM_KSampler` —— 14/16 个有
- `FlashVSR_SM_Model` —— 14/16 个有
- `ImageFromBatch+` —— 14/16 个有
- `LTX2AttentionTunerPatch` —— 14/16 个有
- `LTX2_NAG` —— 14/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 14/16 个有
- `UNETLoader` —— 14/16 个有
- `VAELoader` —— 14/16 个有
- `LTXVLatentUpsampler` —— 13/16 个有
- `RH_LLMAPI_Pro_Node` —— 13/16 个有
- `CreateVideo` —— 12/16 个有
- `Float` —— 12/16 个有
- `SaveVideo` —— 12/16 个有
- `CheckpointLoaderSimple` —— 2/16 个有
- `DuckHideNode` —— 2/16 个有
- `SaveImage` —— 2/16 个有
- `ShellAgentPluginOutputText` —— 2/16 个有
- `TT_img_enc` —— 2/16 个有
- `TT_img_enc_v2` —— 2/16 个有
- `easy showAnything` —— 2/16 个有
- `llama_cpp_instruct_adv` —— 2/16 个有
- `llama_cpp_model_loader` —— 2/16 个有
- `llama_cpp_parameters` —— 2/16 个有
- `GemmaAPITextEncode` —— 1/16 个有
- `ImageSizeInfo` —— 1/16 个有
- `PrimitiveString` —— 1/16 个有
- `Qwen3_VQA` —— 1/16 个有
- `ShowAnything|Mie` —— 1/16 个有
- `TextListSplit` —— 1/16 个有
- `easy mathInt` —— 1/16 个有
- `easy promptConcat` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 16 | 100% |
| 高度 | 25 | 25 - 25 | 16 | 100% |
| 采样步数 | 1.12271e+09 | 1.01555e+07 - 2.01633e+09 | 14 | 40% |
| Prompt 约束强度(CFG) | randomize | - | 14 | 100% |
| 采样算法 | 2 | 2 - 2 | 14 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 14 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，16 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 1.12271e+09，观测区间 1.01555e+07 - 2.01633e+09，14 个样本，取值分散，一致性仅 40%
- Prompt 约束强度(CFG) 最常用 randomize，14 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，14 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，14 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，14 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 2.01633e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
