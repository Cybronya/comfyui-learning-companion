---
name: unknown_workflow_video_upscale_latent_upscale_55
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.942857
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CR Text, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX 2.3图生视频自动提示词版+FlashVSR放大_2036142607784484866.json, 视频生成/图生视频/LTX2.3 图生视频 全自动版_2035704140126494721.json, 视频生成/图生视频/LTX2.3 音色参考+快速采样【漫剧生产力神器】_2036666522667589634.json, 视频生成/图生视频/（最强一致性稳定版）Ltxv 2.3图生视频自动提示词版+顶级放大V1_2029876978643374081.json, 视频生成/图生视频/（最强一致性稳定版）Ltxv 2.3图生视频自动提示词版+顶级放大V1_2030648007024185346.json, 视频生成/文生视频/LTX2.3--文生音视频_2029773958807031810.json, 视频生成/文生视频/Ltx 2.3图生视频 一次采样（新sigmas30step）_2033139562045771778.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_55

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/LTX 2.3图生视频自动提示词版+FlashVSR放大_2036142607784484866.json、视频生成/图生视频/LTX2.3 图生视频 全自动版_2035704140126494721.json、视频生成/图生视频/LTX2.3 音色参考+快速采样【漫剧生产力神器】_2036666522667589634.json、视频生成/图生视频/（最强一致性稳定版）Ltxv 2.3图生视频自动提示词版+顶级放大V1_2029876978643374081.json、视频生成/图生视频/（最强一致性稳定版）Ltxv 2.3图生视频自动提示词版+顶级放大V1_2030648007024185346.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CR Text`
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
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVPreprocess` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `PrimitiveBoolean` —— 6/7 个有
- `CreateVideo` —— 5/7 个有
- `FlashVSR_SM_KSampler` —— 5/7 个有
- `FlashVSR_SM_Model` —— 5/7 个有
- `Float` —— 5/7 个有
- `ImageFromBatch+` —— 5/7 个有
- `JWInteger` —— 5/7 个有
- `LTXVLatentUpsampler` —— 5/7 个有
- `PrimitiveFloat` —— 5/7 个有
- `SaveVideo` —— 5/7 个有
- `easy cleanGpuUsed` —— 5/7 个有
- `ResizeImageMaskNode` —— 4/7 个有
- `INTConstant` —— 2/7 个有
- `PrimitiveInt` —— 2/7 个有
- `easy mathInt` —— 2/7 个有
- `CM_IntToFloat` —— 1/7 个有
- `DuckHideNode` —— 1/7 个有
- `ImageSizeInfo` —— 1/7 个有
- `LTX2_NAG` —— 1/7 个有
- `LTXVReferenceAudio` —— 1/7 个有
- `LoadAudio` —— 1/7 个有
- `MelBandRoFormerModelLoader` —— 1/7 个有
- `MelBandRoFormerSampler` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `SaveAudio` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `SigmasPreview` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `TextPreview` —— 1/7 个有
- `VHS_LoadVideo` —— 1/7 个有
- `VideoInfoSource` —— 1/7 个有
- `easy float` —— 1/7 个有
- `easy showAnything` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 25 - 25 | 7 | 100% |
| 采样步数 | 1.74419e+09 | 4.63552e+08 - 2.10262e+09 | 5 | 51% |
| Prompt 约束强度(CFG) | randomize | - | 5 | 80% |
| 采样算法 | 2 | 2 - 2 | 5 | 100% |
| 调度器 | 3.5 | 3.5 - 3.5 | 5 | 100% |
| 重绘幅度 | 11 | 11 - 11 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
- 采样步数 中位数 1.74419e+09，观测区间 4.63552e+08 - 2.10262e+09，5 个样本
- Prompt 约束强度(CFG) 最常用 randomize，5 个样本，一致性 80%
- 采样算法 中位数 2，观测区间 2 - 2，5 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，观测区间 3.5 - 3.5，5 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，观测区间 11 - 11，5 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 2.10262e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
