---
name: unknown_workflow_video_sampler_vae_136
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.6455
common_nodes: [GetImageSizeAndCount, GetNode, INTConstant, ImageFromBatch, ImageFromBatch+, ImpactFloat, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, PrimitiveFloat, Qwen3_VQA, SetNode, ShowText|pysssss, StringFunction|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoVAELoader, easy anythingIndexSwitch, easy imageSize, easy int, easy positive, easy seed, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/1982743157039349761.json, 视频生成/图生视频/1972739991178792962.json, 视频生成/图生视频/1985620607834501122.json, 视频生成/图生视频/1985638903862439938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_136

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1982743157039349761.json、视频生成/图生视频/1972739991178792962.json、视频生成/图生视频/1985620607834501122.json、视频生成/图生视频/1985638903862439938.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 4 个 workflow 都包含：
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageFromBatch`
- `ImageFromBatch+`
- `ImpactFloat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `PrimitiveFloat`
- `Qwen3_VQA`
- `SetNode`
- `ShowText|pysssss`
- `StringFunction|pysssss`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `easy anythingIndexSwitch`
- `easy imageSize`
- `easy int`
- `easy positive`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 3/4 个有
- `WanVideoLoraSelect` —— 3/4 个有
- `CLIPVisionLoader` —— 2/4 个有
- `CM_FloatToInt` —— 2/4 个有
- `CreateCFGScheduleFloatList` —— 2/4 个有
- `GetImageRangeFromBatch` —— 2/4 个有
- `ImageBatchMulti` —— 2/4 个有
- `LoadWanVideoT5TextEncoder` —— 2/4 个有
- `MathExpression|pysssss` —— 2/4 个有
- `SimpleMath+` —— 2/4 个有
- `VHS_LoadVideo` —— 2/4 个有
- `WanVideoClipVisionEncode` —— 2/4 个有
- `WanVideoScheduler` —— 2/4 个有
- `WanVideoSigmaToStep` —— 2/4 个有
- `WanVideoTextEncode` —— 2/4 个有
- `WanVideoTextEncodeCached` —— 2/4 个有
- `easy mathFloat` —— 2/4 个有
- `easy mathInt` —— 2/4 个有
- `LoadLynxResampler` —— 1/4 个有
- `LynxEncodeFaceIP` —— 1/4 个有
- `LynxInsightFaceCrop` —— 1/4 个有
- `WanVideoAddLynxEmbeds` —— 1/4 个有
- `WanVideoExtraModelSelect` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
