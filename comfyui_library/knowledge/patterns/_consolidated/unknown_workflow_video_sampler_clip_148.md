---
name: unknown_workflow_video_sampler_clip_148
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.951
common_nodes: [CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CheckpointLoaderSimple, KSampler, LoadImage, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, WanImageToVideo]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2014328712942067713.json, 视频生成/图生视频/1970121506326016002.json, 视频生成/文生视频/1962424661311098882.json, 视频生成/文生视频/WAN2.2-AllInOne的文生视频&图生视频_2072999615055831040.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_148

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2014328712942067713.json、视频生成/图生视频/1970121506326016002.json、视频生成/文生视频/1962424661311098882.json、视频生成/文生视频/WAN2.2-AllInOne的文生视频&图生视频_2072999615055831040.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `KSampler`
- `LoadImage`
- `ModelSamplingSD3`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanImageToVideo`

**可变部分**（部分 workflow 才有）：
- `EmptyHunyuanLatentVideo` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `PreviewImage` —— 2/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler_ancestral | - | 4 | 50% |
| 调度器 | beta | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler_ancestral，4 个样本，一致性 50%
- 调度器 最常用 beta，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（6/4 个样本）：Steps较低可能导致细节不足
