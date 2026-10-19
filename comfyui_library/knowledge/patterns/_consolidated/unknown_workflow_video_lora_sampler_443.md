---
name: unknown_workflow_video_lora_sampler_443
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.5796
common_nodes: [CLIPVisionLoader, GetNode, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1935629484227743745.json, 视频生成/图生视频/1935594856536264705.json, 视频生成/图生视频/1935606766069809154.json, 视频生成/图生视频/1945320019179839489.json, 视频生成/图生视频/1935270745905745921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_443

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/1935629484227743745.json、视频生成/图生视频/1935594856536264705.json、视频生成/图生视频/1935606766069809154.json、视频生成/图生视频/1945320019179839489.json、视频生成/图生视频/1935270745905745921.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：58%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageBatch` —— 4/5 个有
- `ImageConcatFromBatch` —— 4/5 个有
- `PreviewImage` —— 4/5 个有
- `RMBG` —— 4/5 个有
- `SimpleMath+` —— 4/5 个有
- `EmptyImage` —— 3/5 个有
- `Label (rgthree)` —— 3/5 个有
- `Anything Everywhere3` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `Primitive integer [Crystools]` —— 1/5 个有
- `RIFE VFI` —— 1/5 个有
- `VHS_LoadVideo` —— 1/5 个有
- `Video_Upscale_With_Model` —— 1/5 个有
- `WanVideoEncode` —— 1/5 个有
- `WanVideoSLG` —— 1/5 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/5 个有
- `WanVideoUni3C_embeds` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
