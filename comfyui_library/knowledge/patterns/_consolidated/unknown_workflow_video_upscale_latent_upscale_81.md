---
name: unknown_workflow_video_upscale_latent_upscale_81
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.753
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, SimpleMath+, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2044928269383897089.json, 视频生成/图生视频/2046030109836054530.json, 视频生成/图生视频/2033537132236640258.json, 视频生成/图生视频/2051476972135567361.json, 视频生成/文生视频/LTX2.3+中间帧+图生视频优化版+三图-首中尾帧_2052272204712300545.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_81

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2044928269383897089.json、视频生成/图生视频/2046030109836054530.json、视频生成/图生视频/2033537132236640258.json、视频生成/图生视频/2051476972135567361.json、视频生成/文生视频/LTX2.3+中间帧+图生视频优化版+三图-首中尾帧_2052272204712300545.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：75%

## 共有节点

全部 5 个 workflow 都包含：
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
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_Pro_Node` —— 4/5 个有
- `easy showAnything` —— 4/5 个有
- `ComfyMathExpression` —— 3/5 个有
- `FloatConstant` —— 3/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `LTXVImgToVideoInplaceKJ` —— 3/5 个有
- `PrimitiveInt` —— 3/5 个有
- `PrimitiveStringMultiline` —— 3/5 个有
- `CR Prompt Text` —— 2/5 个有
- `CR Text` —— 2/5 个有
- `ConcatTextOfUtils` —— 2/5 个有
- `LTXVScheduler` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `TextCombinerTwo` —— 2/5 个有
- `easy float` —— 2/5 个有
- `easy int` —— 2/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ResizeImageMaskNode` —— 1/5 个有
- `ResizeImagesByLongerEdge` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
