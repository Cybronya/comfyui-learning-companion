---
name: unknown_workflow_upscale_latent_upscale_sampler_9
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.6029
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/2058155153185918978.json, 视频生成/图生视频/2038717836129996802.json, 视频生成/图生视频/2030557129664372738.json, 视频生成/图生视频/2035556614480076801.json, 视频生成/图生视频/2035556594234167298.json, 视频生成/图生视频/2037924833685671937.json, 视频生成/文生视频/LTX2.3 单图&文生视频_2035556553025134594.json, 视频生成/文生视频/LTX2.3 生长视频版-18秒视频16分钟生成-单图&文生视频-加强版_2035746141073051650.json, 视频生成/文生视频/LTX2.3 生长视频版-30秒视频8分半钟生成-首尾帧双图&文生视频-加强版_2035952445355986945.json, 视频生成/文生视频/LTX2.3 生长视频版-50秒视频15分钟生成-首中尾帧三图&文生视频-加强版_2036052171002748929.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_9

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2058155153185918978.json、视频生成/图生视频/2038717836129996802.json、视频生成/图生视频/2030557129664372738.json、视频生成/图生视频/2035556614480076801.json、视频生成/图生视频/2035556594234167298.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：60%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `LTX2_NAG` —— 9/10 个有
- `LTXVChunkFeedForward` —— 9/10 个有
- `ModelPatchTorchSettings` —— 9/10 个有
- `PathchSageAttentionKJ` —— 9/10 个有
- `PrimitiveBoolean` —— 9/10 个有
- `UNETLoader` —— 9/10 个有
- `VHS_VideoCombine` —— 9/10 个有
- `easy cleanGpuUsed` —— 8/10 个有
- `Anything Everywhere` —— 7/10 个有
- `CR Text` —— 7/10 个有
- `GetNode` —— 7/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/10 个有
- `MathExpression|pysssss` —— 7/10 个有
- `SetNode` —— 7/10 个有
- `ShowText|pysssss` —— 7/10 个有
- `LTXVImgToVideoInplaceKJ` —— 6/10 个有
- `llama_cpp_instruct_adv` —— 5/10 个有
- `llama_cpp_model_loader` —— 5/10 个有
- `PrimitiveStringMultiline` —— 3/10 个有
- `RH_LLMAPI_Pro_Node` —— 3/10 个有
- `ResizeImagesByLongerEdge` —— 3/10 个有
- `WujiCleaner` —— 3/10 个有
- `ResizeImageMaskNode` —— 2/10 个有
- `easy imageConcat` —— 2/10 个有
- `CreateVideo` —— 1/10 个有
- `EmptyImage` —— 1/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `INTConstant` —— 1/10 个有
- `ImageResizeKJv2` —— 1/10 个有
- `LTXVScheduler` —— 1/10 个有
- `LayerUtility: PurgeVRAM` —— 1/10 个有
- `LoraLoaderModelOnly` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `SaveVideo` —— 1/10 个有
- `Text Concatenate` —— 1/10 个有
- `UnetLoaderGGUF` —— 1/10 个有
- `VRAMReserver` —— 1/10 个有
- `easy ifElse` —— 1/10 个有
- `easy mathString` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 25 - 44 | 10 | 79% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 44，10 个样本
