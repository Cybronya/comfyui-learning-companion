---
name: text_to_image_video_lora_sampler_187
type: Text To Image
frequency: 2
level: weak
coverage: 0.896
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, Fast Groups Bypasser (rgthree), Getter, ImageLoader, ImageResizeKJv2, KSampler, LoraLoaderModelOnly, MultiplePathsInput, QZ_ResolutionPreset, Qwen3_VQA, RIFE VFI, SaveImage, Setter, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, WanMoeKSampler, easy cleanGpuUsed, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [RIFE VFI, easy cleanGpuUsed]
members: [图片生成/文生图/1984243633375297537.json, 视频生成/图生视频/1984243633375297537.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_187

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1984243633375297537.json、视频生成/图生视频/1984243633375297537.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Getter`
- `ImageLoader`
- `ImageResizeKJv2`
- `KSampler`
- `LoraLoaderModelOnly`
- `MultiplePathsInput`
- `QZ_ResolutionPreset`
- `Qwen3_VQA`
- `RIFE VFI`
- `SaveImage`
- `Setter`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `WanMoeKSampler`
- `easy cleanGpuUsed`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 6 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | euler | - | 2 | 100% |
| 宽度 | 1280 | - | 2 | 100% |
| 高度 | 720 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler，2 个样本，一致性 100%
- 宽度 中位数 1280，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 720，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：RIFE VFI、easy cleanGpuUsed
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
