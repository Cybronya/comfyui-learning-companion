---
name: unknown_workflow_video_lora_sampler_578
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.929
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, Primitive integer [Crystools], VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-14B+Lightx2v图生视频加速版-高清放大+30帧补帧_1955296499754307586.json, 视频生成/图生视频/Wan2.2-14B+Lightx2v图生视频加速版-高清放大+补帧+New_1955172399558770689.json, 视频生成/图生视频/Wan2.2-14B+Lightx2v图生视频加速版放大补帧生成2K高清视频_1950107460180860930.json, 视频生成/图生视频/宠物飞天特效图生视频lora_1955612950611443714.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_578

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-14B+Lightx2v图生视频加速版-高清放大+30帧补帧_1955296499754307586.json、视频生成/图生视频/Wan2.2-14B+Lightx2v图生视频加速版-高清放大+补帧+New_1955172399558770689.json、视频生成/图生视频/Wan2.2-14B+Lightx2v图生视频加速版放大补帧生成2K高清视频_1950107460180860930.json、视频生成/图生视频/宠物飞天特效图生视频lora_1955612950611443714.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `Primitive integer [Crystools]`
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

**可变部分**（部分 workflow 才有）：
- `CreateCFGScheduleFloatList` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `ImageUpscaleWithModel` —— 3/4 个有
- `JWInteger` —— 3/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/4 个有
- `RH_Captioner` —— 3/4 个有
- `RIFE VFI` —— 3/4 个有
- `ShowText|pysssss` —— 3/4 个有
- `SimpleMath+` —— 3/4 个有
- `UpscaleModelLoader` —— 3/4 个有
- `easy cleanGpuUsed` —— 3/4 个有
- `ImageResize+` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `GetImageSizeAndCount` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
