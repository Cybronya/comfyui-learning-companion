---
name: unknown_workflow_video_lora_sampler_485
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.81375
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1991707483274309634.json, 视频生成/图生视频/1989700145870721025.json, 视频生成/图生视频/1935525367807672321.json, 视频生成/图生视频/1990058072469106689.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_485

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1991707483274309634.json、视频生成/图生视频/1989700145870721025.json、视频生成/图生视频/1935525367807672321.json、视频生成/图生视频/1990058072469106689.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 3/4 个有
- `InvertMask` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `WanVideoAddBindweaveEmbeds` —— 3/4 个有
- `WanVideoEncodeLatentBatch` —— 3/4 个有
- `WanVideoSetBlockSwap` —— 3/4 个有
- `easy imageRemBg` —— 3/4 个有
- `JWInteger` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `MaskPreview+` —— 2/4 个有
- `WanVideoTorchCompileSettings` —— 2/4 个有
- `CR Prompt Text` —— 1/4 个有
- `GetImageSize+` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ImagePadKJ` —— 1/4 个有
- `JjkText` —— 1/4 个有
- `Primitive integer [Crystools]` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
