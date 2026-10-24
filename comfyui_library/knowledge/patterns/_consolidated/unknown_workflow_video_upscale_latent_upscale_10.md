---
name: unknown_workflow_video_upscale_latent_upscale_10
type: Unknown Workflow
frequency: 21
level: strong
coverage: 0.584143
common_nodes: [CFGGuider, CLIPTextEncode, CR Float To Integer, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, GuHaiAutoImageSplit, INTConstant, ImageFromBatch+, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PreviewImage, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleMath+, Text, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/四宫格-LTX-2.3 图生视频（全面优化版）_2039716029768671234.json, 视频生成/图生视频/AI-短剧-四宫格-LTX-2.3_2042275360716365825.json, 视频生成/图生视频/AI代码侠土豆-LTX-2.3 漫剧视频（四宫格V2.0-单采光速版）_2033887666709733377.json, 视频生成/图生视频/AI漫剧-四宫格-LTX-2.3 图生视频（全面优化版）_2041061447786045441.json, 视频生成/图生视频/Cosmic-RaysX-LTX-2.3 四宫格UGC电商视频生成_2043997002492551169.json, 视频生成/图生视频/LTX-2.3 多分镜镜头参考图生视频 全面优化版_2045139851414085634.json, 视频生成/图生视频/LTX-2.3 漫剧视频V2.0（四宫格-单采极速版）_2041770093574627329.json, 视频生成/图生视频/LTX-2.3 漫剧视频（四宫格V2.0-单采光速版）_2041871035494043650.json, 视频生成/图生视频/ltx单视频_2061788937559040002.json, 视频生成/图生视频/四宫格-LTX-2.3 图生视频 自用_2043234701170708482.json, 视频生成/图生视频/四宫格-LTX-2.3 图生视频不够清晰_2052305027913531394.json, 视频生成/图生视频/四宫格-LTX-2.3 图生视频（全面优_2057622181424746497.json, 视频生成/图生视频/四宫格-LTX-2.3 图生视频（全面优化版）_2037715284160684033.json, 视频生成/图生视频/四宫格-LTX-2.3 图生视频（全面优化版）_2056677088828157954.json, 视频生成/图生视频/四宫格_2050405484393447425.json, 视频生成/图生视频/图生视频一号_2052322749112176642.json, 视频生成/图生视频/图生视频一号_2052396635459727361.json, 视频生成/图生视频/图生视频一号_2053677704922320898.json, 视频生成/图生视频/小Seedance， 连环画视频，短视频 Ltx2.3 自带音效_2037892741253832706.json, 视频生成/图生视频/自用_2044445591786233858.json, 视频生成/文生视频/LTX-2.3+漫剧视频生成 四宫格情景剧本极速版_2064519449834770434.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_10

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（图片生成/图生图/四宫格-LTX-2.3 图生视频（全面优化版）_2039716029768671234.json、视频生成/图生视频/AI-短剧-四宫格-LTX-2.3_2042275360716365825.json、视频生成/图生视频/AI代码侠土豆-LTX-2.3 漫剧视频（四宫格V2.0-单采光速版）_2033887666709733377.json、视频生成/图生视频/AI漫剧-四宫格-LTX-2.3 图生视频（全面优化版）_2041061447786045441.json、视频生成/图生视频/Cosmic-RaysX-LTX-2.3 四宫格UGC电商视频生成_2043997002492551169.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：强结论
- **平均知识覆盖**：58%

## 共有节点

全部 21 个 workflow 都包含：
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
- `ImageResizeKJv2` —— 20/21 个有
- `TTResolutionSelector` —— 20/21 个有
- `easy showAnything` —— 20/21 个有
- `RH_LLMAPI_Pro_Node` —— 19/21 个有
- `RHHiddenNodes` —— 18/21 个有
- `Fast Groups Bypasser (rgthree)` —— 13/21 个有
- `CR Text` —— 11/21 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 11/21 个有
- `SaveImage` —— 11/21 个有
- `CRT_UpscaleModelAdv` —— 1/21 个有
- `GetObjectFromJson` —— 1/21 个有
- `GetTextFromJson` —— 1/21 个有
- `ImageConcanate` —— 1/21 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/21 个有
- `Light-Tool: DeserializeJsonString` —— 1/21 个有
- `LoraLoaderModelOnly` —— 1/21 个有
- `PromptRelayEncode` —— 1/21 个有
- `SaveVideoNode` —— 1/21 个有
- `TwoWaySwitch` —— 1/21 个有
- `Wan22ImageToVideoLatent` —— 1/21 个有
- `easy indexAnything` —— 1/21 个有
- `llama_cpp_instruct_adv` —— 1/21 个有
- `llama_cpp_model_loader` —— 1/21 个有
- `llama_cpp_parameters` —— 1/21 个有
- `孤海-图像添加水印` —— 1/21 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 21 | 100% |
| 高度 | 25 | 25 - 25 | 21 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，21 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，21 个样本，取值集中（一致性 100%）
