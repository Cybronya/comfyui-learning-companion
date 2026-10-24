---
name: unknown_workflow_video_lora_sampler_434
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.83
common_nodes: [GetNode, LoadWanVideoT5TextEncoder, SetNode, String Literal, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetRadialAttention, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoVAELoader, easy globalSeed, easy seed]
problems: []
missing: []
members: [视频生成/图生视频/qwen3-vl视频反推--首款洗视频_1981360668177768450.json, 视频生成/文生视频/Wan2.2文生视频性价比极致加速V2_1965038292615970818.json, 视频生成/文生视频/Wan2.2文生视频性价比极致加速V3_1973095113876484098.json, 视频生成/文生视频/Wan2.2文生视频性价比极致加速V5_1978410048823169026.json, 视频生成/文生视频/qwen3-vl反推+Wan2.2文生视频性价比极致加速V5_1981321615827001346.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_434

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/qwen3-vl视频反推--首款洗视频_1981360668177768450.json、视频生成/文生视频/Wan2.2文生视频性价比极致加速V2_1965038292615970818.json、视频生成/文生视频/Wan2.2文生视频性价比极致加速V3_1973095113876484098.json、视频生成/文生视频/Wan2.2文生视频性价比极致加速V5_1978410048823169026.json、视频生成/文生视频/qwen3-vl反推+Wan2.2文生视频性价比极致加速V5_1981321615827001346.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 5 个 workflow 都包含：
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
- `WanVideoVAELoader`
- `easy globalSeed`
- `easy seed`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 4/5 个有
- `WanVideoTorchCompileSettings` —— 4/5 个有
- `WanVideoVACEEncode` —— 4/5 个有
- `WanVideoVACEModelSelect` —— 4/5 个有
- `easy float` —— 4/5 个有
- `easy int` —— 4/5 个有
- `AILab_QwenVL` —— 2/5 个有
- `LayerUtility: PurgeVRAM V2` —— 2/5 个有
- `VHS_LoadVideo` —— 2/5 个有
- `easy showAnything` —— 2/5 个有
- `WanVideoContextOptions` —— 1/5 个有
- `WanVideoLoraSelectMulti` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
