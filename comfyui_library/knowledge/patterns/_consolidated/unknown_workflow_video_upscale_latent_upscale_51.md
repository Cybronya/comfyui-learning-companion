---
name: unknown_workflow_video_upscale_latent_upscale_51
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.83225
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2033729811360780290.json, 视频生成/图生视频/2067597395021623297.json, 视频生成/图生视频/2054745328590565377.json, 视频生成/图生视频/2033530948851081217.json, 视频生成/图生视频/老孙AI  三图-首中尾帧 视频_2086324689701531649.json, 视频生成/图生视频/2033537132236640258.json, 视频生成/图生视频/2051476972135567361.json, 视频生成/文生视频/LTX2.3+中间帧+图生视频优化版+三图-首中尾帧_2052272204712300545.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_51

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2033729811360780290.json、视频生成/图生视频/2067597395021623297.json、视频生成/图生视频/2054745328590565377.json、视频生成/图生视频/2033530948851081217.json、视频生成/图生视频/老孙AI  三图-首中尾帧 视频_2086324689701531649.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
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
- `FloatConstant` —— 7/8 个有
- `ImageResizeKJv2` —— 7/8 个有
- `LTXVCropGuides` —— 7/8 个有
- `PrimitiveInt` —— 7/8 个有
- `SimpleMath+` —— 7/8 个有
- `ComfyMathExpression` —— 6/8 个有
- `RH_LLMAPI_Pro_Node` —— 6/8 个有
- `ResizeImagesByLongerEdge` —— 6/8 个有
- `ResizeImageMaskNode` —— 5/8 个有
- `TextCombinerTwo` —— 5/8 个有
- `easy showAnything` —— 5/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `MathExpression|pysssss` —— 2/8 个有
- `CR Text` —— 1/8 个有
- `GetNode` —— 1/8 个有
- `INTConstant` —— 1/8 个有
- `LayerUtility: PurgeVRAM` —— 1/8 个有
- `PrimitiveFloat` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `SetNode` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `SimpleCalculatorKJ` —— 1/8 个有
- `VAEDecode` —— 1/8 个有
- `floatToInt _O` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 8 | 100% |
| 高度 | 25 | 25 - 60 | 8 | 61% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，8 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 60，8 个样本
