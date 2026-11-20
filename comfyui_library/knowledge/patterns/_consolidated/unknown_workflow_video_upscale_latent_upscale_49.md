---
name: unknown_workflow_video_upscale_latent_upscale_49
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.5095
common_nodes: [CLIPTextEncode, DualCLIPLoader, EmptyLTXVLatentVideo, GetImageSize, GetNode, INTConstant, ImageResizeKJv2, KSamplerSelect, LTX2SamplingPreviewOverride, LTX2_NAG, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVScheduler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveFloat, ResizeImagesByLongerEdge, Seed (rgthree), SetNode, SimpleCalculatorKJ, UNETLoader, VAEDecodeTiled, VAELoader, VAELoaderKJ, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/LTX 2.3 图生视频工作流_2065192643361067009.json, 视频生成/图生视频/LTX 2.3_2045329040776634370.json, 视频生成/图生视频/LTX2.3 快速蒸馏版（自动提示词）_2044570790150017026.json, 视频生成/图生视频/LTX2.3+文生视频+图生视频(二合一工作流)_2031341493738283009.json, 视频生成/图生视频/【阿良绘】LTx首尾帧 _ 丝滑过渡版（高速）_2040980266277146625.json, 视频生成/图生视频/【阿良绘】LTx首尾帧 _ 丝滑过渡版（高速）_2046788191067312129.json, 视频生成/文生视频/LTX 2.3 文生视频 + 图生视频 （超清）_2031725601656152066.json, 视频生成/文生视频/LTX2.3+文生视频+图生视频(二合一工作流)_2059048742673805313.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_49

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/LTX 2.3 图生视频工作流_2065192643361067009.json、视频生成/图生视频/LTX 2.3_2045329040776634370.json、视频生成/图生视频/LTX2.3 快速蒸馏版（自动提示词）_2044570790150017026.json、视频生成/图生视频/LTX2.3+文生视频+图生视频(二合一工作流)_2031341493738283009.json、视频生成/图生视频/【阿良绘】LTx首尾帧 _ 丝滑过渡版（高速）_2040980266277146625.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：51%

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
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `LTXVAudioVAEDecode`
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
- `PrimitiveFloat`
- `ResizeImagesByLongerEdge`
- `Seed (rgthree)`
- `SetNode`
- `SimpleCalculatorKJ`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VAELoaderKJ`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `JDC_ResizeFactor` —— 5/8 个有
- `LTXVChunkFeedForward` —— 5/8 个有
- `PathchSageAttentionKJ` —— 5/8 个有
- `PrimitiveBoolean` —— 5/8 个有
- `SamplerCustom` —— 5/8 个有
- `CR Text` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 4/8 个有
- `JoinStrings` —— 4/8 个有
- `RH_LLMAPI_NODE` —— 4/8 个有
- `ShowText|pysssss` —— 4/8 个有
- `TextInput_` —— 4/8 个有
- `easy showAnything` —— 4/8 个有
- `CFGGuider` —— 3/8 个有
- `ImageScaleBy` —— 3/8 个有
- `RandomNoise` —— 3/8 个有
- `SamplerCustomAdvanced` —— 3/8 个有
- `AnySwitch` —— 2/8 个有
- `LTXVImgToVideoInplaceKJ` —— 2/8 个有
- `PlaySound|pysssss` —— 2/8 个有
- `RunningHub SeedXPro Translator` —— 2/8 个有
- `easy promptConcat` —— 2/8 个有
- `CR Prompt Text` —— 1/8 个有
- `ConcatTextOfUtils` —— 1/8 个有
- `FlashVSRInitPipe` —— 1/8 个有
- `FlashVSRNodeAdv` —— 1/8 个有
- `LTXVImgToVideoConditionOnly` —— 1/8 个有
- `Label (rgthree)` —— 1/8 个有
- `RH_LLMAPI_Pro_Node` —— 1/8 个有
- `Text Multiline` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 121 | 97 - 121 | 8 | 90% |
| 高度 | 24 | 24 - 25 | 8 | 98% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 121，观测区间 97 - 121，8 个样本，取值集中（一致性 90%）
- 高度 中位数 24，观测区间 24 - 25，8 个样本，取值集中（一致性 98%）
