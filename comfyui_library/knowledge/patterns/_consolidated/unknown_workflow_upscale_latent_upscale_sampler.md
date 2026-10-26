---
name: unknown_workflow_upscale_latent_upscale_sampler
type: Unknown Workflow
frequency: 20
level: strong
coverage: 0.57785
common_nodes: [CFGGuider, CLIPTextEncode, CR Float To Integer, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, GuHaiAutoImageSplit, INTConstant, ImageFromBatch+, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PreviewImage, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SetNode, SimpleMath+, Text, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, easy cleanGpuUsed, easy showAnything]
problems: []
missing: []
members: [图片生成/反推提示词/102 四宫格-LTX-2.3 图生视频（全面优化版）_2058401889703784449.json, 图片生成/图生图/四宫格-LTX-2.3 图生视频（全面优化版）_2039716029768671234.json, 视频生成/图生视频/AI-短剧-四宫格-LTX-2.3_2042275360716365825.json, 视频生成/图生视频/AI代码侠土豆-LTX-2.3 漫剧视频（四宫格V2.0-单采光速版）_2033887666709733377.json, 视频生成/图生视频/AI漫剧-四宫格-LTX-2.3 图生视频（全面优化版）_2041061447786045441.json, 视频生成/图生视频/Cosmic-RaysX-LTX-2.3 四宫格UGC电商视频生成_2043997002492551169.json, 视频生成/图生视频/LTX-2.3 多分镜镜头参考图生视频 全面优化版_2045139851414085634.json, 视频生成/图生视频/LTX-2.3 漫剧视频V2.0（四宫格-单采极速版）_2041770093574627329.json, 视频生成/图生视频/LTX-2.3 漫剧视频（四宫格V2.0-单采光速版）_2041871035494043650.json, 视频生成/图生视频/一键短视频 分镜控制  提示词优化 时间线控制 Ltx2.3  PromptRelay + 丝滑转场_2052633200643588097.json, 视频生成/图生视频/四宫格-LTX-2.3 图生视频 自用_2043234701170708482.json, 视频生成/图生视频/四宫格-LTX-2.3 图生视频不够清晰_2052305027913531394.json, 视频生成/图生视频/四宫格-LTX-2.3 图生视频（全面优_2057622181424746497.json, 视频生成/图生视频/四宫格-LTX-2.3 图生视频（全面优化版）_2037715284160684033.json, 视频生成/图生视频/四宫格-LTX-2.3 图生视频（全面优化版）_2056677088828157954.json, 视频生成/图生视频/图生视频一号_2052322749112176642.json, 视频生成/图生视频/图生视频一号_2052396635459727361.json, 视频生成/图生视频/图生视频一号_2053677704922320898.json, 视频生成/图生视频/自用_2044445591786233858.json, 视频生成/文生视频/LTX-2.3+漫剧视频生成 四宫格情景剧本极速版_2064519449834770434.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/反推提示词/102 四宫格-LTX-2.3 图生视频（全面优化版）_2058401889703784449.json、图片生成/图生图/四宫格-LTX-2.3 图生视频（全面优化版）_2039716029768671234.json、视频生成/图生视频/AI-短剧-四宫格-LTX-2.3_2042275360716365825.json、视频生成/图生视频/AI代码侠土豆-LTX-2.3 漫剧视频（四宫格V2.0-单采光速版）_2033887666709733377.json、视频生成/图生视频/AI漫剧-四宫格-LTX-2.3 图生视频（全面优化版）_2041061447786045441.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：强结论
- **平均知识覆盖**：58%

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
- `easy cleanGpuUsed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 19/20 个有
- `TTResolutionSelector` —— 19/20 个有
- `VHS_VideoCombine` —— 19/20 个有
- `RHHiddenNodes` —— 18/20 个有
- `RH_LLMAPI_Pro_Node` —— 18/20 个有
- `Fast Groups Bypasser (rgthree)` —— 15/20 个有
- `CR Text` —— 11/20 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 11/20 个有
- `SaveImage` —— 11/20 个有
- `CRT_UpscaleModelAdv` —— 1/20 个有
- `CreateVideo` —— 1/20 个有
- `ImageConcanate` —— 1/20 个有
- `ImpactSwitch` —— 1/20 个有
- `Int` —— 1/20 个有
- `LTXICLoRALoaderModelOnly` —— 1/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/20 个有
- `PromptRelayEncodeTimeline` —— 1/20 个有
- `RH_LLMAPI_NODE` —— 1/20 个有
- `RTXVideoSuperResolution` —— 1/20 个有
- `SaveVideo` —— 1/20 个有
- `Wan22ImageToVideoLatent` —— 1/20 个有
- `llama_cpp_instruct_adv` —— 1/20 个有
- `llama_cpp_model_loader` —— 1/20 个有
- `llama_cpp_parameters` —— 1/20 个有
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
