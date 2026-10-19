---
name: unknown_workflow_upscale_latent_upscale_lora_20
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.886
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/2044772850472591362.json, 视频生成/图生视频/2008477289973030914.json, 视频生成/图生视频/2012140284192235522.json, 视频生成/图生视频/2008838542486671361.json, 视频生成/图生视频/2009242619980812289.json, 视频生成/图生视频/2009601705482129409.json, 视频生成/图生视频/2010692328301793282.json, 视频生成/图生视频/2008554221829885954.json, 视频生成/文生视频/LTX 2.3 自动生成播客视频_2035631355412877313.json, 视频生成/文生视频/NVFP4非蒸馏高质量LXT2镜头控制图生视频_2009643815291854849.json, 视频生成/文生视频/非蒸馏高质量LXT2镜头控制图生视频_2009191002166267905.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_20

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2044772850472591362.json、视频生成/图生视频/2008477289973030914.json、视频生成/图生视频/2012140284192235522.json、视频生成/图生视频/2008838542486671361.json、视频生成/图生视频/2009242619980812289.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 9/11 个有
- `GetImageSize` —— 9/11 个有
- `ImageScaleBy` —— 9/11 个有
- `LTXVCropGuides` —— 9/11 个有
- `LTXVPreprocess` —— 9/11 个有
- `LTXVScheduler` —— 9/11 个有
- `LoadImage` —— 9/11 个有
- `LTXVImgToVideoInplace` —— 8/11 个有
- `PrimitiveFloat` —— 7/11 个有
- `ResizeImagesByLongerEdge` —— 7/11 个有
- `VAEDecode` —— 5/11 个有
- `VAEDecodeTiled` —— 5/11 个有
- `ImageResizeKJv2` —— 4/11 个有
- `CM_FloatToInt` —— 3/11 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 3/11 个有
- `PrimitiveStringMultiline` —— 3/11 个有
- `easy cleanGpuUsed` —— 3/11 个有
- `Fast Groups Bypasser (rgthree)` —— 2/11 个有
- `Float to Int` —— 2/11 个有
- `ImpactExecutionOrderController` —— 2/11 个有
- `JWStringReplace` —— 2/11 个有
- `Label (rgthree)` —— 2/11 个有
- `RH_LLMAPI_NODE` —— 2/11 个有
- `TextInput_` —— 2/11 个有
- `easy showAnything` —— 2/11 个有
- `BasicScheduler` —— 1/11 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `PreviewAny` —— 1/11 个有
- `RH_LLMAPI_Pro_Node` —— 1/11 个有
- `RunningHub Deepcleaner` —— 1/11 个有
- `Textbox` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 11 | 91% |
| 高度 | 25 | 25 - 25 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，11 个样本，取值集中（一致性 91%）
- 高度 中位数 25，观测区间 25 - 25，11 个样本，取值集中（一致性 100%）
