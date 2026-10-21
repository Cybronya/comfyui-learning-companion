---
name: unknown_workflow_video_upscale_lora_41
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9085
common_nodes: [ImageUpscaleWithModel, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, TextInput_, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader, easy imageSize]
problems: []
missing: []
members: [视频生成/图生视频/1909470636823949313.json, 视频生成/图生视频/1992837863268216833.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_41

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1909470636823949313.json、视频生成/图生视频/1992837863268216833.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageUpscaleWithModel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `TextInput_`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `Select Image Indices` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
