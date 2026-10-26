---
name: unknown_workflow_video_sampler_vae_89
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8924
common_nodes: [DrawViTPose, ImageResizeKJv2, LayerUtility: PurgeVRAM V2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2 Animate视频主体替换（带货专用）_1985317372301033473.json, 视频生成/图生视频/Wan2.2 Animate姿势参考图生视频_1980564316481044481.json, 视频生成/图生视频/Wan2.2 Animate视频主体替换_1981764143114010626.json, 视频生成/图生视频/Wan2.2Animate主体替换-跳舞_1969243872620650498.json, 视频生成/图生视频/视频替换_跟随动作二合一 wan animate v2 工作流_1975214578143465474.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_89

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Wan2.2 Animate视频主体替换（带货专用）_1985317372301033473.json、视频生成/图生视频/Wan2.2 Animate姿势参考图生视频_1980564316481044481.json、视频生成/图生视频/Wan2.2 Animate视频主体替换_1981764143114010626.json、视频生成/图生视频/Wan2.2Animate主体替换-跳舞_1969243872620650498.json、视频生成/图生视频/视频替换_跟随动作二合一 wan animate v2 工作流_1975214578143465474.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `DrawViTPose`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 4/5 个有
- `CR Text` —— 4/5 个有
- `DownloadAndLoadSAM2Model` —— 4/5 个有
- `DrawMaskOnImage` —— 4/5 个有
- `GetImageSizeAndCount` —— 4/5 个有
- `GrowMaskWithBlur` —— 4/5 个有
- `ImageFromBatch+` —— 4/5 个有
- `PrimitiveInt` —— 4/5 个有
- `Sam2Segmentation` —— 4/5 个有
- `SimpleMath+` —— 4/5 个有
- `VHS_VideoInfo` —— 4/5 个有
- `WanVideoLoraSelect` —— 4/5 个有
- `CLIPVisionLoader` —— 2/5 个有
- `WanVideoClipVisionEncode` —— 2/5 个有
- `Int` —— 1/5 个有
- `LG_LoadImage` —— 1/5 个有
- `Switch any [Crystools]` —— 1/5 个有
- `Text` —— 1/5 个有
- `WanVideoLoraSelectMulti` —— 1/5 个有
- `WanVideoSetLoRAs` —— 1/5 个有
- `easy boolean` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
