---
name: unknown_workflow_lora_sampler_clip_39
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8425
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/HS-template_ltx2_3_style_transition_2042083663428460545.json, 视频生成/图生视频/LTX-2.3图生视频_2035320209401192449.json, 视频生成/图生视频/LTX-2.3首尾帧视频生成_2030927886542180353.json, 视频生成/图生视频/LTX-2.3：把”白狐酱板鸭_装进OpenClaw！_2058356490804752385.json, 视频生成/图生视频/LTX2.3 图生视频_2043581288925372417.json, 视频生成/图生视频/LTX2.3 数字人艾希&李小小《我们都是数字人》播客生产工作流 V3.00331_2038794251055669250.json, 视频生成/图生视频/LTX2.3-图生视频，智能提示词优化_2031273311556079618.json, 视频生成/图生视频/LTX2.3自动首中尾三帧视频_2031361873404239873.json, 视频生成/图生视频/LTX2.3自动首中尾三帧视频（自用）_2036273219824521217.json, 视频生成/图生视频/LTX2.3自动首尾帧流_2073405314405322753.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_39

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/HS-template_ltx2_3_style_transition_2042083663428460545.json、视频生成/图生视频/LTX-2.3图生视频_2035320209401192449.json、视频生成/图生视频/LTX-2.3首尾帧视频生成_2030927886542180353.json、视频生成/图生视频/LTX-2.3：把”白狐酱板鸭_装进OpenClaw！_2058356490804752385.json、视频生成/图生视频/LTX2.3 图生视频_2043581288925372417.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVEmptyLatentAudio`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 9/10 个有
- `KSamplerSelect` —— 9/10 个有
- `LTXVLatentUpsampler` —— 9/10 个有
- `LatentUpscaleModelLoader` —— 9/10 个有
- `LTXVImgToVideoInplace` —— 8/10 个有
- `ResizeImagesByLongerEdge` —— 8/10 个有
- `PrimitiveStringMultiline` —— 7/10 个有
- `RH_LLMAPI_Pro_Node` —— 6/10 个有
- `easy showAnything` —— 5/10 个有
- `LTXVImgToVideoInplaceKJ` —— 4/10 个有
- `FloatConstant` —— 3/10 个有
- `PrimitiveBoolean` —— 3/10 个有
- `Resize` —— 3/10 个有
- `GetImageSize` —— 2/10 个有
- `CR Text` —— 1/10 个有
- `EmptyImage` —— 1/10 个有
- `ImageSizeInfo` —— 1/10 个有
- `LTXVAddGuide` —— 1/10 个有
- `LTXVFirstLastFrameControl_TTP` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `PreviewAny` —— 1/10 个有
- `PrimitiveFloat` —— 1/10 个有
- `SamplerEulerAncestral` —— 1/10 个有
- `SaveImage` —— 1/10 个有
- `StringReplace` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有
- `easy ifElse` —— 1/10 个有
- `easy mathInt` —— 1/10 个有
- `string_util_StrConcat` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 24 - 25 | 10 | 99% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 24 - 25，10 个样本，取值集中（一致性 99%）
