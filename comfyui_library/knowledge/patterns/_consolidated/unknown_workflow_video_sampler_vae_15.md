---
name: unknown_workflow_video_sampler_vae_15
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.662933
common_nodes: [Anything Everywhere, GetNode, ImageResize+, Int, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1989163247343382530.json, 视频生成/图生视频/1941491329644052481.json, 视频生成/图生视频/1935089059322896386.json, 视频生成/图生视频/1935147311754321921.json, 视频生成/图生视频/2039609556543741954.json, 视频生成/图生视频/1952905614798295042.json, 视频生成/图生视频/1952534346064441346.json, 视频生成/图生视频/1951088586961694722.json, 视频生成/图生视频/2029075141904306178.json, 视频生成/图生视频/2030461301822070785.json, 视频生成/图生视频/2041390268406046721.json, 视频生成/图生视频/2012093297564585986.json, 视频生成/图生视频/2041003408856977412.json, 视频生成/图生视频/2058188130242621442.json, 视频生成/图生视频/2068868048580333570.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_15

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/1989163247343382530.json、视频生成/图生视频/1941491329644052481.json、视频生成/图生视频/1935089059322896386.json、视频生成/图生视频/1935147311754321921.json、视频生成/图生视频/2039609556543741954.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 15 个 workflow 都包含：
- `Anything Everywhere`
- `GetNode`
- `ImageResize+`
- `Int`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionLoader` —— 13/15 个有
- `WanVideoClipVisionEncode` —— 13/15 个有
- `WanVideoImageToVideoEncode` —— 13/15 个有
- `WanVideoLoraSelect` —— 13/15 个有
- `CogVideoEnhanceAVideo` —— 12/15 个有
- `RHHiddenNodes` —— 12/15 个有
- `WanVideoExperimentalArgs` —— 12/15 个有
- `WanVideoSLG` —— 12/15 个有
- `PreviewImage` —— 11/15 个有
- `CR Text` —— 10/15 个有
- `ColorCorrectOfUtils` —— 10/15 个有
- `CreateCFGScheduleFloatList` —— 10/15 个有
- `ImageCASharpening+` —— 10/15 个有
- `JWInteger` —— 10/15 个有
- `LayerUtility: PurgeVRAM V2` —— 10/15 个有
- `easy cleanGpuUsed` —— 10/15 个有
- `CR String To Number` —— 8/15 个有
- `FluxResolutionNode` —— 8/15 个有
- `InversionDemoLazyIndexSwitch` —— 8/15 个有
- `WanVideoTextEncode` —— 8/15 个有
- `easy int` —— 8/15 个有
- `easy showAnything` —— 8/15 个有
- `WanVideoApplyNAG` —— 7/15 个有
- `WanVideoTextEncodeSingle` —— 7/15 个有
- `CR Text Concatenate` —— 4/15 个有
- `ShowText|pysssss` —— 4/15 个有
- `WanVideoSetLoRAs` —— 4/15 个有
- `ImageConcanate` —— 3/15 个有
- `ImageCropV2` —— 3/15 个有
- `ImageResizeKJ` —— 3/15 个有
- `ImageScale` —— 3/15 个有
- `PrimitiveBoundingBox` —— 3/15 个有
- `RH_LLMAPI_Pro_Node` —— 3/15 个有
- `SaveImage` —— 3/15 个有
- `VHS_LoadVideo` —— 3/15 个有
- `VHS_VideoInfo` —— 3/15 个有
- `WanVideoTorchCompileSettings` —— 3/15 个有
- `Any Switch (rgthree)` —— 2/15 个有
- `Comfly_api_set` —— 2/15 个有
- `Comfly_gpt_image_2_official_ratio` —— 2/15 个有
- `Fast Groups Muter (rgthree)` —— 2/15 个有
- `GetImageSizeAndCount` —— 2/15 个有
- `RH_Nano_Banana2_Image2Image` —— 2/15 个有
- `RH_RhartImageG2ImageToImage` —— 2/15 个有
- `WanVideoVACEEncode` —— 2/15 个有
- `WanVideoVACEStartToEndFrame` —— 2/15 个有
- `easy imageConcat` —— 2/15 个有
- `easy textSwitch` —— 2/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
