---
name: unknown_workflow_lora_sampler_clip_72
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.838286
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, CreateVideo, EmptyLTXVLatentVideo, Int, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVPreprocess, LTXVSeparateAVLatent, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, RandomNoise, SamplerCustomAdvanced, SaveVideo, VAEDecodeTiled]
problems: []
missing: []
members: [视频生成/图生视频/7-LTX2.3_首尾帧 视频工作流_2038606312925306881.json, 视频生成/图生视频/Dasiwa V2+Prompt Relay精准控制表情_2055852806652874753.json, 视频生成/图生视频/LTX 2.3 三种机甲变身(lora) 流_2041514210315735041.json, 视频生成/图生视频/LTX 2.3 变身特效（亦诚视觉原创）_2041734587340038146.json, 视频生成/图生视频/LTX 2.3 多图引导生视频_2082120324979716097.json, 视频生成/图生视频/LTX 2.3 紫色生物机甲变身(lora)_2038207302813097986.json, 视频生成/图生视频/Sulphur 2+Prompt Relay精准控制表情_2054898098463354882.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_72

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/7-LTX2.3_首尾帧 视频工作流_2038606312925306881.json、视频生成/图生视频/Dasiwa V2+Prompt Relay精准控制表情_2055852806652874753.json、视频生成/图生视频/LTX 2.3 三种机甲变身(lora) 流_2041514210315735041.json、视频生成/图生视频/LTX 2.3 变身特效（亦诚视觉原创）_2041734587340038146.json、视频生成/图生视频/LTX 2.3 多图引导生视频_2082120324979716097.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLTXVLatentVideo`
- `Int`
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
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `VAEDecodeTiled`

**可变部分**（部分 workflow 才有）：
- `PrimitiveInt` —— 6/7 个有
- `LTXVCropGuides` —— 5/7 个有
- `LTXVLatentUpsampler` —— 5/7 个有
- `LatentUpscaleModelLoader` —— 5/7 个有
- `PrimitiveStringMultiline` —— 5/7 个有
- `LayerUtility: PurgeVRAM V2` —— 4/7 个有
- `PrimitiveBoolean` —— 4/7 个有
- `ResizeImagesByLongerEdge` —— 4/7 个有
- `ResizeImageMaskNode` —— 3/7 个有
- `YC_textReplaceNode` —— 3/7 个有
- `GetNode` —— 2/7 个有
- `LayerUtility: TextBox` —— 2/7 个有
- `PathchSageAttentionKJ` —— 2/7 个有
- `PromptRelaySmartEncode` —— 2/7 个有
- `SetNode` —— 2/7 个有
- `UNETLoader` —— 2/7 个有
- `VAELoaderKJ` —— 2/7 个有
- `easy getNode` —— 2/7 个有
- `easy setNode` —— 2/7 个有
- `Float` —— 1/7 个有
- `ImageResizeKJ` —— 1/7 个有
- `LTXVAddGuideMulti` —— 1/7 个有
- `LTXVImgToVideoInplaceKJ` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `PreviewImage` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `YC_ShowText` —— 1/7 个有
- `YC_SingleTextNode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 7 | 100% |
| 高度 | 25 | 25 - 25 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，7 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，7 个样本，取值集中（一致性 100%）
