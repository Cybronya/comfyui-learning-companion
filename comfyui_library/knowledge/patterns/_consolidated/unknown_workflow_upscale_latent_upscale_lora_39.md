---
name: unknown_workflow_upscale_latent_upscale_lora_39
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.872571
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, FloatConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveInt, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, SimpleMath+, VAEDecodeTiled, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/LTX2.3 _ 单图+简单提示词=快速出视频_2057674716944625665.json, 图片生成/图生图/中间帧 图生视频 首中尾帧 LTX2.3_2042479103651094529.json, 图片生成/图生图/二、三图（LTX2.3  Remix）_2056909754852794370.json, 图片生成/图生图/首尾帧图生视频   LTX2.3   丝滑lora版_2042477166348210177.json, 视频生成/图生视频/LTX2.3 --首尾帧双图生视频--全自动提示词--自由控制尾帧位置--超高出片率_2035325472770367490.json, 视频生成/图生视频/LTX2.3 -首尾帧双图生视频-长镜头一镜到底-提示词高遵从-直出1K_2057749829224329218.json, 视频生成/图生视频/LTX2.3 _ 双图-首尾帧 优化版_2052949271544123393.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_39

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/LTX2.3 _ 单图+简单提示词=快速出视频_2057674716944625665.json、图片生成/图生图/中间帧 图生视频 首中尾帧 LTX2.3_2042479103651094529.json、图片生成/图生图/二、三图（LTX2.3  Remix）_2056909754852794370.json、图片生成/图生图/首尾帧图生视频   LTX2.3   丝滑lora版_2042477166348210177.json、视频生成/图生视频/LTX2.3 --首尾帧双图生视频--全自动提示词--自由控制尾帧位置--超高出片率_2035325472770367490.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `VAEDecodeTiled`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LTXVPreprocess` —— 6/7 个有
- `CreateVideo` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `ResizeImagesByLongerEdge` —— 5/7 个有
- `SaveVideo` —— 5/7 个有
- `ImageResizeKJv2` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `TextCombinerTwo` —— 3/7 个有
- `VHS_VideoCombine` —— 3/7 个有
- `CR Prompt Text` —— 2/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `ResizeImageMaskNode` —— 2/7 个有
- `easy int` —— 2/7 个有
- `CLIPLoader` —— 1/7 个有
- `CLIPVisionEncode` —— 1/7 个有
- `CLIPVisionLoader` —— 1/7 个有
- `CM_IntToFloat` —— 1/7 个有
- `DualCLIPLoader` —— 1/7 个有
- `INTConstant` —— 1/7 个有
- `ImageResize+` —— 1/7 个有
- `KSamplerAdvanced` —— 1/7 个有
- `LayerUtility: PurgeVRAM V2` —— 1/7 个有
- `ModelSamplingSD3` —— 1/7 个有
- `PreviewAny` —— 1/7 个有
- `TextGenerateLTX2Prompt` —— 1/7 个有
- `UNETLoader` —— 1/7 个有
- `VAEDecode` —— 1/7 个有
- `VAELoader` —— 1/7 个有
- `WanFirstLastFrameToVideo` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 25 - 25 | 7 | 100% |
| 采样步数 | fixed | - | 1 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 1 | 100% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | euler_ancestral | - | 1 | 100% |
| 重绘幅度 | simple | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
