---
name: text_to_image_video_upscale_latent_upscale_5
type: Text To Image
frequency: 12
level: strong
coverage: 0.947
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3LearnedLatentUpscaleT8Advanced, MiniMaxH3LearnedTwoPassParityPlanT8Advanced, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3TwoPassDetailMixerT8Advanced, MiniMaxH3TwoPassLatentReconcileT8Advanced, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SolAttnMiniMax, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/H3 720P文戏均衡画质加强工作流，图生视频高质量文戏创作工具_2106163296528330753.json, 视频生成/图生视频/H3 POV视角720P超采样版工作流，图生视频第一人称视角创作方案_2106905984181563394.json, 视频生成/图生视频/H3-POV第一人称视角｜720p超采样图生视频_2106607588157771778.json, 视频生成/图生视频/H3_POV视角720P超采样版工作流，图生视频第一人称视角创作方案_2108378553988501505.json, 视频生成/图生视频/H3双采参考生视频Dasiwa V2版本对白战斗动作戏_2100636081782874114.json, 视频生成/图生视频/H3双采参考生视频V2 文戏武戏低显存适配版_2098846488892887041.json, 视频生成/图生视频/MiniMax H3全能参考9图3音频｜HyperVae 2X高清画质输出_2111077634724679682.json, 视频生成/图生视频/MiniMax H3多图参考双采生视频｜HyperVae 2X高清图生视频_2111058302082830338.json, 视频生成/图生视频/MiniMax H3多图参考双采，HyperVae 2X高清图生视频_2111259409954459649.json, 视频生成/图生视频/格莱美慢镜头质感 MiniMax H3双采参考生视频动态可控_2104360820577759233.json, 视频生成/文生视频/MiniMax H3文武双修均衡版 20秒长视频双采多参考图生视频HyperVae 2X高清_2105117710463098882.json, 视频生成/文生视频/MiniMax H3文武双修均衡版｜20秒长视频双采多参考｜HyperVae 2X高清_2104829141102190593.json]
source: knowledge_consolidation
---

# text_to_image_video_upscale_latent_upscale_5

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/H3 720P文戏均衡画质加强工作流，图生视频高质量文戏创作工具_2106163296528330753.json、视频生成/图生视频/H3 POV视角720P超采样版工作流，图生视频第一人称视角创作方案_2106905984181563394.json、视频生成/图生视频/H3-POV第一人称视角｜720p超采样图生视频_2106607588157771778.json、视频生成/图生视频/H3_POV视角720P超采样版工作流，图生视频第一人称视角创作方案_2108378553988501505.json、视频生成/图生视频/H3双采参考生视频Dasiwa V2版本对白战斗动作戏_2100636081782874114.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 12 个 workflow 都包含：
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
- `Float` —— 11/12 个有
- `MiniMaxH3AudioConditioningT8` —— 11/12 个有
- `easy anythingIndexSwitch` —— 11/12 个有
- `孤海注释` —— 11/12 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 9/12 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 9/12 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 9/12 个有
- `easy cleanGpuUsed` —— 9/12 个有
- `RunningHub Deepcleaner` —— 8/12 个有
- `SaveImage` —— 8/12 个有
- `ImageCrop` —— 5/12 个有
- `MiniMaxH3HyperVAE2xLoaderEXPT8` —— 5/12 个有
- `MiniMaxH3OutputTrimT8` —— 5/12 个有
- `GetImageSize` —— 4/12 个有
- `ImageScale` —— 4/12 个有
- `ConcatTextOfUtils` —— 3/12 个有
- `VHS_LoadVideo` —— 3/12 个有
- `VHS_LoadAudioUpload` —— 2/12 个有
- `Fast Muter (rgthree)` —— 1/12 个有
- `GetVideoComponents` —— 1/12 个有
- `ImageFromBatch` —— 1/12 个有
- `LoadAudio` —— 1/12 个有
- `LoadVideo` —— 1/12 个有
- `MiniMaxH3ReferenceToVideo` —— 1/12 个有
- `PreviewImage` —— 1/12 个有
- `PrimitiveInt` —— 1/12 个有
- `SaveAudio` —— 1/12 个有
- `TrimAudioDuration` —— 1/12 个有
- `Video Slice` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 12 | 100% |
| 采样算法 | er_sde | - | 12 | 100% |
| 调度器 | beta | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 80 | 80 - 80 | 12 | 100% |
| 高度 | 80 | 80 - 80 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，12 个样本，一致性 100%
- 调度器 最常用 beta，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，12 个样本，取值集中（一致性 100%）
- 高发问题（12/12 个样本）：Steps较低可能导致细节不足
