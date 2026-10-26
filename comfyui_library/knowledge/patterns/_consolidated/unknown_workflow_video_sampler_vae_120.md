---
name: unknown_workflow_video_sampler_vae_120
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.89175
common_nodes: [BasicGuider, BasicScheduler, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, FluxGuidance, HunyuanImageToVideo, KSamplerSelect, LoadImage, ModelSamplingSD3, RandomNoise, SamplerCustomAdvanced, TextEncodeHunyuanVideo_ImageToVideo, VAEDecodeTiled, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/GGUF_混元I2V官方工作流_图生视频_1930253337390911489.json, 视频生成/图生视频/HunYuan Video v2 一致性修复版_1900545895807754241.json, 视频生成/图生视频/HunyuanVideo图生视频工作流_1935338474637545473.json, 视频生成/图生视频/hunyuanvideo i2v 720p_1897910255437991938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_120

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/GGUF_混元I2V官方工作流_图生视频_1930253337390911489.json、视频生成/图生视频/HunYuan Video v2 一致性修复版_1900545895807754241.json、视频生成/图生视频/HunyuanVideo图生视频工作流_1935338474637545473.json、视频生成/图生视频/hunyuanvideo i2v 720p_1897910255437991938.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
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
- `VAEDecodeTiled`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `UNETLoader` —— 3/4 个有
- `VAEDecode` —— 3/4 个有
- `SaveWEBM` —— 2/4 个有
- `ImageFromBatch` —— 1/4 个有
- `ImageResizeKJ` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `Label (rgthree)` —— 1/4 个有
- `SaveAnimatedWEBP` —— 1/4 个有
- `UnetLoaderGGUF` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy imageSize` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
