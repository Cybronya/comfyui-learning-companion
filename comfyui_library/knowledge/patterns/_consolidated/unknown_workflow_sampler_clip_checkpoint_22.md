---
name: unknown_workflow_sampler_clip_checkpoint_22
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8335
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, Circular VAEDecode, EmptyLatentImage, KSamplerAdvanced, LatentConcat, OffsetImage, PreviewImage, SaveImage, SeamlessLatentTiling, SeamlessPreview_CN]
problems: []
missing: []
members: [图片生成/文生图/unet latent tiling_2061296630023933953.json, 图片生成/文生图/unet latent tiling_2062586701217886209.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_22

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/unet latent tiling_2061296630023933953.json、图片生成/文生图/unet latent tiling_2062586701217886209.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `Circular VAEDecode`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `LatentConcat`
- `OffsetImage`
- `PreviewImage`
- `SaveImage`
- `SeamlessLatentTiling`
- `SeamlessPreview_CN`

**可变部分**（部分 workflow 才有）：
- `CR Apply LoRA Stack` —— 1/2 个有
- `CR LoRA Stack` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 20 | - | 2 | 100% |
| 采样算法 | 8 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 50% |
| 重绘幅度 | simple | - | 2 | 50% |
| 宽度 | 768 | - | 2 | 100% |
| 高度 | 768 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 50%
- 重绘幅度 最常用 simple，2 个样本，一致性 50%
- 宽度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
