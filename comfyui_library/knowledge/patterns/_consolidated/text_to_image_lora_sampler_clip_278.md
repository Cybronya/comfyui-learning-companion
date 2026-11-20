---
name: text_to_image_lora_sampler_clip_278
type: Text To Image
frequency: 8
level: strong
coverage: 0.87875
common_nodes: [CLIPLoader, CLIPTextEncode, CreateVideo, EmptyLatentImage, JjkText, KSampler, LoraLoaderModelOnly, MiniMaxH3Director, SaveVideo, UNETLoader, VAEDecode, VAELoader, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/AIMixer导演台｜MiniMaxH3文生图生视频生视频_2092871164078157825.json, 视频生成/文生视频/H3导演台唱歌数字人版图生视频处理生成工具_2102196028790366209.json, 视频生成/文生视频/H3导演台工作流，文生视频视频生视频图生视频全覆盖方案_2106116054211710977.json, 视频生成/文生视频/MiniMax H3导演台全能机｜灵感来了直接开拍，反推提示词免手写_2099411307467468802.json, 视频生成/文生视频/MiniMax H3导演台满血版工作流｜Ref2va全能视频生成_2097498585955917826.json, 视频生成/文生视频/MiniMax H3电影质感导演台二采放大分镜合成8步加速工具_2101033192529686530.json, 视频生成/文生视频/R2V）导演台全能工作流（外接参数版MiniMax_2086534641690963970.json, 视频生成/文生视频/导演台全能工作流外接参数版｜MiniMax H3参考生视频R2V_2097041962636500994.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_278

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/AIMixer导演台｜MiniMaxH3文生图生视频生视频_2092871164078157825.json、视频生成/文生视频/H3导演台唱歌数字人版图生视频处理生成工具_2102196028790366209.json、视频生成/文生视频/H3导演台工作流，文生视频视频生视频图生视频全覆盖方案_2106116054211710977.json、视频生成/文生视频/MiniMax H3导演台全能机｜灵感来了直接开拍，反推提示词免手写_2099411307467468802.json、视频生成/文生视频/MiniMax H3导演台满血版工作流｜Ref2va全能视频生成_2097498585955917826.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `LoraLoaderModelOnly`
- `MiniMaxH3Director`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 7/8 个有
- `PreviewAny` —— 7/8 个有
- `PathchSageAttentionKJ` —— 6/8 个有
- `LoadImage` —— 5/8 个有
- `MiniMaxH3DirectorRefine` —— 5/8 个有
- `SaveImage` —— 5/8 个有
- `LoadAudio` —— 4/8 个有
- `MiniMaxH3DirectorGroupReferenceToVideo` —— 4/8 个有
- `MiniMaxH3DirectorGroupsCombine` —— 4/8 个有
- `BasicScheduler` —— 3/8 个有
- `UpscaleModelLoader` —— 3/8 个有
- `VHS_LoadVideo` —— 2/8 个有
- `ManualSigmas` —— 1/8 个有
- `ModelAttentionBackend` —— 1/8 个有
- `PreviewImage` —— 1/8 个有
- `TrimAudioDuration` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 8 | 100% |
| 高度 | 80 | 80 - 80 | 8 | 100% |
| 采样步数 | 4 | 4 - 4 | 8 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 8 | 100% |
| 采样算法 | er_sde | - | 8 | 100% |
| 调度器 | beta | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，8 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，8 个样本，一致性 100%
- 调度器 最常用 beta，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
