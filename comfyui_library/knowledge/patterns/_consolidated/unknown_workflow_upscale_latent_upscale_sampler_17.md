---
name: unknown_workflow_upscale_latent_upscale_sampler_17
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8636
common_nodes: [CFGGuider, CLIPTextEncode, ComfyMathExpression, DualCLIPLoader, EmptyLTXVLatentVideo, KSamplerSelect, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImageMaskNode, ResizeImagesByLongerEdge, SamplerCustomAdvanced, UNETLoader, VAEDecodeTiled, VAELoaderKJ]
problems: []
missing: []
members: [视频生成/图生视频/aidir-LTX 2.3  首中尾三图+多图_2069594232695902209.json, 视频生成/图生视频/最新LTX2.3 1.1模型 _ 三图-首中尾帧 极速版_2048705684543381506.json, 视频生成/文生视频/LTX 2.3  首中尾三图+多图_2035272794954539010.json, 视频生成/文生视频/LTX2.3 文生_图生视频 KJ版_2030578285100408833.json, 视频生成/文生视频/最新LTX 2.3  文生视频工作流 智能自动扩写提示词_2031229319539859458.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_sampler_17

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/aidir-LTX 2.3  首中尾三图+多图_2069594232695902209.json、视频生成/图生视频/最新LTX2.3 1.1模型 _ 三图-首中尾帧 极速版_2048705684543381506.json、视频生成/文生视频/LTX 2.3  首中尾三图+多图_2035272794954539010.json、视频生成/文生视频/LTX2.3 文生_图生视频 KJ版_2030578285100408833.json、视频生成/文生视频/最新LTX 2.3  文生视频工作流 智能自动扩写提示词_2031229319539859458.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 5 个 workflow 都包含：
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
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoaderKJ`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `PathchSageAttentionKJ` —— 4/5 个有
- `PrimitiveBoolean` —— 4/5 个有
- `RH_LLMAPI_Pro_Node` —— 4/5 个有
- `VAELoader` —— 4/5 个有
- `FloatConstant` —— 3/5 个有
- `LTXVChunkFeedForward` —— 3/5 个有
- `LTXVImgToVideoInplaceKJ` —— 3/5 个有
- `ModelPatchTorchSettings` —— 3/5 个有
- `VHS_VideoCombine` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `INTConstant` —— 2/5 个有
- `LTX2_NAG` —— 2/5 个有
- `Label (rgthree)` —— 2/5 个有
- `SaveVideo` —— 2/5 个有
- `SimpleCalculatorKJ` —— 2/5 个有
- `SimpleMath+` —— 2/5 个有
- `easy imageScaleDown` —— 2/5 个有
- `Display Any (rgthree)` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `孤海图像缩放按像素` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 5 | 100% |
| 高度 | 25 | 25 - 25 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，5 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，5 个样本，取值集中（一致性 100%）
