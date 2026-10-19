---
name: unknown_workflow_video_lora_sampler_344
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.8405
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CR Text, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveBoolean, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2035345217242537985.json, 视频生成/图生视频/2035366235172507650.json, 视频生成/图生视频/2042424344898445313.json, 视频生成/图生视频/2043902028618932226.json, 视频生成/图生视频/2039873028493938689.json, 视频生成/图生视频/2069596918434590721.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_344

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2035345217242537985.json、视频生成/图生视频/2035366235172507650.json、视频生成/图生视频/2042424344898445313.json、视频生成/图生视频/2043902028618932226.json、视频生成/图生视频/2039873028493938689.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CR Text`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `PreviewAny` —— 5/6 个有
- `INTConstant` —— 4/6 个有
- `LTXVLatentUpsampler` —— 4/6 个有
- `LatentUpscaleModelLoader` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/6 个有
- `PrimitiveInt` —— 4/6 个有
- `RH_LLMAPI_Pro_Node` —— 4/6 个有
- `Text` —— 3/6 个有
- `DapaoImageAspectRatioResizeNode` —— 2/6 个有
- `GetNode` —— 2/6 个有
- `JjkText` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `RH_LLMAPI_NODE` —— 2/6 个有
- `RH_RhartImageNG31FlashImageToImage` —— 2/6 个有
- `RH_RhartVideoGImageToVideo` —— 2/6 个有
- `SaveImage` —— 2/6 个有
- `SaveVideo` —— 2/6 个有
- `Seed (rgthree)` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `SimpleMath+` —— 2/6 个有
- `TextCombinerTwo` —— 2/6 个有
- `easy cleanGpuUsed` —— 2/6 个有
- `easy int` —— 2/6 个有
- `Fast Groups Bypasser (rgthree)` —— 1/6 个有
- `Note Plus (mtb)` —— 1/6 个有
- `Qwen3VL_Chat` —— 1/6 个有
- `RH_RhartImageNG31FlashOfficialImageToImage` —— 1/6 个有
- `RH_RhartVideoV31FastImageToVideo` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 6 | 100% |
| 高度 | 25 | 25 - 25 | 6 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，6 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
