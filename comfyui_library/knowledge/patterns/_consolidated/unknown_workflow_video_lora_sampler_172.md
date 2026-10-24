---
name: unknown_workflow_video_lora_sampler_172
type: Unknown Workflow
frequency: 11
level: moderate
coverage: 0.515818
common_nodes: [GetNode, ImpactSwitch, LoadWanVideoT5TextEncoder, PrimitiveInt, SetNode, VHS_VideoCombine, WanVideoApplyNAG, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, WanVideoVAELoader, easy negative, easy positive]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2真实动态首尾帧新玩法_1969269601903276034.json, 视频生成/图生视频/图生视频-Wan2.2(KJ)_1953403318607511553.json, 视频生成/图生视频/图生视频-Wan2.2(极致效果)_1952225607566438401.json, 视频生成/图生视频/图生视频-Wan2.2(极致效果)_1967507218427994113.json, 视频生成/图生视频/首尾帧视频-Wan2.2(极致效果)_1953348116592427010.json, 视频生成/图生视频/首尾帧视频-Wan2.2(极致效果)_1955836777492725762.json, 视频生成/图生视频/首尾帧视频-Wan2.2(极致效果)_1967511175430803457.json, 视频生成/图生视频/首尾帧视频-Wan2.2(极致效果)_1976833467906506754.json, 视频生成/图生视频/首尾帧视频-Wan2.2｜高清一致性_1955508156764864513.json, 视频生成/文生视频/文生视频-Wan2.2(极致效果)_1952262575440474114.json, 视频生成/文生视频/文生视频-Wan2.2(极致效果)_1966334312981442561.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_172

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/wan2.2真实动态首尾帧新玩法_1969269601903276034.json、视频生成/图生视频/图生视频-Wan2.2(KJ)_1953403318607511553.json、视频生成/图生视频/图生视频-Wan2.2(极致效果)_1952225607566438401.json、视频生成/图生视频/图生视频-Wan2.2(极致效果)_1967507218427994113.json、视频生成/图生视频/首尾帧视频-Wan2.2(极致效果)_1953348116592427010.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：52%

## 共有节点

全部 11 个 workflow 都包含：
- `GetNode`
- `ImpactSwitch`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveInt`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoApplyNAG`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy negative`
- `easy positive`

**可变部分**（部分 workflow 才有）：
- `GetBoolFromJson` —— 10/11 个有
- `GetFloatFromJson` —— 10/11 个有
- `GetIntFromJson` —— 10/11 个有
- `LoadJsonFromText` —— 10/11 个有
- `easy ifElse` —— 10/11 个有
- `easy mathInt` —— 10/11 个有
- `Int` —— 9/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 9/11 个有
- `LoadImage` —— 9/11 个有
- `WanVideoImageToVideoEncode` —— 9/11 个有
- `LayerUtility: ImageMaskScaleAsV2` —— 6/11 个有
- `JWStringSplit` —— 2/11 个有
- `PrimitiveString` —— 2/11 个有
- `WanVideoEmptyEmbeds` —— 2/11 个有
- `easy convertAnything` —— 2/11 个有
- `LoadWanVideoClipTextEncoder` —— 1/11 个有
- `WanVideoClipVisionEncode` —— 1/11 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
