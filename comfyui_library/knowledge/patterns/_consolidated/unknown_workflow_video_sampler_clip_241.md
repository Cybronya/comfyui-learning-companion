---
name: unknown_workflow_video_sampler_clip_241
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.818
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, Fast Groups Bypasser (rgthree), FlashVSR_SM_KSampler, FlashVSR_SM_Model, GetImageSizeAndCount, GetNode, INTConstant, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, ModelSamplingSD3, PrimitiveFloat, RIFE VFI, SetNode, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy mathInt]
problems: []
missing: []
members: [视频生成/图生视频/Smooth&FlashVSR-最新图生视频1080P工作流_1981661831137763329.json, 视频生成/图生视频/Smooth&FlashVSR-最新首尾帧视频1080P工作流_1982375634741665794.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_241

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Smooth&FlashVSR-最新图生视频1080P工作流_1981661831137763329.json、视频生成/图生视频/Smooth&FlashVSR-最新首尾帧视频1080P工作流_1982375634741665794.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：82%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `Fast Groups Bypasser (rgthree)`
- `FlashVSR_SM_KSampler`
- `FlashVSR_SM_Model`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `ModelSamplingSD3`
- `PrimitiveFloat`
- `RIFE VFI`
- `SetNode`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy mathInt`

**可变部分**（部分 workflow 才有）：
- `ColorMatch` —— 1/2 个有
- `ImageLoader` —— 1/2 个有
- `ImageResizeKJv2` —— 1/2 个有
- `MultiplePathsInput` —— 1/2 个有
- `Pick From Batch (mtb)` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `SaveImage` —— 1/2 个有
- `WanFirstLastFrameToVideo` —— 1/2 个有
- `WanImageToVideo` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 1.2389e+09 | - | 2 | 54% |
| Prompt 约束强度(CFG) | randomize | - | 2 | 100% |
| 采样算法 | 2 | - | 2 | 100% |
| 调度器 | 3.5 | - | 2 | 100% |
| 重绘幅度 | 11 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 1.2389e+09，样本不足，未给区间，2 个样本
- Prompt 约束强度(CFG) 最常用 randomize，2 个样本，一致性 100%
- 采样算法 中位数 2，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 中位数 3.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 11，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 风险：采样步数 观测到 1.80685e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
