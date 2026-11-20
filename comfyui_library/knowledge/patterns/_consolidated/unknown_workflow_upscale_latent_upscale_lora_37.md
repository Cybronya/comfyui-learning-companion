---
name: unknown_workflow_upscale_latent_upscale_lora_37
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8445
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, SaveVideo]
problems: []
missing: []
members: [视频生成/文生视频/LTX-2.3_基础文生图生视频双采样_2080467787033694209.json, 视频生成/文生视频/LTX2.3文生视频_2065692334708314114.json, 视频生成/文生视频/LTX2.3文生视频_2071411094870126593.json, 视频生成/文生视频/LTX2.3文生视频_2072147459652014081.json, 视频生成/文生视频/LTX2.3文生视频_2072160114223697921.json, 视频生成/文生视频/LTX2.3文生视频_2072165023333576705.json, 视频生成/文生视频/LTX2.3文生视频_2083869701729509377.json, 视频生成/文生视频/LTX2.3短剧_2042644046811766785.json, 视频生成/文生视频/Y-LTX-2.3-Image or Text to Video -Workflow_2033882686305079298.json, 视频生成/文生视频/咕咕嘎嘎？_2042845410145869826.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_37

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/LTX-2.3_基础文生图生视频双采样_2080467787033694209.json、视频生成/文生视频/LTX2.3文生视频_2065692334708314114.json、视频生成/文生视频/LTX2.3文生视频_2071411094870126593.json、视频生成/文生视频/LTX2.3文生视频_2072147459652014081.json、视频生成/文生视频/LTX2.3文生视频_2072160114223697921.json…）

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
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `ComfyMathExpression` —— 9/10 个有
- `LTXVCropGuides` —— 9/10 个有
- `LTXVImgToVideoInplace` —— 9/10 个有
- `PrimitiveStringMultiline` —— 9/10 个有
- `ResizeImageMaskNode` —— 9/10 个有
- `ResizeImagesByLongerEdge` —— 9/10 个有
- `VAEDecodeTiled` —— 9/10 个有
- `LoraLoader` —— 6/10 个有
- `PreviewAny` —— 6/10 个有
- `TextGenerateLTX2Prompt` —— 6/10 个有
- `ComfySwitchNode` —— 5/10 个有
- `EmptyImage` —— 5/10 个有
- `LoadImage` —— 5/10 个有
- `GetImageSize` —— 1/10 个有
- `LTXFloatToInt` —— 1/10 个有
- `LTXVImgToVideoConditionOnly` —— 1/10 个有
- `LTXVTiledVAEDecode` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `PrimitiveFloat` —— 1/10 个有
- `RH_LLMAPI_Pro_Node` —— 1/10 个有
- `SimpleMath+` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 25 - 25 | 10 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
