---
name: unknown_workflow_video_lora_sampler_11
type: Unknown Workflow
frequency: 49
level: moderate
coverage: 0.726388
common_nodes: [CLIPVisionLoader, GetImageRangeFromBatch, GetImageSizeAndCount, GetNode, LoadImage, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoAddSteadyDancerEmbeds, WanVideoClipVisionEncode, WanVideoContextOptions, WanVideoDecode, WanVideoEncode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSamplerFromSettings, WanVideoSamplerSettings, WanVideoScheduler, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2072526167571263489.json, 视频生成/图生视频/2080951206196899842.json, 视频生成/图生视频/2081641783875952641.json, 视频生成/图生视频/2046492973260611586.json, 视频生成/图生视频/2046851592153993217.json, 视频生成/图生视频/2046910304046551041.json, 视频生成/图生视频/2047145459982012417.json, 视频生成/图生视频/2047160236468867073.json, 视频生成/图生视频/2047231351606222849.json, 视频生成/图生视频/2047249835761344514.json, 视频生成/图生视频/2047904280446771201.json, 视频生成/图生视频/2052439073482129409.json, 视频生成/图生视频/2052755424847384578.json, 视频生成/图生视频/2052818320541396994.json, 视频生成/图生视频/2053175665918267393.json, 视频生成/图生视频/2053496869547982849.json, 视频生成/图生视频/2053511681703198721.json, 视频生成/图生视频/2054254654485221377.json, 视频生成/图生视频/2054257054595993602.json, 视频生成/图生视频/2057737815768784897.json, 视频生成/图生视频/2058284247890350082.json, 视频生成/图生视频/2058284795267997698.json, 视频生成/图生视频/2058286374553473025.json, 视频生成/图生视频/2058444480587583489.json, 视频生成/图生视频/2058481096018452482.json, 视频生成/图生视频/2058639989411500034.json, 视频生成/图生视频/2058649283943026689.json, 视频生成/图生视频/2058772271212359682.json, 视频生成/图生视频/2059550701113659394.json, 视频生成/图生视频/2064427874249166849.json, 视频生成/图生视频/2064996546147602434.json, 视频生成/图生视频/2047497091395624961.json, 视频生成/图生视频/2047889744532606978.json, 视频生成/图生视频/2042172500133548033.json, 视频生成/图生视频/2039232054755332098.json, 视频生成/图生视频/2042121574215589889.json, 视频生成/图生视频/2043974994291593217.json, 视频生成/图生视频/2020736841799962625.json, 视频生成/图生视频/2078749088413212673.json, 视频生成/图生视频/2079073056659689473.json, 视频生成/图生视频/2004423126941401089.json, 视频生成/图生视频/2047269838766215170.json, 视频生成/图生视频/2033430407915511809.json, 视频生成/图生视频/2013167617183326209.json, 视频生成/图生视频/2064360573986492418.json, 视频生成/图生视频/2039288865713823746.json, 视频生成/图生视频/2077308268699021313.json, 视频生成/图生视频/2057722585600843777.json, 视频生成/图生视频/2021769557274271746.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_11

> 由 `engine/knowledge_consolidation` 从 49 个 workflow 归纳得出（视频生成/图生视频/2072526167571263489.json、视频生成/图生视频/2080951206196899842.json、视频生成/图生视频/2081641783875952641.json、视频生成/图生视频/2046492973260611586.json、视频生成/图生视频/2046851592153993217.json…）

- **类型**：Unknown Workflow
- **样本数**：49
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 49 个 workflow 都包含：
- `CLIPVisionLoader`
- `GetImageRangeFromBatch`
- `GetImageSizeAndCount`
- `GetNode`
- `LoadImage`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoAddSteadyDancerEmbeds`
- `WanVideoClipVisionEncode`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSamplerFromSettings`
- `WanVideoSamplerSettings`
- `WanVideoScheduler`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 48/49 个有
- `ImageConcatMulti` —— 47/49 个有
- `ImageResizeKJv2` —— 47/49 个有
- `OnnxDetectionModelLoader` —— 47/49 个有
- `PoseDetectionOneToAllAnimation` —— 47/49 个有
- `WanVideoBlockSwap` —— 43/49 个有
- `WanVideoSetBlockSwap` —— 42/49 个有
- `CR Prompt Text` —— 36/49 个有
- `Int` —— 9/49 个有
- `TextInput_` —— 7/49 个有
- `easy showAnything` —— 3/49 个有
- `DF_Int_to_Float` —— 2/49 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/49 个有
- `PrimitiveStringMultiline` —— 2/49 个有
- `SDPoseOODLoader` —— 2/49 个有
- `SDPoseOODProcessor` —— 2/49 个有
- `WanVideoTorchCompileSettings` —— 2/49 个有
- `YOLOModelLoader` —— 2/49 个有
- `easy cleanGpuUsed` —— 2/49 个有
- `easy indexAnything` —— 2/49 个有
- `easy mathInt` —— 2/49 个有
- `ShowAnything|Mie` —— 1/49 个有
- `VHS_VideoInfoLoaded` —— 1/49 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
