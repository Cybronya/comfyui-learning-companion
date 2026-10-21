---
name: unknown_workflow_video_sampler_vae_17
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.622429
common_nodes: [Anything Everywhere, GetNode, ImageResize+, Int, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoVAELoader]
problems: []
missing: [CR String To Number, CR Text, CR Text Concatenate, ImageCASharpening+, LayerUtility: PurgeVRAM V2, MathExpression|pysssss, easy cleanGpuUsed, easy int, ImageResize+]
members: [视频生成/图生视频/1989163247343382530.json, 视频生成/图生视频/1941491329644052481.json, 视频生成/图生视频/1935089059322896386.json, 视频生成/图生视频/1935147311754321921.json, 视频生成/图生视频/2039609556543741954.json, 视频生成/图生视频/1952905614798295042.json, 视频生成/图生视频/1952534346064441346.json, 视频生成/图生视频/1951088586961694722.json, 视频生成/图生视频/2029075141904306178.json, 视频生成/图生视频/2030461301822070785.json, 视频生成/图生视频/2041390268406046721.json, 视频生成/图生视频/2012093297564585986.json, 视频生成/文生视频/1978980050555015169.json, 视频生成/文生视频/1958341618350899202.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_17

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/图生视频/1989163247343382530.json、视频生成/图生视频/1941491329644052481.json、视频生成/图生视频/1935089059322896386.json、视频生成/图生视频/1935147311754321921.json、视频生成/图生视频/2039609556543741954.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 14 个 workflow 都包含：
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
- `CLIPVisionLoader` —— 12/14 个有
- `RHHiddenNodes` —— 12/14 个有
- `WanVideoClipVisionEncode` —— 12/14 个有
- `WanVideoImageToVideoEncode` —— 12/14 个有
- `WanVideoLoraSelect` —— 12/14 个有
- `CogVideoEnhanceAVideo` —— 11/14 个有
- `WanVideoExperimentalArgs` —— 11/14 个有
- `WanVideoSLG` —— 11/14 个有
- `CR Text` —— 9/14 个有
- `ColorCorrectOfUtils` —— 9/14 个有
- `CreateCFGScheduleFloatList` —— 9/14 个有
- `ImageCASharpening+` —— 9/14 个有
- `JWInteger` —— 9/14 个有
- `LayerUtility: PurgeVRAM V2` —— 9/14 个有
- `easy cleanGpuUsed` —— 9/14 个有
- `PreviewImage` —— 8/14 个有
- `CR String To Number` —— 7/14 个有
- `FluxResolutionNode` —— 7/14 个有
- `InversionDemoLazyIndexSwitch` —— 7/14 个有
- `WanVideoApplyNAG` —— 7/14 个有
- `WanVideoTextEncode` —— 7/14 个有
- `WanVideoTextEncodeSingle` —— 7/14 个有
- `easy int` —— 7/14 个有
- `easy showAnything` —— 7/14 个有
- `CR Text Concatenate` —— 5/14 个有
- `WanVideoTorchCompileSettings` —— 5/14 个有
- `ShowText|pysssss` —— 4/14 个有
- `ImageConcanate` —— 3/14 个有
- `easy textSwitch` —— 3/14 个有
- `GetImageSizeAndCount` —— 2/14 个有
- `WanVideoVACEEncode` —— 2/14 个有
- `WanVideoVACEStartToEndFrame` —— 2/14 个有
- `easy imageConcat` —— 2/14 个有
- `RH_Nano_Banana2_Image2Image` —— 1/14 个有
- `SaveImage` —— 1/14 个有
- `WanVideoSetLoRAs` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR String To Number、CR Text、CR Text Concatenate、ImageCASharpening+、LayerUtility: PurgeVRAM V2
