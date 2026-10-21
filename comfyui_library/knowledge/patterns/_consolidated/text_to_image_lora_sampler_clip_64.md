---
name: text_to_image_lora_sampler_clip_64
type: Text To Image
frequency: 13
level: strong
coverage: 0.939
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, LoadImage, LoraLoaderBypassModelOnly, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3DualClockSamplerT8, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/3段合成双时钟双采｜T8公共参考Lantent Upscaler加速_2093837736695386114.json, 视频生成/图生视频/5段合成双采加速｜T8公共参考Lantent Upscaler超真实_2093818227938914306.json, 视频生成/图生视频/8步去油双时钟参考生视频V2｜Lightx2v正式版Minimax图生视频_2088160534666502145.json, 视频生成/图生视频/BUNNY_H3高动态双采放大｜FL2VA_REF2VA专属｜打斗图生视频专用_2101851538271588353.json, 视频生成/图生视频/Eros Beta4电影感加速｜Minimax H3 Upscaler参考生视频_2095125881621663746.json, 视频生成/图生视频/H3 720P文戏均衡画质加强工作流，图生视频高质量文戏创作工具_2106163296528330753.json, 视频生成/图生视频/H3 POV视角720P超采样版工作流，图生视频第一人称视角创作方案_2106905984181563394.json, 视频生成/图生视频/H3-POV第一人称视角｜720p超采样图生视频_2106607588157771778.json, 视频生成/图生视频/H3_POV视角720P超采样版工作流，图生视频第一人称视角创作方案_2108378553988501505.json, 视频生成/图生视频/H3双采参考生视频Dasiwa V2版本对白战斗动作戏_2100636081782874114.json, 视频生成/图生视频/H3双采参考生视频V2 文戏武戏低显存适配版_2098846488892887041.json, 视频生成/图生视频/MiniMax H3全能参考9图3音频｜HyperVae 2X高清画质输出_2111077634724679682.json, 视频生成/文生视频/10Eros Beta5+FL2VA Ref2VA小脸去油二采精修视频处理工具_2102108154879369218.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_64

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/3段合成双时钟双采｜T8公共参考Lantent Upscaler加速_2093837736695386114.json、视频生成/图生视频/5段合成双采加速｜T8公共参考Lantent Upscaler超真实_2093818227938914306.json、视频生成/图生视频/8步去油双时钟参考生视频V2｜Lightx2v正式版Minimax图生视频_2088160534666502145.json、视频生成/图生视频/BUNNY_H3高动态双采放大｜FL2VA_REF2VA专属｜打斗图生视频专用_2101851538271588353.json、视频生成/图生视频/Eros Beta4电影感加速｜Minimax H3 Upscaler参考生视频_2095125881621663746.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 13 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoadImage`
- `LoraLoaderBypassModelOnly`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3DualClockSamplerT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 12/13 个有
- `MiniMaxH3AudioConditioningT8` —— 12/13 个有
- `MiniMaxH3LearnedLatentUpscaleT8Advanced` —— 12/13 个有
- `MiniMaxH3LearnedTwoPassParityPlanT8Advanced` —— 12/13 个有
- `MiniMaxH3TwoPassDetailMixerT8Advanced` —— 12/13 个有
- `MiniMaxH3TwoPassLatentReconcileT8Advanced` —— 12/13 个有
- `SolAttnMiniMax` —— 12/13 个有
- `VHS_VideoCombine` —— 12/13 个有
- `孤海注释` —— 12/13 个有
- `Float` —— 6/13 个有
- `SaveImage` —— 6/13 个有
- `easy anythingIndexSwitch` —— 6/13 个有
- `LoadAudio` —— 5/13 个有
- `MiniMaxH3ChunkFeedForwardT8Advanced` —— 5/13 个有
- `easy cleanGpuUsed` —— 5/13 个有
- `GetImageSize` —— 4/13 个有
- `ImageCrop` —— 4/13 个有
- `ImageScale` —— 4/13 个有
- `MiniMaxH3SemanticBridgeApplyT8` —— 4/13 个有
- `MiniMaxH3SemanticBridgeConfigT8` —— 4/13 个有
- `RunningHub Deepcleaner` —— 4/13 个有
- `ConcatTextOfUtils` —— 3/13 个有
- `AudioConcat` —— 2/13 个有
- `CreateVideo` —— 2/13 个有
- `GetVideoComponents` —— 2/13 个有
- `ImageBatch` —— 2/13 个有
- `LoadVideo` —— 2/13 个有
- `MiniMaxH3MotionContext` —— 2/13 个有
- `MiniMaxH3MotionContextTrim` —— 2/13 个有
- `SaveVideo` —— 2/13 个有
- `Video Slice` —— 2/13 个有
- `AudioCrop` —— 1/13 个有
- `MiniMaxH3HyperVAE2xLoaderEXPT8` —— 1/13 个有
- `MiniMaxH3OutputTrimT8` —— 1/13 个有
- `MiniMaxH3ReferenceToVideo` —— 1/13 个有
- `ModelPreviewOverrideKJ` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `PrimitiveStringMultiline` —— 1/13 个有
- `SaveAudio` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 13 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 13 | 100% |
| 采样算法 | er_sde | - | 13 | 100% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |
| 宽度 | 80 | 80 - 80 | 13 | 100% |
| 高度 | 80 | 80 - 80 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，13 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，13 个样本，一致性 100%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
