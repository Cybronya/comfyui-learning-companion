---
name: unknown_workflow_video_upscale_sampler_4
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.629667
common_nodes: [ImageUpscaleWithModel, LoadImage, LoadWanVideoT5TextEncoder, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/KJ版Wan2.1图生视频_1921919410783846402.json, 视频生成/图生视频/360度旋转效果Wan2.1_1922551848883077121.json, 视频生成/图生视频/Wan 2.1_14B图生视频加速版 LightX2V_5步工作流_1936301542691491841.json, 视频生成/图生视频/Wan 2.1_14B图生视频超详细基础工作流_1933833926945198081.json, 视频生成/图生视频/Wan 2.1_14B首尾帧图生视频加速LightX2V工作流_1936331081635254274.json, 视频生成/图生视频/Wan 2.1_14B首尾帧图生视频超详细基础工作流_1935669711310872577.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_sampler_4

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/KJ版Wan2.1图生视频_1921919410783846402.json、视频生成/图生视频/360度旋转效果Wan2.1_1922551848883077121.json、视频生成/图生视频/Wan 2.1_14B图生视频加速版 LightX2V_5步工作流_1936301542691491841.json、视频生成/图生视频/Wan 2.1_14B图生视频超详细基础工作流_1933833926945198081.json、视频生成/图生视频/Wan 2.1_14B首尾帧图生视频加速LightX2V工作流_1936331081635254274.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 6 个 workflow 都包含：
- `ImageUpscaleWithModel`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `WanVideoExperimentalArgs` —— 5/6 个有
- `WanVideoSLG` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `CLIPVisionLoader` —— 4/6 个有
- `Fast Groups Bypasser (rgthree)` —— 4/6 个有
- `GetNode` —— 4/6 个有
- `Int` —— 4/6 个有
- `MathExpression|pysssss` —— 4/6 个有
- `RH_OneShot_Prompter` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `WanVideoClipVisionEncode` —— 4/6 个有
- `WanVideoImageToVideoEncode` —— 4/6 个有
- `easy showAnything` —— 4/6 个有
- `RH_Captioner` —— 3/6 个有
- `Text` —— 3/6 个有
- `WanVideoLoraSelect` —— 3/6 个有
- `WanVideoTeaCache` —— 3/6 个有
- `WanVideoVACEModelSelect` —— 3/6 个有
- `GetImageSize+` —— 2/6 个有
- `ImageConcanate` —— 2/6 个有
- `PrimitiveInt` —— 2/6 个有
- `RIFE VFI` —— 2/6 个有
- `WanVideoVACEEncode` —— 2/6 个有
- `WanVideoVACEStartToEndFrame` —— 2/6 个有
- `ImageResizeKJv2` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `easy promptConcat` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
