---
name: unknown_workflow_video_lora_sampler_440
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.931667
common_nodes: [CreateCFGScheduleFloatList, INTConstant, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/wan2.2文生视频 (完整版)_1987398850963025922.json, 视频生成/文生视频/wan2.2文生视频(KJ版)_1951284821798670338.json, 视频生成/文生视频/wan2.2文生视频_1950130157530038274.json, 视频生成/文生视频/wan2.2文生视频（KJ流）加速_1950237819014963201.json, 视频生成/文生视频/wan2.2文生视频，加速版（自动润色提示词）_2006301824508239873.json, 视频生成/文生视频/【Supermate】重温Wan2.2 文生视频_2048801817592602625.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_440

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/文生视频/wan2.2文生视频 (完整版)_1987398850963025922.json、视频生成/文生视频/wan2.2文生视频(KJ版)_1951284821798670338.json、视频生成/文生视频/wan2.2文生视频_1950130157530038274.json、视频生成/文生视频/wan2.2文生视频（KJ流）加速_1950237819014963201.json、视频生成/文生视频/wan2.2文生视频，加速版（自动润色提示词）_2006301824508239873.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
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
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoSetBlockSwap` —— 5/6 个有
- `WanVideoSetLoRAs` —— 5/6 个有
- `WanVideoTorchCompileSettings` —— 5/6 个有
- `GetImageSizeAndCount` —— 4/6 个有
- `MathExpression|pysssss` —— 3/6 个有
- `RH_Translator` —— 3/6 个有
- `RIFE VFI` —— 3/6 个有
- `CR Text` —— 2/6 个有
- `DF_Integer` —— 2/6 个有
- `JWInteger` —— 2/6 个有
- `ShowText|pysssss` —— 2/6 个有
- `SimpleMath+` —— 2/6 个有
- `Text Multiline` —— 2/6 个有
- `easy int` —— 2/6 个有
- `CR Text Concatenate` —— 1/6 个有
- `EmptyHunyuanLatentVideo` —— 1/6 个有
- `Int` —— 1/6 个有
- `PrimitiveBoolean` —— 1/6 个有
- `RH_Prompter` —— 1/6 个有
- `easy ifElse` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
