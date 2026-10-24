---
name: unknown_workflow_video_clip_vae
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.982769
common_nodes: [CLIPTextEncode, GetImageSizeAndCount, INTConstant, ImageResizeKJv2, LoadImage, ModelSamplingSD3, TrimVideoLatent, VAEDecode, VHS_VideoCombine, WanVaceToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/动作迁移MEGA Merge-WAN2.2-AllInOne_1968870212063907841.json, 视频生成/图生视频/动作迁移MEGA_V3-WAN2.2-AllInOne_1969999111397253122.json, 视频生成/图生视频/图生视频-MEGA Merge-WAN2.2-AllInOne_1968839523046236161.json, 视频生成/图生视频/图生视频-MEGA V3-WAN2.2-AllInOne_1969992617129897986.json, 视频生成/图生视频/首尾帧视频-MEGA_Merge-WAN2.2-AllInOne_1968865825916690433.json, 视频生成/图生视频/首尾帧视频-MEGA_V3-WAN2.2-AllInOne_1969995701813977090.json, 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-图生视频_1968252013240832002.json, 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-姿态视频引导加参考_1968251354269536257.json, 视频生成/文生视频/MEGA Merge-WAN2.2-AllInOne-首尾帧_1968252973186994178.json, 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-图生视频_1982048372632764418.json, 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-姿态视频引导加参考_1982051642445045761.json, 视频生成/文生视频/MEGA-v10-WAN2.2-AllInOne-首尾帧_1982051197618135041.json, 视频生成/文生视频/Wan 2.2-Fun-VACE-姿态视频引导加参考无敌控_1967578038525390850.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_vae

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（视频生成/图生视频/动作迁移MEGA Merge-WAN2.2-AllInOne_1968870212063907841.json、视频生成/图生视频/动作迁移MEGA_V3-WAN2.2-AllInOne_1969999111397253122.json、视频生成/图生视频/图生视频-MEGA Merge-WAN2.2-AllInOne_1968839523046236161.json、视频生成/图生视频/图生视频-MEGA V3-WAN2.2-AllInOne_1969992617129897986.json、视频生成/图生视频/首尾帧视频-MEGA_Merge-WAN2.2-AllInOne_1968865825916690433.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPTextEncode`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `ModelSamplingSD3`
- `TrimVideoLatent`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 12/13 个有
- `CheckpointLoaderSimple` —— 9/13 个有
- `WanVideoVACEStartToEndFrame` —— 8/13 个有
- `AIO_Preprocessor` —— 5/13 个有
- `Miaoshouai_Tagger` —— 5/13 个有
- `VHS_LoadVideo` —— 5/13 个有
- `CLIPLoader` —— 4/13 个有
- `PrimitiveStringMultiline` —— 4/13 个有
- `UNETLoader` —— 4/13 个有
- `AV_VAELoader` —— 3/13 个有
- `ImageRepeat` —— 2/13 个有
- `KSamplerAdvanced` —— 1/13 个有
- `LoraLoaderModelOnly` —— 1/13 个有
- `VAELoader` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 6 | 12 | 84% |
| Prompt 约束强度(CFG) | 1 | 1 - 6 | 13 | 4% |
| 采样算法 | euler | - | 13 | 69% |
| 调度器 | beta | - | 13 | 92% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 6，12 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 6，13 个样本，取值分散，一致性仅 4%
- 采样算法 最常用 euler，13 个样本，一致性 69%
- 调度器 最常用 beta，13 个样本，一致性 92%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（12/13 个样本）：Steps较低可能导致细节不足
