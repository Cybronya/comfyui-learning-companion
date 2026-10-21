---
name: unknown_workflow_video_sampler_vae_69
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.969286
common_nodes: [INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1965428165915103234.json, 视频生成/图生视频/1966850900927057922.json, 视频生成/图生视频/1950574501610311681.json, 视频生成/图生视频/1950204585861365762.json, 视频生成/图生视频/1966739330226139137.json, 视频生成/图生视频/1967834051866406914.json, 视频生成/图生视频/1967815071856472066.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_69

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1965428165915103234.json、视频生成/图生视频/1966850900927057922.json、视频生成/图生视频/1950574501610311681.json、视频生成/图生视频/1950204585861365762.json、视频生成/图生视频/1966739330226139137.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateCFGScheduleFloatList` —— 6/7 个有
- `WanVideoLoraSelect` —— 6/7 个有
- `WanVideoSetBlockSwap` —— 6/7 个有
- `WanVideoSetLoRAs` —— 6/7 个有
- `WanVideoVACEEncode` —— 5/7 个有
- `WanVideoVACEModelSelect` —— 5/7 个有
- `VHS_LoadVideo` —— 4/7 个有
- `DWPreprocessor` —— 3/7 个有
- `GetImageSizeAndCount` —— 3/7 个有
- `ImageConcatMulti` —— 3/7 个有
- `VHS_VideoInfo` —— 3/7 个有
- `CLIPLoader` —— 2/7 个有
- `CLIPTextEncode` —— 2/7 个有
- `CR Text` —— 2/7 个有
- `Note Plus (mtb)` —— 2/7 个有
- `SimpleMath+` —— 2/7 个有
- `WanVideoImageToVideoEncode` —— 2/7 个有
- `WanVideoTextEmbedBridge` —— 2/7 个有
- `AIO_Preprocessor` —— 1/7 个有
- `ColorMatch` —— 1/7 个有
- `ImpactInt` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `WanVideoVACEStartToEndFrame` —— 1/7 个有
- `easy int` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
