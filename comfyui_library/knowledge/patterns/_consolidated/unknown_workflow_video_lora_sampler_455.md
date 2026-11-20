---
name: unknown_workflow_video_lora_sampler_455
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.4348
common_nodes: [CLIPVisionLoader, DrawMaskOnImage, INTConstant, ImageResizeKJv2, LoadImage, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy int]
problems: []
missing: []
members: [图片生成/文生图/YJ-FAST-WanAnimate-服装迁移-abao-tmp2-测试-简易_2036362537280741377.json, 数字人/数字人/YJ-APP-WanAnimate-视频人物替换_2034926423135232002.json, 视频生成/图生视频/WanAnimate_Sec-人物_动作迁移（解决长视频偏色等劣化问题）_2027340250565054465.json, 视频生成/图生视频/Work-Fisher-WanAnimate_Sec-人物迁移_动作迁移_长视频循环_2018160297319604226.json, 视频生成/图生视频/无线时长视频换人_2001302724798971906.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_455

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/YJ-FAST-WanAnimate-服装迁移-abao-tmp2-测试-简易_2036362537280741377.json、数字人/数字人/YJ-APP-WanAnimate-视频人物替换_2034926423135232002.json、视频生成/图生视频/WanAnimate_Sec-人物_动作迁移（解决长视频偏色等劣化问题）_2027340250565054465.json、视频生成/图生视频/Work-Fisher-WanAnimate_Sec-人物迁移_动作迁移_长视频循环_2018160297319604226.json、视频生成/图生视频/无线时长视频换人_2001302724798971906.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：43%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 4/5 个有
- `DrawViTPose` —— 4/5 个有
- `GetImageSizeAndCount` —— 4/5 个有
- `ImageFromBatch` —— 4/5 个有
- `OnnxDetectionModelLoader` —— 4/5 个有
- `PoseAndFaceDetection` —— 4/5 个有
- `Fast Groups Bypasser (rgthree)` —— 3/5 个有
- `GrowMaskWithBlur` —— 3/5 个有
- `PointsEditor` —— 3/5 个有
- `PrimitiveInt` —— 3/5 个有
- `SeCModelLoader` —— 3/5 个有
- `SeCVideoSegmentation` —— 3/5 个有
- `WanVideoContextOptions` —— 3/5 个有
- `easy showAnything` —— 3/5 个有
- `JjkText` —— 2/5 个有
- `RIFE VFI` —— 2/5 个有
- `ImageToMask` —— 1/5 个有
- `LayerMask: MaskGrow` —— 1/5 个有
- `RMBG` —— 1/5 个有
- `RunningHub Deepcleaner` —— 1/5 个有
- `SimpleMath+` —— 1/5 个有
- `WujiCleaner` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有
- `easy sam3ModelLoader` —— 1/5 个有
- `easy sam3VideoSegmentation` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
