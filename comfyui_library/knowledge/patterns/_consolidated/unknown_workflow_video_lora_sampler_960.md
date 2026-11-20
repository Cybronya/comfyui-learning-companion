---
name: unknown_workflow_video_lora_sampler_960
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.555
common_nodes: [CLIPVisionLoader, DrawMaskOnImage, INTConstant, ImageResizeKJv2, JjkText, LoadImage, PreviewImage, RIFE VFI, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader, easy int]
problems: []
missing: []
members: [图片生成/文生图/YJ-FAST-WanAnimate-服装迁移-abao-tmp2-测试-简易_2036362537280741377.json, 数字人/数字人/YJ-APP-WanAnimate-视频人物替换_2034926423135232002.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_960

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/YJ-FAST-WanAnimate-服装迁移-abao-tmp2-测试-简易_2036362537280741377.json、数字人/数字人/YJ-APP-WanAnimate-视频人物替换_2034926423135232002.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：55%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `INTConstant`
- `ImageResizeKJv2`
- `JjkText`
- `LoadImage`
- `PreviewImage`
- `RIFE VFI`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
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
- `BlockifyMask` —— 1/2 个有
- `DrawViTPose` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `ImageFromBatch` —— 1/2 个有
- `ImageToMask` —— 1/2 个有
- `LayerMask: MaskGrow` —— 1/2 个有
- `OnnxDetectionModelLoader` —— 1/2 个有
- `PoseAndFaceDetection` —— 1/2 个有
- `RMBG` —— 1/2 个有
- `RunningHub Deepcleaner` —— 1/2 个有
- `SimpleMath+` —— 1/2 个有
- `WujiCleaner` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有
- `easy sam3ModelLoader` —— 1/2 个有
- `easy sam3VideoSegmentation` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
