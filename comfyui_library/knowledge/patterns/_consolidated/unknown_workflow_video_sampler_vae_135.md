---
name: unknown_workflow_video_sampler_vae_135
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.82125
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/【遇见AI】wan2.1图生视频基础流，不带加速_2061018684998635522.json, 视频生成/图生视频/万象ATI视频轨迹控制_1931322403022897154.json, 视频生成/图生视频/新版ATI轨迹指引图生视频超级加速版V1_1941169318455570433.json, 视频生成/文生视频/ComfyUI Wan 2.1 可实现任意轨迹指令运动控制 AI 视频生成工作流_1928353858429566977.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_135

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/【遇见AI】wan2.1图生视频基础流，不带加速_2061018684998635522.json、视频生成/图生视频/万象ATI视频轨迹控制_1931322403022897154.json、视频生成/图生视频/新版ATI轨迹指引图生视频超级加速版V1_1941169318455570433.json、视频生成/文生视频/ComfyUI Wan 2.1 可实现任意轨迹指令运动控制 AI 视频生成工作流_1928353858429566977.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `SplineEditor` —— 3/4 个有
- `WanVideoATITracks` —— 3/4 个有
- `WanVideoBlockSwap` —— 3/4 个有
- `WanVideoLoraSelect` —— 3/4 个有
- `AppendStringsToList` —— 2/4 个有
- `WanVideoATITracksVisualize` —— 2/4 个有
- `CLIPLoader` —— 1/4 个有
- `CLIPTextEncode` —— 1/4 个有
- `CR Prompt Text` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `JWInteger` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `StringConstantMultiline` —— 1/4 个有
- `WanVideoTextEmbedBridge` —— 1/4 个有
- `WanVideoTorchCompileSettings` —— 1/4 个有
- `easy clearCacheAll` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
