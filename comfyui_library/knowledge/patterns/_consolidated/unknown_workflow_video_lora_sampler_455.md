---
name: unknown_workflow_video_lora_sampler_455
type: Unknown Workflow
frequency: 5
level: weak
coverage: 1
common_nodes: [CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, INTConstant, KSampler, LoraLoaderModelOnly, ModelSamplingSD3, PatchModelPatcherOrder, TorchCompileModelWanVideo, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVaceToVideo, WanVideoEnhanceAVideoKJ]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1924845181453934593.json, 视频生成/文生视频/1924863840855465985.json, 视频生成/文生视频/1928042156554862594.json, 视频生成/文生视频/VACE原生文生视频(CausVid与AccVideo10步对比)_2072999757184016384.json, 视频生成/文生视频/文生视频-Wan2.1-VACE-Native_2072999762233958400.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_455

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1924845181453934593.json、视频生成/文生视频/1924863840855465985.json、视频生成/文生视频/1928042156554862594.json、视频生成/文生视频/VACE原生文生视频(CausVid与AccVideo10步对比)_2072999757184016384.json、视频生成/文生视频/文生视频-Wan2.1-VACE-Native_2072999762233958400.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGZeroStarAndInit`
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `KSampler`
- `LoraLoaderModelOnly`
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
- `AIO_Preprocessor` —— 1/5 个有
- `Florence2ModelLoader` —— 1/5 个有
- `Florence2Run` —— 1/5 个有
- `GetImageSizeAndCount` —— 1/5 个有
- `ImageResizeKJ` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `LoadImage` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 5 - 20 | 5 | 45% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 5 | 25% |
| 采样算法 | uni_pc | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 5 - 20，5 个样本，取值分散，一致性仅 45%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，5 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 uni_pc，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
