---
name: unknown_workflow_video_lora_sampler_629
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.888333
common_nodes: [CreateCFGScheduleFloatList, JjkText, LayerUtility: PurgeVRAM, LoadWanVideoT5TextEncoder, MathExpression|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy float, easy int, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/Wan 2.2 图生视频 高清+加速版+自动提示词_1953388513221902338.json, 视频生成/图生视频/【24帧强动态】万相_wan2.2图生视频KJ版_1952243502325420034.json, 视频生成/文生视频/万相_wan2.2文生视频KJ版 基础工作流 旧版lightx2v加速_1951199136504852481.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_629

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan 2.2 图生视频 高清+加速版+自动提示词_1953388513221902338.json、视频生成/图生视频/【24帧强动态】万相_wan2.2图生视频KJ版_1952243502325420034.json、视频生成/文生视频/万相_wan2.2文生视频KJ版 基础工作流 旧版lightx2v加速_1951199136504852481.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `JjkText`
- `LayerUtility: PurgeVRAM`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy float`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `ImpactFloat` —— 2/3 个有
- `ImpactSwitch` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `WanVideoImageToVideoEncode` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `WanVideoEmptyEmbeds` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
