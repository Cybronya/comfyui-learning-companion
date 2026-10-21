---
name: unknown_workflow_video_upscale_latent_upscale_46
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.529
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, ImageResizeKJv2, KSamplerSelect, LTX2_NAG, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, PrimitiveBoolean, ResizeImagesByLongerEdge, SamplerCustom, Seed (rgthree), SetNode, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2065192643361067009.json, 视频生成/图生视频/2045329040776634370.json, 视频生成/图生视频/2053738368332251137.json, 视频生成/图生视频/2031341493738283009.json, 视频生成/图生视频/2049497146432425985.json, 视频生成/图生视频/2057291924830248961.json, 视频生成/文生视频/LTX 2.3 文生视频 + 图生视频 （超清）_2031725601656152066.json, 视频生成/文生视频/LTX-2.3+数字人对口型多人对话唱歌+高清画质工作流_2069356013098196994.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_46

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2065192643361067009.json、视频生成/图生视频/2045329040776634370.json、视频生成/图生视频/2053738368332251137.json、视频生成/图生视频/2031341493738283009.json、视频生成/图生视频/2049497146432425985.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：53%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LTX2_NAG`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
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
- `ResizeImagesByLongerEdge`
- `SamplerCustom`
- `Seed (rgthree)`
- `SetNode`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `JDC_ResizeFactor` —— 7/8 个有
- `Fast Groups Bypasser (rgthree)` —— 6/8 个有
- `JoinStrings` —— 6/8 个有
- `LTXVEmptyLatentAudio` —— 6/8 个有
- `ShowText|pysssss` —— 6/8 个有
- `LTX2SamplingPreviewOverride` —— 5/8 个有
- `LTXVAudioVAEDecode` —— 5/8 个有
- `PrimitiveFloat` —— 5/8 个有
- `RH_LLMAPI_NODE` —— 5/8 个有
- `SimpleCalculatorKJ` —— 5/8 个有
- `TextInput_` —— 5/8 个有
- `AudioInfo` —— 4/8 个有
- `LTXVAudioVAEEncode` —— 4/8 个有
- `PreviewAudio` —— 4/8 个有
- `SetLatentNoiseMask` —— 4/8 个有
- `SimpleMath+` —— 4/8 个有
- `SolidMask` —— 4/8 个有
- `AudioCrop` —— 3/8 个有
- `Display Any (rgthree)` —— 3/8 个有
- `LoadAudio` —— 3/8 个有
- `MelBandRoFormerModelLoader` —— 2/8 个有
- `MelBandRoFormerSampler` —— 2/8 个有
- `AnySwitch` —— 1/8 个有
- `CR Text` —— 1/8 个有
- `FL_Audio_Separation` —— 1/8 个有
- `FlashVSRInitPipe` —— 1/8 个有
- `FlashVSRNodeAdv` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `LazySwitchKJ` —— 1/8 个有
- `PlaySound|pysssss` —— 1/8 个有
- `PrimitiveStringMultiline` —— 1/8 个有
- `ResizeImageMaskNode` —— 1/8 个有
- `Text Multiline` —— 1/8 个有
- `VHS_LoadAudioUpload` —— 1/8 个有
- `easy showAnything` —— 1/8 个有
- `llama_cpp_instruct_adv` —— 1/8 个有
- `llama_cpp_model_loader` —— 1/8 个有
- `llama_cpp_parameters` —— 1/8 个有
- `llama_cpp_unload_model` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 121 - 121 | 6 | 100% |
| 高度 | 24 | 24 - 24 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 121 - 121，6 个样本，取值集中（一致性 100%）
- 高度 中位数 24，观测区间 24 - 24，6 个样本，取值集中（一致性 100%）
