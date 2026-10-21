---
name: unknown_workflow_video_lora_sampler_10
type: Unknown Workflow
frequency: 55
level: moderate
coverage: 0.562873
common_nodes: [BlockifyMask, CLIPVisionLoader, DrawMaskOnImage, DrawViTPose, GetNode, ImageResizeKJv2, LoadImage, OnnxDetectionModelLoader, PoseAndFaceDetection, SeCModelLoader, SeCVideoSegmentation, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2015018676868616194.json, 视频生成/图生视频/2042132086164819970.json, 视频生成/图生视频/2042131699907170305.json, 视频生成/图生视频/2042176153171009537.json, 视频生成/图生视频/2042932527039516674.json, 视频生成/图生视频/2041872588984557569.json, 视频生成/图生视频/2039518740357844993.json, 视频生成/图生视频/2039615736561274882.json, 视频生成/图生视频/2021541718369247233.json, 视频生成/图生视频/Wan2.2 Animate 人物替换 精准替换 二创首选工作流_2088990764796825602.json, 视频生成/图生视频/2039613263704494081.json, 视频生成/图生视频/2039620407292076033.json, 视频生成/图生视频/kitten practicing kung fu_2084182943492300802.json, 视频生成/图生视频/kitten practicing kung fu_2091771507398762498.json, 视频生成/图生视频/2061909733405188097.json, 视频生成/图生视频/2061714173691785218.json, 视频生成/图生视频/2045436584266309633.json, 视频生成/图生视频/2045756399656898561.json, 视频生成/图生视频/2047879824609386498.json, 视频生成/图生视频/2048374565356707842.json, 视频生成/图生视频/2052077583671541761.json, 视频生成/图生视频/2052089396547072002.json, 视频生成/图生视频/2053480599746293761.json, 视频生成/图生视频/2061717483219931137.json, 视频生成/图生视频/2061732736808873986.json, 视频生成/图生视频/2046064441040572417.json, 视频生成/图生视频/2046446441639448578.json, 视频生成/图生视频/2061517996736208897.json, 视频生成/图生视频/2061703653236502530.json, 视频生成/图生视频/2025383055673794562.json, 视频生成/图生视频/2046490215514120193.json, 视频生成/图生视频/2054545413268615170.json, 视频生成/图生视频/1984107698880970753.json, 视频生成/图生视频/2077919550741499905.json, 视频生成/图生视频/2041820466159034370.json, 视频生成/图生视频/2044048099055771650.json, 视频生成/图生视频/2061522776120446978.json, 视频生成/图生视频/2061720298134786049.json, 视频生成/图生视频/2067493148099698690.json, 视频生成/图生视频/2061525825463341057.json, 视频生成/图生视频/2061706268229857282.json, 视频生成/图生视频/2039303290109825025.json, 视频生成/图生视频/2039983104382734337.json, 视频生成/图生视频/2047944109041651714.json, 视频生成/图生视频/2047960672364929025.json, 视频生成/图生视频/2048361532148420610.json, 视频生成/图生视频/2039898768174223362.json, 视频生成/图生视频/2042073520565391361.json, 视频生成/图生视频/2047907869110050818.json, 视频生成/图生视频/2053516783939801089.json, 视频生成/图生视频/2043513913018421250.json, 视频生成/图生视频/2044060077488873474.json, 视频生成/图生视频/2052436872852459521.json, 视频生成/图生视频/2052759183916843010.json, 视频生成/图生视频/2053154685997068289.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_10

> 由 `engine/knowledge_consolidation` 从 55 个 workflow 归纳得出（视频生成/图生视频/2015018676868616194.json、视频生成/图生视频/2042132086164819970.json、视频生成/图生视频/2042131699907170305.json、视频生成/图生视频/2042176153171009537.json、视频生成/图生视频/2042932527039516674.json…）

- **类型**：Unknown Workflow
- **样本数**：55
- **可信度**：中等可信
- **平均知识覆盖**：56%

## 共有节点

全部 55 个 workflow 都包含：
- `BlockifyMask`
- `CLIPVisionLoader`
- `DrawMaskOnImage`
- `DrawViTPose`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `SeCModelLoader`
- `SeCVideoSegmentation`
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

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 54/55 个有
- `GetImageSizeAndCount` —— 54/55 个有
- `GrowMask` —— 54/55 个有
- `INTConstant` —— 54/55 个有
- `ImageConcanate` —— 54/55 个有
- `InvertMask` —— 54/55 个有
- `LayerUtility: ImageBlend` —— 54/55 个有
- `MaskToImage` —— 54/55 个有
- `VHS_VideoInfo` —— 54/55 个有
- `PointsEditor` —— 53/55 个有
- `ImageFromBatch+` —— 52/55 个有
- `PreviewImage` —— 52/55 个有
- `easy cleanGpuUsed` —— 51/55 个有
- `JWInteger` —— 45/55 个有
- `ImageFromBatch` —— 3/55 个有
- `ImageScaleToTotalPixels` —— 2/55 个有
- `IndexTTSNode` —— 2/55 个有
- `MemoryCleaner` —— 2/55 个有
- `SeedVR2LoadDiTModel` —— 2/55 个有
- `SeedVR2LoadVAEModel` —— 2/55 个有
- `SeedVR2VideoUpscaler` —— 2/55 个有
- `Text Multiline` —— 2/55 个有
- `WanVideoTorchCompileSettings` —— 2/55 个有
- `easy framesEditor` —— 2/55 个有
- `GetImageSize` —— 1/55 个有
- `GrowMaskWithBlur` —— 1/55 个有
- `ImpactConditionalBranch` —— 1/55 个有
- `Int` —— 1/55 个有
- `LayerMask: MaskPreview` —— 1/55 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/55 个有
- `PrimitiveInt` —— 1/55 个有
- `PrimitiveStringMultiline` —— 1/55 个有
- `WanVideoContextOptions` —— 1/55 个有
- `easy compare` —— 1/55 个有
- `easy int` —— 1/55 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
