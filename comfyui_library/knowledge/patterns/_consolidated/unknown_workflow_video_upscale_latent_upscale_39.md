---
name: unknown_workflow_video_upscale_latent_upscale_39
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.943889
common_nodes: [CFGGuider, CLIPTextEncode, CM_IntToFloat, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, ImageResizeKJv2, ImageScaleBy, JWInteger, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVImgToVideoInplaceKJ, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, TextInput_, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 丝滑多帧首中尾帧图生视频_2052636641159856129.json, 视频生成/图生视频/LTX2.3 丝滑多帧首中尾帧图生视频_2053362452670234625.json, 视频生成/图生视频/LTX2.3 丝滑多帧首中尾帧图生视频_2104164967065931777.json, 视频生成/图生视频/LTX2.3 丝滑多帧首尾帧V1_2052425175639052290.json, 视频生成/图生视频/LTX2.3 首中尾帧-丝滑多帧首尾帧-自动提示词_2054555811568996354.json, 视频生成/图生视频/LTX2.3--流畅多帧首中尾帧-便宜_2082740876471787522.json, 视频生成/图生视频/LTX2.3--流畅多帧首中尾帧_2052716191759773698.json, 视频生成/图生视频/LTX2.3-Transition丝滑过渡-四图帧首尾帧视频_2053134658111582210.json, 视频生成/图生视频/漫剧开源首尾帧_2054788108406804481.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_39

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 丝滑多帧首中尾帧图生视频_2052636641159856129.json、视频生成/图生视频/LTX2.3 丝滑多帧首中尾帧图生视频_2053362452670234625.json、视频生成/图生视频/LTX2.3 丝滑多帧首中尾帧图生视频_2104164967065931777.json、视频生成/图生视频/LTX2.3 丝滑多帧首尾帧V1_2052425175639052290.json、视频生成/图生视频/LTX2.3 首中尾帧-丝滑多帧首尾帧-自动提示词_2054555811568996354.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 9 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_IntToFloat`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `ImageResizeKJv2`
- `ImageScaleBy`
- `JWInteger`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVImgToVideoInplaceKJ`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `TextInput_`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `LTXVAudioVAEDecode` —— 8/9 个有
- `BatchThief` —— 1/9 个有
- `EnhancedLoadDiffusionModel` —— 1/9 个有
- `GetNode` —— 1/9 个有
- `Int` —— 1/9 个有
- `LoadAudio` —— 1/9 个有
- `MultiTextConcatenate` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `RH_LLMAPI_Pro_Node` —— 1/9 个有
- `RH_Utils` —— 1/9 个有
- `SetNode` —— 1/9 个有
- `ShowAnything|Mie` —— 1/9 个有
- `SimpleMath+` —— 1/9 个有
- `easy mathInt` —— 1/9 个有
- `ttN concat` —— 1/9 个有

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
