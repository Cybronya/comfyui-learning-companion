---
name: unknown_workflow_video_sampler
type: Unknown Workflow
frequency: 21
level: moderate
coverage: 0.671048
common_nodes: [BlockifyMask, CLIPVisionLoader, DWPreprocessor, DownloadAndLoadFlorence2Model, DownloadAndLoadSAM2Model, DrawMaskOnImage, Florence2Run, Florence2toCoordinates, GrowMask, INTConstant, ImageResizeKJv2, LayerUtility: PurgeVRAM V2, LoadImage, PixelPerfectResolution, PrimitiveString, RH_Captioner, RH_Translator, RMBG, Sam2Segmentation, SetNode, ShowText|pysssss, Text Concatenate, Text Multiline, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, WanVideoDecode, WanVideoSLG, WanVideoSampler, WanVideoSetBlockSwap, WanVideoTeaCache, WanVideoTextEncodeCached, easy cleanGpuUsed]
problems: []
missing: []
members: [视频生成/图生视频/2025792425880457218.json, 视频生成/图生视频/2019640646428004354.json, 视频生成/图生视频/2008359387471024130.json, 视频生成/图生视频/2013086174964883457.json, 视频生成/图生视频/2034147966063218690.json, 视频生成/图生视频/2027913310934409217.json, 视频生成/图生视频/2015707307723722753.json, 视频生成/图生视频/2028027873109479425.json, 视频生成/图生视频/2012880075087159297.json, 视频生成/图生视频/2046535118042439682.json, 视频生成/图生视频/2025898220341174274.json, 视频生成/图生视频/2043279973837971458.json, 视频生成/图生视频/2019297921283399682.json, 视频生成/图生视频/2040848580549808130.json, 视频生成/图生视频/1999438379999690753.json, 视频生成/图生视频/角色替换+动作迁移+面部表情=爆款复刻_2002585990092976129.json, 视频生成/图生视频/2039659074442235906.json, 视频生成/图生视频/2040676433374220290.json, 视频生成/图生视频/2012155604432850945.json, 视频生成/图生视频/2012703937253609473.json, 视频生成/文生视频/Wan2.2Animate：角色、动作、表情的三位一体！全维角色重塑，影随心动的迁移艺术_2045338312193351682.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler

> 由 `engine/knowledge_consolidation` 从 21 个 workflow 归纳得出（视频生成/图生视频/2025792425880457218.json、视频生成/图生视频/2019640646428004354.json、视频生成/图生视频/2008359387471024130.json、视频生成/图生视频/2013086174964883457.json、视频生成/图生视频/2034147966063218690.json…）

- **类型**：Unknown Workflow
- **样本数**：21
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 21 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadSAM2Model`
- `DrawMaskOnImage`
- `Florence2Run`
- `Florence2toCoordinates`
- `GrowMask`
- `INTConstant`
- `ImageResizeKJv2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `PixelPerfectResolution`
- `PrimitiveString`
- `RH_Captioner`
- `RH_Translator`
- `RMBG`
- `Sam2Segmentation`
- `SetNode`
- `ShowText|pysssss`
- `Text Concatenate`
- `Text Multiline`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoTeaCache`
- `WanVideoTextEncodeCached`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 20/21 个有
- `OnnxDetectionModelLoader` —— 20/21 个有
- `PoseAndFaceDetection` —— 20/21 个有
- `Primitive integer [Crystools]` —— 20/21 个有
- `SimpleMath+` —— 20/21 个有
- `easy anythingIndexSwitch` —— 20/21 个有
- `easy showAnything` —— 17/21 个有
- `ShowAnything|Mie` —— 12/21 个有
- `LayerMask: MaskPreview` —— 11/21 个有
- `PreviewImage` —— 11/21 个有
- `WanVideoBlockSwap` —— 11/21 个有
- `WanVideoLoraSelectMulti` —— 11/21 个有
- `WanVideoModelLoader` —— 11/21 个有
- `WanVideoSetLoRAs` —— 11/21 个有
- `WanVideoTorchCompileSettings` —— 11/21 个有
- `WanVideoVAELoader` —— 11/21 个有
- `FaceMaskFromPoseKeypoints` —— 10/21 个有
- `ImageCropByMaskAndResize` —— 10/21 个有
- `ImageResizeKJ` —— 10/21 个有
- `RHHiddenNodes` —— 10/21 个有
- `Compare` —— 2/21 个有
- `If ANY execute A else B` —— 2/21 个有
- `Text` —— 2/21 个有
- `VHS_VideoInfoLoaded` —— 1/21 个有
- `WanVideoEncode` —— 1/21 个有
- `WanVideoUni3C_ControlnetLoader` —— 1/21 个有
- `WanVideoUni3C_embeds` —— 1/21 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
