---
name: unknown_workflow_video_lora_sampler_821
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.698
common_nodes: [CR Prompt Text, CR Text, Comfly_LLm_API, CreateCFGScheduleFloatList, Fast Bypasser (rgthree), FloatConstant, GetImageSizeAndCount, GetNode, INTConstant, JWStringConcat, LayerUtility: ImageScaleByAspectRatio V2, LoadWanVideoT5TextEncoder, RH_LLMAPI_NODE, RH_LLMAPI_Pro_Node, SetNode, ShowText|pysssss, Switch, TextConcat, VHS_VideoCombine, Wan22PromptSelector, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoSampler, WanVideoScheduler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSigmaToStep, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/04-02-01-Wan2.2-图生视频-精准调度-kijai_1990967918798249985.json, 视频生成/文生视频/04-01-04-WAN2.2-高阶文生视频-精细控制-kijai_1990967565352640513.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_821

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/04-02-01-Wan2.2-图生视频-精准调度-kijai_1990967918798249985.json、视频生成/文生视频/04-01-04-WAN2.2-高阶文生视频-精细控制-kijai_1990967565352640513.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `CR Text`
- `Comfly_LLm_API`
- `CreateCFGScheduleFloatList`
- `Fast Bypasser (rgthree)`
- `FloatConstant`
- `GetImageSizeAndCount`
- `GetNode`
- `INTConstant`
- `JWStringConcat`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadWanVideoT5TextEncoder`
- `RH_LLMAPI_NODE`
- `RH_LLMAPI_Pro_Node`
- `SetNode`
- `ShowText|pysssss`
- `Switch`
- `TextConcat`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `WanVideoBlockSwap`
- `WanVideoDecode`
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
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 1/2 个有
- `Anything Everywhere3` —— 1/2 个有
- `FlashVSR_SM_KSampler` —— 1/2 个有
- `FlashVSR_SM_Model` —— 1/2 个有
- `ImageFromBatch+` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `Seed Generator` —— 1/2 个有
- `VHS_LoadVideo` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有
- `WanVideoEmptyEmbeds` —— 1/2 个有
- `WanVideoImageToVideoEncode` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.39717e+08 | - | 1 | 100% |
| Prompt 约束强度(CFG) | fixed | - | 1 | 100% |
| 采样算法 | 2 | - | 1 | 100% |
| 调度器 | 3.5 | - | 1 | 100% |
| 重绘幅度 | 11 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 风险：采样步数 观测到 8.39717e+08，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
