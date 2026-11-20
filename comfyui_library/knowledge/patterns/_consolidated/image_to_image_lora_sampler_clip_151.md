---
name: image_to_image_lora_sampler_clip_151
type: Image To Image
frequency: 2
level: weak
coverage: 0.661
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PreviewImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/wan2.1图生图_洗图_1952652175081160705.json, 图片生成/文生图/28.tonnie-Wan2.2文生图、洗图工作流_2001258902077534210.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_151

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/wan2.1图生图_洗图_1952652175081160705.json、图片生成/文生图/28.tonnie-Wan2.2文生图、洗图工作流_2001258902077534210.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PreviewImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere3` —— 1/2 个有
- `CR Text Concatenate` —— 1/2 个有
- `EmptyHunyuanVideo15Latent` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 13 | - | 2 | 46% |
| Prompt 约束强度(CFG) | 2.25 | - | 2 | 44% |
| 采样算法 | res_2s | - | 2 | 50% |
| 调度器 | bong_tangent | - | 2 | 50% |
| 重绘幅度 | 0.365 | - | 2 | 82% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 13，样本不足，未给区间，2 个样本，取值分散，一致性仅 46%
- Prompt 约束强度(CFG) 中位数 2.25，样本不足，未给区间，2 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 res_2s，2 个样本，一致性 50%
- 调度器 最常用 bong_tangent，2 个样本，一致性 50%
- 重绘幅度 中位数 0.365，样本不足，未给区间，2 个样本，取值集中（一致性 82%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
