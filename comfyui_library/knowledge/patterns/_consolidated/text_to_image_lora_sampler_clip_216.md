---
name: text_to_image_lora_sampler_clip_216
type: Text To Image
frequency: 6
level: strong
coverage: 0.901333
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3Director, MiniMaxH3MemoryEfficientSageAttentionPatch, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/AIMixer导演台｜MiniMaxH3文生图生视频生视频_2092871164078157825.json, 视频生成/文生视频/FZ-MinimaxH3视频导演台加速版｜像导演一样控片_2097202638852022273.json, 视频生成/文生视频/FZ-MinimaxH3视频导演台加速版｜文生视频图生视频生成_2097105561631412225.json, 视频生成/文生视频/H3导演台唱歌数字人版图生视频处理生成工具_2102196028790366209.json, 视频生成/文生视频/H3导演台工作流，文生视频视频生视频图生视频全覆盖方案_2106116054211710977.json, 视频生成/文生视频/MiniMax H3导演台全能工作流｜文生视频多模式生成_2097523465933905921.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_216

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/AIMixer导演台｜MiniMaxH3文生图生视频生视频_2092871164078157825.json、视频生成/文生视频/FZ-MinimaxH3视频导演台加速版｜像导演一样控片_2097202638852022273.json、视频生成/文生视频/FZ-MinimaxH3视频导演台加速版｜文生视频图生视频生成_2097105561631412225.json、视频生成/文生视频/H3导演台唱歌数字人版图生视频处理生成工具_2102196028790366209.json、视频生成/文生视频/H3导演台工作流，文生视频视频生视频图生视频全覆盖方案_2106116054211710977.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PathchSageAttentionKJ` —— 5/6 个有
- `PreviewAny` —— 5/6 个有
- `SaveImage` —— 4/6 个有
- `BasicGuider` —— 3/6 个有
- `MiniMaxH3DirectorRefine` —— 3/6 个有
- `BasicScheduler` —— 2/6 个有
- `LoadAudio` —— 2/6 个有
- `LoadImage` —— 2/6 个有
- `ManualSigmas` —— 2/6 个有
- `MiniMaxH3DirectorGroupReferenceToVideo` —— 2/6 个有
- `MiniMaxH3DirectorGroupsCombine` —— 2/6 个有
- `KSamplerSelect` —— 1/6 个有
- `LTXVConcatAVLatent` —— 1/6 个有
- `LTXVSeparateAVLatent` —— 1/6 个有
- `MiniMaxH3LatentUpscaleBy32T8` —— 1/6 个有
- `ModelAttentionBackend` —— 1/6 个有
- `SamplerCustomAdvanced` —— 1/6 个有
- `TrimAudioDuration` —— 1/6 个有
- `UpscaleModelLoader` —— 1/6 个有
- `VAEEncode` —— 1/6 个有
- `VHS_VideoCombine` —— 1/6 个有

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
