---
name: unknown_workflow_video_sampler_clip_37
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.843167
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, LoadImage, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/首尾帧：wan2.2-rapid-mega-aio-V3 工作流_1970185315388452866.json, 图片生成/文生图/文生视频-AIO-MegaV7 (2)_2051834619032555521.json, 图片生成/文生图/极致简单好用的工作流  Want2.2-Rapid-Mega-AIO-V12 工作流_1987118145712361473.json, 视频生成/图生视频/wan2.2图生视频：wan2.2-rapid-mega-aio V10最新工作流_1970170134423871490.json, 视频生成/图生视频/图生视频-AIO-MegaV7_1968180543949012994.json, 视频生成/图生视频/图生视频-AIO-Mega【V3】_1970828010674888705.json, 视频生成/文生视频/【极速生成】wan2.2 rapid首尾帧视频动画生成【AIO Mega版】_1969276766730809345.json, 视频生成/文生视频/文生视频+图生视频+首尾帧工作流_2046504485811396609.json, 视频生成/文生视频/文生视频+图生视频+首尾帧工作流_2046752274625597441.json, 视频生成/文生视频/文生视频+图生视频+首尾帧工作流_2046762436140736513.json, 视频生成/文生视频/文生视频+图生视频+首尾帧工作流（Wan2.2-Rapid-AIO-Mega）_2044790035236528130.json, 视频生成/文生视频/文生视频+图生视频+首尾帧工作流（Wan2.2-Rapid-AIO-Mega）_2048651987276800002.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_37

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/首尾帧：wan2.2-rapid-mega-aio-V3 工作流_1970185315388452866.json、图片生成/文生图/文生视频-AIO-MegaV7 (2)_2051834619032555521.json、图片生成/文生图/极致简单好用的工作流  Want2.2-Rapid-Mega-AIO-V12 工作流_1987118145712361473.json、视频生成/图生视频/wan2.2图生视频：wan2.2-rapid-mega-aio V10最新工作流_1970170134423871490.json、视频生成/图生视频/图生视频-AIO-MegaV7_1968180543949012994.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：84%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 10/12 个有
- `PrimitiveInt` —— 9/12 个有
- `Fast Groups Bypasser (rgthree)` —— 6/12 个有
- `CM_IntToFloat` —— 5/12 个有
- `SimpleMath+` —— 5/12 个有
- `easy cleanGpuUsed` —— 3/12 个有
- `easy clearCacheAll` —— 3/12 个有
- `Int` —— 2/12 个有
- `Label (rgthree)` —— 1/12 个有
- `LoadAudio` —— 1/12 个有
- `MathExpression|pysssss` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 12 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | ipndm | - | 12 | 75% |
| 调度器 | beta | - | 12 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 14/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，12 个样本，一致性 75%
- 调度器 最常用 beta，12 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（14/12 个样本）：Steps较低可能导致细节不足
