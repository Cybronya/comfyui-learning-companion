---
name: text_to_image_lora_sampler_clip_208
type: Text To Image
frequency: 4
level: strong
coverage: 0.8455
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EasyCache, EmptyLatentImage, ImageResizeKJv2, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, PT_H3ConcatAVLatent, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEDecodeAudio, VAEEncode, VAEEncodeAudio, VAELoader, easy clearCacheAll, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Minimax-H3 4步加速单图参考二次采样｜官方节点版文生视频图生视频_2090411973430304769.json, 视频生成/文生视频/二采重绘V2｜H3海螺视频画质增强高清直出_2090143662247333890.json, 视频生成/文生视频/双采高清人脸视频生成｜Minimax自动提示词加最新加速lora_2088767793599700993.json, 视频生成/文生视频/海螺H3二采重绘V2｜文生视频其它视频处理图生视频_2090420618834563073.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_208

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/Minimax-H3 4步加速单图参考二次采样｜官方节点版文生视频图生视频_2090411973430304769.json、视频生成/文生视频/二采重绘V2｜H3海螺视频画质增强高清直出_2090143662247333890.json、视频生成/文生视频/双采高清人脸视频生成｜Minimax自动提示词加最新加速lora_2088767793599700993.json、视频生成/文生视频/海螺H3二采重绘V2｜文生视频其它视频处理图生视频_2090420618834563073.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
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
- `AudioCrop` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `LoadAudio` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `RHLLMChatNode` —— 3/4 个有
- `StringFunction|pysssss` —— 3/4 个有
- `VHS_LoadVideo` —— 3/4 个有
- `VHS_VideoCombine` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `FloatConstant` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `PurgeVRAM_UTK` —— 2/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `Float` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `LoadVideo` —— 1/4 个有
- `LoraLoaderBypassModelOnly` —— 1/4 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 1/4 个有
- `RTXVideoSuperResolution` —— 1/4 个有
- `ResizeShortestToNode` —— 1/4 个有
- `SaveVideo` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `Text` —— 1/4 个有
- `VRAMReserver` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `忽略多组孤海` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 4 | 100% |
| 高度 | 80 | 80 - 80 | 4 | 100% |
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 4 | 100% |
| 采样算法 | er_sde | - | 4 | 100% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，4 个样本，一致性 100%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
