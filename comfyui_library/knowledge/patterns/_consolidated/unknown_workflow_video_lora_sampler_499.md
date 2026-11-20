---
name: unknown_workflow_video_lora_sampler_499
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.685167
common_nodes: [Florence2ModelLoader, Florence2Run, GetImageSizeAndCount, GetNode, INTConstant, ImageConcanate, ImageConcatMulti, ImageFromBatch, ImageFromBatch+, ImageResizeKJ, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SetNode, ShowText|pysssss, StringFunction|pysssss, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, WanVideoVACEEncode, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy positive, easy seed, easy showAnything]
problems: []
missing: []
members: [平台全量/视频-动作迁移-wan2.2vace-KJ_1973089337220968449.json, 平台全量/视频-动作迁移Lynx一致性-wan2.1vace-KJ_1977379034298503169.json, 平台全量/视频-局部编辑替换-wan2.2-vace-KJ_1973617250534076417.json, 视频生成/图生视频/Wan2.2-vace-KJ视频-局部编辑替换_2018865681843888129.json, 视频生成/图生视频/Wan2.2-vace-KJ视频-局部编辑替换_2041438667583004673.json, 视频生成/图生视频/wan2.2视频局部替换_2016758036848709633.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_499

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（平台全量/视频-动作迁移-wan2.2vace-KJ_1973089337220968449.json、平台全量/视频-动作迁移Lynx一致性-wan2.1vace-KJ_1977379034298503169.json、平台全量/视频-局部编辑替换-wan2.2-vace-KJ_1973617250534076417.json、视频生成/图生视频/Wan2.2-vace-KJ视频-局部编辑替换_2018865681843888129.json、视频生成/图生视频/Wan2.2-vace-KJ视频-局部编辑替换_2041438667583004673.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：69%

## 共有节点

全部 6 个 workflow 都包含：
- `Florence2ModelLoader`
- `Florence2Run`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageConcanate`
- `ImageConcatMulti`
- `ImageFromBatch`
- `ImageFromBatch+`
- `ImageResizeKJ`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SetNode`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncodeCached`
- `WanVideoVACEEncode`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy positive`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CreateCFGScheduleFloatList` —— 5/6 个有
- `ImpactFloat` —— 5/6 个有
- `WanVideoScheduler` —— 5/6 个有
- `WanVideoSigmaToStep` —— 5/6 个有
- `ImageToMask` —— 4/6 个有
- `MaskToImage` —— 4/6 个有
- `easy imageRemBg` —— 4/6 个有
- `easy imageSize` —— 4/6 个有
- `AIO_Preprocessor` —— 2/6 个有
- `CM_IntToFloat` —— 2/6 个有
- `CR Upscale Image` —— 2/6 个有
- `easy anythingIndexSwitch` —— 2/6 个有
- `easy int` —— 2/6 个有
- `LoadLynxResampler` —— 1/6 个有
- `LynxEncodeFaceIP` —— 1/6 个有
- `LynxInsightFaceCrop` —— 1/6 个有
- `WanVideoAddLynxEmbeds` —— 1/6 个有
- `WanVideoExtraModelSelect` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
