---
name: unknown_workflow_video_lora_sampler_702
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.961667
common_nodes: [CR Text, CreateCFGScheduleFloatList, GetImageSizeAndCount, INTConstant, JWInteger, LayerUtility: PurgeVRAM, LoadWanVideoT5TextEncoder, QwenLoader, ShowText|pysssss, SimpleMath+, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoPromptExtender, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Wan2.2文生视频_1994337581800292354.json, 视频生成/文生视频/1951121604451442689.json, 视频生成/文生视频/1955825453995999233.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_702

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/Wan2.2文生视频_1994337581800292354.json、视频生成/文生视频/1951121604451442689.json、视频生成/文生视频/1955825453995999233.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 3 个 workflow 都包含：
- `CR Text`
- `CreateCFGScheduleFloatList`
- `GetImageSizeAndCount`
- `INTConstant`
- `JWInteger`
- `LayerUtility: PurgeVRAM`
- `LoadWanVideoT5TextEncoder`
- `QwenLoader`
- `ShowText|pysssss`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoPromptExtender`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Float` —— 2/3 个有
- `WanVideoScheduler` —— 2/3 个有
- `WanVideoSigmaToStep` —— 2/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
