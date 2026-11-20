---
name: unknown_workflow_upscale_latent_upscale_lora_32
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.7034
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, CreateVideo, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo, ShowText|pysssss, TextInput_, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ]
problems: []
missing: []
members: [数字人/数字人/LTX 2.3  数字人对口型优化加速版_2048205996044062721.json, 视频生成/图生视频/LTX 2.3  数字人对口型优化加速版+全节点注释-最新版_2045851201853464578.json, 视频生成/图生视频/LTX 2.3  数字人对口型优化加速版+全节点注释_2042456955284889601.json, 视频生成/图生视频/LTX+2.3 +数字人对口型优化加速版+全节点注释-API改自动_2045890888169164802.json, 视频生成/图生视频/LTX+2.3 +数字人对口型优化加速版_2050462775322923010.json, 视频生成/图生视频/NB➕LTX 2.3_2043280274267574273.json, 视频生成/文生视频/LTX 2.3  图生视频+ 文生视频 二合一工作流_2034848874736656385.json, 视频生成/文生视频/LTX 2.3  数字人对口型优化加速版_2035972657669214210.json, 视频生成/文生视频/LTX 2.3  数字人对口型优化加速版_2050177856264785921.json, 视频生成/文生视频/图生视频，上传图像＋音频，即可做出你想要的短视频，短剧，_2043763255142785026.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_32

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（数字人/数字人/LTX 2.3  数字人对口型优化加速版_2048205996044062721.json、视频生成/图生视频/LTX 2.3  数字人对口型优化加速版+全节点注释-最新版_2045851201853464578.json、视频生成/图生视频/LTX 2.3  数字人对口型优化加速版+全节点注释_2042456955284889601.json、视频生成/图生视频/LTX+2.3 +数字人对口型优化加速版+全节点注释-API改自动_2045890888169164802.json、视频生成/图生视频/LTX+2.3 +数字人对口型优化加速版_2050462775322923010.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXVAudioVAEDecode`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `ShowText|pysssss`
- `TextInput_`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `AudioCrop` —— 8/10 个有
- `AudioInfo` —— 8/10 个有
- `Display Any (rgthree)` —— 8/10 个有
- `LTXVAudioVAEEncode` —— 8/10 个有
- `LoadAudio` —— 8/10 个有
- `PrimitiveFloat` —— 8/10 个有
- `SetLatentNoiseMask` —— 8/10 个有
- `SimpleMath+` —— 8/10 个有
- `SolidMask` —— 8/10 个有
- `TrimAudioDuration` —— 8/10 个有
- `RH_LLMAPI_NODE` —— 7/10 个有
- `Fast Groups Bypasser (rgthree)` —— 6/10 个有
- `JoinStrings` —— 6/10 个有
- `SimpleCalculatorKJ` —— 6/10 个有
- `llama_cpp_instruct_adv` —— 6/10 个有
- `llama_cpp_model_loader` —— 6/10 个有
- `llama_cpp_parameters` —— 6/10 个有
- `llama_cpp_unload_model` —— 6/10 个有
- `CR Text` —— 5/10 个有
- `Label (rgthree)` —— 5/10 个有
- `MelBandRoFormerModelLoader` —— 4/10 个有
- `MelBandRoFormerSampler` —— 4/10 个有
- `PreviewAny` —— 4/10 个有
- `PreviewAudio` —— 4/10 个有
- `INTConstant` —— 2/10 个有
- `LTX2_NAG` —— 2/10 个有
- `LTXVEmptyLatentAudio` —— 2/10 个有
- `LayerUtility: PurgeVRAM V2` —— 2/10 个有
- `RH_LLMAPI_Pro_Node` —— 2/10 个有
- `Bjornulf_LoopBasicBatch` —— 1/10 个有
- `MinNode` —— 1/10 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/10 个有
- `SaveImage` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | - | 2 | 100% |
| 高度 | 25 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
