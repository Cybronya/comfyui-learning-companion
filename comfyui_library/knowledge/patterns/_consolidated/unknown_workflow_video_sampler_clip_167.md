---
name: unknown_workflow_video_sampler_clip_167
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.95825
common_nodes: [CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingSD3, PatchModelPatcherOrder, TorchCompileModelWanVideo, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVaceToVideo, WanVideoEnhanceAVideoKJ]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/VACE首尾帧_1929030828502978562.json, 视频生成/图生视频/首尾帧-Wan2.1-VACE-Native_1925061035089457154.json, 视频生成/文生视频/VACE原生文生视频(CausVid与AccVideo10步对比)_1928042156554862594.json, 视频生成/文生视频/文生视频-Wan2.1-VACE-Native_1924863840855465985.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_167

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/VACE首尾帧_1929030828502978562.json、视频生成/图生视频/首尾帧-Wan2.1-VACE-Native_1925061035089457154.json、视频生成/文生视频/VACE原生文生视频(CausVid与AccVideo10步对比)_1928042156554862594.json、视频生成/文生视频/文生视频-Wan2.1-VACE-Native_1924863840855465985.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGZeroStarAndInit`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingSD3`
- `PatchModelPatcherOrder`
- `TorchCompileModelWanVideo`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoEnhanceAVideoKJ`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 3/4 个有
- `LoraLoaderModelOnly` —— 3/4 个有
- `GetImageSizeAndCount` —— 2/4 个有
- `ImageResizeKJ` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `String Literal` —— 2/4 个有
- `WanVideoVACEStartToEndFrame` —— 2/4 个有
- `ImageUpscaleWithModel` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `RIFE VFI` —— 1/4 个有
- `UpscaleModelLoader` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 15 | 5 - 20 | 4 | 53% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 4 | 4 | 40% |
| 采样算法 | uni_pc | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 15，观测区间 5 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 4，4 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 uni_pc，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
