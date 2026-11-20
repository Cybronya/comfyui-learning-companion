---
name: unknown_workflow_video_lora_sampler_524
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.9445
common_nodes: [INTConstant, ImageResizeKJv2, LoadImage, LoadWanVideoT5TextEncoder, PrimitiveInt, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2Fun-VACE+Controlnet+首尾帧_1967843382921953282.json, 视频生成/图生视频/Wan 2.2 Fun Vace魔改优化版首尾帧V1_1966523015905357825.json, 视频生成/图生视频/wan2.2FunVACE_高动态首尾帧_MPS+HPS_1975370725919952897.json, 视频生成/图生视频/首尾帧动态可控wan2.2超高动态模型+SIMGA精准调度+LLM扩写提示词_1972900147308990465.json, 视频生成/图生视频/首尾帧高动态wan2.2FunVACE+MPS+HPS +SIMGA精准调度_1968343084901781506.json, 视频生成/文生视频/【首尾帧动态可控】wan2.2 顺滑动态特效视频 自动扩写提示词_1977975025720512514.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_524

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（视频生成/图生视频/WAN2.2Fun-VACE+Controlnet+首尾帧_1967843382921953282.json、视频生成/图生视频/Wan 2.2 Fun Vace魔改优化版首尾帧V1_1966523015905357825.json、视频生成/图生视频/wan2.2FunVACE_高动态首尾帧_MPS+HPS_1975370725919952897.json、视频生成/图生视频/首尾帧动态可控wan2.2超高动态模型+SIMGA精准调度+LLM扩写提示词_1972900147308990465.json、视频生成/图生视频/首尾帧高动态wan2.2FunVACE+MPS+HPS +SIMGA精准调度_1968343084901781506.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `INTConstant`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `PrimitiveInt`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 5/6 个有
- `Float` —— 5/6 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 5/6 个有
- `WanVideoScheduler` —— 5/6 个有
- `WanVideoSigmaToStep` —— 5/6 个有
- `Int` —— 4/6 个有
- `LayerUtility: PurgeVRAM V2` —— 4/6 个有
- `PrimitiveFloat` —— 4/6 个有
- `RHHiddenNodes` —— 4/6 个有
- `SimpleMath+` —— 4/6 个有
- `WanVideoEnhanceAVideo` —— 4/6 个有
- `WanVideoExperimentalArgs` —— 4/6 个有
- `WanVideoLoraSelectMulti` —— 4/6 个有
- `WanVideoSLG` —— 4/6 个有
- `CreateCFGScheduleFloatList` —— 3/6 个有
- `StringToFloatList` —— 3/6 个有
- `ImageConcatMulti` —— 2/6 个有
- `PrimitiveString` —— 2/6 个有
- `WanVideoEasyCache` —— 2/6 个有
- `WanVideoLoraSelect` —— 2/6 个有
- `WanVideoTorchCompileSettings` —— 2/6 个有
- `easy anythingIndexSwitch` —— 2/6 个有
- `ColorMatch` —— 1/6 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
