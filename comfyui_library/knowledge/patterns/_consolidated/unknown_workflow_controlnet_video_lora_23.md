---
name: unknown_workflow_controlnet_video_lora_23
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.925667
common_nodes: [CLIPVisionLoader, DWPreprocessor, DrawViTPose, GetImageSizeAndCount, ImageConcatMulti, JoinStrings, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, OnnxDetectionModelLoader, PixelPerfectResolution, PoseAndFaceDetection, PrimitiveStringMultiline, RH_Captioner, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy int]
problems: []
missing: []
members: [视频生成/图生视频/动作迁移+可多镜头+面部表情参考_1982728839811997698.json, 视频生成/图生视频/动作迁移+面部表情参考 (长视频版本）_1982639964624175105.json, 视频生成/图生视频/动作迁移+面部表情参考-WAN-AnimateV2_1971179799987265537.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_23

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/动作迁移+可多镜头+面部表情参考_1982728839811997698.json、视频生成/图生视频/动作迁移+面部表情参考 (长视频版本）_1982639964624175105.json、视频生成/图生视频/动作迁移+面部表情参考-WAN-AnimateV2_1971179799987265537.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DrawViTPose`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `JoinStrings`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PixelPerfectResolution`
- `PoseAndFaceDetection`
- `PrimitiveStringMultiline`
- `RH_Captioner`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageBlend` —— 2/3 个有
- `LayerUtility: ColorImage V2` —— 1/3 个有
- `easy anythingIndexSwitch` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
