---
name: unknown_workflow_video_lora_sampler_249
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.983
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/KJ图生视频工作流_2066888658283753473.json, 视频生成/图生视频/KJ首尾帧图生视频工作流_2066895652839317506.json, 视频生成/图生视频/Lightx2v图生视频优化版_1935507389821157377.json, 视频生成/图生视频/MAGREF+Lightx2v 双图参考图生视频_1935539702722396162.json, 视频生成/图生视频/MAGREF+Lightx2v图生视频电商极速版_1936094603097329666.json, 视频生成/图生视频/Self-Forcing14B（Lightx2v）-图生视频_1935537593000067073.json, 视频生成/图生视频/Wan2.1+Lightx2v图生视频放大_1938448782306508802.json, 视频生成/图生视频/Wan2.1+Lightx2v图生视频放大补帧生成2K高清视频_1935685282568003585.json, 视频生成/图生视频/Wan2.1+Radial 提速版图生视频放大_1947245269056376834.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_249

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/KJ图生视频工作流_2066888658283753473.json、视频生成/图生视频/KJ首尾帧图生视频工作流_2066895652839317506.json、视频生成/图生视频/Lightx2v图生视频优化版_1935507389821157377.json、视频生成/图生视频/MAGREF+Lightx2v 双图参考图生视频_1935539702722396162.json、视频生成/图生视频/MAGREF+Lightx2v图生视频电商极速版_1936094603097329666.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 9 个 workflow 都包含：
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
- `CLIPVisionLoader` —— 7/9 个有
- `WanVideoBlockSwap` —— 7/9 个有
- `WanVideoClipVisionEncode` —— 7/9 个有
- `ImageResizeKJv2` —— 5/9 个有
- `WanVideoEnhanceAVideo` —— 5/9 个有
- `JWInteger` —— 4/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 4/9 个有
- `Text Multiline` —— 4/9 个有
- `WanVideoTorchCompileSettings` —— 4/9 个有
- `ImageUpscaleWithModel` —— 3/9 个有
- `Primitive integer [Crystools]` —— 3/9 个有
- `RIFE VFI` —— 3/9 个有
- `SimpleMath+` —— 3/9 个有
- `UpscaleModelLoader` —— 3/9 个有
- `WanVideoSLG` —— 3/9 个有
- `ImageConcanate` —— 2/9 个有
- `PreviewImage` —— 2/9 个有
- `easy imageRemBg` —— 2/9 个有
- `ImagePadKJ` —— 1/9 个有
- `ImageResize+` —— 1/9 个有
- `WanVideoMagCache` —— 1/9 个有
- `WanVideoSetRadialAttention` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
