---
name: unknown_workflow_lora_sampler_clip_241
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.924667
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CR Text, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, FlashVSR_SM_KSampler, FlashVSR_SM_Model, ImageFromBatch+, JWInteger, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveFloat, RH_LLMAPI_Pro_Node, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/文生视频/Ltxv 2.3图生视频更强一致性和动态_2030110680979869697.json, 视频生成/文生视频/Ltxv 2.3图生视频自动提示词版+顶级放大（最强一致性稳定版）_2030537820573540354.json, 视频生成/文生视频/（贞贞lora-13000步）Ltxv 2.3文生视频自动提示词版+顶级放大V1_2036316995154616322.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_241

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/Ltxv 2.3图生视频更强一致性和动态_2030110680979869697.json、视频生成/文生视频/Ltxv 2.3图生视频自动提示词版+顶级放大（最强一致性稳定版）_2030537820573540354.json、视频生成/文生视频/（贞贞lora-13000步）Ltxv 2.3文生视频自动提示词版+顶级放大V1_2036316995154616322.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CR Text`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `ImageFromBatch+`
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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Float` —— 2/3 个有
- `LatentUpscaleModelLoader` —— 2/3 个有
- `VHS_VideoCombine` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `ConcatTextOfUtils` —— 1/3 个有
- `GemmaAPITextEncode` —— 1/3 个有
- `ImpactConditionalBranch` —— 1/3 个有
- `MuyeSizeSelector` —— 1/3 个有
- `PrimitiveString` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `SimpleMath+` —— 1/3 个有
- `Switch any [Crystools]` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.30682e+08 | 7.1888e+08 - 1.00618e+09 | 3 | 86% |
| Prompt 约束强度(CFG) | randomize | - | 3 | 100% |
| 采样算法 | 2 | 2 - 2 | 3 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 3 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 3 | 100% |
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 25 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 8.30682e+08，观测区间 7.1888e+08 - 1.00618e+09，3 个样本，取值集中（一致性 86%）
- Prompt 约束强度(CFG) 最常用 randomize，3 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，3 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，3 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，3 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.00618e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
