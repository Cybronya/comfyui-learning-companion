---
name: unknown_workflow_video_lora_sampler_490
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.493833
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, GetNode, ImageResizeKJv2, Int, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, SDPoseOODLoader, SDPoseOODProcessor, SetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, YOLOModelLoader]
problems: []
missing: []
members: [平台全量/Wan2.2 Animate动作迁移 个人自用更新第三版4.16_2015321059171508225.json, 平台全量/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose动作识别_2037066553992159233.json, 平台全量/复制抖音，爆款舞蹈，动作迁移，表情迁移，千问姿态识别_2018704980445765633.json, 数字人/数字人/动作迁移+表情迁移 升级版本_1996485212181766146.json, 数字人/数字人/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2045340909658705922.json, 视频生成/图生视频/Wan2.2-Animate 视频换装+换脸+换人三合一_2048980034509086721.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_490

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/Wan2.2 Animate动作迁移 个人自用更新第三版4.16_2015321059171508225.json、平台全量/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose动作识别_2037066553992159233.json、平台全量/复制抖音，爆款舞蹈，动作迁移，表情迁移，千问姿态识别_2018704980445765633.json、数字人/数字人/动作迁移+表情迁移 升级版本_1996485212181766146.json、数字人/数字人/动作迁移+表情迁移—Wan2.2AnimateV2+SDPose姿态识别_2045340909658705922.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `GetNode`
- `ImageResizeKJv2`
- `Int`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
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
- `YOLOModelLoader`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 4/6 个有
- `Text` —— 3/6 个有
- `WanVideoContextOptions` —— 3/6 个有
- `DrawViTPose` —— 2/6 个有
- `INTConstant` —— 2/6 个有
- `ImpactSwitch` —— 2/6 个有
- `MemoryCleaner` —— 2/6 个有
- `MuyeTextEditOutput` —— 2/6 个有
- `Primitive integer [Crystools]` —— 2/6 个有
- `SimpleMath+` —— 2/6 个有
- `WanVideoTeaCache` —— 2/6 个有
- `ZML_AnyTypeSwitchFive` —— 2/6 个有
- `easy anythingIndexSwitch` —— 2/6 个有
- `easy float` —— 2/6 个有
- `easy showAnything` —— 2/6 个有
- `BlockifyMask` —— 1/6 个有
- `DeepTranslatorTextNode` —— 1/6 个有
- `DrawMaskOnImage` —— 1/6 个有
- `Evaluate Integers` —— 1/6 个有
- `GrowMaskWithBlur` —— 1/6 个有
- `JWStringMultiline` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `LayerUtility: PurgeVRAM V2` —— 1/6 个有
- `easy sam3ModelLoader` —— 1/6 个有
- `easy sam3VideoModelExtraConfig` —— 1/6 个有
- `easy sam3VideoSegmentation` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
