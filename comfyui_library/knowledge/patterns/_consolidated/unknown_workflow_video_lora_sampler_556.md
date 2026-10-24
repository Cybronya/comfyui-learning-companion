---
name: unknown_workflow_video_lora_sampler_556
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.95925
common_nodes: [CreateCFGScheduleFloatList, INTConstant, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/wan2.2 文生视频_1956285811346079746.json, 视频生成/文生视频/wan2.2文生视频(KJ版)_1951284821798670338.json, 视频生成/文生视频/wan2.2文生视频_1950130157530038274.json, 视频生成/文生视频/【Supermate】重温Wan2.2 文生视频_2048801817592602625.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_556

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/文生视频/wan2.2 文生视频_1956285811346079746.json、视频生成/文生视频/wan2.2文生视频(KJ版)_1951284821798670338.json、视频生成/文生视频/wan2.2文生视频_1950130157530038274.json、视频生成/文生视频/【Supermate】重温Wan2.2 文生视频_2048801817592602625.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 3/4 个有
- `GetImageSizeAndCount` —— 2/4 个有
- `SimpleMath+` —— 2/4 个有
- `Text Multiline` —— 2/4 个有
- `easy int` —— 2/4 个有
- `DF_Integer` —— 1/4 个有
- `EmptyHunyuanLatentVideo` —— 1/4 个有
- `ImageFromBatch+` —— 1/4 个有
- `JWInteger` —— 1/4 个有
- `LayerColor: Brightness & Contrast` —— 1/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有
- `MathExpression|pysssss` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `RIFE VFI` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
