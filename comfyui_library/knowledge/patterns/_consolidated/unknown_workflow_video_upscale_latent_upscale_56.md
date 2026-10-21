---
name: unknown_workflow_video_upscale_latent_upscale_56
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.585
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GuHaiAutoImageSplit, INTConstant, ImageFromBatch+, ImageResizeKJv2, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PreviewImage, PrimitiveFloat, RH_LLMAPI_Pro_Node, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2045413538109329409.json, 视频生成/图生视频/2070309380381298690.json, 视频生成/图生视频/2052328089341964289.json, 视频生成/图生视频/2044445591786233858.json, 视频生成/文生视频/LTX-2.3+漫剧视频生成 四宫格情景剧本极速版_2064519449834770434.json, 视频生成/文生视频/LTX2.3_四宫格漫剧视频_2064675254458474498.json, 视频生成/文生视频/最强漫剧生成LTX-2.3（四宫格V2.0-单采光速版）_2041148096977047554.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_56

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2045413538109329409.json、视频生成/图生视频/2070309380381298690.json、视频生成/图生视频/2052328089341964289.json、视频生成/图生视频/2044445591786233858.json、视频生成/文生视频/LTX-2.3+漫剧视频生成 四宫格情景剧本极速版_2064519449834770434.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：59%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GuHaiAutoImageSplit`
- `INTConstant`
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
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `PreviewImage`
- `PrimitiveFloat`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 6/7 个有
- `SetNode` —— 6/7 个有
- `CR Float To Integer` —— 4/7 个有
- `SimpleMath+` —— 4/7 个有
- `TTResolutionSelector` —— 4/7 个有
- `Text` —— 4/7 个有
- `VAELoader` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `CM_FloatToInt` —— 3/7 个有
- `Label (rgthree)` —— 3/7 个有
- `LoadAudio` —— 3/7 个有
- `LoadVideo` —— 3/7 个有
- `LoraLoaderModelOnly` —— 3/7 个有
- `PrimitiveStringMultiline` —— 3/7 个有
- `RHHiddenNodes` —— 3/7 个有
- `RecordAudio` —— 3/7 个有
- `ShowText|pysssss` —— 3/7 个有
- `SimpleCalculatorKJ` —— 3/7 个有
- `llama_cpp_instruct_adv` —— 3/7 个有
- `llama_cpp_model_loader` —— 3/7 个有
- `llama_cpp_parameters` —— 3/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 24 - 25 | 7 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，7 个样本，取值集中（一致性 98%）
