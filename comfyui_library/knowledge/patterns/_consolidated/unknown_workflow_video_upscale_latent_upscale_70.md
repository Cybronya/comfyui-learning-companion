---
name: unknown_workflow_video_upscale_latent_upscale_70
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9766
common_nodes: [BasicScheduler, CFGGuider, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DualCLIPLoader, HunyuanVideo15ImageToVideo, HunyuanVideo15LatentUpscaleWithModel, HunyuanVideo15SuperResolution, KSamplerSelect, LatentUpscaleModelLoader, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, RandomNoise, SamplerCustomAdvanced, UNETLoader, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2073280696038289410.json, 视频生成/图生视频/2074119499955130370.json, 视频生成/图生视频/2073289414930944001.json, 视频生成/图生视频/1992198526646153217.json, 视频生成/图生视频/1997913784465391617.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_latent_upscale_70

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2073280696038289410.json、视频生成/图生视频/2074119499955130370.json、视频生成/图生视频/2073289414930944001.json、视频生成/图生视频/1992198526646153217.json、视频生成/图生视频/1997913784465391617.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DualCLIPLoader`
- `HunyuanVideo15ImageToVideo`
- `HunyuanVideo15LatentUpscaleWithModel`
- `HunyuanVideo15SuperResolution`
- `KSamplerSelect`
- `LatentUpscaleModelLoader`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `GetImageSize` —— 3/5 个有
- `VAEDecode` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `ResizeLongestToNode` —— 2/5 个有
- `VAEDecodeTiled` —— 2/5 个有
- `ResizeImagesByLongerEdge` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
