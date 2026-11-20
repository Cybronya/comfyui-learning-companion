---
name: unknown_workflow_video_sampler_18
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.652875
common_nodes: [CLIPVisionLoader, DWPreprocessor, GetNode, INTConstant, LoadImage, PixelPerfectResolution, Primitive integer [Crystools], RH_Captioner, SetNode, ShowText|pysssss, SimpleMath+, Text Concatenate, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoDecode, WanVideoSampler, WanVideoTextEncodeCached, easy anythingIndexSwitch, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/CHARM-动作迁移+面部表情-WanAnimate_1970806141703909377.json, 视频生成/图生视频/角色替换+动作迁移+面部表情-WanAnimate_1983153039076958210.json, 视频生成/图生视频/角色替换+动作迁移+面部表情=爆款复刻_2002585990092976129.json, 视频生成/图生视频/角色替换+动作迁移+面部表情=爆款复刻_2039659074442235906.json, 视频生成/图生视频/角色替换+动作迁移+面部表情=爆款复刻_2040676433374220290.json, 视频生成/图生视频/角色替换+动作迁移+面部表情=爆款复刻（优化版）_2012155604432850945.json, 视频生成/图生视频/角色重塑换脸、动作、表情 高清视频人物替换，动作迁移（支持超长时间输出）Wan2.2Animate_2012703937253609473.json, 视频生成/文生视频/Wan2.2Animate：角色、动作、表情的三位一体！全维角色重塑，影随心动的迁移艺术_2045338312193351682.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_18

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/CHARM-动作迁移+面部表情-WanAnimate_1970806141703909377.json、视频生成/图生视频/角色替换+动作迁移+面部表情-WanAnimate_1983153039076958210.json、视频生成/图生视频/角色替换+动作迁移+面部表情=爆款复刻_2002585990092976129.json、视频生成/图生视频/角色替换+动作迁移+面部表情=爆款复刻_2039659074442235906.json、视频生成/图生视频/角色替换+动作迁移+面部表情=爆款复刻_2040676433374220290.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPVisionLoader`
- `DWPreprocessor`
- `GetNode`
- `INTConstant`
- `LoadImage`
- `PixelPerfectResolution`
- `Primitive integer [Crystools]`
- `RH_Captioner`
- `SetNode`
- `ShowText|pysssss`
- `SimpleMath+`
- `Text Concatenate`
- `Text Multiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `BlockifyMask` —— 7/8 个有
- `DownloadAndLoadFlorence2Model` —— 7/8 个有
- `DownloadAndLoadSAM2Model` —— 7/8 个有
- `DrawMaskOnImage` —— 7/8 个有
- `Florence2Run` —— 7/8 个有
- `Florence2toCoordinates` —— 7/8 个有
- `GrowMask` —— 7/8 个有
- `ImageResizeKJv2` —— 7/8 个有
- `LayerUtility: PurgeVRAM V2` —— 7/8 个有
- `PrimitiveString` —— 7/8 个有
- `RH_Translator` —— 7/8 个有
- `RMBG` —— 7/8 个有
- `Sam2Segmentation` —— 7/8 个有
- `WanVideoSetBlockSwap` —— 7/8 个有
- `easy showAnything` —— 7/8 个有
- `FaceMaskFromPoseKeypoints` —— 6/8 个有
- `ImageCropByMaskAndResize` —— 6/8 个有
- `ImageResizeKJ` —— 6/8 个有
- `OnnxDetectionModelLoader` —— 6/8 个有
- `PoseAndFaceDetection` —— 6/8 个有
- `RHHiddenNodes` —— 6/8 个有
- `WanVideoSLG` —— 6/8 个有
- `WanVideoTeaCache` —— 6/8 个有
- `PreviewImage` —— 3/8 个有
- `ShowAnything|Mie` —— 3/8 个有
- `GetImageSizeAndCount` —— 2/8 个有
- `ImageConcatMulti` —— 2/8 个有
- `ImpactSwitch` —— 2/8 个有
- `LayerMask: MaskPreview` —— 2/8 个有
- `WanVideoBlockSwap` —— 2/8 个有
- `WanVideoContextOptions` —— 2/8 个有
- `WanVideoLoraSelectMulti` —— 2/8 个有
- `WanVideoModelLoader` —— 2/8 个有
- `WanVideoSetLoRAs` —— 2/8 个有
- `WanVideoTorchCompileSettings` —— 2/8 个有
- `WanVideoVAELoader` —— 2/8 个有
- `Compare` —— 1/8 个有
- `If ANY execute A else B` —— 1/8 个有
- `ImageFromBatch` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
