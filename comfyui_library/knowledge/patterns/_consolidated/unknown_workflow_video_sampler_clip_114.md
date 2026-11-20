---
name: unknown_workflow_video_sampler_clip_114
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.928333
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1_首尾帧视频_kijai_1925042033008779266.json, 视频生成/图生视频/Wan2.1图生视频_1992496405681950721.json, 视频生成/图生视频/通义万相Wan2.1Fun首尾帧图生视频TC加速_1907738859516342273.json, 视频生成/图生视频/首尾帧 Wan2.1 FLF2V 模型｜720P_1937753852420472833.json, 视频生成/图生视频/首尾帧—万相官方模型_FLF2V_720P_1914115892282650625.json, 视频生成/图生视频/🦖Wan首尾帧视频_1905876278627733505.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_114

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/Wan2.1_首尾帧视频_kijai_1925042033008779266.json、视频生成/图生视频/Wan2.1图生视频_1992496405681950721.json、视频生成/图生视频/通义万相Wan2.1Fun首尾帧图生视频TC加速_1907738859516342273.json、视频生成/图生视频/首尾帧 Wan2.1 FLF2V 模型｜720P_1937753852420472833.json、视频生成/图生视频/首尾帧—万相官方模型_FLF2V_720P_1914115892282650625.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 5/6 个有
- `WanVideoClipVisionEncode` —— 5/6 个有
- `WanVideoImageToVideoEncode` —— 5/6 个有
- `WanVideoSLG` —— 5/6 个有
- `WanVideoTeaCache` —— 5/6 个有
- `WanVideoExperimentalArgs` —— 4/6 个有
- `WanVideoTorchCompileSettings` —— 3/6 个有
- `ImageResizeKJ` —— 2/6 个有
- `SetNode` —— 2/6 个有
- `ImageCASharpening+` —— 1/6 个有
- `Int` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `ResizeLongestToNode` —— 1/6 个有
- `WanVideoLoraSelect` —— 1/6 个有
- `WanVideoSEImageClipEncode` —— 1/6 个有
- `easy cleanGpuUsed` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
