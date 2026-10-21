---
name: unknown_workflow_video_sampler_clip_26
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.626643
common_nodes: [CFGGuider, CLIPTextEncode, CR Float To Integer, DualCLIPLoader, EmptyLTXVLatentVideo, GuHaiAutoImageSplit, ImageFromBatch+, ImageResizeKJv2, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LoadImage, ManualSigmas, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, TTResolutionSelector, Text, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy indexAnything]
problems: []
missing: []
members: [视频生成/图生视频/2050433781642866689.json, 视频生成/图生视频/2038477520076546049.json, 视频生成/图生视频/2048025601059069954.json, 视频生成/图生视频/2051228355147644930.json, 视频生成/图生视频/2058423071744282626.json, 视频生成/图生视频/2060526792787718145.json, 视频生成/图生视频/2041690462200799233.json, 视频生成/图生视频/2040686679291334658.json, 视频生成/图生视频/2042137204117479425.json, 视频生成/图生视频/2041291651959758850.json, 视频生成/图生视频/2056229432154705921.json, 视频生成/图生视频/2053379997733273601.json, 视频生成/文生视频/AI代码侠土豆-LTX-2.3 批量化漫剧 20宫格 直出1分钟视频_2043750175751020546.json, 视频生成/文生视频/LTX-2.3 批量化漫剧 20宫格 直出1分钟视频_2046021811200069633.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_26

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/2050433781642866689.json、视频生成/图生视频/2038477520076546049.json、视频生成/图生视频/2048025601059069954.json、视频生成/图生视频/2051228355147644930.json、视频生成/图生视频/2058423071744282626.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：63%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Float To Integer`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GuHaiAutoImageSplit`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `TTResolutionSelector`
- `Text`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy indexAnything`

**可变部分**（部分 workflow 才有）：
- `AudioConcat` —— 13/14 个有
- `EmptyAudio` —— 13/14 个有
- `INTConstant` —— 13/14 个有
- `If ANY execute A else B` —— 13/14 个有
- `PreviewImage` —— 13/14 个有
- `SDVM Image List Repeat` —— 13/14 个有
- `SimpleMath+` —— 13/14 个有
- `easy batchAnything` —— 13/14 个有
- `easy cleanGpuUsed` —— 13/14 个有
- `easy forLoopEnd` —— 13/14 个有
- `easy forLoopStart` —— 13/14 个有
- `easy isNone` —— 13/14 个有
- `easy promptList` —— 13/14 个有
- `GetNode` —— 12/14 个有
- `LatentUpscaleModelLoader` —— 12/14 个有
- `SetNode` —— 12/14 个有
- `ShowText|pysssss` —— 12/14 个有
- `easy lengthAnything` —— 12/14 个有
- `RH_LLMAPI_Pro_Node` —— 9/14 个有
- `easy showAnything` —— 9/14 个有
- `Int` —— 7/14 个有
- `GetObjectFromJson` —— 5/14 个有
- `GetTextFromJson` —— 5/14 个有
- `Light-Tool: DeserializeJsonString` —— 5/14 个有
- `LoraLoaderModelOnly` —— 5/14 个有
- `PromptRelayEncode` —— 5/14 个有
- `AILab_QwenVL_Advanced` —— 1/14 个有
- `Bjornulf_ShowInt` —— 1/14 个有
- `CR Text` —— 1/14 个有
- `CR Text Concatenate` —— 1/14 个有
- `Display Any (rgthree)` —— 1/14 个有
- `IfInnerExecute` —— 1/14 个有
- `ImageConcatMulti` —— 1/14 个有
- `ImageListToImageBatch` —— 1/14 个有
- `ImpactInt` —— 1/14 个有
- `JjkText` —— 1/14 个有
- `KOOK_SaveJPGImage` —— 1/14 个有
- `LayerUtility: PurgeVRAM` —— 1/14 个有
- `MathExpression|pysssss` —— 1/14 个有
- `ProcessString` —— 1/14 个有
- `PromptRelayEncodeTimeline` —— 1/14 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/14 个有
- `ShowAnything|Mie` —— 1/14 个有
- `easy compare` —— 1/14 个有
- `easy imageConcat` —— 1/14 个有
- `easy promptLine` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 14 | 100% |
| 高度 | 25 | 25 - 25 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，14 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，14 个样本，取值集中（一致性 100%）
