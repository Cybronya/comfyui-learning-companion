---
name: unknown_workflow_upscale_latent_upscale_lora_16
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.840615
common_nodes: [CFGGuider, CLIPTextEncode, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, PrimitiveBoolean, PrimitiveInt, RandomNoise, ResizeImagesByLongerEdge, SamplerCustomAdvanced, SaveVideo]
problems: []
missing: []
members: [视频生成/文生视频/LTX 2.3 -22b IC-LoRA Cameraman_v2 视频工作流_2053468262532435970.json, 视频生成/文生视频/LTX-2.3-Text to Video-workflow_2034124938138882049.json, 视频生成/文生视频/LTX-2.3文_图生视频二合一_2030147617967050753.json, 视频生成/文生视频/LTX-2.3生成Logo展示视频_2030526628283027457.json, 视频生成/文生视频/LTX-2.3生成电影公司厂标视频_2030534215535693825.json, 视频生成/文生视频/LTX-文生视频-官方标准版-必收藏_2069062124302852097.json, 视频生成/文生视频/LTX2.3官方工作流_2070310733811896321.json, 视频生成/文生视频/LTX2.3文生视频_2071411094870126593.json, 视频生成/文生视频/LTX2.3文生视频_2072147459652014081.json, 视频生成/文生视频/LTX2.3文生视频_2072160114223697921.json, 视频生成/文生视频/LTX2.3文生视频_2072165023333576705.json, 视频生成/文生视频/LTX2.3文生视频_2083869701729509377.json, 视频生成/文生视频/Y-LTX-2.3-Image or Text to Video -Workflow_2033882686305079298.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_16

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/文生视频/LTX 2.3 -22b IC-LoRA Cameraman_v2 视频工作流_2053468262532435970.json、视频生成/文生视频/LTX-2.3-Text to Video-workflow_2034124938138882049.json、视频生成/文生视频/LTX-2.3文_图生视频二合一_2030147617967050753.json、视频生成/文生视频/LTX-2.3生成Logo展示视频_2030526628283027457.json、视频生成/文生视频/LTX-2.3生成电影公司厂标视频_2030534215535693825.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 13 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
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
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `RandomNoise`
- `ResizeImagesByLongerEdge`
- `SamplerCustomAdvanced`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `CheckpointLoaderSimple` —— 12/13 个有
- `ComfyMathExpression` —— 12/13 个有
- `LTXVAudioVAELoader` —— 12/13 个有
- `PrimitiveStringMultiline` —— 12/13 个有
- `ResizeImageMaskNode` —— 12/13 个有
- `VAEDecodeTiled` —— 12/13 个有
- `PreviewAny` —— 9/13 个有
- `EmptyImage` —— 8/13 个有
- `LoraLoader` —— 8/13 个有
- `TextGenerateLTX2Prompt` —— 8/13 个有
- `ComfySwitchNode` —— 7/13 个有
- `LoadImage` —— 5/13 个有
- `Label (rgthree)` —— 3/13 个有
- `CR Text` —— 2/13 个有
- `CR Text Replace` —— 2/13 个有
- `GetImageSize` —— 2/13 个有
- `ImageResizeKJv2` —— 1/13 个有
- `LTX2_NAG` —— 1/13 个有
- `MathExpression|pysssss` —— 1/13 个有
- `RH_LLMAPI_Pro_Node` —— 1/13 个有
- `UNETLoader` —— 1/13 个有
- `VAEDecode` —— 1/13 个有
- `VAELoader` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有
- `easy clearCacheAll` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 13 | 100% |
| 高度 | 25 | 25 - 25 | 13 | 100% |
| LoRA 模型强度 | 1 | 1 - 1 | 8 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，13 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，13 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
