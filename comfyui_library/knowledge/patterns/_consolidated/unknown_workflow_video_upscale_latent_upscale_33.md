---
name: unknown_workflow_video_upscale_latent_upscale_33
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.853083
common_nodes: [CFGGuider, CLIPTextEncode, CheckpointLoaderSimple, EmptyLTXVLatentVideo, INTConstant, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVEmptyLatentAudio, LTXVImgToVideoConditionOnly, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ManualSigmas, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveBoolean, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/文生视频/图&文生视频-LTX2.3-自动提示词-稳定优化版_2030497638990225409.json, 视频生成/文生视频/图生视频 -LTX2.3 全自动   图生视频_ 文生视频_2030510007468429313.json, 视频生成/文生视频/图生视频 文生视频 -LTX2.3 一键生成_2030565382297227266.json, 视频生成/文生视频/文生视频  开源（2）_2046762687073357825.json, 视频生成/文生视频/最强优化  LTX2.3  图 _ 文 生视频合并版_2030179257439227905.json, 视频生成/文生视频/最强优化 LTX2.3 全自动 图生视频 文生视频_2039869978068914177.json, 视频生成/文生视频/最强优化 LTX2.3 全自动 图生视频 文生视频_2039873268945002497.json, 视频生成/文生视频/最强优化—LTX2.3全自动—图生_ 文生视频-邻家AI大女孩_2043235520297312257.json, 视频生成/文生视频/最强优化—LTX2.3全自动—图生_ 文生视频_2029868442429427713.json, 视频生成/文生视频/最强优化—LTX2.3全自动—图生_ 文生视频_2047737799259983873.json, 视频生成/文生视频/最新LTX2.3 图生&文生合并版全面优化版 V2.0_2036310266039771138.json, 视频生成/文生视频/画音同步-LTX2.3全自动-图生+文生视频-优化版_2031929220158464002.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_33

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/图&文生视频-LTX2.3-自动提示词-稳定优化版_2030497638990225409.json、视频生成/文生视频/图生视频 -LTX2.3 全自动   图生视频_ 文生视频_2030510007468429313.json、视频生成/文生视频/图生视频 文生视频 -LTX2.3 一键生成_2030565382297227266.json、视频生成/文生视频/文生视频  开源（2）_2046762687073357825.json、视频生成/文生视频/最强优化  LTX2.3  图 _ 文 生视频合并版_2030179257439227905.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 12 个 workflow 都包含：
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
- `CM_FloatToInt` —— 11/12 个有
- `CR Text` —— 11/12 个有
- `PrimitiveFloat` —— 11/12 个有
- `PrimitiveInt` —— 11/12 个有
- `PreviewAny` —— 9/12 个有
- `RH_LLMAPI_Pro_Node` —— 9/12 个有
- `SetNode` —— 4/12 个有
- `SimpleMath+` —— 3/12 个有
- `easy showAnything` —— 3/12 个有
- `GetNode` —— 2/12 个有
- `TextInputNode` —— 2/12 个有
- `AILab_QwenVL` —— 1/12 个有
- `CM_IntToFloat` —— 1/12 个有
- `FancyTimerNode` —— 1/12 个有
- `JoinStrings` —— 1/12 个有
- `MathExpression|pysssss` —— 1/12 个有
- `Text Multiline` —— 1/12 个有
- `VRAMReserver` —— 1/12 个有
- `easy int` —— 1/12 个有

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
