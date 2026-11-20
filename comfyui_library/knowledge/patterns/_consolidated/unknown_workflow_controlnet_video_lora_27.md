---
name: unknown_workflow_controlnet_video_lora_27
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.967
common_nodes: [CLIPVisionLoader, DrawViTPose, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy int]
problems: []
missing: []
members: [数字人/数字人/AI舞蹈 Animate动作迁移支持长视频_2055876427450462209.json, 数字人/数字人/AI舞蹈 Animate动作迁移支持长视频_2055885393765126145.json, 数字人/数字人/Animate动作迁移支持长视频_2055885150025732097.json, 视频生成/图生视频/动作表情迁移工作流-单路ViTPose+Draw ViT Pose_2038158092025729026.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_27

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（数字人/数字人/AI舞蹈 Animate动作迁移支持长视频_2055876427450462209.json、数字人/数字人/AI舞蹈 Animate动作迁移支持长视频_2055885393765126145.json、数字人/数字人/Animate动作迁移支持长视频_2055885150025732097.json、视频生成/图生视频/动作表情迁移工作流-单路ViTPose+Draw ViT Pose_2038158092025729026.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPVisionLoader`
- `DrawViTPose`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 3/4 个有
- `DWPreprocessor` —— 3/4 个有
- `PixelPerfectResolution` —— 3/4 个有
- `easy float` —— 3/4 个有
- `easy getNode` —— 3/4 个有
- `easy setNode` —— 3/4 个有
- `GetNode` —— 2/4 个有
- `ImageConcanate` —— 2/4 个有
- `ImageConcatMulti` —— 2/4 个有
- `SetNode` —— 2/4 个有
- `GetImageSize` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `SaveVideoRGBA` —— 1/4 个有
- `WanVideoSetBlockSwap` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
