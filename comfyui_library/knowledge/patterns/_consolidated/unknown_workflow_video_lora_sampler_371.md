---
name: unknown_workflow_video_lora_sampler_371
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.492
common_nodes: [Float, GetNode, If ANY execute A else B, ImageResizeKJv2, ImpactSwitch, JWStringSplit, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, PrimitiveBoolean, PrimitiveString, SetNode, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoClipVisionEncode, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVAELoader, easy convertAnything, easy imageRemBg]
problems: []
missing: []
members: [视频生成/图生视频/参考生成视频-三图_1950878198265487362.json, 视频生成/图生视频/参考生成视频-三图_1967512579738361857.json, 视频生成/图生视频/参考生成视频-单图_1950857772990660610.json, 视频生成/图生视频/参考生成视频-单图_1967526201378136065.json, 视频生成/图生视频/参考生成视频-双图_1950866948588503042.json, 视频生成/图生视频/参考生成视频-双图_1967525929503297538.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_371

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/参考生成视频-三图_1950878198265487362.json、视频生成/图生视频/参考生成视频-三图_1967512579738361857.json、视频生成/图生视频/参考生成视频-单图_1950857772990660610.json、视频生成/图生视频/参考生成视频-单图_1967526201378136065.json、视频生成/图生视频/参考生成视频-双图_1950866948588503042.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：49%

## 共有节点

全部 6 个 workflow 都包含：
- `Float`
- `GetNode`
- `If ANY execute A else B`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `JWStringSplit`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveBoolean`
- `PrimitiveString`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy convertAnything`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `ImageBatchMultiple+` —— 4/6 个有
- `ImageConcatFromBatch` —— 4/6 个有
- `MathExpression|pysssss` —— 4/6 个有
- `PreviewImage` —— 4/6 个有
- `PrimitiveInt` —— 4/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
