---
name: unknown_workflow_video_sampler_clip_201
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.806667
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, GetImageSizeAndCount, INTConstant, ImageBatchMulti, ImageResizeKJ, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, ModelSamplingSD3, VAEDecode, VHS_VideoCombine, WanVaceToVideo, WanVideoVACEStartToEndFrame, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/图像首尾帧（Wan2.2-aio-v12+QwenVL)_2001552417814638593.json, 视频生成/文生视频/mega-aio-v11+qwenvl-2图首尾帧_1985602110437961730.json, 视频生成/文生视频/mega-aio-v11+qwenvl多图首尾帧_1985602066460692482.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_201

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/图像首尾帧（Wan2.2-aio-v12+QwenVL)_2001552417814638593.json、视频生成/文生视频/mega-aio-v11+qwenvl-2图首尾帧_1985602110437961730.json、视频生成/文生视频/mega-aio-v11+qwenvl多图首尾帧_1985602066460692482.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `GetImageSizeAndCount`
- `INTConstant`
- `ImageBatchMulti`
- `ImageResizeKJ`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `ModelSamplingSD3`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoVACEStartToEndFrame`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `CR Image Size` —— 1/3 个有
- `GetImageRangeFromBatch` —— 1/3 个有
- `GetNode` —— 1/3 个有
- `MaskBatchMulti` —— 1/3 个有
- `Qwen3_VQA` —— 1/3 个有
- `SetNode` —— 1/3 个有
- `String Literal` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | ipndm | - | 3 | 100% |
| 调度器 | beta | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 ipndm，3 个样本，一致性 100%
- 调度器 最常用 beta，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
