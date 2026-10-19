---
name: unknown_workflow_video_upscale_latent_upscale_34
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.930182
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2040113981662175234.json, 视频生成/图生视频/2052636641159856129.json, 视频生成/图生视频/2053362452670234625.json, 视频生成/图生视频/LTX2.3 丝滑多帧首中尾帧图生视频_2104164967065931777.json, 视频生成/图生视频/2052425175639052290.json, 视频生成/图生视频/2064713194668650497.json, 视频生成/图生视频/2063969422162882561.json, 视频生成/图生视频/2054555811568996354.json, 视频生成/图生视频/LTX2.3--流畅多帧首中尾帧-便宜_2082740876471787522.json, 视频生成/图生视频/2052716191759773698.json, 视频生成/图生视频/2053134658111582210.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_34

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2040113981662175234.json、视频生成/图生视频/2052636641159856129.json、视频生成/图生视频/2053362452670234625.json、视频生成/图生视频/LTX2.3 丝滑多帧首中尾帧图生视频_2104164967065931777.json、视频生成/图生视频/2052425175639052290.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 11 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTX2_NAG` —— 10/11 个有
- `ImageResizeKJv2` —— 9/11 个有
- `CM_IntToFloat` —— 8/11 个有
- `GetImageSize` —— 8/11 个有
- `ImageScaleBy` —— 8/11 个有
- `JWInteger` —— 8/11 个有
- `LTX2SamplingPreviewOverride` —— 8/11 个有
- `LTXVImgToVideoInplaceKJ` —— 8/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/11 个有
- `TextInput_` —— 8/11 个有
- `VAELoader` —— 8/11 个有
- `ComfyMathExpression` —— 3/11 个有
- `LTXVCropGuides` —— 3/11 个有
- `PrimitiveStringMultiline` —— 3/11 个有
- `ResizeImagesByLongerEdge` —— 3/11 个有
- `LTXTiledSampler` —— 2/11 个有
- `LTXVChunkFeedForward` —— 2/11 个有
- `LayerUtility: PurgeVRAM` —— 2/11 个有
- `ModelPatchTorchSettings` —— 2/11 个有
- `PathchSageAttentionKJ` —— 2/11 个有
- `PromptRelayEncode` —— 2/11 个有
- `GetNode` —— 1/11 个有
- `Int` —— 1/11 个有
- `LoraLoader` —— 1/11 个有
- `MultiTextConcatenate` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `RH_LLMAPI_Pro_Node` —— 1/11 个有
- `RH_Utils` —— 1/11 个有
- `SetNode` —— 1/11 个有
- `ShowAnything|Mie` —— 1/11 个有
- `SimpleMath+` —— 1/11 个有
- `ttN concat` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 11 | 100% |
| 高度 | 25 | 25 - 44 | 11 | 74% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，11 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 44，11 个样本
