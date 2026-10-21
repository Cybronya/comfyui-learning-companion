---
name: unknown_workflow_video_sampler_clip_96
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.755333
common_nodes: [ImageResize+, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1904223352662433793.json, 视频生成/图生视频/1904530272136704001.json, 视频生成/文生视频/1923970677043286018.json, 视频生成/文生视频/1927317975609806849.json, 视频生成/文生视频/1927010943581192194.json, 视频生成/文生视频/1946379105648697346.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_96

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1904223352662433793.json、视频生成/图生视频/1904530272136704001.json、视频生成/文生视频/1923970677043286018.json、视频生成/文生视频/1927317975609806849.json、视频生成/文生视频/1927010943581192194.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 6 个 workflow 都包含：
- `ImageResize+`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AddLabel` —— 5/6 个有
- `EmptyImage` —— 5/6 个有
- `GetImageSizeAndCount` —— 5/6 个有
- `GetNode` —— 5/6 个有
- `ImageConcatMulti` —— 5/6 个有
- `SetNode` —— 5/6 个有
- `WanVideoSLG` —— 5/6 个有
- `WanVideoBlockSwap` —— 4/6 个有
- `WanVideoExperimentalArgs` —— 3/6 个有
- `Anything Everywhere` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `RIFE VFI` —— 2/6 个有
- `WanVideoTorchCompileSettings` —— 2/6 个有
- `WanVideoVRAMManagement` —— 2/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
