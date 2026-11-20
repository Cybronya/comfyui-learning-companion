---
name: unknown_workflow_sampler_clip_unet_479
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.815
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSamplerAdvanced, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/z_image_base+turbo+controlnet_2047566373903142913.json, 图片生成/文生图/z_image_base+turbo_workflow_2018248328844156930.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_479

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/z_image_base+turbo+controlnet_2047566373903142913.json、图片生成/文生图/z_image_base+turbo_workflow_2018248328844156930.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSamplerAdvanced`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DWPreprocessor` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `ModelPatchLoader` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `QwenImageDiffsynthControlnet` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 20 | - | 2 | 100% |
| 采样算法 | 4 | - | 2 | 100% |
| 调度器 | res_multistep | - | 2 | 100% |
| 重绘幅度 | simple | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 res_multistep，2 个样本，一致性 100%
- 重绘幅度 最常用 simple，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
