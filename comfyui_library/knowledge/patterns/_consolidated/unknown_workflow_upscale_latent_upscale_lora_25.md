---
name: unknown_workflow_upscale_latent_upscale_lora_25
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.850083
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, FloatConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveInt, PrimitiveStringMultiline, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, SimpleMath+, VAEDecodeTiled, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/LTX2.3 _ 单图+简单提示词=快速出视频_2057674716944625665.json, 图片生成/图生图/中间帧 图生视频 首中尾帧 LTX2.3_2042479103651094529.json, 图片生成/图生图/二、三图（LTX2.3  Remix）_2056909754852794370.json, 图片生成/图生图/首尾帧图生视频   LTX2.3   丝滑lora版_2042477166348210177.json, 视频生成/图生视频/1FINAL - LTX2.3 _ 单图+提示词=快速出视频_2052231209417232385.json, 视频生成/图生视频/LTX2.3 _ 三图-首中尾帧 优化版_2033038199701905410.json, 视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版_2033156764371263490.json, 视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版_2044341747362304001.json, 视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版_2049303254957297665.json, 视频生成/图生视频/LTX2.3 _ 首尾帧 快速优化版_2044586983204327425.json, 视频生成/图生视频/LTX2.3 _ 首尾帧 视频_2052216878214467585.json, 视频生成/图生视频/LTX2.3 中间帧+图生视频 三图-首中尾帧+优化版_2051164751694184449.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_25

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/LTX2.3 _ 单图+简单提示词=快速出视频_2057674716944625665.json、图片生成/图生图/中间帧 图生视频 首中尾帧 LTX2.3_2042479103651094529.json、图片生成/图生图/二、三图（LTX2.3  Remix）_2056909754852794370.json、图片生成/图生图/首尾帧图生视频   LTX2.3   丝滑lora版_2042477166348210177.json、视频生成/图生视频/1FINAL - LTX2.3 _ 单图+提示词=快速出视频_2052231209417232385.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `EmptyLTXVLatentVideo`
- `FloatConstant`
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
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `VAEDecodeTiled`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ResizeImagesByLongerEdge` —— 11/12 个有
- `CreateVideo` —— 9/12 个有
- `SaveVideo` —— 9/12 个有
- `ImageResizeKJv2` —— 5/12 个有
- `ResizeImageMaskNode` —— 4/12 个有
- `TextCombinerTwo` —— 4/12 个有
- `VHS_VideoCombine` —— 4/12 个有
- `Fast Groups Bypasser (rgthree)` —— 3/12 个有
- `Resize` —— 2/12 个有
- `kkResize` —— 2/12 个有
- `AILab_QwenVL` —— 1/12 个有
- `CLIPLoader` —— 1/12 个有
- `CLIPVisionEncode` —— 1/12 个有
- `CLIPVisionLoader` —— 1/12 个有
- `CM_IntToFloat` —— 1/12 个有
- `CombineImagesForQwen3VL` —— 1/12 个有
- `INTConstant` —— 1/12 个有
- `KSamplerAdvanced` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `LayerUtility: PurgeVRAM V2` —— 1/12 个有
- `ModelSamplingSD3` —— 1/12 个有
- `UNETLoader` —— 1/12 个有
- `VAEDecode` —— 1/12 个有
- `VAELoader` —— 1/12 个有
- `WanFirstLastFrameToVideo` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 12 | 100% |
| 高度 | 25 | 25 - 25 | 12 | 100% |
| 采样步数 | fixed | - | 1 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 1 | 100% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | euler_ancestral | - | 1 | 100% |
| 重绘幅度 | simple | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，12 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，12 个样本，取值集中（一致性 100%）
