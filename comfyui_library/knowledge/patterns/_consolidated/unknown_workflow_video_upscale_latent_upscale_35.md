---
name: unknown_workflow_video_upscale_latent_upscale_35
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8547
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveBoolean, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/图&文生视频-LTX2.3-自动提示词-稳定优化版_2030497638990225409.json, 视频生成/文生视频/文生视频  开源（2）_2046762687073357825.json, 视频生成/文生视频/最强优化  LTX2.3  图 _ 文 生视频合并版_2030179257439227905.json, 视频生成/文生视频/最强优化 LTX2.3 全自动 图生视频 文生视频_2039869978068914177.json, 视频生成/文生视频/最强优化 LTX2.3 全自动 图生视频 文生视频_2039873268945002497.json, 视频生成/文生视频/最强优化—LTX2.3全自动—图生_ 文生视频-邻家AI大女孩_2043235520297312257.json, 视频生成/文生视频/最强优化—LTX2.3全自动—图生_ 文生视频_2029868442429427713.json, 视频生成/文生视频/最强优化—LTX2.3全自动—图生_ 文生视频_2047737799259983873.json, 视频生成/文生视频/最新LTX2.3 图生&文生合并版全面优化版 V2.0_2036310266039771138.json, 视频生成/文生视频/画音同步-LTX2.3全自动-图生+文生视频-优化版_2031929220158464002.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_35

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/文生视频/图&文生视频-LTX2.3-自动提示词-稳定优化版_2030497638990225409.json、视频生成/文生视频/文生视频  开源（2）_2046762687073357825.json、视频生成/文生视频/最强优化  LTX2.3  图 _ 文 生视频合并版_2030179257439227905.json、视频生成/文生视频/最强优化 LTX2.3 全自动 图生视频 文生视频_2039869978068914177.json、视频生成/文生视频/最强优化 LTX2.3 全自动 图生视频 文生视频_2039873268945002497.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVConditioning`
- `LTXVEmptyLatentAudio`
- `LTXVImgToVideoConditionOnly`
- `LTXVLatentUpsampler`
- `LTXVPreprocess`
- `LTXVSeparateAVLatent`
- `LatentUpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CM_FloatToInt` —— 9/10 个有
- `CR Text` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `PrimitiveInt` —— 9/10 个有
- `PreviewAny` —— 7/10 个有
- `RH_LLMAPI_Pro_Node` —— 7/10 个有
- `GetNode` —— 2/10 个有
- `SetNode` —— 2/10 个有
- `AILab_QwenVL` —— 1/10 个有
- `CM_IntToFloat` —— 1/10 个有
- `FancyTimerNode` —— 1/10 个有
- `JoinStrings` —— 1/10 个有
- `MathExpression|pysssss` —— 1/10 个有
- `SimpleMath+` —— 1/10 个有
- `Text Multiline` —— 1/10 个有
- `VRAMReserver` —— 1/10 个有
- `easy int` —— 1/10 个有
- `easy showAnything` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 10 | 100% |
| 高度 | 25 | 25 - 25 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，10 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，10 个样本，取值集中（一致性 100%）
