---
name: unknown_workflow_video_lora_sampler_852
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6705
common_nodes: [Bjornulf_AnythingToText, Bjornulf_ShowInt, Bjornulf_ShowStringText, CLIPTextEncode, CR String To Boolean, CR String To Number, CR Text Input Switch (4 way), GetNode, ImpactSwitch, Int, JjkText, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, Note _O, SetNode, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, WanVideoVRAMManagement]
problems: []
missing: []
members: [视频生成/图生视频/1902736464273158146.json, 视频生成/图生视频/1902985509671440385.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_852

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1902736464273158146.json、视频生成/图生视频/1902985509671440385.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：67%

## 共有节点

全部 2 个 workflow 都包含：
- `Bjornulf_AnythingToText`
- `Bjornulf_ShowInt`
- `Bjornulf_ShowStringText`
- `CLIPTextEncode`
- `CR String To Boolean`
- `CR String To Number`
- `CR Text Input Switch (4 way)`
- `GetNode`
- `ImpactSwitch`
- `Int`
- `JjkText`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `Note _O`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `WanVideoVRAMManagement`

**可变部分**（部分 workflow 才有）：
- `RH_Captioner` —— 1/2 个有
- `easy textSwitch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
