---
name: unknown_workflow_video_lora_sampler_21
type: Unknown Workflow
frequency: 28
level: moderate
coverage: 0.680429
common_nodes: [Anything Everywhere, CLIPVisionLoader, CR String To Number, CR Text, FluxResolutionNode, GetNode, ImageCASharpening+, ImageResize+, Int, InversionDemoLazyIndexSwitch, JWInteger, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoVAELoader, easy cleanGpuUsed, easy int, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1978980050555015169.json, 视频生成/图生视频/2010899703377960962.json, 视频生成/图生视频/1979077194871902210.json, 视频生成/图生视频/2047489081042542593.json, 视频生成/图生视频/2018852274944090113.json, 视频生成/图生视频/1981885885119643650.json, 视频生成/图生视频/1951203527219720194.json, 视频生成/图生视频/1962522962995855362.json, 视频生成/图生视频/1983778975518531585.json, 视频生成/图生视频/1958007892207185921.json, 视频生成/图生视频/2048675014282584066.json, 视频生成/图生视频/1979015207190171649.json, 视频生成/图生视频/1933812324643819521.json, 视频生成/图生视频/1951105819150589953.json, 视频生成/图生视频/2067073649651306497.json, 视频生成/图生视频/2067075192274382849.json, 视频生成/图生视频/1931043397564608513.json, 视频生成/图生视频/1950329201004077057.json, 视频生成/图生视频/2039984689393442817.json, 视频生成/图生视频/2043879387652694017.json, 视频生成/图生视频/1955450074836996098.json, 视频生成/图生视频/1955598143335403521.json, 视频生成/图生视频/2007976462116200450.json, 视频生成/图生视频/2037787300108705793.json, 视频生成/图生视频/1934553565845200897.json, 视频生成/图生视频/1951191570521464834.json, 视频生成/图生视频/1991161112701829121.json, 视频生成/图生视频/1951090702346297346.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_21

> 由 `engine/knowledge_consolidation` 从 28 个 workflow 归纳得出（视频生成/图生视频/1978980050555015169.json、视频生成/图生视频/2010899703377960962.json、视频生成/图生视频/1979077194871902210.json、视频生成/图生视频/2047489081042542593.json、视频生成/图生视频/2018852274944090113.json…）

- **类型**：Unknown Workflow
- **样本数**：28
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 28 个 workflow 都包含：
- `Anything Everywhere`
- `CLIPVisionLoader`
- `CR String To Number`
- `CR Text`
- `FluxResolutionNode`
- `GetNode`
- `ImageCASharpening+`
- `ImageResize+`
- `Int`
- `InversionDemoLazyIndexSwitch`
- `JWInteger`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `easy int`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 27/28 个有
- `WanVideoTextEncode` —— 27/28 个有
- `ColorCorrectOfUtils` —— 26/28 个有
- `CreateCFGScheduleFloatList` —— 25/28 个有
- `RHHiddenNodes` —— 25/28 个有
- `CogVideoEnhanceAVideo` —— 23/28 个有
- `WanVideoExperimentalArgs` —— 23/28 个有
- `WanVideoSLG` —— 23/28 个有
- `CR Text Concatenate` —— 15/28 个有
- `WanVideoTorchCompileSettings` —— 14/28 个有
- `ShowText|pysssss` —— 8/28 个有
- `PreviewImage` —— 4/28 个有
- `RH_Nano_Banana2_Image2Image` —— 4/28 个有
- `SaveImage` —— 4/28 个有
- `WanVideoSetLoRAs` —— 4/28 个有
- `AudioCrop` —— 3/28 个有
- `LoadAudio` —— 3/28 个有
- `PreviewAudio` —— 3/28 个有
- `PreviewBridge` —— 3/28 个有
- `VHS_LoadVideo` —— 3/28 个有
- `easy anythingIndexSwitch` —— 3/28 个有
- `easy textSwitch` —— 3/28 个有
- `AudioCombine` —— 2/28 个有
- `Evaluate Integers` —— 2/28 个有
- `MMAudioFeatureUtilsLoader` —— 2/28 个有
- `MMAudioModelLoader` —— 2/28 个有
- `MMAudioSampler` —— 2/28 个有
- `RH_LLMAPI_NODE` —— 2/28 个有
- `Text Multiline` —— 2/28 个有
- `WanVideoApplyNAG` —— 2/28 个有
- `WanVideoTeaCache` —— 2/28 个有
- `AudioCleanupNode` —— 1/28 个有
- `LayerColor: Brightness & Contrast` —— 1/28 个有
- `RH_Captioner` —— 1/28 个有
- `WanVideoTextEncodeSingle` —— 1/28 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
