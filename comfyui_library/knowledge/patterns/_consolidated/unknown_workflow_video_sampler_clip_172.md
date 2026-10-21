---
name: unknown_workflow_video_sampler_clip_172
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.615333
common_nodes: [GetNode, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, Note Plus (mtb), SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy int, easy positive, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/1948656021569974274.json, 视频生成/图生视频/1906433912804151297.json, 视频生成/图生视频/1906434175170170881.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_172

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1948656021569974274.json、视频生成/图生视频/1906433912804151297.json、视频生成/图生视频/1906434175170170881.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 3 个 workflow 都包含：
- `GetNode`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `Note Plus (mtb)`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy int`
- `easy positive`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Bookmark (rgthree)` —— 2/3 个有
- `ImageScale` —— 2/3 个有
- `JoinStrings` —— 2/3 个有
- `String Literal` —— 2/3 个有
- `WanVideoClipVisionEncode` —— 2/3 个有
- `WanVideoImageToVideoEncode` —— 2/3 个有
- `easy float` —— 2/3 个有
- `LoadImageFromUrl` —— 1/3 个有
- `WanVideoImageClipEncode` —— 1/3 个有
- `WanVideoVRAMManagement` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
