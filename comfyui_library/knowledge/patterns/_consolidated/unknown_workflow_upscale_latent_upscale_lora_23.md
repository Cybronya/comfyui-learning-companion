---
name: unknown_workflow_upscale_latent_upscale_lora_23
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.885667
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/LTX2.0 最新图生视频工作流（48G）_2017463595512111106.json, 视频生成/图生视频/LTX2.0 音画同步生视频_2009155672465743874.json, 视频生成/图生视频/LTX2.0 音视频同步-图生视频工作流_2009919579048382465.json, 视频生成/图生视频/LTX2.0+图生视频工作流（48G）_2009073353373519874.json, 视频生成/图生视频/LTX2.0+图生视频工作流（48G）_2048596027241930753.json, 视频生成/图生视频/LTX2.0-首尾帧视频（须运行plus）_2010692328301793282.json, 视频生成/图生视频/LTX2.0图生视频(已修复)_2008482127481933826.json, 视频生成/图生视频/LTX2.0图生视频V1_2008532910646763522.json, 视频生成/图生视频/LTX2.0图生视频工作流（48G）视频与音频同步生成_2008794813583331330.json, 视频生成/图生视频/LTX2.0图生视频工作流（48G）视频与音频同步生成_2021544395123724290.json, 视频生成/图生视频/LTX2.0图生视频（须运行plus）_2009279040347185153.json, 视频生成/图生视频/LTX2.3图生视频_2031246343607422977.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_23

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/LTX2.0 最新图生视频工作流（48G）_2017463595512111106.json、视频生成/图生视频/LTX2.0 音画同步生视频_2009155672465743874.json、视频生成/图生视频/LTX2.0 音视频同步-图生视频工作流_2009919579048382465.json、视频生成/图生视频/LTX2.0+图生视频工作流（48G）_2009073353373519874.json、视频生成/图生视频/LTX2.0+图生视频工作流（48G）_2048596027241930753.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyImage`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideoInplace` —— 11/12 个有
- `ManualSigmas` —— 11/12 个有
- `PrimitiveInt` —— 11/12 个有
- `VAEDecode` —— 10/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/12 个有
- `CreateVideo` —— 6/12 个有
- `ImageResizeKJv2` —— 6/12 个有
- `SaveVideo` —— 6/12 个有
- `VHS_VideoCombine` —— 6/12 个有
- `Int` —— 4/12 个有
- `DF_Int_to_Float` —— 3/12 个有
- `GetNode` —— 3/12 个有
- `MathExpression|pysssss` —— 3/12 个有
- `SetNode` —— 3/12 个有
- `VAEDecodeTiled` —— 3/12 个有
- `CR Text` —— 2/12 个有
- `PrimitiveFloat` —— 2/12 个有
- `DF_Integer` —— 1/12 个有
- `ImpactSwitch` —— 1/12 个有
- `KSampler` —— 1/12 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/12 个有
- `LayerUtility: PurgeVRAM V2` —— 1/12 个有
- `PrimitiveStringMultiline` —— 1/12 个有
- `RH_LLMAPI_NODE` —— 1/12 个有
- `ResizeImageMaskNode` —— 1/12 个有
- `SaveImage` —— 1/12 个有
- `ShowText|pysssss` —— 1/12 个有
- `SimpleMath+` —— 1/12 个有
- `ToFloat` —— 1/12 个有
- `easy int` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 12 | 100% |
| 高度 | 25 | 25 - 40 | 12 | 84% |
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 0.35 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，12 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 40，12 个样本，取值集中（一致性 84%）
