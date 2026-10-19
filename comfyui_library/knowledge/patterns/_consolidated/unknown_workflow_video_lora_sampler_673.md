---
name: unknown_workflow_video_lora_sampler_673
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.940333
common_nodes: [CFGZeroStarAndInit, CLIPLoader, CLIPTextEncode, INTConstant, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PatchModelPatcherOrder, PreviewImage, TorchCompileModelWanVideo, TrimVideoLatent, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanVaceToVideo, WanVideoEnhanceAVideoKJ]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/1924839944982831106.json, 视频生成/图生视频/1924845197476175874.json, 视频生成/图生视频/1924845161095098369.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_673

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1924839944982831106.json、视频生成/图生视频/1924845197476175874.json、视频生成/图生视频/1924845161095098369.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGZeroStarAndInit`
- `CLIPLoader`
- `CLIPTextEncode`
- `INTConstant`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PatchModelPatcherOrder`
- `PreviewImage`
- `TorchCompileModelWanVideo`
- `TrimVideoLatent`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `WanVideoEnhanceAVideoKJ`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 2/3 个有
- `LayerMask: LoadFlorence2Model` —— 2/3 个有
- `LayerMask: ObjectDetectorFL2` —— 2/3 个有
- `LayerMask: SAM2Ultra` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `GetImageSize` —— 1/3 个有
- `GrowMaskWithBlur` —— 1/3 个有
- `Image Blank` —— 1/3 个有
- `ImageCompositeMasked` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageResizeKJv2` —— 1/3 个有
- `InpaintPreprocessor` —— 1/3 个有
- `LayerUtility: PurgeVRAM V2` —— 1/3 个有
- `VHS_LoadVideo` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 5 - 20 | 3 | 53% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 3 | 53% |
| 采样算法 | uni_pc | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 5 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，3 个样本
- 采样算法 最常用 uni_pc，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
