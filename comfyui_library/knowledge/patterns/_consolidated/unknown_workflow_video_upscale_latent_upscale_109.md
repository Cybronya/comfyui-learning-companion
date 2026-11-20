---
name: unknown_workflow_video_upscale_latent_upscale_109
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.492
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, DualCLIPLoader, EmptyLTXVLatentVideo, GetNode, GuHaiAutoImageSplit, INTConstant, ImageFromBatch+, ImageResizeKJv2, KSamplerSelect, LTXVAddGuideMulti, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVSeparateAVLatent, Label (rgthree), LatentUpscaleModelLoader, LoadAudio, LoadImage, LoadVideo, LoraLoaderModelOnly, ManualSigmas, PreviewImage, PrimitiveFloat, PrimitiveStringMultiline, RH_LLMAPI_Pro_Node, RandomNoise, RecordAudio, SamplerCustomAdvanced, SetNode, ShowText|pysssss, SimpleCalculatorKJ, UNETLoader, VAEDecodeTiled, VAELoaderKJ, VHS_VideoCombine, easy cleanGpuUsed, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/LTX2.3 四宫格短剧_2045413538109329409.json, 视频生成/图生视频/aidir-LTX2.3 四宫格生视频_2070309380381298690.json, 视频生成/图生视频/图生视频二号_2052328089341964289.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_109

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/LTX2.3 四宫格短剧_2045413538109329409.json、视频生成/图生视频/aidir-LTX2.3 四宫格生视频_2070309380381298690.json、视频生成/图生视频/图生视频二号_2052328089341964289.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：49%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetNode`
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
- `Label (rgthree)`
- `LatentUpscaleModelLoader`
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PreviewImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_Pro_Node`
- `RandomNoise`
- `RecordAudio`
- `SamplerCustomAdvanced`
- `SetNode`
- `ShowText|pysssss`
- `SimpleCalculatorKJ`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 3 | 100% |
| 高度 | 24 | 24 - 24 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，3 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，3 个样本，取值集中（一致性 100%）
