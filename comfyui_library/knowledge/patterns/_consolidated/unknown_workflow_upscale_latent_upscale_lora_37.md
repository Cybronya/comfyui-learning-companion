---
name: unknown_workflow_upscale_latent_upscale_lora_37
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.871375
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/LTX 2.3 自动生成播客视频_2044772850472591362.json, 视频生成/图生视频/LTX-2 文生视频 ComfyUI官方流_2008477289973030914.json, 视频生成/图生视频/LTX-2 音画同步训练lora多种搭建方式工作流（防音频过拟合）_2012140284192235522.json, 视频生成/图生视频/LTX-2 高质量图生视频  电影镜头动画 可智能反推提示词 真实摄影_2013159959533461506.json, 视频生成/图生视频/LTX2.0图生视频（须运行plus）_2009279040347185153.json, 视频生成/文生视频/LTX 2.3 自动生成播客视频_2035631355412877313.json, 视频生成/文生视频/NVFP4非蒸馏高质量LXT2镜头控制图生视频_2009643815291854849.json, 视频生成/文生视频/非蒸馏高质量LXT2镜头控制图生视频_2009191002166267905.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_37

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/LTX 2.3 自动生成播客视频_2044772850472591362.json、视频生成/图生视频/LTX-2 文生视频 ComfyUI官方流_2008477289973030914.json、视频生成/图生视频/LTX-2 音画同步训练lora多种搭建方式工作流（防音频过拟合）_2012140284192235522.json、视频生成/图生视频/LTX-2 高质量图生视频  电影镜头动画 可智能反推提示词 真实摄影_2013159959533461506.json、视频生成/图生视频/LTX2.0图生视频（须运行plus）_2009279040347185153.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 8 个 workflow 都包含：
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
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `EmptyImage` —— 6/8 个有
- `GetImageSize` —— 6/8 个有
- `ImageScaleBy` —— 6/8 个有
- `LTXVCropGuides` —— 6/8 个有
- `LTXVImgToVideoInplace` —— 6/8 个有
- `LTXVPreprocess` —— 6/8 个有
- `LTXVScheduler` —— 6/8 个有
- `LoadImage` —— 6/8 个有
- `VAEDecodeTiled` —— 6/8 个有
- `ResizeImagesByLongerEdge` —— 4/8 个有
- `CM_FloatToInt` —— 3/8 个有
- `LTXVSpatioTemporalTiledVAEDecode` —— 3/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `easy showAnything` —— 3/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `Float to Int` —— 2/8 个有
- `ImpactExecutionOrderController` —— 2/8 个有
- `JWStringReplace` —— 2/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/8 个有
- `RH_LLMAPI_NODE` —— 2/8 个有
- `TextInput_` —— 2/8 个有
- `easy cleanGpuUsed` —— 2/8 个有
- `BasicScheduler` —— 1/8 个有
- `JWInteger` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `RH_LLMAPI_Pro_Node` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `SimpleMath+` —— 1/8 个有
- `Text` —— 1/8 个有
- `VAEDecode` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 121 | 8 | 90% |
| 高度 | 25 | 25 - 25 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 121，8 个样本，取值集中（一致性 90%）
- 高度 中位数 25，观测区间 25 - 25，8 个样本，取值集中（一致性 100%）
