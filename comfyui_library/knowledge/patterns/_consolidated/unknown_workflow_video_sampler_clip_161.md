---
name: unknown_workflow_video_sampler_clip_161
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.819
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, LoadImage, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Wan2.2-ALL IN ONE-MEGA-极速首尾帧_1969029965058633729.json, 视频生成/图生视频/wan2.2 rapid-aio-mega all in one图生视频+首尾帧【gen全能视频Si】_1968298916649283585.json, 视频生成/图生视频/wan2.2图生视频_2013075887306055682.json, 视频生成/文生视频/Wan2.2-ALL IN ONE-MEGA-极速文生视频_1969033295201792002.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_161

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-ALL IN ONE-MEGA-极速首尾帧_1969029965058633729.json、视频生成/图生视频/wan2.2 rapid-aio-mega all in one图生视频+首尾帧【gen全能视频Si】_1968298916649283585.json、视频生成/图生视频/wan2.2图生视频_2013075887306055682.json、视频生成/文生视频/Wan2.2-ALL IN ONE-MEGA-极速文生视频_1969033295201792002.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
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
- `PrimitiveInt` —— 3/4 个有
- `wanBlockSwap` —— 2/4 个有
- `CreateVideo` —— 1/4 个有
- `DuckHideNode` —— 1/4 个有
- `INTConstant` —— 1/4 个有
- `ImageScaleByAspectRatio_UTK` —— 1/4 个有
- `PreViewVideo` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | ipndm | - | 4 | 75% |
| 调度器 | sgm_uniform | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，4 个样本，一致性 75%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
