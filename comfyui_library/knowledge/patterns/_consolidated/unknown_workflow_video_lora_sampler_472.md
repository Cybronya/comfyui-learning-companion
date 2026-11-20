---
name: unknown_workflow_video_lora_sampler_472
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.8184
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CR Text, CheckpointLoaderSimple, EmptyLTXVLatentVideo, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVPreprocess, LTXVSeparateAVLatent, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PreviewAny, PrimitiveBoolean, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/005.LTX2.3音视融合001.LTX2.3首帧图生视频_2035345217242537985.json, 视频生成/图生视频/005.LTX2.3音视融合004.LTX2.3全自动—图生_文生视频_2035366235172507650.json, 视频生成/图生视频/AIGC-KOC视角批量_2042424344898445313.json, 视频生成/图生视频/AIGC-LTX-产品动图_2043902028618932226.json, 视频生成/图生视频/AIGC-黄金产品素材C流_2039873028493938689.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_472

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/005.LTX2.3音视融合001.LTX2.3首帧图生视频_2035345217242537985.json、视频生成/图生视频/005.LTX2.3音视融合004.LTX2.3全自动—图生_文生视频_2035366235172507650.json、视频生成/图生视频/AIGC-KOC视角批量_2042424344898445313.json、视频生成/图生视频/AIGC-LTX-产品动图_2043902028618932226.json、视频生成/图生视频/AIGC-黄金产品素材C流_2039873028493938689.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 5 个 workflow 都包含：
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
- `PreviewAny`
- `PrimitiveBoolean`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 4/5 个有
- `LTXVLatentUpsampler` —— 4/5 个有
- `LatentUpscaleModelLoader` —— 4/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/5 个有
- `PrimitiveInt` —— 4/5 个有
- `RH_LLMAPI_Pro_Node` —— 3/5 个有
- `Text` —— 3/5 个有
- `GetNode` —— 2/5 个有
- `JjkText` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `RH_LLMAPI_NODE` —— 2/5 个有
- `RH_RhartImageNG31FlashImageToImage` —— 2/5 个有
- `RH_RhartVideoGImageToVideo` —— 2/5 个有
- `SaveImage` —— 2/5 个有
- `SaveVideo` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `TextCombinerTwo` —— 2/5 个有
- `DapaoImageAspectRatioResizeNode` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `Qwen3VL_Chat` —— 1/5 个有
- `RH_RhartImageNG31FlashOfficialImageToImage` —— 1/5 个有
- `RH_RhartVideoV31FastImageToVideo` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy int` —— 1/5 个有

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
