---
name: unknown_workflow_video_upscale_lora_4
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.947714
common_nodes: [ImageUpscaleWithModel, LoadImage, LoadWanVideoT5TextEncoder, RIFE VFI, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1922551848883077121.json, 视频生成/图生视频/1938448782306508802.json, 视频生成/图生视频/1935685282568003585.json, 视频生成/图生视频/1947245269056376834.json, 视频生成/图生视频/1955296499754307586.json, 视频生成/图生视频/1955172399558770689.json, 视频生成/图生视频/1950107460180860930.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/1922551848883077121.json、视频生成/图生视频/1938448782306508802.json、视频生成/图生视频/1935685282568003585.json、视频生成/图生视频/1947245269056376834.json、视频生成/图生视频/1955296499754307586.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `ImageUpscaleWithModel`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `RIFE VFI`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJv2` —— 6/7 个有
- `JWInteger` —— 6/7 个有
- `Primitive integer [Crystools]` —— 6/7 个有
- `SimpleMath+` —— 6/7 个有
- `CLIPVisionLoader` —— 4/7 个有
- `Text Multiline` —— 4/7 个有
- `WanVideoClipVisionEncode` —— 4/7 个有
- `WanVideoEnhanceAVideo` —— 4/7 个有
- `easy cleanGpuUsed` —— 4/7 个有
- `CreateCFGScheduleFloatList` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/7 个有
- `RH_Captioner` —— 3/7 个有
- `ShowText|pysssss` —— 3/7 个有
- `WanVideoSLG` —— 3/7 个有
- `WanVideoSetBlockSwap` —— 3/7 个有
- `WanVideoSetLoRAs` —— 3/7 个有
- `ImageResize+` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `PrimitiveInt` —— 1/7 个有
- `WanVideoMagCache` —— 1/7 个有
- `WanVideoSetRadialAttention` —— 1/7 个有
- `WanVideoTeaCache` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
