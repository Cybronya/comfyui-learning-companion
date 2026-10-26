---
name: unknown_workflow_video_lora_sampler_96
type: Unknown Workflow
frequency: 16
level: moderate
coverage: 0.336375
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetNode, GrowMask, ImageBlend, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, PreviewImage, PrimitiveInt, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [图片生成/图生图/Wan Animate_Mix_KJ版_正式版 最强人物替换 动作迁移_2012510535283118082.json, 数字人/数字人/Wan2.2-Animate【换人迁移】kj遮罩-高质+快速+细节_1990762965668405249.json, 数字人/数字人/自用动作迁移_2001962250321707010.json, 数字人/数字人/自用影视二创人物替换_2003676483702956034.json, 视频生成/图生视频/Wan Animate_Mix_KJ版_人物迁移视频_1996047658001317889.json, 视频生成/图生视频/Wan Animate_Mix_KJ版_正式版 最强人物替换 动作迁移_2011070672583270401.json, 视频生成/图生视频/Wan Animate_Mix_KJ版_正式版_1998677074959327233.json, 视频生成/图生视频/Wan Animate_Mix_KJ版_正式版_2004430696947085313.json, 视频生成/图生视频/Wan Animate_Mix_KJ版_正式版最强视频人物替换、动作迁移_2059530149854539777.json, 视频生成/图生视频/Wan Animate_Mix_KJ版动作迁移 v2_2043972881754890241.json, 视频生成/图生视频/Wan Animate_Mix_KJ版动作迁移_1997150814663819266.json, 视频生成/图生视频/Wan animate升级版 影视二创_1997671860680765442.json, 视频生成/图生视频/Wan+Animate_8807_2009294068987203586.json, 视频生成/图生视频/YZ金鱼-Wan Animate_Mix_KJ版_正式版_1994708135476596738.json, 视频生成/图生视频/人物替换（自用）_2015831314653515777.json, 视频生成/图生视频/角色替换_Wan Animate_2003406585529573378.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_96

> 由 `engine/knowledge_consolidation` 从 16 个 workflow 归纳得出（图片生成/图生图/Wan Animate_Mix_KJ版_正式版 最强人物替换 动作迁移_2012510535283118082.json、数字人/数字人/Wan2.2-Animate【换人迁移】kj遮罩-高质+快速+细节_1990762965668405249.json、数字人/数字人/自用动作迁移_2001962250321707010.json、数字人/数字人/自用影视二创人物替换_2003676483702956034.json、视频生成/图生视频/Wan Animate_Mix_KJ版_人物迁移视频_1996047658001317889.json…）

- **类型**：Unknown Workflow
- **样本数**：16
- **可信度**：中等可信
- **平均知识覆盖**：34%

## 共有节点

全部 16 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetNode`
- `GrowMask`
- `ImageBlend`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `PreviewImage`
- `PrimitiveInt`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 15/16 个有
- `ImageFromBatch` —— 15/16 个有
- `ImageResizeKJv2` —— 15/16 个有
- `PointsEditor` —— 15/16 个有
- `CoordinatePlotter` —— 14/16 个有
- `INTConstant` —— 14/16 个有
- `PlaySound|pysssss` —— 14/16 个有
- `PrimitiveFloat` —— 14/16 个有
- `RHHiddenNodes` —— 14/16 个有
- `RIFE VFI` —— 14/16 个有
- `SDPoseOODLoader` —— 14/16 个有
- `SDPoseOODProcessor` —— 14/16 个有
- `SeCModelLoader_Ultra-Fast` —— 14/16 个有
- `SeCVideoSegmentation_Ultra-Fast` —— 14/16 个有
- `easy int` —— 2/16 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/16 个有
- `GIMMVFI_interpolate` —— 1/16 个有
- `GetImageSizeAndCount` —— 1/16 个有
- `ImageConcatMulti` —— 1/16 个有
- `ImageRemoveBackground+` —— 1/16 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 1/16 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/16 个有
- `PreviewAny` —— 1/16 个有
- `PrimitiveStringMultiline` —— 1/16 个有
- `RMBG` —— 1/16 个有
- `RemBGSession+` —— 1/16 个有
- `SeCModelLoader` —— 1/16 个有
- `SeCVideoSegmentation` —— 1/16 个有
- `Seed (rgthree)` —— 1/16 个有
- `easy showAnything` —— 1/16 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
