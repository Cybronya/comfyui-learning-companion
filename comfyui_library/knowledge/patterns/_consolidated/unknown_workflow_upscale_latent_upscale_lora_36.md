---
name: unknown_workflow_upscale_latent_upscale_lora_36
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.786
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, RandomNoise, SamplerCustomAdvanced]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2009447921246281729.json, 视频生成/图生视频/2008477289973030914.json, 视频生成/图生视频/2010303270488641537.json, 视频生成/图生视频/2012140284192235522.json, 视频生成/图生视频/2009279040347185153.json, 视频生成/图生视频/2031246343607422977.json, 视频生成/图生视频/2010620501831458818.json, 视频生成/文生视频/NVFP4非蒸馏高质量LXT2镜头控制图生视频_2009643815291854849.json, 视频生成/文生视频/非蒸馏高质量LXT2镜头控制图生视频_2009191002166267905.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_36

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2009447921246281729.json、视频生成/图生视频/2008477289973030914.json、视频生成/图生视频/2010303270488641537.json、视频生成/图生视频/2012140284192235522.json、视频生成/图生视频/2009279040347185153.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 9 个 workflow 都包含：
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
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `SamplerCustomAdvanced`

**可变部分**（部分 workflow 才有）：
- `ManualSigmas` —— 8/9 个有
- `LTXVPreprocess` —— 7/9 个有
- `LoadImage` —— 7/9 个有
- `PrimitiveInt` —— 7/9 个有
- `CreateVideo` —— 6/9 个有
- `LTXVCropGuides` —— 6/9 个有
- `LTXVImgToVideoInplace` —— 6/9 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 6/9 个有
- `PrimitiveFloat` —— 6/9 个有
- `SaveVideo` —— 6/9 个有
- `ResizeImagesByLongerEdge` —— 5/9 个有
- `PrimitiveStringMultiline` —— 4/9 个有
- `VAEDecode` —— 4/9 个有
- `easy cleanGpuUsed` —— 4/9 个有
- `CM_FloatToInt` —— 3/9 个有
- `GetNode` —— 3/9 个有
- `ImpactExecutionOrderController` —— 3/9 个有
- `Int` —— 3/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/9 个有
- `SetNode` —— 3/9 个有
- `SimpleMath+` —— 3/9 个有
- `VAEDecodeTiled` —— 3/9 个有
- `VHS_VideoCombine` —— 3/9 个有
- `Fast Groups Bypasser (rgthree)` —— 2/9 个有
- `LayerUtility: PurgeVRAM V2` —— 2/9 个有
- `BasicScheduler` —— 1/9 个有
- `CR Float To Integer` —— 1/9 个有
- `DF_Int_to_Float` —— 1/9 个有
- `DF_Integer` —— 1/9 个有
- `KSampler` —— 1/9 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/9 个有
- `LTXVGemmaCLIPModelLoader` —— 1/9 个有
- `LTXVGemmaEnhancePrompt` —— 1/9 个有
- `ResizeImageMaskNode` —— 1/9 个有
- `easy int` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 97 - 121 | 9 | 89% |
| 高度 | 25 | 25 - 40 | 9 | 82% |
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | euler | - | 1 | 100% |
| 调度器 | simple | - | 1 | 100% |
| 重绘幅度 | 0.35 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 121，观测区间 97 - 121，9 个样本，取值集中（一致性 89%）
- 高度 中位数 25，观测区间 25 - 40，9 个样本，取值集中（一致性 82%）
