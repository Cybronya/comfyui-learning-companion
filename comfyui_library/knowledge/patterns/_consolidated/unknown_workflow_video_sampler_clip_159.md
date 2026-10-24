---
name: unknown_workflow_video_sampler_clip_159
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.912
common_nodes: [Int, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, RIFE VFI, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.1最新fun首尾帧视频工作流_1913080907685687298.json, 视频生成/图生视频/wan2.1首尾帧视频_1930189801167732738.json, 视频生成/图生视频/【首尾帧】WanV2 FLF_1913875085944418305.json, 视频生成/图生视频/通义官方最新版wan2.1首尾帧V2版本（14B参数高清版）_1913039877968199682.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_159

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/wan2.1最新fun首尾帧视频工作流_1913080907685687298.json、视频生成/图生视频/wan2.1首尾帧视频_1930189801167732738.json、视频生成/图生视频/【首尾帧】WanV2 FLF_1913875085944418305.json、视频生成/图生视频/通义官方最新版wan2.1首尾帧V2版本（14B参数高清版）_1913039877968199682.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 4 个 workflow 都包含：
- `Int`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `RIFE VFI`
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
- `ImageResize+` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 3/4 个有
- `Primitive integer [Crystools]` —— 3/4 个有
- `SetNode` —— 3/4 个有
- `Text Multiline` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `CR Upscale Image` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `WanVideoTorchCompileSettings` —— 1/4 个有
- `easy int` —— 1/4 个有
- `easy positive` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
