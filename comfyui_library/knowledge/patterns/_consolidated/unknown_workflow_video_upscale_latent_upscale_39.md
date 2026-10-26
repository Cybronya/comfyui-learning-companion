---
name: unknown_workflow_video_upscale_latent_upscale_39
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8179
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyImage, EmptyLTXVLatentVideo, GetImageSize, ImageScaleBy, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX2图生视频（for creator）_2019249142207352834.json, 视频生成/图生视频/LTX2首尾帧图生视频_2010620501831458818.json, 视频生成/图生视频/LTXV2.0图生视频+对话配音_2010611172453654529.json, 视频生成/图生视频/[1月] 音画同步_ASMR LTX2图生视频_2009275287908913153.json, 视频生成/图生视频/[1月] 音画同步_ASMR LTX2图生视频_2012538447445106690.json, 视频生成/图生视频/ltx-2极速图生视频数字人视频高清数字人视频照片生成ai数字人高清对口型数字人视频工（48G）_2011488577225494530.json, 视频生成/图生视频/video_ltx2_i2v_unpack_2008723483076861954.json, 视频生成/图生视频/图生视频带有对话配音的话音同步-LTXV2.0开源王炸_2009222188091576321.json, 视频生成/图生视频/音画精准匹配+图生视频 （ASMR+LTX2）_2012772374625652737.json, 视频生成/图生视频/🦖LTX2.0 图生视频（48G）_2008714518439927810.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_39

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/LTX2图生视频（for creator）_2019249142207352834.json、视频生成/图生视频/LTX2首尾帧图生视频_2010620501831458818.json、视频生成/图生视频/LTXV2.0图生视频+对话配音_2010611172453654529.json、视频生成/图生视频/[1月] 音画同步_ASMR LTX2图生视频_2009275287908913153.json、视频生成/图生视频/[1月] 音画同步_ASMR LTX2图生视频_2012538447445106690.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 10 个 workflow 都包含：
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
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVImgToVideoInplace` —— 9/10 个有
- `VAEDecode` —— 8/10 个有
- `ImageResizeKJv2` —— 7/10 个有
- `CR Text` —— 6/10 个有
- `JWInteger` —— 5/10 个有
- `MathExpression|pysssss` —— 5/10 个有
- `PrimitiveInt` —— 5/10 个有
- `ResizeImagesByLongerEdge` —— 5/10 个有
- `GetNode` —— 4/10 个有
- `SetNode` —— 4/10 个有
- `Int` —— 3/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/10 个有
- `PreviewImage` —— 3/10 个有
- `SimpleMath+` —— 3/10 个有
- `easy cleanGpuUsed` —— 3/10 个有
- `PrimitiveFloat` —— 2/10 个有
- `VAEDecodeTiled` —— 2/10 个有
- `DF_Int_to_Float` —— 1/10 个有
- `ImpactSwitch` —— 1/10 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/10 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 1/10 个有
- `LayerUtility: PurgeVRAM V2` —— 1/10 个有
- `MemoryCleaner` —— 1/10 个有
- `ResizeLongestToNode` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 10 | 93% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，10 个样本，取值集中（一致性 93%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
