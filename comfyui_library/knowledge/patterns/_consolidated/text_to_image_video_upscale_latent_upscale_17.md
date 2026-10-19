---
name: text_to_image_video_upscale_latent_upscale_17
type: Text To Image
frequency: 4
level: strong
coverage: 0.833
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Apply LoRA Stack, CR Text, CS-MultiImageLoader, ComfyMathExpression, ConditioningZeroOut, CreateVideo, EmptyLatentImage, Fast Groups Bypasser (rgthree), FlashVSRNode, Int, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LiconMSR, LoadAudioUI, LoadVideoUI, LoraLoaderModelOnly, ManualSigmas, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3MotionContext, MiniMaxH3MotionContextTrim, MiniMaxH3ReferenceToVideo, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, PreviewAny, PreviewAudio, PreviewVideoNode, PrimitiveFloat, PrimitiveStringMultiline, RH_LLMAPI_NODE, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, Seed (rgthree), SolAttnPatch, SplitSigmas, Switch any [Crystools], TTResolutionSelector, Text Multiline, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, VRGDG_MiniMaxH3AudioDrive, easy loraStack, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/MiniMax H3多参极简分镜参考 V3.0加速版三分钟出片_2098117837658353665.json, 视频生成/图生视频/MiniMax H3多参极简工作流V4.0，剧本分镜生成图生视频平替全能图片G方案_2103553483323559937.json, 视频生成/图生视频/多参极简工作流V3.0｜MiniMax H3分镜强参考图生视频_2096291857121763330.json, 视频生成/图生视频/极简上手不折腾｜MiniMax H3多参分镜强参考V3.0_2096547096676618241.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_17

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/MiniMax H3多参极简分镜参考 V3.0加速版三分钟出片_2098117837658353665.json、视频生成/图生视频/MiniMax H3多参极简工作流V4.0，剧本分镜生成图生视频平替全能图片G方案_2103553483323559937.json、视频生成/图生视频/多参极简工作流V3.0｜MiniMax H3分镜强参考图生视频_2096291857121763330.json、视频生成/图生视频/极简上手不折腾｜MiniMax H3多参分镜强参考V3.0_2096547096676618241.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Apply LoRA Stack`
- `CR Text`
- `CS-MultiImageLoader`
- `ComfyMathExpression`
- `ConditioningZeroOut`
- `CreateVideo`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `FlashVSRNode`
- `Int`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LiconMSR`
- `LoadAudioUI`
- `LoadVideoUI`
- `LoraLoaderModelOnly`
- `ManualSigmas`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3MotionContext`
- `MiniMaxH3MotionContextTrim`
- `MiniMaxH3ReferenceToVideo`
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `PreviewAny`
- `PreviewAudio`
- `PreviewVideoNode`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `SolAttnPatch`
- `SplitSigmas`
- `Switch any [Crystools]`
- `TTResolutionSelector`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `VRGDG_MiniMaxH3AudioDrive`
- `easy loraStack`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadVideo` —— 3/4 个有
- `MiniMaxH3AVDecodeT8` —— 3/4 个有
- `MiniMaxH3DualClockSamplerT8` —— 3/4 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 3/4 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 3/4 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 3/4 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 3/4 个有
- `GetImageSize` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `SaveImage` —— 2/4 个有
- `VHS_MergeImages` —— 2/4 个有
- `Float` —— 1/4 个有
- `ImageFromBatch` —— 1/4 个有
- `Text` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高发问题（9/4 个样本）：Steps较低可能导致细节不足
