---
name: unknown_workflow_controlnet_video_lora_10
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.908444
common_nodes: [CLIPVisionLoader, CR Text, DrawViTPose, ImageConcatMulti, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, easy float, easy getNode, easy int, easy setNode]
problems: []
missing: []
members: [平台全量/Animate进阶版 动作迁移+角色替换+换头+换身体，支持长视频、运镜_2015828255433035778.json, 平台全量/动作迁移+角色替换+换头+换身体，支持长视频、运镜_2061239749427421186.json, 数字人/数字人/AI舞蹈 Animate动作迁移支持长视频_2055876427450462209.json, 视频生成/图生视频/2.22Animate进阶版 动作迁移+角色替换+换头+换身体，支持长视频、运镜_2025560069735194626.json, 视频生成/图生视频/4.13_动作迁移+角色替换+换头+换身体，支持长视频、运镜_2042608499846287361.json, 视频生成/图生视频/Animate动作迁移角色替换换头换身体长视频运镜_2057464822907887617.json, 视频生成/图生视频/修改模式动作迁移+角色替换+换头+换身体，支持长视频、运镜_2044943790498123778.json, 视频生成/图生视频/修改模式动作迁移+角色替换+换头+换身体，支持长视频、运镜_2061275051634286593.json, 视频生成/图生视频/动作迁移+角色替换+换头+换身体，支持长视频、运镜_2044662499303231490.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_10

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（平台全量/Animate进阶版 动作迁移+角色替换+换头+换身体，支持长视频、运镜_2015828255433035778.json、平台全量/动作迁移+角色替换+换头+换身体，支持长视频、运镜_2061239749427421186.json、数字人/数字人/AI舞蹈 Animate动作迁移支持长视频_2055876427450462209.json、视频生成/图生视频/2.22Animate进阶版 动作迁移+角色替换+换头+换身体，支持长视频、运镜_2025560069735194626.json、视频生成/图生视频/4.13_动作迁移+角色替换+换头+换身体，支持长视频、运镜_2042608499846287361.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPVisionLoader`
- `CR Text`
- `DrawViTPose`
- `ImageConcatMulti`
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
- `easy float`
- `easy getNode`
- `easy int`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `Any Switch (rgthree)` —— 8/9 个有
- `Anything Everywhere` —— 8/9 个有
- `BlockifyMask` —— 8/9 个有
- `DrawMaskOnImage` —— 8/9 个有
- `Fast Groups Bypasser (rgthree)` —— 8/9 个有
- `GetImageRangeFromBatch` —— 8/9 个有
- `GrowMask` —— 8/9 个有
- `MaskToImage` —— 8/9 个有
- `PreviewImage` —— 8/9 个有
- `SDPoseOODLoader` —— 8/9 个有
- `SDPoseOODProcessor` —— 8/9 个有
- `YOLOModelLoader` —— 8/9 个有
- `easy framesEditor` —— 8/9 个有
- `easy sam3ModelLoader` —— 8/9 个有
- `easy sam3VideoModelExtraConfig` —— 8/9 个有
- `easy sam3VideoSegmentation` —— 8/9 个有
- `easy sam3Visualization` —— 8/9 个有
- `ImpactSwitch` —— 2/9 个有
- `Int` —— 2/9 个有
- `easy anythingIndexSwitch` —— 2/9 个有
- `easy mathInt` —— 2/9 个有
- `DWPreprocessor` —— 1/9 个有
- `PixelPerfectResolution` —— 1/9 个有
- `Primitive integer [Crystools]` —— 1/9 个有
- `SimpleMath+` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
