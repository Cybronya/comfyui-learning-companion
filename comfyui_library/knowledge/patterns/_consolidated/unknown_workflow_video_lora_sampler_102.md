---
name: unknown_workflow_video_lora_sampler_102
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.964667
common_nodes: [CreateCFGScheduleFloatList, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1951564039392579586.json, 视频生成/图生视频/1952197474423353346.json, 视频生成/图生视频/1952270588733804545.json, 视频生成/图生视频/2040755258175004674.json, 视频生成/图生视频/2044660138820247554.json, 视频生成/图生视频/1950913701371117569.json, 视频生成/图生视频/1904943116204576769.json, 视频生成/图生视频/2042949137406103554.json, 视频生成/图生视频/2043184542202208257.json, 视频生成/图生视频/2044662528826941441.json, 视频生成/图生视频/2075046170388422658.json, 视频生成/图生视频/2047121992129712129.json, 视频生成/图生视频/2048604067320045570.json, 视频生成/图生视频/2048924949674463234.json, 视频生成/图生视频/2072871692606726146.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_102

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（视频生成/图生视频/1951564039392579586.json、视频生成/图生视频/1952197474423353346.json、视频生成/图生视频/1952270588733804545.json、视频生成/图生视频/2040755258175004674.json、视频生成/图生视频/2044660138820247554.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 15 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 14/15 个有
- `ImageResizeKJv2` —— 13/15 个有
- `easy cleanGpuUsed` —— 12/15 个有
- `MathExpression|pysssss` —— 11/15 个有
- `easy clearCacheAll` —— 11/15 个有
- `CR Text` —— 10/15 个有
- `Int` —— 10/15 个有
- `LayerUtility: PurgeVRAM` —— 9/15 个有
- `PrimitiveFloat` —— 9/15 个有
- `GetImageSizeAndCount` —— 5/15 个有
- `ImageResize+` —— 1/15 个有
- `ImpactSwitch` —— 1/15 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/15 个有
- `LayerUtility: PurgeVRAM V2` —— 1/15 个有
- `RH_LLMAPI_NODE` —— 1/15 个有
- `SeargePromptText` —— 1/15 个有
- `ShowText` —— 1/15 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
