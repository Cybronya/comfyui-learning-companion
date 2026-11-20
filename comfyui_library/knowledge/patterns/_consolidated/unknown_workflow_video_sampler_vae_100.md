---
name: unknown_workflow_video_sampler_vae_100
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9505
common_nodes: [ImageResizeKJ, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/FLF2V首尾帧图生视频_1913525261151760386.json, 视频生成/图生视频/FLF2V首尾帧高质量视频_1916010425433915394.json, 视频生成/图生视频/SLG 提升 WAN2.1 视频画质工作流_1919056662093561858.json, 视频生成/图生视频/Wan FusionX 图生视频-极速版_1962815833489715202.json, 视频生成/图生视频/Wan-Fun视频首尾帧-KJ版_1905999669091307522.json, 视频生成/文生视频/【Wan2.1系列】画质救星SLG技术_1918486985445675009.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_100

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/FLF2V首尾帧图生视频_1913525261151760386.json、视频生成/图生视频/FLF2V首尾帧高质量视频_1916010425433915394.json、视频生成/图生视频/SLG 提升 WAN2.1 视频画质工作流_1919056662093561858.json、视频生成/图生视频/Wan FusionX 图生视频-极速版_1962815833489715202.json、视频生成/图生视频/Wan-Fun视频首尾帧-KJ版_1905999669091307522.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 6 个 workflow 都包含：
- `ImageResizeKJ`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoClipVisionEncode` —— 5/6 个有
- `WanVideoSLG` —— 5/6 个有
- `WanVideoTorchCompileSettings` —— 5/6 个有
- `LoadWanVideoClipTextEncoder` —— 3/6 个有
- `WanVideoExperimentalArgs` —— 3/6 个有
- `CLIPVisionLoader` —— 2/6 个有
- `CR Text` —— 1/6 个有
- `DF_Integer` —— 1/6 个有
- `Evaluate Integers` —— 1/6 个有
- `GetNode` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `easy imageSize` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
