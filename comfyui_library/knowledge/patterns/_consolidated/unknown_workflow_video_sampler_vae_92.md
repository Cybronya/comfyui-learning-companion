---
name: unknown_workflow_video_sampler_vae_92
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.6398
common_nodes: [GetImageSizeAndCount, GetNode, ImageFromBatch, ImageFromBatch+, ImpactFloat, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, PrimitiveFloat, Qwen3_VQA, SetNode, ShowText|pysssss, StringFunction|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoVAELoader, easy anythingIndexSwitch, easy imageSize, easy int, easy positive, easy seed, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/视频-图生视频长视频-wan2.1-SVI 2.0-KJ_1985612085986045953.json, 视频生成/图生视频/视频-图生视频扩写-wan2.2-smoothMix-KJ_1982743157039349761.json, 视频生成/图生视频/视频-图生视频自动扩写-wan2.2-KJ_1972739991178792962.json, 视频生成/图生视频/视频-视频延长视频-wan2.1-SVI 2.0-KJ_1985620607834501122.json, 视频生成/图生视频/视频-视频延长视频＋参考图一致性-wan2.1-lynx-SVI 2.0-KJ_1985638903862439938.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_92

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/视频-图生视频长视频-wan2.1-SVI 2.0-KJ_1985612085986045953.json、视频生成/图生视频/视频-图生视频扩写-wan2.2-smoothMix-KJ_1982743157039349761.json、视频生成/图生视频/视频-图生视频自动扩写-wan2.2-KJ_1972739991178792962.json、视频生成/图生视频/视频-视频延长视频-wan2.1-SVI 2.0-KJ_1985620607834501122.json、视频生成/图生视频/视频-视频延长视频＋参考图一致性-wan2.1-lynx-SVI 2.0-KJ_1985638903862439938.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 5 个 workflow 都包含：
- `GetImageSizeAndCount`
- `GetNode`
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
- `INTConstant` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `WanVideoLoraSelect` —— 4/5 个有
- `CLIPVisionLoader` —— 3/5 个有
- `MathExpression|pysssss` —— 3/5 个有
- `WanVideoClipVisionEncode` —— 3/5 个有
- `WanVideoTextEncodeCached` —— 3/5 个有
- `CM_FloatToInt` —— 2/5 个有
- `CreateCFGScheduleFloatList` —— 2/5 个有
- `GetImageRangeFromBatch` —— 2/5 个有
- `ImageBatchMulti` —— 2/5 个有
- `LoadWanVideoT5TextEncoder` —— 2/5 个有
- `SimpleMath+` —— 2/5 个有
- `VHS_LoadVideo` —— 2/5 个有
- `WanVideoScheduler` —— 2/5 个有
- `WanVideoSigmaToStep` —— 2/5 个有
- `WanVideoTextEncode` —— 2/5 个有
- `easy mathFloat` —— 2/5 个有
- `easy mathInt` —— 2/5 个有
- `LoadLynxResampler` —— 1/5 个有
- `LynxEncodeFaceIP` —— 1/5 个有
- `LynxInsightFaceCrop` —— 1/5 个有
- `WanVideoAddLynxEmbeds` —— 1/5 个有
- `WanVideoExtraModelSelect` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
