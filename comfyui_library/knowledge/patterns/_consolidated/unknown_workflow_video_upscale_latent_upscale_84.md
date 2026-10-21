---
name: unknown_workflow_video_upscale_latent_upscale_84
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.8655
common_nodes: [CFGGuider, CLIPTextEncode, CM_FloatToInt, CheckpointLoaderSimple, EmptyLTXVLatentVideo, INTConstant, ImageResize+, Int, KSamplerSelect, LTXAVTextEncoderLoader, LTXVAudioVAEDecode, LTXVAudioVAELoader, LTXVChunkFeedForward, LTXVConcatAVLatent, LTXVConditioning, LTXVCropGuides, LTXVEmptyLatentAudio, LTXVImgToVideoInplace, LTXVLatentUpsampler, LTXVPreprocess, LTXVSeparateAVLatent, LatentUpscaleModelLoader, LoraLoaderModelOnly, ManualSigmas, MathExpression|pysssss, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveFloat, PrimitiveInt, RandomNoise, SamplerCustomAdvanced, VAEDecodeTiled, VHS_VideoCombine, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2035008599692414977.json, 视频生成/图生视频/2034668496671481857.json, 视频生成/图生视频/2045878381895487489.json, 视频生成/文生视频/复刻抖音爆款短视频，适用各种台词_2046116661975064577.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_84

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2035008599692414977.json、视频生成/图生视频/2034668496671481857.json、视频生成/图生视频/2045878381895487489.json、视频生成/文生视频/复刻抖音爆款短视频，适用各种台词_2046116661975064577.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPTextEncode`
- `CM_FloatToInt`
- `CheckpointLoaderSimple`
- `EmptyLTXVLatentVideo`
- `INTConstant`
- `ImageResize+`
- `Int`
- `KSamplerSelect`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAEDecode`
- `LTXVAudioVAELoader`
- `LTXVChunkFeedForward`
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
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveFloat`
- `PrimitiveInt`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `VAEDecodeTiled`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 3/4 个有
- `CR Prompt Text` —— 3/4 个有
- `EmptySD3LatentImage` —— 3/4 个有
- `KSampler` —— 3/4 个有
- `LTXVImgToVideoConditionOnly` —— 3/4 个有
- `ModelSamplingAuraFlow` —— 3/4 个有
- `QwenImageLatentAspectRatio` —— 3/4 个有
- `RH_LLMAPI_Pro_Node` —— 3/4 个有
- `SaveImage` —— 3/4 个有
- `SplitAndExtractText` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `VAEDecode` —— 3/4 个有
- `VAELoader` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `孤海_kontext生图比例` —— 3/4 个有
- `CR Text` —— 1/4 个有
- `LTXVImgToVideoInplaceKJ` —— 1/4 个有
- `LoadImage` —— 1/4 个有
- `Make Image Batch` —— 1/4 个有
- `QWEN_TextDisplay` —— 1/4 个有
- `Qwen3_VQA` —— 1/4 个有
- `ttN concat` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 97 | 97 - 97 | 4 | 100% |
| 高度 | 25 | 25 - 25 | 4 | 100% |
| 采样步数 | 10 | 8 - 500 | 3 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 97，观测区间 97 - 97，4 个样本，取值集中（一致性 100%）
- 高度 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 10，观测区间 8 - 500，3 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 500，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
