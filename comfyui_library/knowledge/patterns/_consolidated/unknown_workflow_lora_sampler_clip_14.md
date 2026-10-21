---
name: unknown_workflow_lora_sampler_clip_14
type: Unknown Workflow
frequency: 14
level: strong
coverage: 0.835714
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/2055852806652874753.json, 视频生成/图生视频/2032374429937836033.json, 视频生成/图生视频/2032414154048413698.json, 视频生成/图生视频/2033429258751709185.json, 视频生成/图生视频/2033403811573800961.json, 视频生成/图生视频/2031361873404239873.json, 视频生成/图生视频/2036273219824521217.json, 视频生成/图生视频/2073405314405322753.json, 视频生成/图生视频/2054898098463354882.json, 视频生成/图生视频/2053653678917206018.json, 视频生成/图生视频/2053653864032813058.json, 视频生成/文生视频/AI真人短剧工作流+文生_图生视频_2035632455331356674.json, 视频生成/文生视频/LTX2.3文生_图生视频 AI真人短剧工作流_2053318411618398209.json, 视频生成/文生视频/LTX2.3文生_图生视频 AI真人短剧工作流_2054136644139266049.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_14

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/2055852806652874753.json、视频生成/图生视频/2032374429937836033.json、视频生成/图生视频/2032414154048413698.json、视频生成/图生视频/2033429258751709185.json、视频生成/图生视频/2033403811573800961.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 14 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `PrimitiveStringMultiline`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `LTXVCropGuides` —— 12/14 个有
- `LTXVLatentUpsampler` —— 12/14 个有
- `LatentUpscaleModelLoader` —— 12/14 个有
- `RH_LLMAPI_Pro_Node` —— 12/14 个有
- `PrimitiveInt` —— 11/14 个有
- `easy showAnything` —— 10/14 个有
- `ResizeImageMaskNode` —— 9/14 个有
- `ResizeImagesByLongerEdge` —— 9/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 7/14 个有
- `LTXVImgToVideoInplaceKJ` —— 6/14 个有
- `PrimitiveBoolean` —— 6/14 个有
- `GetNode` —— 5/14 个有
- `Int` —— 5/14 个有
- `SetNode` —— 5/14 个有
- `SimpleMath+` —— 4/14 个有
- `DeepTranslatorTextNode` —— 3/14 个有
- `FloatConstant` —— 2/14 个有
- `PathchSageAttentionKJ` —— 2/14 个有
- `PromptRelaySmartEncode` —— 2/14 个有
- `Resize` —— 2/14 个有
- `UNETLoader` —— 2/14 个有
- `VAELoaderKJ` —— 2/14 个有
- `easy getNode` —— 2/14 个有
- `easy setNode` —— 2/14 个有
- `EmptyImage` —— 1/14 个有
- `ImageSizeInfo` —— 1/14 个有
- `PreviewImage` —— 1/14 个有
- `SaveImage` —— 1/14 个有
- `easy mathInt` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 14 | 100% |
| 高度 | 25 | 25 - 25 | 14 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，14 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，14 个样本，取值集中（一致性 100%）
