---
name: unknown_workflow_controlnet_video_lora_41
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.5105
common_nodes: [Anything Everywhere, CLIPVisionLoader, CR Prompt Text, DrawViTPose, GetImageSizeAndCount, GetNode, ImageConcatMulti, ImageFromBatch+, ImageResizeKJv2, JWInteger, LoadImage, Manual XY Entry Info, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/Wan Animate2.2各种风格视频转绘集合_1971230843148681218.json, 平台全量/Wan Animate2.2替换主体和背景V2_1976640783187054593.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_41

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/Wan Animate2.2各种风格视频转绘集合_1971230843148681218.json、平台全量/Wan Animate2.2替换主体和背景V2_1976640783187054593.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：51%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageConcatMulti`
- `ImageFromBatch+`
- `ImageResizeKJv2`
- `JWInteger`
- `LoadImage`
- `Manual XY Entry Info`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `CR String To Combo` —— 1/2 个有
- `Display Any (rgthree)` —— 1/2 个有
- `Int2String` —— 1/2 个有
- `Primitive integer [Crystools]` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `RunningHub OmniConsistency LoraLoader` —— 1/2 个有
- `RunningHub OmniConsistency Sampler` —— 1/2 个有
- `Switch any [Crystools]` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `TextSwitchCase` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
