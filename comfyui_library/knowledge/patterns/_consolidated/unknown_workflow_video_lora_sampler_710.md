---
name: unknown_workflow_video_lora_sampler_710
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.709667
common_nodes: [ImpactSwitch, LoadWanVideoT5TextEncoder, MathExpression|pysssss, PrimitiveInt, PrimitiveStringMultiline, RH_LLMAPI_NODE, ShowText|pysssss, Text Concatenate, VHS_VideoCombine, Wan22PromptSelector, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1+Stand-In身份一致性文生视频_1956534345093840897.json, 视频生成/文生视频/Wan2.2+14B 4步加速文生视频KJ-智能扩写版_1953992083726225410.json, 视频生成/文生视频/【KJ版】Wan2.2 14B加速文生视+提示词智能扩写_1951972629169295361.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_710

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Wan2.1+Stand-In身份一致性文生视频_1956534345093840897.json、视频生成/文生视频/Wan2.2+14B 4步加速文生视频KJ-智能扩写版_1953992083726225410.json、视频生成/文生视频/【KJ版】Wan2.2 14B加速文生视+提示词智能扩写_1951972629169295361.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `ImpactSwitch`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `PrimitiveInt`
- `PrimitiveStringMultiline`
- `RH_LLMAPI_NODE`
- `ShowText|pysssss`
- `Text Concatenate`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ApplyFaceProcessor` —— 1/3 个有
- `CreateCFGScheduleFloatList` —— 1/3 个有
- `DF_Int_to_Float` —— 1/3 个有
- `FaceProcessorLoader` —— 1/3 个有
- `FloatToSigmas` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `LoadImage` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `StringToFloatList` —— 1/3 个有
- `WanVideoAddStandInLatent` —— 1/3 个有
- `WanVideoEncode` —— 1/3 个有
- `easy imageScaleDownToSize` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
