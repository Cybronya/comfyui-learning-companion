---
name: unknown_workflow_upscale_latent_upscale_sampler_7
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7769
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [图片生成/文生图/2030338706959245314.json, 数字人/数字人/LTX2.3首尾帧_2037413437122289666.json, 视频生成/图生视频/ITX2.3--首尾帧_2032004087528562690.json, 视频生成/图生视频/LTX-2.3  5图高清参考工作流V1.0_2038717836129996802.json, 视频生成/图生视频/LTX2.3 三段采样+去字幕_2040113981662175234.json, 视频生成/图生视频/LTX2.3--高动态图生视频_2041388395624140802.json, 视频生成/图生视频/LTX2.3-三段采样-- 视频质感飙升秒变大片_2041110942255161346.json, 视频生成/图生视频/LTX2.3强化对口型 KJ版_2040052966710845441.json, 视频生成/图生视频/LTX23_i2v_pose_control_2076514549532024833.json, 视频生成/图生视频/video_ltx2_3_i2v_galaxyAce_2037940462845169665.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_7

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/2030338706959245314.json、数字人/数字人/LTX2.3首尾帧_2037413437122289666.json、视频生成/图生视频/ITX2.3--首尾帧_2032004087528562690.json、视频生成/图生视频/LTX-2.3  5图高清参考工作流V1.0_2038717836129996802.json、视频生成/图生视频/LTX2.3 三段采样+去字幕_2040113981662175234.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
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

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 9/10 个有
- `LTXVCropGuides` —— 9/10 个有
- `LTXVImgToVideoInplace` —— 9/10 个有
- `PrimitiveInt` —— 9/10 个有
- `ResizeImagesByLongerEdge` —— 9/10 个有
- `ImageResizeKJv2` —— 8/10 个有
- `LoraLoaderModelOnly` —— 7/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `VHS_VideoCombine` —— 7/10 个有
- `PrimitiveBoolean` —— 6/10 个有
- `ResizeImageMaskNode` —— 6/10 个有
- `LoraLoader` —— 5/10 个有
- `CreateVideo` —— 4/10 个有
- `PreviewImage` —— 4/10 个有
- `GetNode` —— 3/10 个有
- `LTXVImgToVideoInplaceKJ` —— 3/10 个有
- `SaveVideo` —— 3/10 个有
- `SetNode` —— 3/10 个有
- `CM_FloatToInt` —— 1/10 个有
- `Int` —— 1/10 个有
- `LTXAddVideoICLoRAGuide` —— 1/10 个有
- `LTXICLoRALoaderModelOnly` —— 1/10 个有
- `LTXVImgToVideoConditionOnly` —— 1/10 个有
- `MatAnyone` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `PrimitiveFloat` —— 1/10 个有
- `RH_LLMAPI_Pro_Node` —— 1/10 个有
- `RebatchImages` —— 1/10 个有
- `SaveAudio` —— 1/10 个有
- `Text` —— 1/10 个有
- `UnetLoaderGGUF` —— 1/10 个有
- `VAELoader` —— 1/10 个有
- `VHS_LoadVideo` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 25 - 25 | 10 | 100% |
| LoRA 模型强度 | 1 | 0 - 1 | 5 | 50% |
| LoRA 文本强度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0 - 1，5 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
