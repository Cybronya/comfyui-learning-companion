---
name: unknown_workflow_video_sampler_clip_60
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.6673
common_nodes: [CLIPLoader, CLIPTextEncode, GetImageSizeAndCount, INTConstant, ImageLoader, ImageResizeKJ, ImpactFloat, LayerUtility: ImageScaleByAspectRatio V2, PathchSageAttentionKJ, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine, WanFirstLastFrameToVideo, WanMoeKSampler, WanVideoNAG, easy int, easy positive, easy seed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/100.首尾帧生成视频_2003823135168339969.json, 视频生成/图生视频/首尾帧_图生视频_Wan2.2_RemixV2(亲测稳定)_1986710201665581058.json, 视频生成/图生视频/首尾帧图生视频wan2.2_2003745744496541698.json, 视频生成/图生视频/首尾帧视频扩写-wan2.2-smoothMix-官方_1998710144752046081.json, 视频生成/图生视频/首尾帧视频扩写-wan2.2-smoothMix-官方_2009163344107806722.json, 视频生成/图生视频/首尾帧视频扩写-wan2.2-smoothMix_2006637796416561154.json, 视频生成/图生视频/首尾帧视频扩写_2018215388487618561.json, 视频生成/图生视频/高效首尾帧视频扩写-wan2.2-smoothMix-官方_1998783558367989762.json, 视频生成/图生视频/🔥首尾帧视频扩写-wan2.2-smoothMix 通义万相 首尾帧视频动画生成_2004366389764915202.json, 视频生成/文生视频/首尾帧视频扩写-wan2.2-smoothMix-官方_2004136060017909761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_60

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/100.首尾帧生成视频_2003823135168339969.json、视频生成/图生视频/首尾帧_图生视频_Wan2.2_RemixV2(亲测稳定)_1986710201665581058.json、视频生成/图生视频/首尾帧图生视频wan2.2_2003745744496541698.json、视频生成/图生视频/首尾帧视频扩写-wan2.2-smoothMix-官方_1998710144752046081.json、视频生成/图生视频/首尾帧视频扩写-wan2.2-smoothMix-官方_2009163344107806722.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：67%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageLoader`
- `ImageResizeKJ`
- `ImpactFloat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`
- `WanFirstLastFrameToVideo`
- `WanMoeKSampler`
- `WanVideoNAG`
- `easy int`
- `easy positive`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 9/10 个有
- `MathExpression|pysssss` —— 9/10 个有
- `MultiplePathsInput` —— 9/10 个有
- `PreviewImage` —— 9/10 个有
- `PrimitiveFloat` —— 9/10 个有
- `Qwen3_VQA` —— 9/10 个有
- `SetNode` —— 9/10 个有
- `StringFunction|pysssss` —— 9/10 个有
- `easy anythingIndexSwitch` —— 9/10 个有
- `ImageFromBatch` —— 8/10 个有
- `MemoryCleaner` —— 8/10 个有
- `ModelBlockSwap` —— 8/10 个有
- `easy imageSize` —— 8/10 个有
- `CLIPVisionEncode` —— 1/10 个有
- `CLIPVisionLoader` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 10 | 100% |
| Prompt 约束强度(CFG) | 20 | 20 - 20 | 10 | 100% |
| 采样算法 | 1 | 1 - 1 | 10 | 100% |
| 调度器 | 1 | 1 - 1 | 10 | 100% |
| 重绘幅度 | sa_solver | - | 10 | 90% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，10 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，观测区间 20 - 20，10 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 sa_solver，10 个样本，一致性 90%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
