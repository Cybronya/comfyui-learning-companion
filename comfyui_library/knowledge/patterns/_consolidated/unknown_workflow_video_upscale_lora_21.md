---
name: unknown_workflow_video_upscale_lora_21
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.925667
common_nodes: [CreateCFGScheduleFloatList, ImageResizeKJv2, ImageUpscaleWithModel, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, Primitive integer [Crystools], RIFE VFI, SimpleMath+, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-14B+Lightx2v图生视频加速版-高清放大+30帧补帧_1955296499754307586.json, 视频生成/图生视频/Wan2.2-14B+Lightx2v图生视频加速版-高清放大+补帧+New_1955172399558770689.json, 视频生成/图生视频/Wan2.2-14B+Lightx2v图生视频加速版放大补帧生成2K高清视频_1950107460180860930.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_21

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-14B+Lightx2v图生视频加速版-高清放大+30帧补帧_1955296499754307586.json、视频生成/图生视频/Wan2.2-14B+Lightx2v图生视频加速版-高清放大+补帧+New_1955172399558770689.json、视频生成/图生视频/Wan2.2-14B+Lightx2v图生视频加速版放大补帧生成2K高清视频_1950107460180860930.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `ImageResizeKJv2`
- `ImageUpscaleWithModel`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Primitive integer [Crystools]`
- `RIFE VFI`
- `SimpleMath+`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `ImageResize+` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `ShowText|pysssss` —— 2/3 个有
- `Text Multiline` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
