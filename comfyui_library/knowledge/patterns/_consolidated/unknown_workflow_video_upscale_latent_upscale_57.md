---
name: unknown_workflow_video_upscale_latent_upscale_57
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.576571
common_nodes: [CFGGuider, CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, Fast Groups Bypasser (rgthree), GetNode, ImageScaleBy, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveImage, SetNode, ShowText|pysssss, UNETLoader, VAELoaderKJ, VHS_VideoCombine, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [视频生成/图生视频/2075059054535335938.json, 视频生成/图生视频/2075058166324355073.json, 视频生成/图生视频/2079969756626636802.json, 视频生成/图生视频/2080319460522680321.json, 视频生成/图生视频/2080675157340934145.json, 视频生成/文生视频/LTX2.3 Dasiwa Vdieo Gen 大丝袜 ltx2.3视频生成_2075063498681442305.json, 视频生成/文生视频/LTX2.3 TI2V 图文生视频（超速版6分钟十秒视频）_2075070146934304769.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_57

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/2075059054535335938.json、视频生成/图生视频/2075058166324355073.json、视频生成/图生视频/2079969756626636802.json、视频生成/图生视频/2080319460522680321.json、视频生成/图生视频/2080675157340934145.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImageScaleBy`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `ShowText|pysssss`
- `UNETLoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 6/7 个有
- `LTXVCropGuides` —— 6/7 个有
- `LTXVImgToVideoInplace` —— 6/7 个有
- `LTXVPreprocess` —— 6/7 个有
- `SimpleMath+` —— 6/7 个有
- `VAEDecode` —— 6/7 个有
- `GetImageSize` —— 5/7 个有
- `INTConstant` —— 5/7 个有
- `PrimitiveBoolean` —— 5/7 个有
- `PrimitiveFloat` —— 5/7 个有
- `PrimitiveInt` —— 5/7 个有
- `SimpleCalculatorKJ` —— 5/7 个有
- `VAELoader` —— 5/7 个有
- `easy cleanGpuUsed` —— 5/7 个有
- `BasicScheduler` —— 4/7 个有
- `ModelSamplingSD3` —— 4/7 个有
- `Label (rgthree)` —— 2/7 个有
- `LoraLoaderModelOnly` —— 2/7 个有
- `ResizeImagesByLongerEdge` —— 2/7 个有
- `easy imageSize` —— 2/7 个有
- `easy int` —— 2/7 个有
- `CS-MultiImageLoader` —— 1/7 个有
- `LTXSequencer` —— 1/7 个有
- `LTXVScheduler` —— 1/7 个有
- `VAEDecodeTiled` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 361 | 7 | 33% |
| 高度 | 24 | 24 - 24 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 361，7 个样本，取值分散，一致性仅 33%
- 高度 中位数 24，观测区间 24 - 24，7 个样本，取值集中（一致性 100%）
