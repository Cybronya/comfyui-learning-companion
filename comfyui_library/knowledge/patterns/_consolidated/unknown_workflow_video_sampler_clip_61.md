---
name: unknown_workflow_video_sampler_clip_61
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.786111
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, KSampler, LoadImage, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1969029965058633729.json, 视频生成/图生视频/1968298916649283585.json, 视频生成/图生视频/2013075887306055682.json, 视频生成/图生视频/1968180543949012994.json, 视频生成/图生视频/1968176738117255170.json, 视频生成/文生视频/01 Wan2.2 Smooth Mix I2V 图生视频+全节点注释_2055497064678739970.json, 视频生成/文生视频/1968182535878488065.json, 视频生成/文生视频/1970121529851867137.json, 视频生成/文生视频/1969033295201792002.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_61

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1969029965058633729.json、视频生成/图生视频/1968298916649283585.json、视频生成/图生视频/2013075887306055682.json、视频生成/图生视频/1968180543949012994.json、视频生成/图生视频/1968176738117255170.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 9 个 workflow 都包含：
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
- `PrimitiveInt` —— 7/9 个有
- `INTConstant` —— 5/9 个有
- `wanBlockSwap` —— 2/9 个有
- `CreateVideo` —— 1/9 个有
- `DuckHideNode` —— 1/9 个有
- `ImageScaleByAspectRatio_UTK` —— 1/9 个有
- `PreViewVideo` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 7 | 9 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | ipndm | - | 9 | 56% |
| 调度器 | beta | - | 9 | 56% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 7，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，9 个样本，一致性 56%
- 调度器 最常用 beta，9 个样本，一致性 56%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
