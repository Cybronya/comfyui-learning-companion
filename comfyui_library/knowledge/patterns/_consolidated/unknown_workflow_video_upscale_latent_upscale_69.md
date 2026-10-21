---
name: unknown_workflow_video_upscale_latent_upscale_69
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.472167
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, ImageResizeKJv2, JDC_ResizeFactor, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveFloat, ResizeImagesByLongerEdge, SamplerCustom, Seed (rgthree), SetNode, SimpleCalculatorKJ, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/LTX 2.3 文生视频工作流_2065135919526662145.json, 视频生成/文生视频/LTX2.3+文生视频+图生视频(二合一工作流)_2059048742673805313.json, 视频生成/文生视频/文生视频 + 图生视频 二合一工作流_2099902577730220034.json, 视频生成/文生视频/文生视频 + 图生视频 二合一工作流_2100620352736022529.json, 视频生成/文生视频/文生视频_+_图生视频_二合一工作流_2100755479424233473.json, 视频生成/文生视频/文生视频_+_图生视频_二合一工作流_2101124003149733889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_69

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/LTX 2.3 文生视频工作流_2065135919526662145.json、视频生成/文生视频/LTX2.3+文生视频+图生视频(二合一工作流)_2059048742673805313.json、视频生成/文生视频/文生视频 + 图生视频 二合一工作流_2099902577730220034.json、视频生成/文生视频/文生视频 + 图生视频 二合一工作流_2100620352736022529.json、视频生成/文生视频/文生视频_+_图生视频_二合一工作流_2100755479424233473.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：47%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `EmptyLTXVLatentVideo`
- `GetImageSize`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `JDC_ResizeFactor`
- `KSamplerSelect`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
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
- `Fast Groups Bypasser (rgthree)` —— 5/6 个有
- `JoinStrings` —— 5/6 个有
- `RH_LLMAPI_NODE` —— 5/6 个有
- `ShowText|pysssss` —— 5/6 个有
- `TextInput_` —— 5/6 个有
- `Label (rgthree)` —— 2/6 个有
- `AnySwitch` —— 1/6 个有
- `CR Text` —— 1/6 个有
- `FlashVSRInitPipe` —— 1/6 个有
- `FlashVSRNodeAdv` —— 1/6 个有
- `PlaySound|pysssss` —— 1/6 个有
- `easy showAnything` —— 1/6 个有

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
