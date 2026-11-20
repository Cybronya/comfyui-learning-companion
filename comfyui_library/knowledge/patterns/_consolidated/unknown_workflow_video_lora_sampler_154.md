---
name: unknown_workflow_video_lora_sampler_154
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.59
common_nodes: [CLIPVisionLoader, GetImageSizeAndCount, ImageConcatMulti, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/动作+运镜迁移_2029542798399115265.json, 数字人/数字人/带货视频角色替换稳定版_2019053733203677185.json, 视频生成/图生视频/Wan Animate2.2人物融合(Mix)V2增强版_2073214426706173954.json, 视频生成/图生视频/Wan Animate2.2人物融合_2073212185333026818.json, 视频生成/图生视频/Wan Animate2.2加速版无限时长_1969703078859579394.json, 视频生成/图生视频/Wan Animate2.2动作迁移Move魔改加速版V2（无限时长）_1969116607094157313.json, 视频生成/图生视频/Wan Animate2.2动作迁移V2(Move)增强版_2073218471797805057.json, 视频生成/图生视频/Wan Animate2.2动作迁移_2073212149740163073.json, 视频生成/图生视频/Wan2.2 Animate 双重脸部一致性优化Mix主体迁移版V1（ED作者参数版）_1971950073557020673.json, 视频生成/图生视频/Wan2.2 Animate 双重脸部一致性优化Mix主体迁移版V2（ED实验版）_1971886866809221121.json, 视频生成/图生视频/Wan2.2 Animate 多重组合脸部一致性优化Mix主体迁移加速版V2（ED实验版）_1971891163009642497.json, 视频生成/图生视频/溪南人物替换，影视、动漫二创V2_1998309417806389249.json, 视频生成/图生视频/超自动化+超多功能+拉满质量wan2.2 animate超长时长优化 t8 kj v2 不超级版_1975795950243418113.json, 视频生成/图生视频/超自动化+超多功能+拉满质量wan2.2 animate超长时长优化 t8 kj v2 不超级版_1988846148821585921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_154

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（平台全量/动作+运镜迁移_2029542798399115265.json、数字人/数字人/带货视频角色替换稳定版_2019053733203677185.json、视频生成/图生视频/Wan Animate2.2人物融合(Mix)V2增强版_2073214426706173954.json、视频生成/图生视频/Wan Animate2.2人物融合_2073212185333026818.json、视频生成/图生视频/Wan Animate2.2加速版无限时长_1969703078859579394.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：59%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 13/14 个有
- `DrawMaskOnImage` —— 13/14 个有
- `GrowMask` —— 13/14 个有
- `PointsEditor` —— 13/14 个有
- `DownloadAndLoadSAM2Model` —— 12/14 个有
- `GetNode` —— 12/14 个有
- `ImageResizeKJv2` —— 12/14 个有
- `JWInteger` —— 12/14 个有
- `Sam2Segmentation` —— 12/14 个有
- `SetNode` —— 12/14 个有
- `WanVideoLoraSelectMulti` —— 12/14 个有
- `WanVideoTorchCompileSettings` —— 12/14 个有
- `CR Prompt Text` —— 10/14 个有
- `DrawViTPose` —— 9/14 个有
- `OnnxDetectionModelLoader` —— 9/14 个有
- `PoseAndFaceDetection` —— 9/14 个有
- `WanVideoEncode` —— 9/14 个有
- `WanVideoUni3C_ControlnetLoader` —— 9/14 个有
- `WanVideoUni3C_embeds` —— 9/14 个有
- `ACE_ImageFaceCrop` —— 7/14 个有
- `WanVideoContextOptions` —— 7/14 个有
- `PoseRetargetPromptHelper` —— 6/14 个有
- `easy showAnything` —— 6/14 个有
- `LayerUtility: PurgeVRAM` —— 5/14 个有
- `DWPreprocessor` —— 4/14 个有
- `FaceMaskFromPoseKeypoints` —— 4/14 个有
- `ImageCropByMaskAndResize` —— 4/14 个有
- `PixelPerfectResolution` —— 4/14 个有
- `RHHiddenNodes` —— 3/14 个有
- `DF_Text_Box` —— 2/14 个有
- `Float to Int` —— 2/14 个有
- `JWLoopImageSequence` —— 2/14 个有
- `Label (rgthree)` —— 2/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/14 个有
- `PrimitiveStringMultiline` —— 2/14 个有
- `SimpleMath+` —— 2/14 个有
- `VHS_VideoInfo` —— 2/14 个有
- `easy float` —— 2/14 个有
- `ImageBatch` —— 1/14 个有
- `ImageFromBatch+` —— 1/14 个有
- `Int` —— 1/14 个有
- `MathExpression|pysssss` —— 1/14 个有
- `Note Plus (mtb)` —— 1/14 个有
- `SeCModelLoader` —— 1/14 个有
- `SeCVideoSegmentation` —— 1/14 个有
- `easy forLoopEnd` —— 1/14 个有
- `easy forLoopStart` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
