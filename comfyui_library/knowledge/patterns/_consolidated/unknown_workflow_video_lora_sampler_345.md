---
name: unknown_workflow_video_lora_sampler_345
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.432
common_nodes: [Any Switch (rgthree), Fast Groups Muter (rgthree), GetNode, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), PrimitiveString, PrimitiveStringMultiline, SetNode, StringConcatenate, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoEnhanceAVideo, WanVideoExperimentalArgs, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSampler, WanVideoTeaCache, WanVideoTorchCompileSettings, WanVideoVAELoader, easy int, easy seed]
problems: []
missing: [Bookmark (rgthree), Label (rgthree), Mute / Bypass Relay (rgthree), Mute / Bypass Repeater (rgthree), Note Plus (mtb), easy int, easy seed]
members: [视频生成/图生视频/1936095695604715522.json, 视频生成/图生视频/1936129945431101441.json, 视频生成/文生视频/1936095695604715522.json, 视频生成/文生视频/1936129945431101441.json, 视频生成/文生视频/1943222604020793345.json, 视频生成/文生视频/1936768190418685954.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_345

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1936095695604715522.json、视频生成/图生视频/1936129945431101441.json、视频生成/文生视频/1936095695604715522.json、视频生成/文生视频/1936129945431101441.json、视频生成/文生视频/1943222604020793345.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：43%

## 共有节点

全部 6 个 workflow 都包含：
- `Any Switch (rgthree)`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `Mute / Bypass Relay (rgthree)`
- `Mute / Bypass Repeater (rgthree)`
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `SetNode`
- `StringConcatenate`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoEnhanceAVideo`
- `WanVideoExperimentalArgs`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `Bookmark (rgthree)` —— 5/6 个有
- `Label (rgthree)` —— 5/6 个有
- `WanVideoTextEncode` —— 5/6 个有
- `WanVideoVRAMManagement` —— 5/6 个有
- `Note Plus (mtb)` —— 4/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/6 个有
- `WanVideoApplyNAG` —— 1/6 个有
- `WanVideoTextEncodeSingle` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：Bookmark (rgthree)、Label (rgthree)、Mute / Bypass Relay (rgthree)、Mute / Bypass Repeater (rgthree)、Note Plus (mtb)
