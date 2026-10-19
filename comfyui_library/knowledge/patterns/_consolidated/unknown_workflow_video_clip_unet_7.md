---
name: unknown_workflow_video_clip_unet_7
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8598
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text Replace, DF_Integer, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, ModelSamplingSD3, PrimitiveBoolean, RH_Captioner, SimpleMath+, TextBox, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy ifElse, easy int, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [CR Text Replace, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, SimpleMath+, easy cleanGpuUsed, easy int]
members: [视频生成/图生视频/1950737220787458049.json, 视频生成/图生视频/1950763373552164866.json, 视频生成/图生视频/1950052256939950082.json, 视频生成/图生视频/1950373850129326082.json, 视频生成/图生视频/1950111733920784385.json, 视频生成/文生视频/1950878967190454273.json, 视频生成/文生视频/1951086042193571841.json, 视频生成/文生视频/wan2.2-14B+官方图生视频+自动提示词_1983353614280368130.json, 视频生成/文生视频/1950410149463769089.json, 视频生成/文生视频/1949867321068314625.json]
source: knowledge_consolidation
---

# unknown_workflow_video_clip_unet_7

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/1950737220787458049.json、视频生成/图生视频/1950763373552164866.json、视频生成/图生视频/1950052256939950082.json、视频生成/图生视频/1950373850129326082.json、视频生成/图生视频/1950111733920784385.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text Replace`
- `DF_Integer`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `ModelSamplingSD3`
- `PrimitiveBoolean`
- `RH_Captioner`
- `SimpleMath+`
- `TextBox`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy ifElse`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 8/10 个有
- `CLIPVisionLoader` —— 8/10 个有
- `KSamplerAdvanced` —— 8/10 个有
- `easy cleanGpuUsed` —— 8/10 个有
- `PatchModelPatcherOrder` —— 6/10 个有
- `PathchSageAttentionKJ` —— 6/10 个有
- `TorchCompileModelWanVideoV2` —— 6/10 个有
- `KSampler` —— 2/10 个有
- `Wan_video_prompt_generator` —— 2/10 个有
- `easy promptLine` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 10 | 60% |
| Prompt 约束强度(CFG) | 20 | 1 - 20 | 10 | 53% |
| 采样算法 | 3.5 | 3.5 - 3.5 | 8 | 100% |
| 调度器 | euler | - | 10 | 80% |
| 重绘幅度 | simple | - | 10 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，10 个样本，一致性 60%
- Prompt 约束强度(CFG) 中位数 20，观测区间 1 - 20，10 个样本
- 采样算法 中位数 3.5，观测区间 3.5 - 3.5，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，10 个样本，一致性 80%
- 重绘幅度 最常用 simple，10 个样本，一致性 80%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text Replace、LayerUtility: ImageScaleByAspectRatio V2、LayerUtility: PurgeVRAM、SimpleMath+、easy cleanGpuUsed
