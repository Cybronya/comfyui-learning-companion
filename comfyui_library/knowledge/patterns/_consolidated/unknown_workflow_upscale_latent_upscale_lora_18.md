---
name: unknown_workflow_upscale_latent_upscale_lora_18
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.832571
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/多图参考-LTX2.3图生视频_2042794910578905089.json, 视频生成/文生视频/LTX-2.3文_图生视频二合一_2030147617967050753.json, 视频生成/文生视频/LTX-2.3生成Logo展示视频_2030526628283027457.json, 视频生成/文生视频/LTX-2.3生成电影公司厂标视频_2030534215535693825.json, 视频生成/文生视频/LTX-2.3龙虾术：把”白狐酱板鸭_视频生成器装进OpenClaw！_2034812167572164610.json, 视频生成/文生视频/LTX-文生视频-官方标准版-必收藏_2069062124302852097.json, 视频生成/文生视频/LTX2.3官方工作流_2070310733811896321.json, 视频生成/文生视频/LTX2.3文生视频_2065692334708314114.json, 视频生成/文生视频/LTX2.3文生视频_2071411094870126593.json, 视频生成/文生视频/LTX2.3文生视频_2072147459652014081.json, 视频生成/文生视频/LTX2.3文生视频_2072160114223697921.json, 视频生成/文生视频/LTX2.3文生视频_2072165023333576705.json, 视频生成/文生视频/LTX2.3文生视频_2083869701729509377.json, 视频生成/文生视频/Y-LTX-2.3-Image or Text to Video -Workflow_2033882686305079298.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_18

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/多图参考-LTX2.3图生视频_2042794910578905089.json、视频生成/文生视频/LTX-2.3文_图生视频二合一_2030147617967050753.json、视频生成/文生视频/LTX-2.3生成Logo展示视频_2030526628283027457.json、视频生成/文生视频/LTX-2.3生成电影公司厂标视频_2030534215535693825.json、视频生成/文生视频/LTX-2.3龙虾术：把”白狐酱板鸭_视频生成器装进OpenClaw！_2034812167572164610.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVCropGuides`
- `LTXVImgToVideoInplace`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `CreateVideo` —— 13/14 个有
- `EmptyLTXVLatentVideo` —— 13/14 个有
- `LTXVEmptyLatentAudio` —— 13/14 个有
- `PrimitiveBoolean` —— 13/14 个有
- `ResizeImageMaskNode` —— 13/14 个有
- `SaveVideo` —— 13/14 个有
- `ComfyMathExpression` —— 12/14 个有
- `PreviewAny` —— 11/14 个有
- `LoraLoader` —— 9/14 个有
- `TextGenerateLTX2Prompt` —— 9/14 个有
- `ComfySwitchNode` —— 7/14 个有
- `EmptyImage` —— 7/14 个有
- `LoadImage` —— 7/14 个有
- `Label (rgthree)` —— 3/14 个有
- `CR Text` —— 2/14 个有
- `CR Text Replace` —— 2/14 个有
- `LTX2_NAG` —— 2/14 个有
- `Fast Groups Bypasser (rgthree)` —— 1/14 个有
- `GetImageSize` —— 1/14 个有
- `ImageResizeKJv2` —— 1/14 个有
- `Int` —— 1/14 个有
- `MathExpression|pysssss` —— 1/14 个有
- `RHHiddenNodes` —— 1/14 个有
- `RH_LLMAPI_Pro_Node` —— 1/14 个有
- `StringReplace` —— 1/14 个有
- `VHS_VideoCombine` —— 1/14 个有
- `string_util_StrConcat` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 97 | 97 - 97 | 13 | 100% |
| 高度 | 25 | 25 - 25 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 97，观测区间 97 - 97，13 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，13 个样本，取值集中（一致性 100%）
