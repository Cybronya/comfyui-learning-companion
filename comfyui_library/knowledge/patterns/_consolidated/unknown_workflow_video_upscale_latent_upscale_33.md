---
name: unknown_workflow_video_upscale_latent_upscale_33
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.471273
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, ImageResizeKJv2, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveFloat, ResizeImagesByLongerEdge, SamplerCustom, Seed (rgthree), SetNode, SimpleCalculatorKJ, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX 2.3 图生视频工作流_2065192643361067009.json, 视频生成/图生视频/LTX 2.3_2045329040776634370.json, 视频生成/图生视频/LTX2.3+文生视频+图生视频(二合一工作流)_2031341493738283009.json, 视频生成/图生视频/ltx2.3数字人_2049497146432425985.json, 视频生成/文生视频/LTX 2.3 文生视频 + 图生视频 （超清）_2031725601656152066.json, 视频生成/文生视频/LTX 2.3 文生视频工作流_2065135919526662145.json, 视频生成/文生视频/LTX2.3+文生视频+图生视频(二合一工作流)_2059048742673805313.json, 视频生成/文生视频/文生视频 + 图生视频 二合一工作流_2099902577730220034.json, 视频生成/文生视频/文生视频 + 图生视频 二合一工作流_2100620352736022529.json, 视频生成/文生视频/文生视频_+_图生视频_二合一工作流_2100755479424233473.json, 视频生成/文生视频/文生视频_+_图生视频_二合一工作流_2101124003149733889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_33

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/LTX 2.3 图生视频工作流_2065192643361067009.json、视频生成/图生视频/LTX 2.3_2045329040776634370.json、视频生成/图生视频/LTX2.3+文生视频+图生视频(二合一工作流)_2031341493738283009.json、视频生成/图生视频/ltx2.3数字人_2049497146432425985.json、视频生成/文生视频/LTX 2.3 文生视频 + 图生视频 （超清）_2031725601656152066.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：47%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVScheduler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `ResizeImagesByLongerEdge`
- `SamplerCustom`
- `Seed (rgthree)`
- `SetNode`
- `SimpleCalculatorKJ`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `JDC_ResizeFactor` —— 10/11 个有
- `LTXVAudioVAEDecode` —— 10/11 个有
- `Fast Groups Bypasser (rgthree)` —— 9/11 个有
- `JoinStrings` —— 9/11 个有
- `ShowText|pysssss` —— 9/11 个有
- `RH_LLMAPI_NODE` —— 8/11 个有
- `TextInput_` —— 8/11 个有
- `Label (rgthree)` —— 3/11 个有
- `AnySwitch` —— 2/11 个有
- `CR Text` —— 2/11 个有
- `FlashVSRInitPipe` —— 2/11 个有
- `FlashVSRNodeAdv` —— 2/11 个有
- `PlaySound|pysssss` —— 2/11 个有
- `easy showAnything` —— 2/11 个有
- `AudioInfo` —— 1/11 个有
- `FL_Audio_Separation` —— 1/11 个有
- `LTXVAudioVAEEncode` —— 1/11 个有
- `LazySwitchKJ` —— 1/11 个有
- `PreviewAudio` —— 1/11 个有
- `PrimitiveStringMultiline` —— 1/11 个有
- `ResizeImageMaskNode` —— 1/11 个有
- `SetLatentNoiseMask` —— 1/11 个有
- `SimpleMath+` —— 1/11 个有
- `SolidMask` —— 1/11 个有
- `Text Multiline` —— 1/11 个有
- `VHS_LoadAudioUpload` —— 1/11 个有
- `llama_cpp_instruct_adv` —— 1/11 个有
- `llama_cpp_model_loader` —— 1/11 个有
- `llama_cpp_parameters` —— 1/11 个有
- `llama_cpp_unload_model` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 11 | 100% |
| 高度 | 24 | 24 - 24 | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，11 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，11 个样本，取值集中（一致性 100%）
