---
name: unknown_workflow_video_lora_sampler_354
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.6445
common_nodes: [CLIPVisionLoader, DrawViTPose, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2069422147151417345.json, 视频生成/图生视频/2050899529087635457.json, 视频生成/图生视频/1983039224398131201.json, 视频生成/图生视频/1980910878105227266.json, 视频生成/图生视频/1982691601984167937.json, 视频生成/图生视频/2070126355764830210.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_354

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/2069422147151417345.json、视频生成/图生视频/2050899529087635457.json、视频生成/图生视频/1983039224398131201.json、视频生成/图生视频/1980910878105227266.json、视频生成/图生视频/1982691601984167937.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 5/6 个有
- `GetNode` —— 4/6 个有
- `ImageFromBatch` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `BlockifyMask` —— 3/6 个有
- `DrawMaskOnImage` —— 3/6 个有
- `ImageConcanate` —— 3/6 个有
- `ImageResize+` —— 3/6 个有
- `ImageResizeKJv2` —— 3/6 个有
- `SeCModelLoader` —— 3/6 个有
- `SeCVideoSegmentation` —— 3/6 个有
- `WanVideoSetBlockSwap` —— 3/6 个有
- `WanVideoSetLoRAs` —— 3/6 个有
- `LayerMask: MaskGrow` —— 2/6 个有
- `LayerMask: MaskPreview` —— 2/6 个有
- `PointsEditor` —— 2/6 个有
- `SaveImage` —— 1/6 个有
- `WanVideoContextOptions` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
