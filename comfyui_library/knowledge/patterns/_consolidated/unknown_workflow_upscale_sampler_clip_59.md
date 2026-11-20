---
name: unknown_workflow_upscale_sampler_clip_59
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.94
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ImageSharpen, ImageUpscaleWithModel, KSamplerAdvanced, SaveImage, UNETLoader, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-Image文生图 双采破随机+极氪典藏版V6_2012164483946389506.json, 图片生成/文生图/Z-image-蓝色多脑盒-增强随机性版本_1999611975741079553.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_clip_59

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-Image文生图 双采破随机+极氪典藏版V6_2012164483946389506.json、图片生成/文生图/Z-image-蓝色多脑盒-增强随机性版本_1999611975741079553.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImageSharpen`
- `ImageUpscaleWithModel`
- `KSamplerAdvanced`
- `SaveImage`
- `UNETLoader`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 1/2 个有
- `LayerUtility: ImageReel` —— 1/2 个有
- `LayerUtility: ImageReelComposit` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1004 | - | 2 | 92% |
| 高度 | 1792 | - | 2 | 93% |
| 采样步数 | randomize | - | 2 | 100% |
| Prompt 约束强度(CFG) | 20 | - | 2 | 50% |
| 采样算法 | 1.75 | - | 2 | 57% |
| 调度器 | dpmpp_3m_sde | - | 2 | 100% |
| 重绘幅度 | ddim_uniform | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1004，样本不足，未给区间，2 个样本，取值集中（一致性 92%）
- 高度 中位数 1792，样本不足，未给区间，2 个样本，取值集中（一致性 93%）
- 采样步数 最常用 randomize，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 20，样本不足，未给区间，2 个样本
- 采样算法 中位数 1.75，样本不足，未给区间，2 个样本
- 调度器 最常用 dpmpp_3m_sde，2 个样本，一致性 100%
- 重绘幅度 最常用 ddim_uniform，2 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
