---
name: unknown_workflow_video_sampler_clip_209
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.719333
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, ImageResizeKJv2, ImpactInt, KSamplerAdvanced, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveStringMultiline, RIFE VFI, Seed (rgthree), SetNode, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/一键换装+电商女装丝滑带货文图生视频工作流_2082688216334946306.json, 视频生成/图生视频/丝滑SmoothMix模型文图生视频工作流_2036515691074949121.json, 视频生成/图生视频/最强电商女装丝滑带货文图生视频工作流_2050045558773035009.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_209

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/一键换装+电商女装丝滑带货文图生视频工作流_2082688216334946306.json、视频生成/图生视频/丝滑SmoothMix模型文图生视频工作流_2036515691074949121.json、视频生成/图生视频/最强电商女装丝滑带货文图生视频工作流_2050045558773035009.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：72%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `ImageResizeKJv2`
- `ImpactInt`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `RIFE VFI`
- `Seed (rgthree)`
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CropWithPadInfo` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `KSampler` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `QwenEditConfigPreparer` —— 1/3 个有
- `QwenEditOutputExtractor` —— 1/3 个有
- `Text` —— 1/3 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 67% |
| Prompt 约束强度(CFG) | 6 | 1 - 6 | 3 | 46% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler_ancestral | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 67% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 6，观测区间 1 - 6，3 个样本，取值分散，一致性仅 46%
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 67%
