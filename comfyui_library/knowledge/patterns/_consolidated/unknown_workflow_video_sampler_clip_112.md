---
name: unknown_workflow_video_sampler_clip_112
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.914
common_nodes: [ImageResize+, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1925042033008779266.json, 视频生成/图生视频/1992496405681950721.json, 视频生成/图生视频/1937753852420472833.json, 视频生成/图生视频/1914115892282650625.json, 视频生成/图生视频/1905876278627733505.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_112

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1925042033008779266.json、视频生成/图生视频/1992496405681950721.json、视频生成/图生视频/1937753852420472833.json、视频生成/图生视频/1914115892282650625.json、视频生成/图生视频/1905876278627733505.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageResize+`
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
- `WanVideoClipVisionEncode` —— 4/5 个有
- `WanVideoImageToVideoEncode` —— 4/5 个有
- `WanVideoSLG` —— 4/5 个有
- `WanVideoTeaCache` —— 4/5 个有
- `WanVideoExperimentalArgs` —— 3/5 个有
- `SetNode` —— 2/5 个有
- `WanVideoTorchCompileSettings` —— 2/5 个有
- `ImageCASharpening+` —— 1/5 个有
- `ImageResizeKJ` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `ResizeLongestToNode` —— 1/5 个有
- `WanVideoLoraSelect` —— 1/5 个有
- `WanVideoSEImageClipEncode` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
