---
name: unknown_workflow_video_sampler_clip_35
type: Unknown Workflow
frequency: 13
level: strong
coverage: 0.978692
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, GetImageSizeAndCount, INTConstant, ImageResizeKJv2, KSampler, LoadImage, ModelSamplingSD3, TrimVideoLatent, VAEDecode, VHS_VideoCombine, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1968870212063907841.json, 视频生成/图生视频/1969999111397253122.json, 视频生成/图生视频/1968839523046236161.json, 视频生成/图生视频/1969992617129897986.json, 视频生成/图生视频/1968865825916690433.json, 视频生成/图生视频/1969995701813977090.json, 视频生成/文生视频/1968251354269536257.json, 视频生成/文生视频/1968252013240832002.json, 视频生成/文生视频/1968252973186994178.json, 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-图生视频_2072999568805240832.json, 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-姿态视频引导加参考_2072999569325334528.json, 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-首尾帧_2072999567903465472.json, 视频生成/文生视频/mega-aio-v11+qwenvl姿态引导_1985633536239644673.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_35

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/1968870212063907841.json、视频生成/图生视频/1969999111397253122.json、视频生成/图生视频/1968839523046236161.json、视频生成/图生视频/1969992617129897986.json、视频生成/图生视频/1968865825916690433.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageResizeKJv2`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `TrimVideoLatent`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `WanVideoVACEStartToEndFrame` —— 8/13 个有
- `AIO_Preprocessor` —— 5/13 个有
- `VHS_LoadVideo` —— 5/13 个有
- `Miaoshouai_Tagger` —— 4/13 个有
- `PrimitiveStringMultiline` —— 4/13 个有
- `ImageRepeat` —— 2/13 个有
- `AILab_QwenVL` —— 1/13 个有
- `LayerUtility: PurgeVRAM V2` —— 1/13 个有
- `easy showAnything` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 13 | 91% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 13 | 100% |
| 采样算法 | euler | - | 13 | 92% |
| 调度器 | beta | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，13 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，13 个样本，一致性 92%
- 调度器 最常用 beta，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
- 高发问题（13/13 个样本）：Steps较低可能导致细节不足
