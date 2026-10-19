---
name: unknown_workflow_video_sampler_clip_152
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.82875
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ColorMatch, DWPreprocessor, GetImageSizeAndCount, ImageBlend, ImageResizeKJv2, KSampler, LayerUtility: TextJoin, LoadImage, ModelSamplingSD3, PrimitiveInt, RH_Captioner, VAEDecode, VHS_LoadVideo, VHS_VideoCombine, WanVaceToVideo, Zoe-DepthMapPreprocessor]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1969267205433159682.json, 视频生成/图生视频/1970822875995377665.json, 视频生成/图生视频/1968309282762575874.json, 视频生成/图生视频/2074750685471657985.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_152

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1969267205433159682.json、视频生成/图生视频/1970822875995377665.json、视频生成/图生视频/1968309282762575874.json、视频生成/图生视频/2074750685471657985.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ColorMatch`
- `DWPreprocessor`
- `GetImageSizeAndCount`
- `ImageBlend`
- `ImageResizeKJv2`
- `KSampler`
- `LayerUtility: TextJoin`
- `LoadImage`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `RH_Captioner`
- `VAEDecode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `Zoe-DepthMapPreprocessor`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `PathchSageAttentionKJ` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | ipndm | - | 4 | 50% |
| 调度器 | sgm_uniform | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，4 个样本，一致性 50%
- 调度器 最常用 sgm_uniform，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（4/4 个样本）：Steps较低可能导致细节不足
