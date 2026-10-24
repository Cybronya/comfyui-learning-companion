---
name: unknown_workflow_upscale_latent_upscale_sampler_15
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.878833
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/Dasiwa V2 ltx2.3 I2V_2058155153185918978.json, 视频生成/图生视频/ITX2.3--首尾帧_2032004087528562690.json, 视频生成/图生视频/LTX-2.3  5图高清参考工作流V1.0_2038717836129996802.json, 视频生成/图生视频/LTX2-3-文生-图生视频（极大概率去台词，强一致性修订版V4）_2030557129664372738.json, 视频生成/图生视频/NB➕LTX 2.3_2043280274267574273.json, 视频生成/文生视频/LTX 2.3  图生视频+ 文生视频 二合一工作流_2034848874736656385.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_15

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Dasiwa V2 ltx2.3 I2V_2058155153185918978.json、视频生成/图生视频/ITX2.3--首尾帧_2032004087528562690.json、视频生成/图生视频/LTX-2.3  5图高清参考工作流V1.0_2038717836129996802.json、视频生成/图生视频/LTX2-3-文生-图生视频（极大概率去台词，强一致性修订版V4）_2030557129664372738.json、视频生成/图生视频/NB➕LTX 2.3_2043280274267574273.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
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
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `ResizeImageMaskNode` —— 5/6 个有
- `CreateVideo` —— 4/6 个有
- `LTX2_NAG` —— 4/6 个有
- `LTXVChunkFeedForward` —— 4/6 个有
- `PathchSageAttentionKJ` —— 4/6 个有
- `SaveVideo` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `INTConstant` —— 3/6 个有
- `LoraLoaderModelOnly` —— 3/6 个有
- `ShowText|pysssss` —— 3/6 个有
- `llama_cpp_instruct_adv` —— 3/6 个有
- `llama_cpp_model_loader` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `ImageResizeKJv2` —— 2/6 个有
- `JoinStrings` —— 2/6 个有
- `LTXVImgToVideoInplaceKJ` —— 2/6 个有
- `LayerUtility: PurgeVRAM V2` —— 2/6 个有
- `ModelPatchTorchSettings` —— 2/6 个有
- `SimpleCalculatorKJ` —— 2/6 个有
- `TextInput_` —— 2/6 个有
- `VAELoader` —— 2/6 个有
- `VHS_VideoCombine` —— 2/6 个有
- `llama_cpp_parameters` —— 2/6 个有
- `llama_cpp_unload_model` —— 2/6 个有
- `Bjornulf_LoopBasicBatch` —— 1/6 个有
- `EmptyImage` —— 1/6 个有
- `LTXVScheduler` —— 1/6 个有
- `Label (rgthree)` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `MinNode` —— 1/6 个有
- `PreviewAny` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有
- `RH_LLMAPI_Pro_Node` —— 1/6 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `Text` —— 1/6 个有
- `Text Concatenate` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `easy ifElse` —— 1/6 个有
- `easy mathString` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 25 - 44 | 6 | 75% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 44，6 个样本
