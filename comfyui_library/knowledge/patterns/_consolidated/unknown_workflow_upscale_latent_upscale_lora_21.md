---
name: unknown_workflow_upscale_latent_upscale_lora_21
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.885583
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLTXVLatentVideo, FloatConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SimpleMath+, VAEDecodeTiled, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/LTX2.3 _ 单图+简单提示词=快速出视频_2057674716944625665.json, 图片生成/图生图/中间帧 图生视频 首中尾帧 LTX2.3_2042479103651094529.json, 图片生成/图生图/二、三图（LTX2.3  Remix）_2056909754852794370.json, 图片生成/图生图/首尾帧图生视频   LTX2.3   丝滑lora版_2042477166348210177.json, 视频生成/图生视频/LTX2.3 --首尾帧双图生视频--全自动提示词--自由控制尾帧位置--超高出片率_2035325472770367490.json, 视频生成/图生视频/LTX2.3 中间帧+图生视频 三图-首中尾帧+优化版_2051164751694184449.json, 视频生成/图生视频/LTX2.3 全自动提示词--首中尾帧三图生视频_2035325465820405761.json, 视频生成/图生视频/LTX2.3-五图生视频10秒电商展示变装-全自动提示词_2051490555791720450.json, 视频生成/图生视频/LTX2.3-五图生视频15秒电商展示变装-全自动提示词_2051660543777361922.json, 视频生成/图生视频/LTX2.3首尾帧双图生视频-单镜头自动提示词版本_2051217425542201345.json, 视频生成/图生视频/LTX2.3首尾帧双图生视频-手动提示词版--注释含提示词模板_2051911216334942209.json, 视频生成/图生视频/全能图片G 2.0+LTX2.3文生图首尾帧生视频&自动提示词版本_2051654152509501441.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_21

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/LTX2.3 _ 单图+简单提示词=快速出视频_2057674716944625665.json、图片生成/图生图/中间帧 图生视频 首中尾帧 LTX2.3_2042479103651094529.json、图片生成/图生图/二、三图（LTX2.3  Remix）_2056909754852794370.json、图片生成/图生图/首尾帧图生视频   LTX2.3   丝滑lora版_2042477166348210177.json、视频生成/图生视频/LTX2.3 --首尾帧双图生视频--全自动提示词--自由控制尾帧位置--超高出片率_2035325472770367490.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：89%

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
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `VAEDecodeTiled`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 11/12 个有
- `RH_LLMAPI_Pro_Node` —— 11/12 个有
- `LTXVPreprocess` —— 10/12 个有
- `CreateVideo` —— 9/12 个有
- `ResizeImagesByLongerEdge` —— 9/12 个有
- `SaveVideo` —— 9/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/12 个有
- `CR Prompt Text` —— 7/12 个有
- `DualCLIPLoader` —— 7/12 个有
- `PreviewAny` —— 7/12 个有
- `TextGenerateLTX2Prompt` —— 7/12 个有
- `PrimitiveStringMultiline` —— 5/12 个有
- `ImageResizeKJv2` —— 4/12 个有
- `TextCombinerTwo` —— 4/12 个有
- `VHS_VideoCombine` —— 4/12 个有
- `easy int` —— 4/12 个有
- `Fast Groups Bypasser (rgthree)` —— 3/12 个有
- `ResizeImageMaskNode` —— 3/12 个有
- `CLIPLoader` —— 1/12 个有
- `CLIPVisionEncode` —— 1/12 个有
- `CLIPVisionLoader` —— 1/12 个有
- `CM_IntToFloat` —— 1/12 个有
- `CR Text Concatenate` —— 1/12 个有
- `INTConstant` —— 1/12 个有
- `KSamplerAdvanced` —— 1/12 个有
- `LayerUtility: PurgeVRAM V2` —— 1/12 个有
- `ModelSamplingSD3` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `RH_RhartImageG2TextToImage` —— 1/12 个有
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
