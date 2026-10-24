---
name: unknown_workflow_lora_sampler_clip_17
type: Unknown Workflow
frequency: 16
level: strong
coverage: 0.917625
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CR Text, EmptyLTXVLatentVideo, JWInteger, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveFloat, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/Dasiwa LTX2.3 超强一致性工作i流，宽审核！_2073670944987635714.json, 视频生成/图生视频/LTX2.3 图生视频 自动提示词 一致性最新模型改进版_2045468289630998529.json, 视频生成/图生视频/Ltx 2.3 Dasiwa V3模型最强人脸一致性图生视频自动提示词V1_2070413012745412609.json, 视频生成/图生视频/Ltx 2.3 Dasiwa V3模型最强人脸一致性图生视频自动提示词V1_2070799952854474753.json, 视频生成/图生视频/Ltx 2.3 Dasiwa图生视频自动提示词V1_2051501055195791361.json, 视频生成/图生视频/Ltx 2.3 Dasiwa图生视频自动提示词V1_2053052230592409601.json, 视频生成/图生视频/Ltx 2.3 Dasiwa图生视频自动提示词工作流_2051614845358886913.json, 视频生成/图生视频/Ltx 2.3 Dasiwa图生视频自动提示词工作流_2052714455703801858.json, 视频生成/图生视频/Ltx 2.3 Dasiwa图生视频自动提示词工作流_2074073783828307970.json, 视频生成/图生视频/Ltx 2.3 Dasiwa图生视频自动提示词工作流_2075903253178572801.json, 视频生成/图生视频/Ltx 2.3图生视频自动提示词一致性改进版V2（新版模型）_2043901634517929985.json, 视频生成/图生视频/Ltx 2.3图生视频自动提示词一致性改进版（转自T8大佬）_2044013454645796866.json, 视频生成/图生视频/Ltx+2.3_Dasiwa图生视频+高清_2051956185665949698.json, 视频生成/图生视频/【阿良绘】Ltx 2.3图生视频 _ 自动提示词 改进版V2（新版模型）_2047130634124005377.json, 视频生成/图生视频/电商Ltx 2.3 Dasiwa V3最强人脸一致性-图生视频-自动提示词_2071794248864845826.json, 视频生成/文生视频/（贞贞lora-13000步）Ltxv 2.3文生视频自动提示词版+顶级放大V1_2036316995154616322.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_17

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（视频生成/图生视频/Dasiwa LTX2.3 超强一致性工作i流，宽审核！_2073670944987635714.json、视频生成/图生视频/LTX2.3 图生视频 自动提示词 一致性最新模型改进版_2045468289630998529.json、视频生成/图生视频/Ltx 2.3 Dasiwa V3模型最强人脸一致性图生视频自动提示词V1_2070413012745412609.json、视频生成/图生视频/Ltx 2.3 Dasiwa V3模型最强人脸一致性图生视频自动提示词V1_2070799952854474753.json、视频生成/图生视频/Ltx 2.3 Dasiwa图生视频自动提示词V1_2051501055195791361.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：强结论
- **平均知识覆盖**：92%

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
- `LTXVSeparateAVLatent`
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

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 15/16 个有
- `ConcatTextOfUtils` —— 15/16 个有
- `LTX2AttentionTunerPatch` —— 15/16 个有
- `LTX2_NAG` —— 15/16 个有
- `RH_LLMAPI_Pro_Node` —— 15/16 个有
- `UNETLoader` —— 15/16 个有
- `VAELoader` —— 15/16 个有
- `VHS_VideoCombine` —— 15/16 个有
- `easy cleanGpuUsed` —— 15/16 个有
- `CreateVideo` —— 14/16 个有
- `LTXVPreprocess` —— 14/16 个有
- `LatentUpscaleModelLoader` —— 14/16 个有
- `SaveVideo` —— 14/16 个有
- `FlashVSR_SM_KSampler` —— 13/16 个有
- `FlashVSR_SM_Model` —— 13/16 个有
- `Float` —— 13/16 个有
- `ImageFromBatch+` —— 13/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 13/16 个有
- `LTXVLatentUpsampler` —— 12/16 个有
- `GetNode` —— 2/16 个有
- `Int` —— 2/16 个有
- `LTXICLoRALoaderModelOnly` —— 2/16 个有
- `SetNode` —— 2/16 个有
- `SimpleMath+` —— 2/16 个有
- `孤海注释` —— 2/16 个有
- `CheckpointLoaderSimple` —— 1/16 个有
- `GemmaAPITextEncode` —— 1/16 个有
- `GetImageSize` —— 1/16 个有
- `ImageScaleBy` —— 1/16 个有
- `PreviewAny` —— 1/16 个有
- `PrimitiveString` —— 1/16 个有
- `Qwen3_VQA` —— 1/16 个有
- `ShowAnything|Mie` —— 1/16 个有
- `TextListSplit` —— 1/16 个有
- `easy promptConcat` —— 1/16 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 16 | 100% |
| 高度 | 25 | 25 - 25 | 16 | 100% |
| 采样步数 | 1.43765e+09 | 1.01555e+07 - 2.01633e+09 | 13 | 41% |
| Prompt 约束强度(CFG) | randomize | - | 13 | 100% |
| 采样算法 | 2 | 2 - 2 | 13 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 13 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，16 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，16 个样本，取值集中（一致性 100%）
- 采样步数 中位数 1.43765e+09，观测区间 1.01555e+07 - 2.01633e+09，13 个样本，取值分散，一致性仅 41%
- Prompt 约束强度(CFG) 最常用 randomize，13 个样本，一致性 100%
- 采样算法 中位数 2，观测区间 2 - 2，13 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，13 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，13 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 2.01633e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
