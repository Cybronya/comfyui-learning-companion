---
name: unknown_workflow_lora_sampler_clip_10
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.910364
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CR Text, EmptyLTXVLatentVideo, JWInteger, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVSeparateAVLatent, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveFloat, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2073670944987635714.json, 视频生成/图生视频/2045468289630998529.json, 视频生成/图生视频/2044013454645796866.json, 视频生成/图生视频/2070741486152544258.json, 视频生成/图生视频/2047130634124005377.json, 视频生成/图生视频/2071794248864845826.json, 视频生成/图生视频/2044326986830585858.json, 视频生成/图生视频/2029876978643374081.json, 视频生成/图生视频/2030648007024185346.json, 视频生成/文生视频/LTX2.3--文生音视频_2029773958807031810.json, 视频生成/文生视频/Ltx 2.3图生视频 一次采样（新sigmas30step）_2033139562045771778.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_10

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2073670944987635714.json、视频生成/图生视频/2045468289630998529.json、视频生成/图生视频/2044013454645796866.json、视频生成/图生视频/2070741486152544258.json、视频生成/图生视频/2047130634124005377.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 11 个 workflow 都包含：
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
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 10/11 个有
- `ResizeImageMaskNode` —— 10/11 个有
- `VHS_VideoCombine` —— 10/11 个有
- `easy cleanGpuUsed` —— 10/11 个有
- `LTXVPreprocess` —— 9/11 个有
- `LatentUpscaleModelLoader` —— 9/11 个有
- `LTX2_NAG` —— 8/11 个有
- `CR Prompt Text` —— 7/11 个有
- `ConcatTextOfUtils` —— 7/11 个有
- `CreateVideo` —— 7/11 个有
- `LTX2AttentionTunerPatch` —— 7/11 个有
- `LTXVLatentUpsampler` —— 7/11 个有
- `SaveVideo` —— 7/11 个有
- `UNETLoader` —— 7/11 个有
- `VAELoader` —— 7/11 个有
- `FlashVSR_SM_KSampler` —— 6/11 个有
- `FlashVSR_SM_Model` —— 6/11 个有
- `Float` —— 6/11 个有
- `ImageFromBatch+` —— 6/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/11 个有
- `CheckpointLoaderSimple` —— 4/11 个有
- `GetNode` —— 2/11 个有
- `Int` —— 2/11 个有
- `LTXICLoRALoaderModelOnly` —— 2/11 个有
- `SetNode` —— 2/11 个有
- `SimpleMath+` —— 2/11 个有
- `孤海注释` —— 2/11 个有
- `DuckHideNode` —— 1/11 个有
- `GetImageSize` —— 1/11 个有
- `ImageScaleBy` —— 1/11 个有
- `PreviewAny` —— 1/11 个有
- `SaveImage` —— 1/11 个有
- `SigmasPreview` —— 1/11 个有
- `TextPreview` —— 1/11 个有
- `VHS_LoadVideo` —— 1/11 个有
- `VideoInfoSource` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 11 | 100% |
| 高度 | 25 | 25 - 25 | 11 | 100% |
| 采样步数 | 1.87181e+09 | 4.63552e+08 - 2.10262e+09 | 6 | 67% |
| Prompt 约束强度(CFG) | randomize | - | 6 | 83% |
| 采样算法 | 2 | 2 - 2 | 6 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 6 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，11 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，11 个样本，取值集中（一致性 100%）
- 采样步数 中位数 1.87181e+09，观测区间 4.63552e+08 - 2.10262e+09，6 个样本
- Prompt 约束强度(CFG) 最常用 randomize，6 个样本，一致性 83%
- 采样算法 中位数 2，观测区间 2 - 2，6 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，6 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，6 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 2.10262e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
