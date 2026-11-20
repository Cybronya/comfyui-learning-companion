---
name: unknown_workflow_lora_sampler_clip_35
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.8305
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, PrimitiveStringMultiline, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/Dasiwa V2+Prompt Relay精准控制表情_2055852806652874753.json, 视频生成/图生视频/LTX2.3_自动【首尾帧】视频工作流优化版_2032374429937836033.json, 视频生成/图生视频/LTX2.3_自动【首尾帧】视频工作流优化版_2032414154048413698.json, 视频生成/图生视频/LTX2.3_首尾帧 视频工作流_2033429258751709185.json, 视频生成/图生视频/Sulphur 2+Prompt Relay精准控制表情_2054898098463354882.json, 视频生成/图生视频/fast图生视频_2053653678917206018.json, 视频生成/图生视频/full图生视频_2053653864032813058.json, 视频生成/图生视频/【LTX2.3官方工作流优化】首尾帧控制 _含提示词扩写模板_2033785787984125953.json, 视频生成/图生视频/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）_2033190788460453889.json, 视频生成/图生视频/万象AI真人短剧专用文_图生视频工作流（LTX2.3自动提示词优化版10秒）自动横屏竖屏_2033053099966865410.json, 视频生成/文生视频/AI真人短剧工作流+文生_图生视频_2035632455331356674.json, 视频生成/文生视频/【LTX2.3官方工作流优化】文生视频+图生视频_含提示词扩写模板_2033142799469649922.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_35

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/Dasiwa V2+Prompt Relay精准控制表情_2055852806652874753.json、视频生成/图生视频/LTX2.3_自动【首尾帧】视频工作流优化版_2032374429937836033.json、视频生成/图生视频/LTX2.3_自动【首尾帧】视频工作流优化版_2032414154048413698.json、视频生成/图生视频/LTX2.3_首尾帧 视频工作流_2033429258751709185.json、视频生成/图生视频/Sulphur 2+Prompt Relay精准控制表情_2054898098463354882.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 12 个 workflow 都包含：
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
- `LTXVCropGuides` —— 10/12 个有
- `LTXVLatentUpsampler` —— 10/12 个有
- `LatentUpscaleModelLoader` —— 10/12 个有
- `RH_LLMAPI_Pro_Node` —— 10/12 个有
- `PrimitiveInt` —— 9/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/12 个有
- `easy showAnything` —— 8/12 个有
- `ResizeImagesByLongerEdge` —— 7/12 个有
- `PrimitiveBoolean` —— 6/12 个有
- `ResizeImageMaskNode` —— 6/12 个有
- `Int` —— 5/12 个有
- `LTXVImgToVideoInplaceKJ` —— 4/12 个有
- `GetNode` —— 3/12 个有
- `SetNode` —— 3/12 个有
- `SimpleMath+` —— 3/12 个有
- `Fast Groups Bypasser (rgthree)` —— 2/12 个有
- `PathchSageAttentionKJ` —— 2/12 个有
- `PlaySound|pysssss` —— 2/12 个有
- `PromptRelaySmartEncode` —— 2/12 个有
- `Text` —— 2/12 个有
- `UNETLoader` —— 2/12 个有
- `VAELoaderKJ` —— 2/12 个有
- `easy getNode` —— 2/12 个有
- `easy setNode` —— 2/12 个有
- `CR Text` —— 1/12 个有
- `DeepTranslatorTextNode` —— 1/12 个有
- `ImageResizeKJv2` —— 1/12 个有
- `PreviewImage` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 12 | 100% |
| 高度 | 25 | 25 - 25 | 12 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，12 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，12 个样本，取值集中（一致性 100%）
