---
name: unknown_workflow_video_lora_sampler_156
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.703643
common_nodes: [CLIPVisionLoader, ImageResizeKJv2, LoadImage, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoVAELoader]
problems: []
missing: []
members: [平台全量/单人、双人、多人视频SCAIL丝滑动作运镜迁移  适配各种风格运行速度嘎嘎快_2000959757265629186.json, 平台全量/固定镜头跳舞迁移_2058793226844336129.json, 平台全量/多人动作迁移_2002430717466406913.json, 平台全量/多（人）动物跳舞-SCAIL_2016061837359456257.json, 平台全量/智绘动作迁移-支持多人(二创必选)_2015736014836338690.json, 平台全量/智绘动作迁移-支持多人(二创必选)_2015742560509104129.json, 平台全量/智绘动作迁移：多人同框互动迁移_2016094115393441794.json, 平台全量/智绘动作迁移：支持复杂运动+比例自适应调整（单人版）_2016100105018941442.json, 平台全量/最新SCAIL动作迁移美女跳舞，支持双人对战_2061424859514757122.json, 平台全量/最新SCAIL萌宠跳舞动作迁移 多人动作迁移_2016431715253751810.json, 平台全量/自用-Scail 一键跳舞！骨骼完美驱动！_2010716676785967105.json, 平台全量/视频-动作迁移单人-wan2.1-SCAIL-KJ_2001889566749519874.json, 平台全量/视频-动作迁移多人-wan2.1-SCAIL-KJ_2001836547823550465.json, 数字人/数字人/视频-动作迁移单人-wan2.1-SCAIL-KJ_2011817884372180993.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_156

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（平台全量/单人、双人、多人视频SCAIL丝滑动作运镜迁移  适配各种风格运行速度嘎嘎快_2000959757265629186.json、平台全量/固定镜头跳舞迁移_2058793226844336129.json、平台全量/多人动作迁移_2002430717466406913.json、平台全量/多（人）动物跳舞-SCAIL_2016061837359456257.json、平台全量/智绘动作迁移-支持多人(二创必选)_2015736014836338690.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `LoadImage`
- `NLFPredict`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `RenderNLFPoses`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerExtraArgs`
- `WanVideoSamplerv2`
- `WanVideoSchedulerv2`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `DownloadAndLoadNLFModel` —— 12/14 个有
- `GetImageSizeAndCount` —— 12/14 个有
- `ImageConcatMulti` —— 12/14 个有
- `WanVideoSetBlockSwap` —— 12/14 个有
- `WanVideoSetLoRAs` —— 12/14 个有
- `GetNode` —— 11/14 个有
- `LoadWanVideoT5TextEncoder` —— 11/14 个有
- `SetNode` —— 11/14 个有
- `SimpleMath+` —— 11/14 个有
- `WanVideoEncode` —— 11/14 个有
- `WanVideoTextEncode` —— 11/14 个有
- `WanVideoTorchCompileSettings` —— 11/14 个有
- `WanVideoUni3C_ControlnetLoader` —— 11/14 个有
- `WanVideoUni3C_embeds` —— 11/14 个有
- `FloatConstant` —— 10/14 个有
- `ConvertOpenPoseKeypointsToDWPose` —— 9/14 个有
- `DWPreprocessor` —— 9/14 个有
- `INTConstant` —— 9/14 个有
- `PreviewImage` —— 6/14 个有
- `easy int` —— 6/14 个有
- `CM_IntToFloat` —— 3/14 个有
- `CR Text` —— 3/14 个有
- `Fast Groups Bypasser (rgthree)` —— 3/14 个有
- `Florence2ModelLoader` —— 3/14 个有
- `Florence2Run` —— 3/14 个有
- `ImageFromBatch` —— 3/14 个有
- `ImageFromBatch+` —— 3/14 个有
- `Int` —— 3/14 个有
- `Label (rgthree)` —— 3/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/14 个有
- `MathExpression|pysssss` —— 3/14 个有
- `ShowText|pysssss` —— 3/14 个有
- `SimpleCalculatorKJ` —— 3/14 个有
- `VHS_VideoInfoLoaded` —— 3/14 个有
- `WanVideoTextEncodeCached` —— 3/14 个有
- `easy anythingIndexSwitch` —— 3/14 个有
- `easy positive` —— 3/14 个有
- `easy seed` —— 3/14 个有
- `easy showAnything` —— 3/14 个有
- `LoadNLFModel` —— 2/14 个有
- `CustomAddLabel` —— 1/14 个有
- `Fast Bypasser (rgthree)` —— 1/14 个有
- `JWInteger` —— 1/14 个有
- `Mute / Bypass Repeater (rgthree)` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
