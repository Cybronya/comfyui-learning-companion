---
name: unknown_workflow_video_upscale_latent_upscale_108
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.827
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 _ 三图-首中尾帧 优化版_2033729811360780290.json, 视频生成/图生视频/ltx2.3首尾帧_2067597395021623297.json, 视频生成/图生视频/首尾帧图生视频 LTX2.3 优化版_2051476972135567361.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_108

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 _ 三图-首中尾帧 优化版_2033729811360780290.json、视频生成/图生视频/ltx2.3首尾帧_2067597395021623297.json、视频生成/图生视频/首尾帧图生视频 LTX2.3 优化版_2051476972135567361.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
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
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoInplaceKJ`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `FloatConstant` —— 2/3 个有
- `ImageResizeKJv2` —— 2/3 个有
- `LTXVCropGuides` —— 2/3 个有
- `MathExpression|pysssss` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `ResizeImagesByLongerEdge` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `ComfyMathExpression` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `RH_LLMAPI_Pro_Node` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `ResizeImageMaskNode` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `ShowText|pysssss` —— 1/3 个有
- `SimpleCalculatorKJ` —— 1/3 个有
- `VAEDecode` —— 1/3 个有
- `floatToInt _O` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 25 | 25 - 60 | 3 | 55% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 60，3 个样本
