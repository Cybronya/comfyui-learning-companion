---
name: unknown_workflow_upscale_latent_upscale_lora_63
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.681
common_nodes: [CLIPLoader, CLIPTextEncode, ClownsharKSampler_Beta, EmptyHunyuanLatentVideo, Image Comparer (rgthree), Image Sharpen FS, KSampler, LatentUpscaleBy, LoraLoaderModelOnly, PreviewImage, SaveImage, String, Text, Text Concatenate, UnetLoaderGGUF, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: [Image Sharpen FS, Text Concatenate]
members: [图片生成/文生图/1955155949084446721.json, 图片生成/文生图/1963603441133375490.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_latent_upscale_lora_63

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/1955155949084446721.json、图片生成/文生图/1963603441133375490.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：68%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ClownsharKSampler_Beta`
- `EmptyHunyuanLatentVideo`
- `Image Comparer (rgthree)`
- `Image Sharpen FS`
- `KSampler`
- `LatentUpscaleBy`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `String`
- `Text`
- `Text Concatenate`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | bong_tangent | - | 2 | 100% |
| Prompt 约束强度(CFG) | 20 | - | 2 | 100% |
| 采样算法 | 10 | - | 2 | 100% |
| 调度器 | 1 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 bong_tangent，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 10，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 风险：重绘幅度 观测到 1，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 高发问题（4/2 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：Image Sharpen FS、Text Concatenate
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
