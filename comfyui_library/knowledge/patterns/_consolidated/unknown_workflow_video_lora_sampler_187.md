---
name: unknown_workflow_video_lora_sampler_187
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.9441
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2066888658283753473.json, 视频生成/图生视频/2066895652839317506.json, 视频生成/图生视频/1935507389821157377.json, 视频生成/图生视频/1935539702722396162.json, 视频生成/图生视频/1936094603097329666.json, 视频生成/图生视频/1935537593000067073.json, 视频生成/图生视频/1934996455494983682.json, 视频生成/图生视频/1927959918765031425.json, 视频生成/图生视频/1936041797762076674.json, 视频生成/图生视频/1935209763875508226.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_187

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2066888658283753473.json、视频生成/图生视频/2066895652839317506.json、视频生成/图生视频/1935507389821157377.json、视频生成/图生视频/1935539702722396162.json、视频生成/图生视频/1936094603097329666.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 10 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 8/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/10 个有
- `WanVideoBlockSwap` —— 8/10 个有
- `WanVideoClipVisionEncode` —— 8/10 个有
- `WanVideoEnhanceAVideo` —— 6/10 个有
- `JWInteger` —— 4/10 个有
- `Text Multiline` —— 4/10 个有
- `PreviewImage` —— 3/10 个有
- `WanVideoVRAMManagement` —— 3/10 个有
- `ImageConcanate` —— 2/10 个有
- `ImageResizeKJv2` —— 2/10 个有
- `WanVideoTorchCompileSettings` —— 2/10 个有
- `easy imageRemBg` —— 2/10 个有
- `Fast Groups Bypasser (rgthree)` —— 1/10 个有
- `ImagePadKJ` —— 1/10 个有
- `ImageResize+` —— 1/10 个有
- `easy cleanGpuUsed` —— 1/10 个有
- `easy int` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
