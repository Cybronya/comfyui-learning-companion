---
name: unknown_workflow_video_sampler_clip_81
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.79275
common_nodes: [ImageResize+, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1首尾帧关键帧视频生成_1904223352662433793.json, 视频生成/图生视频/通义万相WAN2.1首尾帧过度视频-StarAI_1904530272136704001.json, 视频生成/图生视频/首尾帧 Wan2.1 FLF2V 模型｜720P_1937753852420472833.json, 视频生成/图生视频/首尾帧—万相官方模型_FLF2V_720P_1914115892282650625.json, 视频生成/文生视频/2张照片文生视频，可以中文提示词_1923970677043286018.json, 视频生成/文生视频/CG迷-WAN fun首尾帧视频动画工作流_1927317975609806849.json, 视频生成/文生视频/CG迷-Wan视频升级版720P精度首尾帧FLF2V_1927010943581192194.json, 视频生成/文生视频/首尾帧图像稳定全自动稳定输出视频丨自动生成_1946379105648697346.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_81

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Wan2.1首尾帧关键帧视频生成_1904223352662433793.json、视频生成/图生视频/通义万相WAN2.1首尾帧过度视频-StarAI_1904530272136704001.json、视频生成/图生视频/首尾帧 Wan2.1 FLF2V 模型｜720P_1937753852420472833.json、视频生成/图生视频/首尾帧—万相官方模型_FLF2V_720P_1914115892282650625.json、视频生成/文生视频/2张照片文生视频，可以中文提示词_1923970677043286018.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 8 个 workflow 都包含：
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
- `SetNode` —— 7/8 个有
- `WanVideoSLG` —— 7/8 个有
- `WanVideoBlockSwap` —— 6/8 个有
- `AddLabel` —— 5/8 个有
- `EmptyImage` —— 5/8 个有
- `GetImageSizeAndCount` —— 5/8 个有
- `GetNode` —— 5/8 个有
- `ImageConcatMulti` —— 5/8 个有
- `WanVideoExperimentalArgs` —— 5/8 个有
- `WanVideoTorchCompileSettings` —— 4/8 个有
- `Anything Everywhere` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `RIFE VFI` —— 2/8 个有
- `WanVideoVRAMManagement` —— 2/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
