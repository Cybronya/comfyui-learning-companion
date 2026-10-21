---
name: unknown_workflow_video_upscale_latent_upscale_10
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.5869
common_nodes: [CFGGuider, CLIPTextEncode, CR Float To Integer, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, GuHaiAutoImageSplit, INTConstant, ImageFromBatch+, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PreviewImage, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleMath+, Text, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2042275360716365825.json, 视频生成/图生视频/2033887666709733377.json, 视频生成/图生视频/2041061447786045441.json, 视频生成/图生视频/2043997002492551169.json, 视频生成/图生视频/2045139851414085634.json, 视频生成/图生视频/2041770093574627329.json, 视频生成/图生视频/2041871035494043650.json, 视频生成/图生视频/2061788937559040002.json, 视频生成/图生视频/2052633200643588097.json, 视频生成/图生视频/2043234701170708482.json, 视频生成/图生视频/2052305027913531394.json, 视频生成/图生视频/2057622181424746497.json, 视频生成/图生视频/2037715284160684033.json, 视频生成/图生视频/2056677088828157954.json, 视频生成/图生视频/2050405484393447425.json, 视频生成/图生视频/2052322749112176642.json, 视频生成/图生视频/2052396635459727361.json, 视频生成/图生视频/2053677704922320898.json, 视频生成/图生视频/2037892741253832706.json, 视频生成/图生视频/2052550289055596546.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_10

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（视频生成/图生视频/2042275360716365825.json、视频生成/图生视频/2033887666709733377.json、视频生成/图生视频/2041061447786045441.json、视频生成/图生视频/2043997002492551169.json、视频生成/图生视频/2045139851414085634.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 20 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CR Float To Integer`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
- `GuHaiAutoImageSplit`
- `INTConstant`
- `ImageFromBatch+`
- `KSamplerSelect`
- `LTXVAddGuideMulti`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `PreviewImage`
- `PrimitiveFloat`
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

**可变部分**（部分 workflow 才有）：
- `RH_LLMAPI_Pro_Node` —— 19/20 个有
- `easy showAnything` —— 19/20 个有
- `ImageResizeKJv2` —— 17/20 个有
- `TTResolutionSelector` —— 17/20 个有
- `RHHiddenNodes` —— 15/20 个有
- `Fast Groups Bypasser (rgthree)` —— 14/20 个有
- `CR Text` —— 11/20 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 11/20 个有
- `SaveImage` —— 11/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/20 个有
- `ImpactSwitch` —— 2/20 个有
- `Int` —— 2/20 个有
- `LTXICLoRALoaderModelOnly` —— 2/20 个有
- `PromptRelayEncodeTimeline` —— 2/20 个有
- `CRT_UpscaleModelAdv` —— 1/20 个有
- `GetObjectFromJson` —— 1/20 个有
- `GetTextFromJson` —— 1/20 个有
- `ImageConcanate` —— 1/20 个有
- `LTXVAudioVAEEncode` —— 1/20 个有
- `Light-Tool: DeserializeJsonString` —— 1/20 个有
- `LoadAudio` —— 1/20 个有
- `LoraLoaderModelOnly` —— 1/20 个有
- `PromptRelayEncode` —— 1/20 个有
- `SaveVideoNode` —— 1/20 个有
- `SetLatentNoiseMask` —— 1/20 个有
- `SolidMask` —— 1/20 个有
- `TwoWaySwitch` —— 1/20 个有
- `Wan22ImageToVideoLatent` —— 1/20 个有
- `easy indexAnything` —— 1/20 个有
- `孤海-图像添加水印` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 20 | 100% |
| 高度 | 25 | 25 - 25 | 20 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，20 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，20 个样本，取值集中（一致性 100%）
