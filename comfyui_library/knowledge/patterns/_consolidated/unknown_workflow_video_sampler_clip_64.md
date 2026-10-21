---
name: unknown_workflow_video_sampler_clip_64
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.651333
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageSizeAndCount, GetNode, INTConstant, ImageLoader, ImageResizeKJ, ImpactFloat, LayerUtility: ImageScaleByAspectRatio V2, MultiplePathsInput, PathchSageAttentionKJ, PreviewImage, Qwen3_VQA, SetNode, StringFunction|pysssss, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, WanMoeKSampler, WanVideoNAG, easy anythingIndexSwitch, easy int, easy positive, easy seed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1986710201665581058.json, 视频生成/图生视频/2003745744496541698.json, 视频生成/图生视频/1998710144752046081.json, 视频生成/图生视频/2009163344107806722.json, 视频生成/图生视频/2006637796416561154.json, 视频生成/图生视频/2018215388487618561.json, 视频生成/图生视频/1998783558367989762.json, 视频生成/图生视频/2004366389764915202.json, 视频生成/文生视频/首尾帧视频扩写-wan2.2-smoothMix-官方_2004136060017909761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_64

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1986710201665581058.json、视频生成/图生视频/2003745744496541698.json、视频生成/图生视频/1998710144752046081.json、视频生成/图生视频/2009163344107806722.json、视频生成/图生视频/2006637796416561154.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：65%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageLoader`
- `ImageResizeKJ`
- `ImpactFloat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MultiplePathsInput`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `Qwen3_VQA`
- `SetNode`
- `StringFunction|pysssss`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `WanMoeKSampler`
- `WanVideoNAG`
- `easy anythingIndexSwitch`
- `easy int`
- `easy positive`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch` —— 8/9 个有
- `MathExpression|pysssss` —— 8/9 个有
- `MemoryCleaner` —— 8/9 个有
- `ModelBlockSwap` —— 8/9 个有
- `PrimitiveFloat` —— 8/9 个有
- `easy imageSize` —— 8/9 个有
- `CLIPVisionEncode` —— 1/9 个有
- `CLIPVisionLoader` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 9 | 100% |
| Prompt 约束强度(CFG) | 20 | 20 - 20 | 9 | 100% |
| 采样算法 | 1 | 1 - 1 | 9 | 100% |
| 调度器 | 1 | 1 - 1 | 9 | 100% |
| 重绘幅度 | sa_solver | - | 9 | 89% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，9 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，观测区间 20 - 20，9 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 sa_solver，9 个样本，一致性 89%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
