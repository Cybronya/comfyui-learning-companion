---
name: unknown_workflow_video_sampler_unet_61
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9324
common_nodes: [BasicGuider, BasicScheduler, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, HunyuanImageToVideo, KSamplerSelect, LoadImage, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, TextEncodeHunyuanVideo_ImageToVideo, UNETLoader, VAEDecodeTiled, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/1900545895807754241.json, 视频生成/图生视频/1935338474637545473.json, 视频生成/图生视频/1897910255437991938.json, 视频生成/图生视频/1897851566873858049.json, 视频生成/图生视频/1897700159466491905.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_unet_61

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1900545895807754241.json、视频生成/图生视频/1935338474637545473.json、视频生成/图生视频/1897910255437991938.json、视频生成/图生视频/1897851566873858049.json、视频生成/图生视频/1897700159466491905.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `FluxGuidance`
- `HunyuanImageToVideo`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingSD3`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `TextEncodeHunyuanVideo_ImageToVideo`
- `UNETLoader`
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `ImageFromBatch` —— 3/5 个有
- `Primitive integer [Crystools]` —— 2/5 个有
- `SaveWEBM` —— 2/5 个有
- `VAEDecode` —— 2/5 个有
- `CR Prompt Text` —— 1/5 个有
- `ImageResizeKJ` —— 1/5 个有
- `ImageScaleToTotalPixels` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `Primitive string [Crystools]` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy imageSize` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
