---
name: unknown_workflow_video_lora_sampler_379
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.763
common_nodes: [GetNode, LoadWanVideoT5TextEncoder, SetNode, String Literal, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetRadialAttention, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, easy float, easy globalSeed, easy int, easy seed]
problems: []
missing: [String Literal, easy float, easy int, easy globalSeed, easy seed]
members: [视频生成/图生视频/1981360668177768450.json, 视频生成/文生视频/1973095113876484098.json, 视频生成/文生视频/1978410048823169026.json, 视频生成/文生视频/Wan2.2 V3 Fast Text-to-Video_2072999534793629696.json, 视频生成/文生视频/Wan2.2文生视频性价比极致加速V5_2072999498567426048.json, 视频生成/文生视频/qwen3-vl反推+Wan2.2文生视频性价比极致加速V5_1981321615827001346.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_379

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/1981360668177768450.json、视频生成/文生视频/1973095113876484098.json、视频生成/文生视频/1978410048823169026.json、视频生成/文生视频/Wan2.2 V3 Fast Text-to-Video_2072999534793629696.json、视频生成/文生视频/Wan2.2文生视频性价比极致加速V5_2072999498567426048.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 6 个 workflow 都包含：
- `GetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `String Literal`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetRadialAttention`
- `WanVideoSigmaToStep`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `easy float`
- `easy globalSeed`
- `easy int`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 5/6 个有
- `WanVideoLoraSelect` —— 4/6 个有
- `AILab_QwenVL` —— 2/6 个有
- `LayerUtility: PurgeVRAM V2` —— 2/6 个有
- `VHS_LoadVideo` —— 2/6 个有
- `WanVideoLoraSelectMulti` —— 2/6 个有
- `easy showAnything` —— 2/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：String Literal、easy float、easy int、easy globalSeed、easy seed
