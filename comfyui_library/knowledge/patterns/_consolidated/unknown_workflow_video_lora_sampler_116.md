---
name: unknown_workflow_video_lora_sampler_116
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.766786
common_nodes: [CR Prompt Text, CreateCFGScheduleFloatList, INTConstant, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: [CR Prompt Text, ImageFromBatch+]
members: [视频生成/文生视频/1950804830958845953.json, 视频生成/文生视频/1950936240545800193.json, 视频生成/文生视频/1950828100848386049.json, 视频生成/文生视频/1955828934376132610.json, 视频生成/文生视频/1954869013831565314.json, 视频生成/文生视频/1952587209671159809.json, 视频生成/文生视频/1952589120671559682.json, 视频生成/文生视频/1959964511526662146.json, 视频生成/文生视频/1972106036679208961.json, 视频生成/文生视频/1972112233536876545.json, 视频生成/文生视频/1972282645650534402.json, 视频生成/文生视频/1973017295171751938.json, 视频生成/文生视频/1959252235161120769.json, 视频生成/文生视频/1959251891186249729.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_116

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（视频生成/文生视频/1950804830958845953.json、视频生成/文生视频/1950936240545800193.json、视频生成/文生视频/1950828100848386049.json、视频生成/文生视频/1955828934376132610.json、视频生成/文生视频/1954869013831565314.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 14 个 workflow 都包含：
- `CR Prompt Text`
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
- `JWInteger` —— 13/14 个有
- `JWStringConcat` —— 13/14 个有
- `ShowText|pysssss` —— 13/14 个有
- `Wan22PromptSelector` —— 13/14 个有
- `WanVideoTorchCompileSettings` —— 13/14 个有
- `easy showAnything` —— 13/14 个有
- `GetImageSizeAndCount` —— 12/14 个有
- `RH_LLMAPI_NODE` —— 12/14 个有
- `TextConcat` —— 12/14 个有
- `ImageFromBatch+` —— 4/14 个有
- `LoadImage` —— 2/14 个有
- `LoadLatent` —— 2/14 个有
- `SaveImage` —— 2/14 个有
- `SaveLatent` —— 2/14 个有
- `GLM_Text_Chat` —— 1/14 个有
- `Int` —— 1/14 个有
- `LayerUtility: PurgeVRAM V2` —— 1/14 个有
- `MathExpression|pysssss` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Prompt Text、ImageFromBatch+
