---
name: unknown_workflow_video_upscale_latent_upscale_43
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.875889
common_nodes: [CFGGuider, CLIPTextEncode, CR Text, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/反推提示词/LTX2.3全自动—图生_ 文生视频_2030357182566375426.json, 图片生成/图生图/LTX2.3+图生视频+全节点注释_2068871492833730562.json, 图片生成/文生图/万象AI-LTX2.3专用文_图生视频10秒工作流（提示词动态优化版）_2047327004025954305.json, 视频生成/图生视频/(方案2)Ltx 2.3图生视频自动提示词一致性改进版V1（新版模型）_2043952648432394241.json, 视频生成/图生视频/(方案2)Ltx 2.3图生视频自动提示词一致性改进版V1（新版模型）_2046122180257255425.json, 视频生成/图生视频/(自用)N版Ltx 2.3 Dasiwa图生视频自动提示词V1_2051571267114938370.json, 视频生成/图生视频/(自用)N版Ltx 2.3 Dasiwa图生视频自动提示词V1_2053658888255356930.json, 视频生成/图生视频/Ltx2.3-Dasiwa_V3--图生视频(人脸一致性)_2070741486152544258.json, 视频生成/图生视频/（新版模型）Ltx 2.3图生视频自动提示词一致性改进版_2044326986830585858.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_43

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/反推提示词/LTX2.3全自动—图生_ 文生视频_2030357182566375426.json、图片生成/图生图/LTX2.3+图生视频+全节点注释_2068871492833730562.json、图片生成/文生图/万象AI-LTX2.3专用文_图生视频10秒工作流（提示词动态优化版）_2047327004025954305.json、视频生成/图生视频/(方案2)Ltx 2.3图生视频自动提示词一致性改进版V1（新版模型）_2043952648432394241.json、视频生成/图生视频/(方案2)Ltx 2.3图生视频自动提示词一致性改进版V1（新版模型）_2046122180257255425.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
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
- `PrimitiveBoolean`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CM_FloatToInt` —— 8/9 个有
- `LTXVChunkFeedForward` —— 8/9 个有
- `LTXVLatentUpsampler` —— 8/9 个有
- `ModelPatchTorchSettings` —— 8/9 个有
- `PathchSageAttentionKJ` —— 8/9 个有
- `PrimitiveFloat` —— 8/9 个有
- `CR Prompt Text` —— 6/9 个有
- `ConcatTextOfUtils` —— 6/9 个有
- `JWInteger` —— 6/9 个有
- `LTX2AttentionTunerPatch` —— 6/9 个有
- `LTX2_NAG` —— 6/9 个有
- `RH_LLMAPI_Pro_Node` —— 6/9 个有
- `ResizeImageMaskNode` —— 6/9 个有
- `UNETLoader` —— 6/9 个有
- `VAELoader` —— 6/9 个有
- `easy cleanGpuUsed` —— 6/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/9 个有
- `CheckpointLoaderSimple` —— 3/9 个有
- `INTConstant` —— 3/9 个有
- `DuckHideNode` —— 2/9 个有
- `FlashVSR_SM_KSampler` —— 2/9 个有
- `FlashVSR_SM_Model` —— 2/9 个有
- `ImageFromBatch+` —— 2/9 个有
- `PreviewAny` —— 2/9 个有
- `PrimitiveInt` —— 2/9 个有
- `SaveImage` —— 2/9 个有
- `ShellAgentPluginOutputText` —— 2/9 个有
- `TT_img_enc` —— 2/9 个有
- `TT_img_enc_v2` —— 2/9 个有
- `easy showAnything` —— 2/9 个有
- `llama_cpp_instruct_adv` —— 2/9 个有
- `llama_cpp_model_loader` —— 2/9 个有
- `llama_cpp_parameters` —— 2/9 个有
- `MathExpression|pysssss` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 9 | 100% |
| 高度 | 25 | 25 - 25 | 9 | 100% |
| 采样步数 | 1.18841e+09 | - | 2 | 87% |
| Prompt 约束强度(CFG) | randomize | - | 2 | 100% |
| 采样算法 | 2 | - | 2 | 100% |
| 调度器 | 3.5 | - | 2 | 100% |
| 重绘幅度 | 11 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，9 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，9 个样本，取值集中（一致性 100%）
- 采样步数 中位数 1.18841e+09，样本不足，未给区间，2 个样本，取值集中（一致性 87%）
- Prompt 约束强度(CFG) 最常用 randomize，2 个样本，一致性 100%
- 采样算法 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.34714e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
