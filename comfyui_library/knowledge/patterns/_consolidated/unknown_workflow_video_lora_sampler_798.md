---
name: unknown_workflow_video_lora_sampler_798
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7725
common_nodes: [ApplyFaceProcessor, FaceProcessorLoader, ImpactSwitch, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, PreviewImage, RH_LLMAPI_NODE, Text Concatenate, VHS_VideoCombine, Wan22PromptSelector, WanVideoAddStandInLatent, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy imageScaleDownToSize]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.1+Stand-In身份一致性文生视频_1956534345093840897.json, 视频生成/文生视频/Wan2.1+Stand-In身份一致性文生视频_1956197962999320577.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_798

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan2.1+Stand-In身份一致性文生视频_1956534345093840897.json、视频生成/文生视频/Wan2.1+Stand-In身份一致性文生视频_1956197962999320577.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `ApplyFaceProcessor`
- `FaceProcessorLoader`
- `ImpactSwitch`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `Text Concatenate`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `WanVideoAddStandInLatent`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy imageScaleDownToSize`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `GetNode` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `ImageConcatMulti` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `PrimitiveStringMultiline` —— 1/2 个有
- `SetNode` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
