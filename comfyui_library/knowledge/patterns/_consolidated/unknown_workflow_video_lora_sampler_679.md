---
name: unknown_workflow_video_lora_sampler_679
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.831
common_nodes: [AILab_QwenVL, CLIPVisionLoader, GetImageRangeFromBatch, ImageConcanate, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, SaveImage, Text Concatenate, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/ChronoEdit图片编辑模型_1989211681295306753.json, 视频生成/图生视频/KJ版-ChronoEdit图像编辑_1987441783527419906.json, 视频生成/图生视频/KJ版-ChronoEdit图像编辑新神器_1986952330576900097.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_679

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/ChronoEdit图片编辑模型_1989211681295306753.json、视频生成/图生视频/KJ版-ChronoEdit图像编辑_1987441783527419906.json、视频生成/图生视频/KJ版-ChronoEdit图像编辑新神器_1986952330576900097.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `AILab_QwenVL`
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `ImageConcanate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SaveImage`
- `Text Concatenate`
- `Text Multiline`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/3 个有
- `JWInteger` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `LoadVideo` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
