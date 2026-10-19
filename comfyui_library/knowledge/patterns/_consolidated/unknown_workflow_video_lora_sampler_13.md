---
name: unknown_workflow_video_lora_sampler_13
type: Unknown Workflow
frequency: 39
level: moderate
coverage: 0.699462
common_nodes: [CLIPVisionLoader, ConvertOpenPoseKeypointsToDWPose, ImageResizeKJv2, Int, LoadImage, NLFPredict, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, RenderNLFPoses, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerExtraArgs, WanVideoSamplerv2, WanVideoSchedulerv2, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2014280344236724226.json, 视频生成/图生视频/2015659195076452354.json, 视频生成/图生视频/SCAIL 动物多人跳舞小猫小狗人物跳舞视频工作流 scaila 多人跳舞跨物种舞蹈合拍生成神器_2015747193864462338.json, 视频生成/图生视频/2028347107450560514.json, 视频生成/图生视频/2000467442830897154.json, 视频生成/图生视频/2014586479497977857.json, 视频生成/图生视频/2015807283493605378.json, 视频生成/图生视频/2060202407728074754.json, 视频生成/图生视频/2061258943049068546.json, 视频生成/图生视频/2070055592605081601.json, 视频生成/图生视频/2070875275063283713.json, 视频生成/图生视频/2003797202612961282.json, 视频生成/图生视频/2013930664512462850.json, 视频生成/图生视频/2070419354554036226.json, 视频生成/图生视频/2069249951540015105.json, 视频生成/图生视频/2003741598695497730.json, 视频生成/图生视频/2004185141352296449.json, 视频生成/图生视频/2016200341376737281.json, 视频生成/图生视频/2013066531797737474.json, 视频生成/图生视频/2063413138116145153.json, 视频生成/图生视频/2061338178342178818.json, 视频生成/图生视频/2057470162856665090.json, 视频生成/图生视频/2027611708860145666.json, 视频生成/图生视频/2033355110813802497.json, 视频生成/图生视频/2014580771620659201.json, 视频生成/图生视频/2016085257711263746.json, 视频生成/图生视频/2022569352733663234.json, 视频生成/图生视频/2063499066276925442.json, 视频生成/图生视频/2027264869686317057.json, 视频生成/图生视频/2057793982742228993.json, 视频生成/图生视频/2044291284843630593.json, 视频生成/图生视频/2014181903984762881.json, 视频生成/图生视频/2036792778885173250.json, 视频生成/图生视频/2062564633763995649.json, 视频生成/图生视频/2065067395315757058.json, 视频生成/图生视频/2065103727006142465.json, 视频生成/图生视频/2067593207650807809.json, 视频生成/图生视频/2067595594784395266.json, 视频生成/图生视频/2044671295245262850.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_13

> 由 `engine/knowledge_consolidation` 从 39 个 workflow 归纳得出（视频生成/图生视频/2014280344236724226.json、视频生成/图生视频/2015659195076452354.json、视频生成/图生视频/SCAIL 动物多人跳舞小猫小狗人物跳舞视频工作流 scaila 多人跳舞跨物种舞蹈合拍生成神器_2015747193864462338.json、视频生成/图生视频/2028347107450560514.json、视频生成/图生视频/2000467442830897154.json…）

- **类型**：Unknown Workflow
- **样本数**：39
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 39 个 workflow 都包含：
- `CLIPVisionLoader`
- `ConvertOpenPoseKeypointsToDWPose`
- `ImageResizeKJv2`
- `Int`
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
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 38/39 个有
- `DWPreprocessor` —— 38/39 个有
- `SDPoseOODLoader` —— 38/39 个有
- `SDPoseOODProcessor` —— 38/39 个有
- `YOLOModelLoader` —— 38/39 个有
- `GroundingDinoModelLoader_SDPose` —— 36/39 个有
- `LoadWanVideoT5TextEncoder` —— 36/39 个有
- `SimpleMath+` —— 36/39 个有
- `WanVideoTextEncode` —— 36/39 个有
- `ImageConcatMulti` —— 27/39 个有
- `GetNode` —— 23/39 个有
- `SetNode` —— 23/39 个有
- `WanVideoEncode` —— 22/39 个有
- `WanVideoUni3C_ControlnetLoader` —— 22/39 个有
- `WanVideoUni3C_embeds` —— 22/39 个有
- `Any Switch (rgthree)` —— 21/39 个有
- `DownloadAndLoadNLFModel` —— 21/39 个有
- `INTConstant` —— 21/39 个有
- `WanVideoSetLoRAs` —— 21/39 个有
- `easy cleanGpuUsed` —— 21/39 个有
- `GetImageSizeAndCount` —— 20/39 个有
- `LoadNLFModel` —— 18/39 个有
- `VHS_VideoInfoLoaded` —— 18/39 个有
- `LayerUtility: PurgeVRAM V2` —— 17/39 个有
- `Fast Groups Muter (rgthree)` —— 15/39 个有
- `Fast Groups Bypasser (rgthree)` —— 8/39 个有
- `GetImageRangeFromBatch` —— 7/39 个有
- `PreviewImage` —— 5/39 个有
- `FloatConstant` —— 3/39 个有
- `RIFE VFI` —— 3/39 个有
- `SimpleCalculatorKJ` —— 3/39 个有
- `TwoWaySwitch` —— 3/39 个有
- `WanVideoSetBlockSwap` —— 3/39 个有
- `WanVideoTextEncodeCached` —— 3/39 个有
- `SaveImage` —— 2/39 个有
- `BatchThief` —— 1/39 个有
- `Label (rgthree)` —— 1/39 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/39 个有
- `RH_Nano_Banana2_Image2Image` —— 1/39 个有
- `VHS_VideoInfo` —— 1/39 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
