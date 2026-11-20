---
name: unknown_workflow_video_lora_sampler_441
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.753286
common_nodes: [DWPreprocessor, ImageResizeKJv2, LoadImage, PixelPerfectResolution, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/43.tonnie-Wan2.2 Animate视频动作迁移_2004764267972882433.json, 视频生成/图生视频/47.tonnie-Wan2.2 VACE 视频动作迁移_2007574568222859266.json, 视频生成/图生视频/wan2.2Animate美女跳舞工作流_2033057095406329858.json, 视频生成/图生视频/【人物替换】Wan2.2+Animate+角色替换视频动作迁移+KJ加速版-StarAI_1982315306993500162.json, 视频生成/图生视频/优化版 人物模特替换 动作克隆 首尾帧+角色替换 Wan2.2+Animate+角色替换视频动作迁移_1995682413978193921.json, 视频生成/图生视频/新Wan2.2 Animate-动作迁移_1983713271683457025.json, 视频生成/图生视频/男用动作迁移复制一键跳舞Wan2.2-Animate-视频动作迁移_2067576219452919809.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_441

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/43.tonnie-Wan2.2 Animate视频动作迁移_2004764267972882433.json、视频生成/图生视频/47.tonnie-Wan2.2 VACE 视频动作迁移_2007574568222859266.json、视频生成/图生视频/wan2.2Animate美女跳舞工作流_2033057095406329858.json、视频生成/图生视频/【人物替换】Wan2.2+Animate+角色替换视频动作迁移+KJ加速版-StarAI_1982315306993500162.json、视频生成/图生视频/优化版 人物模特替换 动作克隆 首尾帧+角色替换 Wan2.2+Animate+角色替换视频动作迁移_1995682413978193921.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 7 个 workflow 都包含：
- `DWPreprocessor`
- `ImageResizeKJv2`
- `LoadImage`
- `PixelPerfectResolution`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 6/7 个有
- `WanVideoClipVisionEncode` —— 6/7 个有
- `FaceMaskFromPoseKeypoints` —— 5/7 个有
- `ImageConcatMulti` —— 5/7 个有
- `ImageCropByMaskAndResize` —— 5/7 个有
- `WanVideoSetLoRAs` —— 5/7 个有
- `GetImageSizeAndCount` —— 4/7 个有
- `JWInteger` —— 4/7 个有
- `WanVideoAnimateEmbeds` —— 4/7 个有
- `GetNode` —— 3/7 个有
- `INTConstant` —— 3/7 个有
- `SetNode` —— 3/7 个有
- `CR Text` —— 2/7 个有
- `Int` —— 2/7 个有
- `RHHiddenNodes` —— 2/7 个有
- `Text` —— 2/7 个有
- `WanVideoTorchCompileSettings` —— 2/7 个有
- `CreateCFGScheduleFloatList` —— 1/7 个有
- `SaveImage` —— 1/7 个有
- `SimpleMath+` —— 1/7 个有
- `TT_img_enc` —— 1/7 个有
- `WanVideoVACEEncode` —— 1/7 个有
- `WanVideoVACEModelSelect` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
