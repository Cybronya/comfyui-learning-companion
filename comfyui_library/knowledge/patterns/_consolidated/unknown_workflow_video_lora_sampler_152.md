---
name: unknown_workflow_video_lora_sampler_152
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.678857
common_nodes: [CLIPVisionLoader, LoadImage, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/Wan Animate2.2动作迁移（无限时长）_2005534329495322626.json, 平台全量/Wan Animate姿势迁移KJ版_1990428195201716225.json, 平台全量/Wan Animate角色替换KJ版_1990777123520585729.json, 平台全量/Wan2.2 Animate V2全自动视频人物替换_1978460418932887554.json, 平台全量/【直出高清】人物跳舞动作迁移Wan2.2+Animate+V2版本（超快5分钟）_1975571105782083586.json, 平台全量/动作迁移人物替换图生视频Wan2.2 Animate V2版本（支持10s）_1975502091256991746.json, 平台全量/🦖Wan Animate2.2动物迁移_1975784351843659777.json, 数字人/数字人/Wan2.2 Animate V2替换视频人物，保留原声_1983884901671993345.json, 视频生成/图生视频/(骨骼自适应)Wan2.2 Animate V2模型Move模式运动迁移V1_1998610915446677506.json, 视频生成/图生视频/Wan Animate2.2主体迁移（自动裁剪脸部，增强主体一致性）v3_1972998201764655106.json, 视频生成/图生视频/（自用）Wan Animate KJ V2版Move模式视频V2（换装前置）_1977660761738739714.json, 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Mix主体混合版V2_1974413564041670657.json, 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Move运动迁移Uni3c运镜版V1_1974430400560893954.json, 视频生成/文生视频/Wan2.2 Animate V2模型高质量版本一致性优化Move运动迁移V1_1974423112462766082.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_152

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（平台全量/Wan Animate2.2动作迁移（无限时长）_2005534329495322626.json、平台全量/Wan Animate姿势迁移KJ版_1990428195201716225.json、平台全量/Wan Animate角色替换KJ版_1990777123520585729.json、平台全量/Wan2.2 Animate V2全自动视频人物替换_1978460418932887554.json、平台全量/【直出高清】人物跳舞动作迁移Wan2.2+Animate+V2版本（超快5分钟）_1975571105782083586.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPVisionLoader`
- `LoadImage`
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
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 13/14 个有
- `OnnxDetectionModelLoader` —— 13/14 个有
- `PoseAndFaceDetection` —— 13/14 个有
- `WanVideoSetLoRAs` —— 13/14 个有
- `WanVideoTorchCompileSettings` —— 13/14 个有
- `BlockifyMask` —— 12/14 个有
- `DrawMaskOnImage` —— 12/14 个有
- `DrawViTPose` —— 12/14 个有
- `GrowMask` —— 12/14 个有
- `ImageConcatMulti` —— 12/14 个有
- `ImageResizeKJv2` —— 12/14 个有
- `CR Prompt Text` —— 11/14 个有
- `JWInteger` —— 11/14 个有
- `ACE_ImageFaceCrop` —— 10/14 个有
- `DownloadAndLoadSAM2Model` —— 10/14 个有
- `GetNode` —— 10/14 个有
- `Sam2Segmentation` —— 10/14 个有
- `SetNode` —— 10/14 个有
- `PointsEditor` —— 9/14 个有
- `PoseRetargetPromptHelper` —— 9/14 个有
- `easy showAnything` —— 9/14 个有
- `WanVideoContextOptions` —— 7/14 个有
- `WanVideoEncode` —— 7/14 个有
- `WanVideoUni3C_ControlnetLoader` —— 7/14 个有
- `WanVideoUni3C_embeds` —— 7/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/14 个有
- `VHS_VideoInfo` —— 4/14 个有
- `SimpleMath+` —— 3/14 个有
- `DF_Int_to_Float` —— 2/14 个有
- `MathExpression|pysssss` —— 2/14 个有
- `PixelPerfectResolution` —— 2/14 个有
- `RMBG` —— 2/14 个有
- `SaveImage` —— 2/14 个有
- `AnimalPosePreprocessor` —— 1/14 个有
- `Bjornulf_ShowInt` —— 1/14 个有
- `DWPreprocessor` —— 1/14 个有
- `EmptyImage` —— 1/14 个有
- `INTConstant` —— 1/14 个有
- `PoseDetectionOneToAllAnimation` —— 1/14 个有
- `TT_img_enc_v2` —— 1/14 个有
- `easy anythingIndexSwitch` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
