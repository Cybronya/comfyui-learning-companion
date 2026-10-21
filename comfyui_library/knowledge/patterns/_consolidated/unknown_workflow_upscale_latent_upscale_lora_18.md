---
name: unknown_workflow_upscale_latent_upscale_lora_18
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.831077
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVLatentUpsampler, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveInt, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2042794910578905089.json, 视频生成/文生视频/LTX-文生视频-官方标准版-必收藏_2069062124302852097.json, 视频生成/文生视频/LTX2.3  文生视频 优化版_2030871574055755778.json, 视频生成/文生视频/LTX2.3-文生视频，智能提示词优化_2031263174128836610.json, 视频生成/文生视频/LTX2.3官方工作流_2070310733811896321.json, 视频生成/文生视频/LTX2.3文生_图生视频_2055972165740179457.json, 视频生成/文生视频/LTX2.3文生视频_2071411094870126593.json, 视频生成/文生视频/LTX2.3文生视频_2072147459652014081.json, 视频生成/文生视频/LTX2.3文生视频_2072160114223697921.json, 视频生成/文生视频/LTX2.3文生视频_2072165023333576705.json, 视频生成/文生视频/LTX2.3文生视频_2083869701729509377.json, 视频生成/文生视频/LTX2.3短剧_2042644046811766785.json, 视频生成/文生视频/Y-LTX-2.3-Image or Text to Video -Workflow_2033882686305079298.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_18

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/2042794910578905089.json、视频生成/文生视频/LTX-文生视频-官方标准版-必收藏_2069062124302852097.json、视频生成/文生视频/LTX2.3  文生视频 优化版_2030871574055755778.json、视频生成/文生视频/LTX2.3-文生视频，智能提示词优化_2031263174128836610.json、视频生成/文生视频/LTX2.3官方工作流_2070310733811896321.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 13 个 workflow 都包含：
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
- `LTXVLatentUpsampler`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 12/13 个有
- `CreateVideo` —— 12/13 个有
- `EmptyLTXVLatentVideo` —— 12/13 个有
- `LTXVEmptyLatentAudio` —— 12/13 个有
- `LTXVImgToVideoInplace` —— 12/13 个有
- `LTXVPreprocess` —— 12/13 个有
- `PrimitiveBoolean` —— 12/13 个有
- `ResizeImagesByLongerEdge` —— 12/13 个有
- `SaveVideo` —— 12/13 个有
- `ResizeImageMaskNode` —— 11/13 个有
- `LoraLoader` —— 9/13 个有
- `PreviewAny` —— 9/13 个有
- `TextGenerateLTX2Prompt` —— 9/13 个有
- `ComfySwitchNode` —— 7/13 个有
- `EmptyImage` —— 7/13 个有
- `LoadImage` —— 5/13 个有
- `easy showAnything` —— 4/13 个有
- `RH_LLMAPI_Pro_Node` —— 3/13 个有
- `LTX2_NAG` —— 2/13 个有
- `DeepTranslatorTextNode` —— 1/13 个有
- `Fast Groups Bypasser (rgthree)` —— 1/13 个有
- `GetImageSize` —— 1/13 个有
- `ImageResizeKJv2` —— 1/13 个有
- `Int` —— 1/13 个有
- `Qwen3_VQA` —— 1/13 个有
- `RHHiddenNodes` —— 1/13 个有
- `SimpleMath+` —— 1/13 个有
- `TextConcatenator` —— 1/13 个有
- `VHS_VideoCombine` —— 1/13 个有
- `easy ifElse` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 9 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 97 | 97 - 97 | 12 | 100% |
| 高度 | 25 | 25 - 25 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 97，观测区间 97 - 97，12 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，12 个样本，取值集中（一致性 100%）
