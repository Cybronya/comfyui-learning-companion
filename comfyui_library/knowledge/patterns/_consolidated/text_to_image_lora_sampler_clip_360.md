---
name: text_to_image_lora_sampler_clip_360
type: Text To Image
frequency: 6
level: strong
coverage: 0.7935
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EasyCache, EmptyLatentImage, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PT_H3ConcatAVLatent, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAEEncodeAudio, VAELoader, easy clearCacheAll, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Minimax-H3 4步加速单图参考二次采样｜官方节点版文生视频图生视频_2090411973430304769.json, 视频生成/文生视频/二采重绘V2｜H3海螺视频画质增强高清直出_2090143662247333890.json, 视频生成/文生视频/双采高清人脸视频生成｜Minimax自动提示词加最新加速lora_2088767793599700993.json, 视频生成/文生视频/海螺H3二采重绘V2｜文生视频其它视频处理图生视频_2090420618834563073.json, 视频生成/视频生视频/双模型加强版二采重绘MiniMax H3全能参考RH兼容版，9图参考图生视频_2106499744423043074.json, 视频生成/视频生视频/双模型加强版二采重绘｜MinimaxH3全能参考图生视频RH兼容版_2106194718110609410.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_360

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/Minimax-H3 4步加速单图参考二次采样｜官方节点版文生视频图生视频_2090411973430304769.json、视频生成/文生视频/二采重绘V2｜H3海螺视频画质增强高清直出_2090143662247333890.json、视频生成/文生视频/双采高清人脸视频生成｜Minimax自动提示词加最新加速lora_2088767793599700993.json、视频生成/文生视频/海螺H3二采重绘V2｜文生视频其它视频处理图生视频_2090420618834563073.json、视频生成/视频生视频/双模型加强版二采重绘MiniMax H3全能参考RH兼容版，9图参考图生视频_2106499744423043074.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 6 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EasyCache`
- `EmptyLatentImage`
- `ImageResizeKJv2`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `PT_H3ConcatAVLatent`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAEEncode`
- `VAEEncodeAudio`
- `VAELoader`
- `easy clearCacheAll`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 5/6 个有
- `LoadAudio` —— 5/6 个有
- `PrimitiveStringMultiline` —— 5/6 个有
- `VHS_LoadVideo` —— 5/6 个有
- `VHS_VideoCombine` —— 5/6 个有
- `CreateVideo` —— 4/6 个有
- `AudioCrop` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 3/6 个有
- `GetNode` —— 3/6 个有
- `LoraLoaderBypassModelOnly` —— 3/6 个有
- `RHLLMChatNode` —— 3/6 个有
- `ResizeShortestToNode` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `StringFunction|pysssss` —— 3/6 个有
- `easy showAnything` —— 3/6 个有
- `FloatConstant` —— 2/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/6 个有
- `MiniMaxChunkFeedForward` —— 2/6 个有
- `MiniMaxLowVRAMAttention` —— 2/6 个有
- `PurgeVRAM_UTK` —— 2/6 个有
- `TrimAudioDuration` —— 2/6 个有
- `UniBlockSwap` —— 2/6 个有
- `UniBlockSwapTE` —— 2/6 个有
- `Float` —— 1/6 个有
- `LoadVideo` —— 1/6 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/6 个有
- `RTXVideoSuperResolution` —— 1/6 个有
- `SaveImage` —— 1/6 个有
- `SaveVideo` —— 1/6 个有
- `Text` —— 1/6 个有
- `VRAMReserver` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有
- `忽略多组孤海` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 6 | 100% |
| 高度 | 80 | 80 - 80 | 6 | 100% |
| 采样步数 | 4 | 4 - 4 | 6 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
