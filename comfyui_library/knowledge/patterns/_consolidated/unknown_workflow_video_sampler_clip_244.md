---
name: unknown_workflow_video_sampler_clip_244
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.73
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, ImageResizeKJv2, ImpactInt, KSamplerAdvanced, LoadImage, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveStringMultiline, RIFE VFI, Seed (rgthree), SetNode, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/2082688216334946306.json, 视频生成/图生视频/2050045558773035009.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_244

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2082688216334946306.json、视频生成/图生视频/2050045558773035009.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
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
- `CropWithPadInfo` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `KSampler` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `QwenEditConfigPreparer` —— 1/2 个有
- `QwenEditOutputExtractor` —— 1/2 个有
- `Text` —— 1/2 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 1/2 个有
- `easy imageRemBg` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 1 | 100% |
| Prompt 约束强度(CFG) | 3.5 | - | 2 | 29% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | beta57 | - | 2 | 50% |
| 重绘幅度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 3.5，样本不足，未给区间，2 个样本，取值分散，一致性仅 29%
- 调度器 最常用 beta57，2 个样本，一致性 50%
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
