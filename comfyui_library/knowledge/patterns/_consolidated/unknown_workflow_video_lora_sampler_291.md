---
name: unknown_workflow_video_lora_sampler_291
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.74725
common_nodes: [GetNode, LoadWanVideoT5TextEncoder, SetNode, String Literal, VHS_VideoCombine, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetRadialAttention, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy globalSeed, easy seed]
problems: []
missing: [String Literal, easy globalSeed, easy seed]
members: [视频生成/文生视频/1959889034724192257.json, 视频生成/文生视频/1963202515145822209.json, 视频生成/文生视频/1965038292615970818.json, 视频生成/文生视频/1965041345570197506.json, 视频生成/文生视频/MiniCPM反推+Wan2.2文生视频_2072999609892642816.json, 视频生成/文生视频/Wan2.2图生视频性价比极致加速V2_2072999587365036032.json, 视频生成/文生视频/Wan2.2文生视频性价比极致加速V2_2072999587830603776.json, 视频生成/文生视频/Wan2.2文生视频性价比极致加速_2072999631145181184.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_291

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/文生视频/1959889034724192257.json、视频生成/文生视频/1963202515145822209.json、视频生成/文生视频/1965038292615970818.json、视频生成/文生视频/1965041345570197506.json、视频生成/文生视频/MiniCPM反推+Wan2.2文生视频_2072999609892642816.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：75%

## 共有节点

全部 8 个 workflow 都包含：
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `String Literal`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetRadialAttention`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `easy globalSeed`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `WanVideoEmptyEmbeds` —— 6/8 个有
- `FloatToSigmas` —— 4/8 个有
- `StringToFloatList` —— 4/8 个有
- `WanVideoScheduler` —— 4/8 个有
- `WanVideoSigmaToStep` —— 4/8 个有
- `AILab_MiniCPM_4_V` —— 2/8 个有
- `ImageResizeKJv2` —— 2/8 个有
- `LoadImage` —— 2/8 个有
- `LoadVideo` —— 2/8 个有
- `ShowText` —— 2/8 个有
- `WanVideoImageToVideoEncode` —— 2/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：String Literal、easy globalSeed、easy seed
