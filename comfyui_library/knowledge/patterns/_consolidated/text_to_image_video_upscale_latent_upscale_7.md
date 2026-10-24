---
name: text_to_image_video_upscale_latent_upscale_7
type: Text To Image
frequency: 11
level: strong
coverage: 0.855455
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3 720P文戏均衡画质加强工作流，图生视频高质量文戏创作工具_2106163296528330753.json, 视频生成/图生视频/H3 POV视角720P超采样版工作流，图生视频第一人称视角创作方案_2106905984181563394.json, 视频生成/图生视频/H3-POV第一人称视角｜720p超采样图生视频_2106607588157771778.json, 视频生成/图生视频/H3_POV视角720P超采样版工作流，图生视频第一人称视角创作方案_2108378553988501505.json, 视频生成/图生视频/H3双采参考生视频Dasiwa V2版本对白战斗动作戏_2100636081782874114.json, 视频生成/图生视频/H3双采参考生视频V2 文戏武戏低显存适配版_2098846488892887041.json, 视频生成/图生视频/MiniMax H3全能参考9图3音频｜HyperVae 2X高清画质输出_2111077634724679682.json, 视频生成/图生视频/MiniMax H3双采V3语义桥｜文戏不油武戏动态强_2106606073850454017.json, 视频生成/图生视频/MiniMax H3双采全能V3语义桥 文戏自然武戏动态强长视频_2110355426595401730.json, 视频生成/图生视频/MiniMax H3双采全能工作流V3语义桥，文戏不油武戏动态强参考生视频_2106823219750727681.json, 视频生成/文生视频/MiniMax H3双采全能工作流V3语义桥文生视频版，长视频高清直出方案_2106998489740828674.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_7

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/H3 720P文戏均衡画质加强工作流，图生视频高质量文戏创作工具_2106163296528330753.json、视频生成/图生视频/H3 POV视角720P超采样版工作流，图生视频第一人称视角创作方案_2106905984181563394.json、视频生成/图生视频/H3-POV第一人称视角｜720p超采样图生视频_2106607588157771778.json、视频生成/图生视频/H3_POV视角720P超采样版工作流，图生视频第一人称视角创作方案_2108378553988501505.json、视频生成/图生视频/H3双采参考生视频Dasiwa V2版本对白战斗动作戏_2100636081782874114.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3LearnedLatentUpscaleT8Advanced`
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3TwoPassDetailMixerT8Advanced`
- `MiniMaxH3TwoPassLatentReconcileT8Advanced`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SolAttnMiniMax`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `Float` —— 10/11 个有
- `MiniMaxH3AudioConditioningT8` —— 10/11 个有
- `easy anythingIndexSwitch` —— 10/11 个有
- `孤海注释` —— 10/11 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 9/11 个有
- `easy cleanGpuUsed` —— 9/11 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 8/11 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 8/11 个有
- `RunningHub Deepcleaner` —— 8/11 个有
- `SaveImage` —— 8/11 个有
- `MiniMaxH3HyperVAE2xLoaderEXPT8` —— 5/11 个有
- `Astra` —— 4/11 个有
- `CreateVideo` —— 4/11 个有
- `Fast Groups Bypasser (rgthree)` —— 4/11 个有
- `GetImageSize` —— 4/11 个有
- `GetNode` —— 4/11 个有
- `ImageCrop` —— 4/11 个有
- `ImageScale` —— 4/11 个有
- `ImpactFloat` —— 4/11 个有
- `Int` —— 4/11 个有
- `SaveVideo` —— 4/11 个有
- `SetNode` —— 4/11 个有
- `SimpleMath+` —— 4/11 个有
- `MiniMaxH3ActivationChunkT8Advanced` —— 3/11 个有
- `ConcatTextOfUtils` —— 2/11 个有
- `LoadVideo` —— 2/11 个有
- `GetVideoComponents` —— 1/11 个有
- `LoadAudio` —— 1/11 个有
- `MiniMaxH3OutputTrimT8` —— 1/11 个有
- `MiniMaxH3ReferenceToVideo` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `SaveAudio` —— 1/11 个有
- `Video Slice` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
