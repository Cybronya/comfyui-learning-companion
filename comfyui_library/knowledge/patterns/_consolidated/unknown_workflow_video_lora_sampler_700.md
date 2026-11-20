---
name: unknown_workflow_video_lora_sampler_700
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.6305
common_nodes: [CM_IntToFloat, CR Prompt Text, GetImageSizeAndCount, GetNode, INTConstant, ImageConcanate, ImageFromBatch, ImageFromBatch+, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, SetNode, StringFunction|pysssss, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfoLoaded, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy int, easy positive, easy seed, easy showAnything]
problems: []
missing: []
members: [平台全量/视频-视频转真人-wan2.1-ditto-KJ_1980506852125491201.json, 平台全量/视频-视频转绘-wan2.1-ditto-KJ_1980500985380519937.json, 平台全量/视频-视频转绘-wan2.1-ditto-KJ_2087411184407506945.json, 视频生成/图生视频/视频-视频转绘-wan2.1ditto-KJ_30s_1988019422692577281.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_700

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/视频-视频转真人-wan2.1-ditto-KJ_1980506852125491201.json、平台全量/视频-视频转绘-wan2.1-ditto-KJ_1980500985380519937.json、平台全量/视频-视频转绘-wan2.1-ditto-KJ_2087411184407506945.json、视频生成/图生视频/视频-视频转绘-wan2.1ditto-KJ_30s_1988019422692577281.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：63%

## 共有节点

全部 4 个 workflow 都包含：
- `CM_IntToFloat`
- `CR Prompt Text`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `ImageConcanate`
- `ImageFromBatch`
- `ImageFromBatch+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `SetNode`
- `StringFunction|pysssss`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfoLoaded`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeCached`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy int`
- `easy positive`
- `easy seed`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `ShowText` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
