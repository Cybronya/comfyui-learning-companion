---
name: unknown_workflow_video_sampler_clip_141
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.1最新fun首尾帧视频工作流_1913080907685687298.json, 视频生成/图生视频/wan2.1首尾帧视频_1930189801167732738.json, 视频生成/图生视频/【首尾帧】WanV2 FLF_1913875085944418305.json, 视频生成/图生视频/【首尾帧】通义万相WAN2.1 首尾帧视频动画生成_1912089601203236866.json, 视频生成/图生视频/通义官方最新版wan2.1首尾帧V2版本（14B参数高清版）_1913039877968199682.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_141

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/wan2.1最新fun首尾帧视频工作流_1913080907685687298.json、视频生成/图生视频/wan2.1首尾帧视频_1930189801167732738.json、视频生成/图生视频/【首尾帧】WanV2 FLF_1913875085944418305.json、视频生成/图生视频/【首尾帧】通义万相WAN2.1 首尾帧视频动画生成_1912089601203236866.json、视频生成/图生视频/通义官方最新版wan2.1首尾帧V2版本（14B参数高清版）_1913039877968199682.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Int` —— 4/5 个有
- `RIFE VFI` —— 4/5 个有
- `ImageResize+` —— 3/5 个有
- `LayerUtility: PurgeVRAM` —— 3/5 个有
- `Primitive integer [Crystools]` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `Text Multiline` —— 3/5 个有
- `easy cleanGpuUsed` —— 3/5 个有
- `ImageScale` —— 2/5 个有
- `WanVideoTorchCompileSettings` —— 2/5 个有
- `easy int` —— 2/5 个有
- `easy positive` —— 2/5 个有
- `CR Upscale Image` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `Fast Groups Muter (rgthree)` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
