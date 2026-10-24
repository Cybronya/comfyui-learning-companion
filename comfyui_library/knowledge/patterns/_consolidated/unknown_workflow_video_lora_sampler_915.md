---
name: unknown_workflow_video_lora_sampler_915
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.664
common_nodes: [CreateCFGScheduleFloatList, Fast Groups Bypasser (rgthree), FloatConstant, GetImageSizeAndCount, GetNode, INTConstant, JjkText, LayerUtility: PurgeVRAM, LoadWanVideoT5TextEncoder, Seed Generator, SetNode, VHS_LoadVideo, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/04-01-03-WAN2.2-文生视频-精准调度-kijai-1_1990967460138524673.json, 视频生成/文生视频/04-01-05-WAN2.2-文生视频-视频反推-精准调度-kijai_1991078170763853825.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_915

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/04-01-03-WAN2.2-文生视频-精准调度-kijai-1_1990967460138524673.json、视频生成/文生视频/04-01-05-WAN2.2-文生视频-视频反推-精准调度-kijai_1991078170763853825.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `Fast Groups Bypasser (rgthree)`
- `FloatConstant`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `JjkText`
- `LayerUtility: PurgeVRAM`
- `LoadWanVideoT5TextEncoder`
- `Seed Generator`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoScheduler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSigmaToStep`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `AILab_MiniCPM_4_V` —— 1/2 个有
- `Anything Everywhere3` —— 1/2 个有
- `CR Prompt Text` —— 1/2 个有
- `Fast Bypasser (rgthree)` —— 1/2 个有
- `FlashVSR_SM_KSampler` —— 1/2 个有
- `FlashVSR_SM_Model` —— 1/2 个有
- `ImageFromBatch+` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoadVideo` —— 1/2 个有
- `Qwen3VLProcessor` —— 1/2 个有
- `RunningHub Deepcleaner` —— 1/2 个有
- `Switch` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有
- `VRAMReserver` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4.55333e+08 | - | 1 | 100% |
| Prompt 约束强度(CFG) | randomize | - | 1 | 100% |
| 采样算法 | 2 | - | 1 | 100% |
| 调度器 | 3.5 | - | 1 | 100% |
| 重绘幅度 | 11 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 风险：采样步数 观测到 4.55333e+08，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
