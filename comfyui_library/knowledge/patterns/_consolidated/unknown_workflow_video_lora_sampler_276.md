---
name: unknown_workflow_video_lora_sampler_276
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.664625
common_nodes: [GetNode, INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, SetNode, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/chronoedit_kj_example_1985639843248123906.json, 图片生成/文生图/wan2_2-ki-文生图_1956565680000782337.json, 视频生成/图生视频/03-15-01-WAN2.1-长视频多段生成-SVI_1992627593610588161.json, 视频生成/图生视频/SVI FILM长视频工作流（适合多场景）_1985341047272316930.json, 视频生成/图生视频/SVI SHOT 1分钟长视频（适合变化小的）_1985248262460481537.json, 视频生成/图生视频/SVI+2.0+SmoothMix+长序列图生视频无限延长生成工作流_2057618532237664258.json, 视频生成/图生视频/SVI-Wan22 长视频_1998600702769422338.json, 视频生成/文生视频/6窗口-svi-film长视频生产_1983866504603172866.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_276

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/chronoedit_kj_example_1985639843248123906.json、图片生成/文生图/wan2_2-ki-文生图_1956565680000782337.json、视频生成/图生视频/03-15-01-WAN2.1-长视频多段生成-SVI_1992627593610588161.json、视频生成/图生视频/SVI FILM长视频工作流（适合多场景）_1985341047272316930.json、视频生成/图生视频/SVI SHOT 1分钟长视频（适合变化小的）_1985248262460481537.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 8 个 workflow 都包含：
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageRangeFromBatch` —— 7/8 个有
- `VHS_VideoCombine` —— 7/8 个有
- `WanVideoTorchCompileSettings` —— 7/8 个有
- `GetImageSizeAndCount` —— 6/8 个有
- `ImageBatchMulti` —— 6/8 个有
- `RepeatImageBatch` —— 6/8 个有
- `SimpleMath+` —— 6/8 个有
- `CLIPVisionLoader` —— 5/8 个有
- `WanVideoClipVisionEncode` —— 5/8 个有
- `InvertMask` —— 4/8 个有
- `WanVideoSetLoRAs` —— 4/8 个有
- `WanVideoVACEStartToEndFrame` —— 4/8 个有
- `CLIPLoader` —— 2/8 个有
- `CLIPTextEncode` —— 2/8 个有
- `ColorMatch` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `SaveImage` —— 2/8 个有
- `VRAM_Debug` —— 2/8 个有
- `WanVideoTextEmbedBridge` —— 2/8 个有
- `AILab_QwenVL` —— 1/8 个有
- `Fast Groups Bypasser (rgthree)` —— 1/8 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/8 个有
- `PreviewAny` —— 1/8 个有
- `String Literal` —— 1/8 个有
- `Text Load Line From File` —— 1/8 个有
- `WanVideoEmptyEmbeds` —— 1/8 个有
- `easy showAnything` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
