---
name: unknown_workflow_video_upscale_latent_upscale_26
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.868
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, ImageResizeKJv2, KSamplerSelect, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 三段采样+去字幕_2040113981662175234.json, 视频生成/图生视频/LTX2.3 丝滑多帧首中尾帧图生视频_2052636641159856129.json, 视频生成/图生视频/LTX2.3 丝滑多帧首中尾帧图生视频_2053362452670234625.json, 视频生成/图生视频/LTX2.3 丝滑多帧首中尾帧图生视频_2104164967065931777.json, 视频生成/图生视频/LTX2.3 丝滑多帧首尾帧V1_2052425175639052290.json, 视频生成/图生视频/LTX2.3 首中尾帧-丝滑多帧首尾帧-自动提示词_2054555811568996354.json, 视频生成/图生视频/LTX2.3--流畅多帧首中尾帧-便宜_2082740876471787522.json, 视频生成/图生视频/LTX2.3--流畅多帧首中尾帧_2052716191759773698.json, 视频生成/图生视频/LTX2.3--高动态图生视频_2041388395624140802.json, 视频生成/图生视频/LTX2.3-Transition丝滑过渡-四图帧首尾帧视频_2053134658111582210.json, 视频生成/图生视频/LTX2.3-三段采样-- 视频质感飙升秒变大片_2041110942255161346.json, 视频生成/图生视频/漫剧开源首尾帧_2054788108406804481.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_26

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 三段采样+去字幕_2040113981662175234.json、视频生成/图生视频/LTX2.3 丝滑多帧首中尾帧图生视频_2052636641159856129.json、视频生成/图生视频/LTX2.3 丝滑多帧首中尾帧图生视频_2053362452670234625.json、视频生成/图生视频/LTX2.3 丝滑多帧首中尾帧图生视频_2104164967065931777.json、视频生成/图生视频/LTX2.3 丝滑多帧首尾帧V1_2052425175639052290.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
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
- `LTXVAudioVAEDecode` —— 11/12 个有
- `PrimitiveInt` —— 11/12 个有
- `LoraLoaderModelOnly` —— 10/12 个有
- `CM_IntToFloat` —— 9/12 个有
- `GetImageSize` —— 9/12 个有
- `ImageScaleBy` —— 9/12 个有
- `JWInteger` —— 9/12 个有
- `LTX2SamplingPreviewOverride` —— 9/12 个有
- `LTX2_NAG` —— 9/12 个有
- `LTXVImgToVideoInplaceKJ` —— 9/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/12 个有
- `TextInput_` —— 9/12 个有
- `VAELoader` —— 9/12 个有
- `ComfyMathExpression` —— 3/12 个有
- `GetNode` —— 3/12 个有
- `LTXVCropGuides` —— 3/12 个有
- `LoraLoader` —— 3/12 个有
- `PreviewImage` —— 3/12 个有
- `PrimitiveStringMultiline` —— 3/12 个有
- `ResizeImagesByLongerEdge` —— 3/12 个有
- `SetNode` —— 3/12 个有
- `Int` —— 2/12 个有
- `BatchThief` —— 1/12 个有
- `EnhancedLoadDiffusionModel` —— 1/12 个有
- `LoadAudio` —— 1/12 个有
- `MultiTextConcatenate` —— 1/12 个有
- `RH_LLMAPI_Pro_Node` —— 1/12 个有
- `RH_Utils` —— 1/12 个有
- `ShowAnything|Mie` —— 1/12 个有
- `SimpleMath+` —— 1/12 个有
- `easy mathInt` —— 1/12 个有
- `ttN concat` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 12 | 100% |
| 高度 | 25 | 25 - 25 | 12 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 3 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，12 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，12 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
