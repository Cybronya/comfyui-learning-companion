---
name: text_to_image_video_lora_sampler_183
type: Text To Image
frequency: 3
level: strong
coverage: 0.709
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadAudio, LoadImage, LoraLoaderModelOnly, MiniMaxH3AVDecodeT8, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/8步二次采样1088p多参视频｜MinimaxH3文生图生视频生视频工作流_2088128342645104641.json, 视频生成/文生视频/MinimaxH3全能参考电影质感V2｜高质量视频生成_2094884318077345793.json, 视频生成/文生视频/电影质感V2｜MinimaxH3全能参考三模视频生成_2095082549973438466.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_183

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/8步二次采样1088p多参视频｜MinimaxH3文生图生视频生视频工作流_2088128342645104641.json、视频生成/文生视频/MinimaxH3全能参考电影质感V2｜高质量视频生成_2094884318077345793.json、视频生成/文生视频/电影质感V2｜MinimaxH3全能参考三模视频生成_2095082549973438466.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3AVDecodeT8`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Float` —— 2/3 个有
- `MiniMaxH3ConcatAVLatent` —— 2/3 个有
- `MinimaxH3LatentUpscaler3D` —— 2/3 个有
- `VHS_LoadVideo` —— 2/3 个有
- `easy clearCacheAll` —— 2/3 个有
- `忽略多组孤海` —— 2/3 个有
- `ConditioningZeroOut` —— 1/3 个有
- `HAIGC_VideoLoader` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `LTXVConcatAVLatent` —— 1/3 个有
- `MiniMaxH3BlockCacheT8` —— 1/3 个有
- `PrimitiveStringMultiline` —— 1/3 个有
- `UniBlockSwap` —— 1/3 个有
- `VAEEncode` —— 1/3 个有
- `VAEEncodeAudio` —— 1/3 个有
- `VRAM_Debug` —— 1/3 个有
- `easy ifElse` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 3 | 100% |
| 采样算法 | er_sde | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 80 | 80 - 80 | 3 | 100% |
| 高度 | 80 | 80 - 80 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
