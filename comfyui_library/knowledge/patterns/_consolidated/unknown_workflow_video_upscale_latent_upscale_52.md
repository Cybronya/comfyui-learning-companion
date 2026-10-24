---
name: unknown_workflow_video_upscale_latent_upscale_52
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.743714
common_nodes: [CFGGuider, CLIPTextEncode, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/文生图/2030338706959245314.json, 视频生成/图生视频/LTX2.3 三段采样+去字幕_2040113981662175234.json, 视频生成/图生视频/LTX2.3 完美人物一致性_2064713194668650497.json, 视频生成/图生视频/LTX2.3 自用优化版 I2V_2063969422162882561.json, 视频生成/图生视频/LTX2.3--高动态图生视频_2041388395624140802.json, 视频生成/图生视频/LTX2.3-三段采样-- 视频质感飙升秒变大片_2041110942255161346.json, 视频生成/图生视频/LTX2.3_图生视频_多帧_2045362870476607490.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_52

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/2030338706959245314.json、视频生成/图生视频/LTX2.3 三段采样+去字幕_2040113981662175234.json、视频生成/图生视频/LTX2.3 完美人物一致性_2064713194668650497.json、视频生成/图生视频/LTX2.3 自用优化版 I2V_2063969422162882561.json、视频生成/图生视频/LTX2.3--高动态图生视频_2041388395624140802.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `DualCLIPLoader` —— 6/7 个有
- `LTXVCropGuides` —— 6/7 个有
- `ResizeImagesByLongerEdge` —— 6/7 个有
- `ComfyMathExpression` —— 5/7 个有
- `LTXVImgToVideoInplace` —— 5/7 个有
- `LoraLoaderModelOnly` —— 5/7 个有
- `PrimitiveInt` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `ImageResizeKJv2` —— 4/7 个有
- `LoraLoader` —— 4/7 个有
- `GetNode` —— 3/7 个有
- `LTX2_NAG` —— 3/7 个有
- `LTXVChunkFeedForward` —— 3/7 个有
- `ModelPatchTorchSettings` —— 3/7 个有
- `PathchSageAttentionKJ` —— 3/7 个有
- `PreviewImage` —— 3/7 个有
- `SetNode` —— 3/7 个有
- `CM_FloatToInt` —— 2/7 个有
- `Int` —— 2/7 个有
- `LTXTiledSampler` —— 2/7 个有
- `LTXVImgToVideoConditionOnly` —— 2/7 个有
- `LayerUtility: PurgeVRAM` —— 2/7 个有
- `PromptRelayEncode` —— 2/7 个有
- `VAELoader` —— 2/7 个有
- `BOOLConstant` —— 1/7 个有
- `Float` —— 1/7 个有
- `LTX2SamplingPreviewOverride` —— 1/7 个有
- `LTXAVTextEncoderLoader` —— 1/7 个有
- `LTXVImgToVideoInplaceKJ` —— 1/7 个有
- `PrimitiveBoolean` —— 1/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `ResizeImageMaskNode` —— 1/7 个有
- `TTResolutionSelector` —— 1/7 个有
- `Text` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有
- `math_calculate` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 25 - 44 | 7 | 72% |
| LoRA 模型强度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 44，7 个样本
- LoRA 模型强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
