---
name: unknown_workflow_video_lora_sampler_143
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.56125
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, EmptyLTXVLatentVideo, ImageResizeKJv2, Int, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SimpleMath+, TTResolutionSelector, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2032479656754028546.json, 视频生成/图生视频/图生视频High-Definition Zoom Convert Images to Video_2094247562952925185.json, 视频生成/图生视频/2051999667881295873.json, 视频生成/图生视频/2051983699100614658.json, 视频生成/文生视频/LTX-2.3 图生视频（四宫格剧情版）_2037078723727466498.json, 视频生成/文生视频/LTX-2.3 文&图生视频（高清放大版）_2029905437574828033.json, 视频生成/文生视频/LTX-2.3+图生视频（四宫格剧情版）_2039691601596911617.json, 视频生成/文生视频/LTX-2.3_文&图生视频（单采极速版）_2042119919898202114.json, 视频生成/文生视频/LTX-2.3_文&图生视频（精简版）_2029879882641055746.json, 视频生成/文生视频/LTX2.3+全节点注释_2052022977276989442.json, 视频生成/文生视频/LTX2.3分镜视频生成+节点注释（自学版）_2052036301666439170.json, 视频生成/文生视频/【超强】LTX-2.3首尾帧_2032085446586535937.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_143

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/2032479656754028546.json、视频生成/图生视频/图生视频High-Definition Zoom Convert Images to Video_2094247562952925185.json、视频生成/图生视频/2051999667881295873.json、视频生成/图生视频/2051983699100614658.json、视频生成/文生视频/LTX-2.3 图生视频（四宫格剧情版）_2037078723727466498.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：56%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `ImageResizeKJv2`
- `Int`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `TTResolutionSelector`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 10/12 个有
- `LTXVImgToVideoConditionOnly` —— 10/12 个有
- `LTXVLatentUpsampler` —— 10/12 个有
- `LatentUpscaleModelLoader` —— 10/12 个有
- `RH_LLMAPI_Pro_Node` —— 10/12 个有
- `SetNode` —— 10/12 个有
- `Text` —— 10/12 个有
- `easy showAnything` —— 10/12 个有
- `ImageScaleBy` —— 8/12 个有
- `LTXVImgToVideoInplaceKJ` —— 8/12 个有
- `GuHaiAutoImageSplit` —— 6/12 个有
- `ImageFromBatch+` —— 6/12 个有
- `LTXVPreprocess` —— 6/12 个有
- `DualCLIPLoader` —— 5/12 个有
- `PreviewAny` —— 5/12 个有
- `TextGenerateLTX2Prompt` —— 5/12 个有
- `ComfyMathExpression` —— 4/12 个有
- `FloatConstant` —— 4/12 个有
- `PreviewImage` —— 4/12 个有
- `PrimitiveBoolean` —— 4/12 个有
- `easy cleanGpuUsed` —— 4/12 个有
- `CR Text Replace` —— 2/12 个有
- `ImageConcatMulti` —— 2/12 个有
- `RH_Utils` —— 2/12 个有
- `MultiTextConcatenate` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 12 | 100% |
| 高度 | 25 | 25 - 25 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，12 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，12 个样本，取值集中（一致性 100%）
