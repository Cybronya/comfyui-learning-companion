---
name: unknown_workflow_controlnet_video_lora_13
type: Unknown Workflow
frequency: 9
level: strong
coverage: 0.483444
common_nodes: [Amage FPS Converter, Any Switch (rgthree), BlockifyMask, CLIPLoader, CLIPVisionLoader, CM_FloatToInt, CM_IntToFloat, CR Text, CR Text Concatenate, DWPreprocessor, Display Any (rgthree), DrawMaskOnImage, Fast Groups Bypasser (rgthree), GetImageRangeFromBatch, GetImageSize, GetNode, GroundingDinoModelLoader_SDPose, GrowMaskWithBlur, INTConstant, Image Comparer (rgthree), ImageAddMulti, ImageBlend, ImageConcatMulti, ImageResizeKJv2, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, MaskToImage, MathExpression|pysssss, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), OnnxDetectionModelLoader, PainterFluxImageEdit, PoseAndFaceDetection, PoseDetectionOneToAllAnimation, PreviewImage, PrimitiveBoolean, PrimitiveString, RH_Translator, SDPoseOODLoader, SDPoseOODProcessor, SeCModelLoader, SeCVideoSegmentation, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, VRAM_Debug, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, WanVideoVAELoader, YOLOModelLoader, easy anythingIndexSwitch, easy cleanGpuUsed, easy compare, easy framesEditor, easy ifElse, easy sam3ModelLoader, easy sam3VideoSegmentation]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/Wan animate动作迁移  长视频49s_1500帧_2058907859634704386.json, 视频生成/图生视频/Wan animate动作迁移 49s_1500帧长视频 V5_2000724883581566977.json, 视频生成/图生视频/Wan animate动作迁移 49s_1500帧长视频 V5_2051932334483623937.json, 视频生成/图生视频/Wan animate动作迁移 49s_1500帧长视频 V5_2053653917556322306.json, 视频生成/图生视频/图生视频--Wan animate动作迁移 49s_1500帧长视频 V5_2053647610828861442.json, 视频生成/图生视频/图生视频--Wan animate动作迁移 49s_1500帧长视频 V5_2054006088726523905.json, 视频生成/图生视频/图生视频--Wan animate动作迁移 49s_1500帧长视频 V5_2056233170009370625.json, 视频生成/图生视频/图生视频--Wan animate动作迁移 49s_1500帧长视频 V5_2056623424361033730.json, 视频生成/图生视频/真无敌！！Wan+animate动作迁移+49s_最长1500帧长视频_2029921582344310785.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_video_lora_13

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/Wan animate动作迁移  长视频49s_1500帧_2058907859634704386.json、视频生成/图生视频/Wan animate动作迁移 49s_1500帧长视频 V5_2000724883581566977.json、视频生成/图生视频/Wan animate动作迁移 49s_1500帧长视频 V5_2051932334483623937.json、视频生成/图生视频/Wan animate动作迁移 49s_1500帧长视频 V5_2053653917556322306.json、视频生成/图生视频/图生视频--Wan animate动作迁移 49s_1500帧长视频 V5_2053647610828861442.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：强结论
- **平均知识覆盖**：48%

## 共有节点

全部 9 个 workflow 都包含：
- `Amage FPS Converter`
- `Any Switch (rgthree)`
- `BlockifyMask`
- `CLIPLoader`
- `CLIPVisionLoader`
- `CM_FloatToInt`
- `CM_IntToFloat`
- `CR Text`
- `CR Text Concatenate`
- `DWPreprocessor`
- `Display Any (rgthree)`
- `DrawMaskOnImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageRangeFromBatch`
- `GetImageSize`
- `GetNode`
- `GroundingDinoModelLoader_SDPose`
- `GrowMaskWithBlur`
- `INTConstant`
- `Image Comparer (rgthree)`
- `ImageAddMulti`
- `ImageBlend`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `MaskToImage`
- `MathExpression|pysssss`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `OnnxDetectionModelLoader`
- `PainterFluxImageEdit`
- `PoseAndFaceDetection`
- `PoseDetectionOneToAllAnimation`
- `PreviewImage`
- `PrimitiveBoolean`
- `PrimitiveString`
- `RH_Translator`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SeCModelLoader`
- `SeCVideoSegmentation`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `VRAM_Debug`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `WanVideoVAELoader`
- `YOLOModelLoader`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`
- `easy compare`
- `easy framesEditor`
- `easy ifElse`
- `easy sam3ModelLoader`
- `easy sam3VideoSegmentation`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 9 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，9 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 高发问题（9/9 个样本）：Steps较低可能导致细节不足
