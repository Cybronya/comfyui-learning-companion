---
name: unknown_workflow_video_lora_sampler_351
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.844333
common_nodes: [AppendStringsToList, CLIPVisionLoader, LoadImage, LoadWanVideoT5TextEncoder, SplineEditor, VHS_VideoCombine, WanVideoATITracks, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1929480166395822081.json, 视频生成/图生视频/1929748784421703681.json, 视频生成/图生视频/1928747025259511810.json, 视频生成/图生视频/1929199069892349953.json, 视频生成/图生视频/1929817339246624770.json, 视频生成/图生视频/1928843752012681217.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_351

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1929480166395822081.json、视频生成/图生视频/1929748784421703681.json、视频生成/图生视频/1928747025259511810.json、视频生成/图生视频/1929199069892349953.json、视频生成/图生视频/1929817339246624770.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 6 个 workflow 都包含：
- `AppendStringsToList`
- `CLIPVisionLoader`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SplineEditor`
- `VHS_VideoCombine`
- `WanVideoATITracks`
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
- `ImageResizeKJv2` —— 5/6 个有
- `WanVideoTorchCompileSettings` —— 5/6 个有
- `CreateShapeImageOnPath` —— 3/6 个有
- `ImageCompositeMasked` —— 3/6 个有
- `Text Multiline` —— 3/6 个有
- `Primitive integer [Crystools]` —— 2/6 个有
- `WanVideoATITracksVisualize` —— 2/6 个有
- `GetNode` —— 1/6 个有
- `INTConstant` —— 1/6 个有
- `ImageConcanate` —— 1/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `SetNode` —— 1/6 个有
- `WanVideoTeaCache` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
