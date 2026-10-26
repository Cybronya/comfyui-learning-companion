---
name: unknown_workflow_video_lora_sampler_169
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.95925
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2 lora_1996855253331058690.json, 视频生成/图生视频/wan2.2图生视频(KJ版)_1951528284905525250.json, 视频生成/图生视频/wan2.2图生视频-标准版-(必收藏)_2059069738726285313.json, 视频生成/图生视频/wan2.2首尾帧kj图生视频+加速版=艾橘溪_1904943116204576769.json, 视频生成/图生视频/wan2.2首尾帧kj图生视频+加速版_2042949137406103554.json, 视频生成/图生视频/wan2.2首尾帧kj图生视频+加速版_2043184542202208257.json, 视频生成/图生视频/wan2.2首尾帧kj图生视频+加速版_2044662528826941441.json, 视频生成/图生视频/wan2.2首尾帧kj图生视频+加速版_2075046170388422658.json, 视频生成/图生视频/图生视频加速版-wan2.2首尾帧_2047121992129712129.json, 视频生成/图生视频/图生视频加速版-wan2.2首尾帧_2048604067320045570.json, 视频生成/图生视频/图生视频加速版-wan2.2首尾帧_2048924949674463234.json, 视频生成/图生视频/图生视频加速版-wan2.2首尾帧_2072871692606726146.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_169

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/wan2.2 lora_1996855253331058690.json、视频生成/图生视频/wan2.2图生视频(KJ版)_1951528284905525250.json、视频生成/图生视频/wan2.2图生视频-标准版-(必收藏)_2059069738726285313.json、视频生成/图生视频/wan2.2首尾帧kj图生视频+加速版=艾橘溪_1904943116204576769.json、视频生成/图生视频/wan2.2首尾帧kj图生视频+加速版_2042949137406103554.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 12 个 workflow 都包含：
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
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateCFGScheduleFloatList` —— 11/12 个有
- `INTConstant` —— 11/12 个有
- `MathExpression|pysssss` —— 11/12 个有
- `ImageResizeKJv2` —— 10/12 个有
- `PrimitiveFloat` —— 10/12 个有
- `WanVideoTorchCompileSettings` —— 10/12 个有
- `easy cleanGpuUsed` —— 10/12 个有
- `CR Text` —— 9/12 个有
- `Int` —— 9/12 个有
- `LayerUtility: PurgeVRAM` —— 9/12 个有
- `easy clearCacheAll` —— 9/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/12 个有
- `LoadAudio` —— 1/12 个有
- `Primitive integer [Crystools]` —— 1/12 个有
- `RIFE VFI` —— 1/12 个有
- `easy seed` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
