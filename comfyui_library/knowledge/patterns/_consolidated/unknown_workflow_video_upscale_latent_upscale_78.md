---
name: unknown_workflow_video_upscale_latent_upscale_78
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.6068
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, GuHaiAutoImageSplit, ImageFromBatch+, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PreviewImage, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleMath+, Text, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/ltx2.3图生视频4图参考音色版（无字幕)_2046461995771236354.json, 视频生成/图生视频/一键短视频 分镜控制  提示词优化 时间线控制 Ltx2.3  PromptRelay + 丝滑转场_2052633200643588097.json, 视频生成/图生视频/一键短视频 四宫格短视频    自带声音 音乐 LTX-2.3（Fisher大佬优化版）_2037855814051958786.json, 视频生成/图生视频/四宫格-LTX-2.3 图生视频（全面优化版）音频驱动_2041772367239712769.json, 视频生成/图生视频/短剧制作，图生视频，四宫格+ Ltx2.3 Prompt Relay V3版本_2052550289055596546.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_78

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/ltx2.3图生视频4图参考音色版（无字幕)_2046461995771236354.json、视频生成/图生视频/一键短视频 分镜控制  提示词优化 时间线控制 Ltx2.3  PromptRelay + 丝滑转场_2052633200643588097.json、视频生成/图生视频/一键短视频 四宫格短视频    自带声音 音乐 LTX-2.3（Fisher大佬优化版）_2037855814051958786.json、视频生成/图生视频/四宫格-LTX-2.3 图生视频（全面优化版）音频驱动_2041772367239712769.json、视频生成/图生视频/短剧制作，图生视频，四宫格+ Ltx2.3 Prompt Relay V3版本_2052550289055596546.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：61%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GuHaiAutoImageSplit`
- `ImageFromBatch+`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `PreviewImage`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SetNode`
- `SimpleMath+`
- `Text`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Float To Integer` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `LTXVEmptyLatentAudio` —— 4/5 个有
- `PrimitiveFloat` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/5 个有
- `LoadAudio` —— 3/5 个有
- `ImageResizeKJv2` —— 2/5 个有
- `ImpactSwitch` —— 2/5 个有
- `Int` —— 2/5 个有
- `LTXICLoRALoaderModelOnly` —— 2/5 个有
- `LTXVAudioVAEEncode` —— 2/5 个有
- `MelBandRoFormerModelLoader` —— 2/5 个有
- `MelBandRoFormerSampler` —— 2/5 个有
- `PreviewAudio` —— 2/5 个有
- `PromptRelayEncodeTimeline` —— 2/5 个有
- `SetLatentNoiseMask` —— 2/5 个有
- `SolidMask` —— 2/5 个有
- `easy anythingIndexSwitch` —— 2/5 个有
- `AudioCrop` —— 1/5 个有
- `AudioInfo` —— 1/5 个有
- `CM_IntToFloat` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `DapaoSmartMemoryOptimizerNode` —— 1/5 个有
- `Display Any (rgthree)` —— 1/5 个有
- `ImpactInversedSwitch` —— 1/5 个有
- `LTXVReferenceAudio` —— 1/5 个有
- `LoraLoaderModelOnly` —— 1/5 个有
- `NormalizeAudioLoudness` —— 1/5 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/5 个有
- `SaveImage` —— 1/5 个有
- `TTResolutionSelector` —— 1/5 个有
- `easy imageConcat` —— 1/5 个有
- `easy int` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
