---
name: unknown_workflow_video_lora_sampler_951
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.901
common_nodes: [CreateCFGScheduleFloatList, INTConstant, LoadWanVideoT5TextEncoder, ShowText|pysssss, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/文生视频/Smooth_Mix文生图工作流KJ版_1979830318448414721.json, 视频生成/文生视频/1950237819014963201.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_951

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Smooth_Mix文生图工作流KJ版_1979830318448414721.json、视频生成/文生视频/1950237819014963201.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `LoadWanVideoT5TextEncoder`
- `ShowText|pysssss`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `GLM_Text_Chat` —— 1/2 个有
- `GetImageSizeAndCount` —— 1/2 个有
- `Int` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有
- `PrimitiveInt` —— 1/2 个有
- `RH_Translator` —— 1/2 个有
- `WanVideoEasyCache` —— 1/2 个有
- `WanVideoExperimentalArgs` —— 1/2 个有
- `WanVideoSLG` —— 1/2 个有
- `Wan_video_prompt_generator` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
