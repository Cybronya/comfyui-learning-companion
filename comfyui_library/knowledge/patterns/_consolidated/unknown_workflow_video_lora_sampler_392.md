---
name: unknown_workflow_video_lora_sampler_392
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.747167
common_nodes: [CreateCFGScheduleFloatList, INTConstant, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: [CR Prompt Text]
members: [视频生成/文生视频/04-01-02-WAN2.2-文生视频-kijai_1990967408930267138.json, 视频生成/文生视频/1977042886363631618.json, 视频生成/文生视频/1950485785722146818.json, 视频生成/文生视频/1952405030194360321.json, 视频生成/文生视频/1950130157530038274.json, 视频生成/文生视频/1950738636969021442.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_392

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/04-01-02-WAN2.2-文生视频-kijai_1990967408930267138.json、视频生成/文生视频/1977042886363631618.json、视频生成/文生视频/1950485785722146818.json、视频生成/文生视频/1952405030194360321.json、视频生成/文生视频/1950130157530038274.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 6 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 5/6 个有
- `GetImageSizeAndCount` —— 4/6 个有
- `WanVideoTorchCompileSettings` —— 4/6 个有
- `CR Prompt Text` —— 3/6 个有
- `GetNode` —— 3/6 个有
- `JWInteger` —— 3/6 个有
- `SetNode` —— 3/6 个有
- `Bjornulf_ShowInt` —— 1/6 个有
- `EmptyHunyuanLatentVideo` —— 1/6 个有
- `JjkText` —— 1/6 个有
- `LayerUtility: PurgeVRAM` —— 1/6 个有
- `RH_LLMAPI_NODE` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `WanVideoEasyCache` —— 1/6 个有
- `WanVideoLoraSelectMulti` —— 1/6 个有
- `easy seed` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text
