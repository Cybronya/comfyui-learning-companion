---
name: unknown_workflow_video_lora_sampler_572
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.55675
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, GetNode, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan Animate2.2动作迁移V3(Move) 骨骼增强版_2073292954780917762.json, 视频生成/图生视频/Wan2.2 Animate人物动作+表情迁移_1972599286972231682.json, 视频生成/图生视频/animate+move视频动作模仿_2042582047956410370.json, 视频生成/图生视频/姿态声音Animate Wan2.2 增强更新版人物一致性百分百_1974720060226973697.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_572

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Wan Animate2.2动作迁移V3(Move) 骨骼增强版_2073292954780917762.json、视频生成/图生视频/Wan2.2 Animate人物动作+表情迁移_1972599286972231682.json、视频生成/图生视频/animate+move视频动作模仿_2042582047956410370.json、视频生成/图生视频/姿态声音Animate Wan2.2 增强更新版人物一致性百分百_1974720060226973697.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SetNode`
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `ImageConcatMulti` —— 3/4 个有
- `JWInteger` —— 3/4 个有
- `DWPreprocessor` —— 2/4 个有
- `DrawViTPose` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `EmptyImage` —— 1/4 个有
- `Int` —— 1/4 个有
- `PixelPerfectResolution` —— 1/4 个有
- `PoseDetectionOneToAllAnimation` —— 1/4 个有
- `PoseRetargetPromptHelper` —— 1/4 个有
- `Primitive integer [Crystools]` —— 1/4 个有
- `VHS_VideoInfo` —— 1/4 个有
- `WanVideoTorchCompileSettings` —— 1/4 个有
- `easy anythingIndexSwitch` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
