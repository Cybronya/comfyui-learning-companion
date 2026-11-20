---
name: unknown_workflow_lora_sampler_clip_326
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.565
common_nodes: [AudioEncoderEncode, AudioEncoderLoader, CLIPLoader, CLIPTextEncode, CreateVideo, GetNode, ImageFromBatch, ImageResizeKJv2, KSampler, LatentConcat, LatentCut, LoadAudio, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PrimitiveInt, SaveVideo, SetNode, UNETLoader, VAEDecode, VAELoader, Video Slice, WanSoundImageToVideo, easy float]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/无限音频视频数字人_2058075340735606785.json, 视频生成/图生视频/无限音频视频数字人进阶版（循环）_2059625088659582978.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_326

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/无限音频视频数字人_2058075340735606785.json、视频生成/图生视频/无限音频视频数字人进阶版（循环）_2059625088659582978.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：56%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioEncoderEncode`
- `AudioEncoderLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `CreateVideo`
- `GetNode`
- `ImageFromBatch`
- `ImageResizeKJv2`
- `KSampler`
- `LatentConcat`
- `LatentCut`
- `LoadAudio`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `SaveVideo`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `Video Slice`
- `WanSoundImageToVideo`
- `easy float`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 1/2 个有
- `MathExpression|pysssss` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `WanSoundImageToVideoExtend` —— 1/2 个有
- `easy forLoopEnd` —— 1/2 个有
- `easy forLoopStart` —— 1/2 个有
- `easy seed` —— 1/2 个有
- `workflow>wan2.2 s2v extend` —— 1/2 个有
- `workflow>wan2.2 s2v extend2` —— 1/2 个有
- `workflow>wan2.2 s2v extend3` —— 1/2 个有
- `workflow>wan2.2 s2v extend4` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | uni_pc | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 uni_pc，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（3/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
