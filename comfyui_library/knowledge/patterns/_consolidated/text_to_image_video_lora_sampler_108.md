---
name: text_to_image_video_lora_sampler_108
type: Text To Image
frequency: 8
level: strong
coverage: 0.87825
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, CR Text, CS-MultiImageLoader, ComfyMathExpression, CreateVideo, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LTXVConcatAVLatent, LTXVSeparateAVLatent, LoadAudioUI, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PreviewAny, PreviewVideoNode, PrimitiveFloat, PrimitiveStringMultiline, RH_LLMAPI_NODE, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/多参极简V2.0｜MiniMax H3自动提示词+二采生成_2091017100998569985.json, 视频生成/图生视频/多参极简V2.0｜MiniMax H3自动提示词+高清二采_2091199421529808898.json, 视频生成/图生视频/多参极简V2.0｜MiniMax H3自动提示词二采图生视频_2089829668701691905.json, 视频生成/图生视频/多参极简V3.0｜MiniMax H3多参考长视频续接图生视频_2093125812944986114.json, 视频生成/文生视频/MiniMax H3 多参极简 V3.0｜多参考长视频续接不断篇_2096843243878174721.json, 视频生成/文生视频/多参极简工作流V3.0｜MiniMax H3多参考长视频续接_2096645855133655041.json, 视频生成/文生视频/多参极简工作流V3.0｜MiniMax H3多参考长视频续接_2096660374702616577.json, 视频生成/文生视频/多参考长视频续接｜MiniMax H3首段视频生成V4_2095052143274319874.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_108

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/多参极简V2.0｜MiniMax H3自动提示词+二采生成_2091017100998569985.json、视频生成/图生视频/多参极简V2.0｜MiniMax H3自动提示词+高清二采_2091199421529808898.json、视频生成/图生视频/多参极简V2.0｜MiniMax H3自动提示词二采图生视频_2089829668701691905.json、视频生成/图生视频/多参极简V3.0｜MiniMax H3多参考长视频续接图生视频_2093125812944986114.json、视频生成/文生视频/MiniMax H3 多参极简 V3.0｜多参考长视频续接不断篇_2096843243878174721.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CS-MultiImageLoader`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LoadAudioUI`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PreviewAny`
- `PreviewVideoNode`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `VAEDecodeAudio` —— 7/8 个有
- `MinimaxH3LatentUpscaler3D` —— 6/8 个有
- `ConditioningZeroOut` —— 5/8 个有
- `Fast Groups Bypasser (rgthree)` —— 5/8 个有
- `FlashVSRNode` —— 5/8 个有
- `Int` —— 5/8 个有
- `LoadVideoUI` —— 5/8 个有
- `MiniMaxH3MotionContext` —— 5/8 个有
- `MiniMaxH3MotionContextTrim` —— 5/8 个有
- `Text Multiline` —— 5/8 个有
- `CR Apply LoRA Stack` —— 4/8 个有
- `LoadVideo` —— 4/8 个有
- `ManualSigmas` —— 4/8 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 4/8 个有
- `easy loraStack` —— 4/8 个有
- `MiniMaxH3SigmaShift` —— 3/8 个有
- `ModelAttentionBackend` —— 3/8 个有
- `PreviewAudio` —— 3/8 个有
- `Switch any [Crystools]` —— 3/8 个有
- `LoadImage` —— 1/8 个有
- `MinimaxH3LatentUpscalerNode3D` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高发问题（13/8 个样本）：Steps较低可能导致细节不足
