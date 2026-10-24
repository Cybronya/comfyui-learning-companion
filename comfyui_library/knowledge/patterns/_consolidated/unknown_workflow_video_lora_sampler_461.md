---
name: unknown_workflow_video_lora_sampler_461
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.55975
common_nodes: [BasicScheduler, CLIPLoader, CLIPTextEncode, DisableNoise, GetNode, ImageBatchExtendWithOverlap, ImageResizeKJv2, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, ScheduledCFGGuidance, SetNode, SplitSigmas, VAEDecode, VAEEncode, VAELoader, VHS_VideoCombine, WanImageToVideoSVIPro]
problems: []
missing: []
members: [图片生成/图生图/wan22_SVI_Pro长视频优化版_2030979131311132674.json, 视频生成/图生视频/wan22_SVI_Pro_2005599683508666370.json, 视频生成/文生视频/【晨晨的AI应用包004】一键图生长视频SVI-PRO-15s_2012003623286349826.json, 视频生成/文生视频/大凯辰光SVI-V2.0-Pro-长视频流（非子图）_2008153457944956930.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_461

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/wan22_SVI_Pro长视频优化版_2030979131311132674.json、视频生成/图生视频/wan22_SVI_Pro_2005599683508666370.json、视频生成/文生视频/【晨晨的AI应用包004】一键图生长视频SVI-PRO-15s_2012003623286349826.json、视频生成/文生视频/大凯辰光SVI-V2.0-Pro-长视频流（非子图）_2008153457944956930.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `DisableNoise`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `ImageResizeKJv2`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `ScheduledCFGGuidance`
- `SetNode`
- `SplitSigmas`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideoSVIPro`

**可变部分**（部分 workflow 才有）：
- `DiffusionModelLoaderKJ` —— 2/4 个有
- `PreviewImage` —— 1/4 个有
- `SaveLatent` —— 1/4 个有
- `Text` —— 1/4 个有
- `UNETLoader` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
