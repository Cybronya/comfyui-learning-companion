---
name: unknown_workflow_upscale_latent_upscale_lora_30
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8264
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [图片生成/文生图/万象AI-LTX2.3专用文_图生视频工作流（提示词动态优化版自由时长自动横竖屏）_2047327567736217602.json, 图片生成/文生图/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）自动横屏竖屏_2037526578241998850.json, 视频生成/图生视频/Heishen-video_ltx2_3_id_lora_2041874975627415554.json, 视频生成/图生视频/KK图生视频工作流_2079742870340325377.json, 视频生成/图生视频/LTX 2.3 多人数字人--音频驱动图片生视频_2030885319217782785.json, 视频生成/图生视频/LTX 2.3 多人数字人--音频驱动图片生视频_2031213206097633281.json, 视频生成/图生视频/万象AI真人短剧专用图生视频工作流（LTX2.3自动提示词优化版自动横屏竖屏自动时长）_2040620367496089602.json, 视频生成/图生视频/图生视频一镜到底_已修复_2078421854469050370.json, 视频生成/图生视频/（1图 1音频）LTX2.3 图 + 音频数字人对口型_2111327625162612737.json, 视频生成/文生视频/LTX2.3数字人音频驱动视频生成_2031965741934714882.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_30

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/万象AI-LTX2.3专用文_图生视频工作流（提示词动态优化版自由时长自动横竖屏）_2047327567736217602.json、图片生成/文生图/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）自动横屏竖屏_2037526578241998850.json、视频生成/图生视频/Heishen-video_ltx2_3_id_lora_2041874975627415554.json、视频生成/图生视频/KK图生视频工作流_2079742870340325377.json、视频生成/图生视频/LTX 2.3 多人数字人--音频驱动图片生视频_2030885319217782785.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LTXVAudioVAEDecode` —— 9/10 个有
- `LTXVEmptyLatentAudio` —— 9/10 个有
- `LoadAudio` —— 9/10 个有
- `PrimitiveBoolean` —— 9/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/10 个有
- `easy showAnything` —— 7/10 个有
- `Int` —— 6/10 个有
- `CR Text` —— 5/10 个有
- `RH_LLMAPI_Pro_Node` —— 5/10 个有
- `SolidMask` —— 5/10 个有
- `CR Integer To String` —— 4/10 个有
- `GetAudioDurationFromAudio` —— 4/10 个有
- `LTXVAudioVAEEncode` —— 4/10 个有
- `MathExpression|pysssss` —— 4/10 个有
- `RH_LLMAPI_NODE` —— 4/10 个有
- `SetLatentNoiseMask` —— 4/10 个有
- `TrimAudioDuration` —— 4/10 个有
- `easy promptReplace` —— 4/10 个有
- `MelBandRoFormerModelLoader` —— 3/10 个有
- `MelBandRoFormerSampler` —— 3/10 个有
- `PrimitiveFloat` —— 3/10 个有
- `CM_FloatToInt` —— 2/10 个有
- `LayerUtility: PurgeVRAM V2` —— 2/10 个有
- `SimpleMath+` —— 2/10 个有
- `SoundFlow_GetLength` —— 2/10 个有
- `GetNode` —— 1/10 个有
- `LTXVReferenceAudio` —— 1/10 个有
- `RecordAudio` —— 1/10 个有
- `SetNode` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 9 | 100% |
| 高度 | 25 | 25 - 25 | 9 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，9 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，9 个样本，取值集中（一致性 100%）
