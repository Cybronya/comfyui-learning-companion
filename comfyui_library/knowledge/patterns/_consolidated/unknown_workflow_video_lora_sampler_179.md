---
name: unknown_workflow_video_lora_sampler_179
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.551636
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetNode, GrowMask, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/Wan2.2-Animate_去AI感新版动作迁移，美女跳舞（体型自适应 脸部更一致）_1971077076524638209.json, 数字人/数字人/Wan Animate V2版 视频多人场景精准替换_1970675787114422273.json, 数字人/数字人/Wan2.2 Animate V2替换视频人物，保留原声_1983884901671993345.json, 视频生成/图生视频/(骨骼自适应)Wan2.2 Animate V2模型Move模式运动迁移V1_1998610915446677506.json, 视频生成/图生视频/Wan2.2 Animate 双重脸部一致性优化Mix主体迁移版V1（ED作者参数版）_1971950073557020673.json, 视频生成/图生视频/Wan2.2 Animate 双重脸部一致性优化Mix主体迁移版V2（ED实验版）_1971886866809221121.json, 视频生成/图生视频/Wan2.2 Animate 多重组合脸部一致性优化Mix主体迁移加速版V2（ED实验版）_1971891163009642497.json, 视频生成/图生视频/Wan2.2 Animate高质量电商换模特_1972598111484968962.json, 视频生成/图生视频/溪南人物替换，影视、动漫二创V2_1998309417806389249.json, 视频生成/图生视频/超自动化+超多功能+拉满质量wan2.2 animate超长时长优化 t8 kj v2 不超级版_1975795950243418113.json, 视频生成/图生视频/超自动化+超多功能+拉满质量wan2.2 animate超长时长优化 t8 kj v2 不超级版_1988846148821585921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_179

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/Wan2.2-Animate_去AI感新版动作迁移，美女跳舞（体型自适应 脸部更一致）_1971077076524638209.json、数字人/数字人/Wan Animate V2版 视频多人场景精准替换_1970675787114422273.json、数字人/数字人/Wan2.2 Animate V2替换视频人物，保留原声_1983884901671993345.json、视频生成/图生视频/(骨骼自适应)Wan2.2 Animate V2模型Move模式运动迁移V1_1998610915446677506.json、视频生成/图生视频/Wan2.2 Animate 双重脸部一致性优化Mix主体迁移版V1（ED作者参数版）_1971950073557020673.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：55%

## 共有节点

全部 11 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetNode`
- `GrowMask`
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
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetImageSizeAndCount` —— 10/11 个有
- `ImageConcatMulti` —— 10/11 个有
- `ImageResizeKJv2` —— 10/11 个有
- `PointsEditor` —— 10/11 个有
- `PoseRetargetPromptHelper` —— 10/11 个有
- `DownloadAndLoadSAM2Model` —— 9/11 个有
- `JWInteger` —— 9/11 个有
- `Sam2Segmentation` —— 9/11 个有
- `WanVideoTorchCompileSettings` —— 9/11 个有
- `WanVideoEncode` —— 8/11 个有
- `WanVideoUni3C_ControlnetLoader` —— 8/11 个有
- `WanVideoUni3C_embeds` —— 8/11 个有
- `ACE_ImageFaceCrop` —— 7/11 个有
- `WanVideoContextOptions` —— 7/11 个有
- `CR Prompt Text` —— 6/11 个有
- `PrimitiveStringMultiline` —— 3/11 个有
- `DF_Text_Box` —— 2/11 个有
- `Float to Int` —— 2/11 个有
- `Int` —— 2/11 个有
- `JWLoopImageSequence` —— 2/11 个有
- `RHHiddenNodes` —— 2/11 个有
- `SeCModelLoader` —— 2/11 个有
- `SeCVideoSegmentation` —— 2/11 个有
- `SimpleMath+` —— 2/11 个有
- `easy float` —— 2/11 个有
- `Anything Everywhere` —— 1/11 个有
- `EmptyImage` —— 1/11 个有
- `ImageBatch` —— 1/11 个有
- `ImageFromBatch+` —— 1/11 个有
- `ImageResize+` —— 1/11 个有
- `LayerMask: MaskPreview` —— 1/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/11 个有
- `LayerUtility: PurgeVRAM` —— 1/11 个有
- `LayerUtility: PurgeVRAM V2` —— 1/11 个有
- `MathExpression|pysssss` —— 1/11 个有
- `Note Plus (mtb)` —— 1/11 个有
- `PoseDetectionOneToAllAnimation` —— 1/11 个有
- `PreviewImage` —— 1/11 个有
- `RepeatImageBatch` —— 1/11 个有
- `SaveImage` —— 1/11 个有
- `easy anythingIndexSwitch` —— 1/11 个有
- `easy cleanGpuUsed` —— 1/11 个有
- `easy forLoopEnd` —— 1/11 个有
- `easy forLoopStart` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
