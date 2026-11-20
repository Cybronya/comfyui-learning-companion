---
name: unknown_workflow_video_lora_sampler_771
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.781
common_nodes: [GetNode, LoadWanVideoT5TextEncoder, SetNode, String Literal, VHS_VideoCombine, WanVideoBlockSwap, WanVideoContextOptions, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetRadialAttention, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy globalSeed, easy seed]
problems: []
missing: []
members: [视频生成/文生视频/MiniCPM反推+Wan2.2文生视频_1963202515145822209.json, 视频生成/文生视频/Wan2.2文生视频性价比极致加速V2_1965038292615970818.json, 视频生成/文生视频/Wan2.2文生视频性价比极致加速_1959889034724192257.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_771

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/文生视频/MiniCPM反推+Wan2.2文生视频_1963202515145822209.json、视频生成/文生视频/Wan2.2文生视频性价比极致加速V2_1965038292615970818.json、视频生成/文生视频/Wan2.2文生视频性价比极致加速_1959889034724192257.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `String Literal`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoContextOptions`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
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
- `FloatToSigmas` —— 2/3 个有
- `StringToFloatList` —— 2/3 个有
- `AILab_MiniCPM_4_V` —— 1/3 个有
- `LoadVideo` —— 1/3 个有
- `ShowText` —— 1/3 个有
- `WanVideoScheduler` —— 1/3 个有
- `WanVideoSigmaToStep` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
