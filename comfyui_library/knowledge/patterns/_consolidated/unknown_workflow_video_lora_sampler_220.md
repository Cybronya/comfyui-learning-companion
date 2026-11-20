---
name: unknown_workflow_video_lora_sampler_220
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.5431
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, EmptyLTXVLatentVideo, Int, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SimpleMath+, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3图生视频_2045757493573328897.json, 视频生成/图生视频/图生视频High-Definition Zoom Convert Images to Video_2094247562952925185.json, 视频生成/文生视频/LTX-2.3 图生视频（四宫格剧情版）_2037078723727466498.json, 视频生成/文生视频/LTX-2.3 文&图生视频（高清放大版）_2029905437574828033.json, 视频生成/文生视频/LTX-2.3+图生视频（四宫格剧情版）_2039691601596911617.json, 视频生成/文生视频/LTX-2.3_文&图生视频（单采极速版）_2042119919898202114.json, 视频生成/文生视频/LTX-2.3_文&图生视频（精简版）_2029879882641055746.json, 视频生成/文生视频/LTX2.3+全节点注释_2052022977276989442.json, 视频生成/文生视频/LTX2.3分镜视频生成+节点注释（自学版）_2052036301666439170.json, 视频生成/文生视频/【超强】LTX-2.3首尾帧_2032085446586535937.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_220

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/LTX2.3图生视频_2045757493573328897.json、视频生成/图生视频/图生视频High-Definition Zoom Convert Images to Video_2094247562952925185.json、视频生成/文生视频/LTX-2.3 图生视频（四宫格剧情版）_2037078723727466498.json、视频生成/文生视频/LTX-2.3 文&图生视频（高清放大版）_2029905437574828033.json、视频生成/文生视频/LTX-2.3+图生视频（四宫格剧情版）_2039691601596911617.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
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
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SimpleMath+`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 9/10 个有
- `LTXVImgToVideoConditionOnly` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `TTResolutionSelector` —— 9/10 个有
- `GetNode` —— 8/10 个有
- `SetNode` —— 8/10 个有
- `LTXVLatentUpsampler` —— 7/10 个有
- `LatentUpscaleModelLoader` —— 7/10 个有
- `RH_LLMAPI_Pro_Node` —— 7/10 个有
- `Text` —— 7/10 个有
- `easy showAnything` —— 7/10 个有
- `ImageScaleBy` —— 6/10 个有
- `LTXVPreprocess` —— 6/10 个有
- `LTXVImgToVideoInplaceKJ` —— 5/10 个有
- `DualCLIPLoader` —— 4/10 个有
- `GuHaiAutoImageSplit` —— 4/10 个有
- `ImageFromBatch+` —— 4/10 个有
- `PreviewAny` —— 4/10 个有
- `PrimitiveBoolean` —— 4/10 个有
- `TextGenerateLTX2Prompt` —— 4/10 个有
- `easy cleanGpuUsed` —— 4/10 个有
- `ComfyMathExpression` —— 2/10 个有
- `FloatConstant` —— 2/10 个有
- `PreviewImage` —— 2/10 个有
- `Float` —— 1/10 个有
- `ImageConcatMulti` —— 1/10 个有
- `MemoryCleaner` —— 1/10 个有
- `PlaySound|pysssss` —— 1/10 个有
- `Text Multiline` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
