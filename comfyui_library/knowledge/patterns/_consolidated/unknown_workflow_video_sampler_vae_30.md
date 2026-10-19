---
name: unknown_workflow_video_sampler_vae_30
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.867455
common_nodes: [LoadWanVideoT5TextEncoder, Primitive integer [Crystools], ShowText, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: [Primitive integer [Crystools], Text Multiline, easy cleanGpuUsed, Text Concatenate]
members: [图片生成/文生图/1923249753776451586.json, 图片生成/文生图/1932599018294013953.json, 图片生成/文生图/1934653525920292866.json, 视频生成/文生视频/1933556886325346305.json, 视频生成/文生视频/1945801674319601665.json, 视频生成/文生视频/1923635839874551809.json, 视频生成/文生视频/1923291518734356481.json, 视频生成/文生视频/1927750568260059137.json, 视频生成/文生视频/极速万相文生视频-Self-Forcing+LLM_2071395063619477505.json, 视频生成/文生视频/极速万相文生视频_2029388586482667522.json, 视频生成/文生视频/1932781703125422081.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_30

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/1923249753776451586.json、图片生成/文生图/1932599018294013953.json、图片生成/文生图/1934653525920292866.json、视频生成/文生视频/1933556886325346305.json、视频生成/文生视频/1945801674319601665.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 11 个 workflow 都包含：
- `LoadWanVideoT5TextEncoder`
- `Primitive integer [Crystools]`
- `ShowText`
- `Text Multiline`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 10/11 个有
- `WanVideoEnhanceAVideo` —— 9/11 个有
- `RHHiddenNodes` —— 8/11 个有
- `Text Concatenate` —— 7/11 个有
- `Fast Groups Bypasser (rgthree)` —— 5/11 个有
- `WanVideoTeaCache` —— 5/11 个有
- `ShowText|pysssss` —— 4/11 个有
- `easy cleanGpuUsed` —— 4/11 个有
- `RH_LLMAPI_NODE` —— 3/11 个有
- `CM_IntToFloat` —— 2/11 个有
- `ColorMatch` —— 2/11 个有
- `JWStringReplace` —— 2/11 个有
- `WanVideoVACEModelSelect` —— 2/11 个有
- `WanVideoExperimentalArgs` —— 1/11 个有
- `WanVideoFreeInitArgs` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Primitive integer [Crystools]、Text Multiline、easy cleanGpuUsed、Text Concatenate
