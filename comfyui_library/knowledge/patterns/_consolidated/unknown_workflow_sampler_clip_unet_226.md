---
name: unknown_workflow_sampler_clip_unet_226
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8735
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, ImageScaleToTotalPixels, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Flux2-Klein-9B-True-V2 文生图+图像编辑_2053278001936248833.json, 视频生成/图生视频/2014254176355753986.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_226

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Flux2-Klein-9B-True-V2 文生图+图像编辑_2053278001936248833.json、视频生成/图生视频/2014254176355753986.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `ImageScaleToTotalPixels`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Simple Text Watermark` —— 1/2 个有
- `ClownsharKSampler_Beta` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `LCSColorAnchor` —— 1/2 个有
- `LCSLoadData` —— 1/2 个有
- `LCSSharpnessCalibrate` —— 1/2 个有
- `LCSSharpnessIntervene` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `Seed (rgthree)` —— 1/2 个有
- `SetNode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | sgm_uniform | - | 1 | 100% |
| Prompt 约束强度(CFG) | 30 | - | 1 | 100% |
| 采样算法 | -1 | - | 1 | 100% |
| 调度器 | 1 | - | 1 | 100% |
| 重绘幅度 | 0.85 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 风险：Prompt 约束强度(CFG) 观测到 30，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
