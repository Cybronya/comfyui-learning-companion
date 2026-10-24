---
name: unknown_workflow_video_lora_sampler_791
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.43
common_nodes: [AILab_QwenVL, Any Switch (rgthree), Anything Everywhere, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_FloatToInt, CM_IntToFloat, CR Prompt Text, Fast Groups Bypasser (rgthree), GetNode, INTConstant, ImageConcatFromBatch, ImageResizeKJv2, ImpactFloat, ImpactSwitch, Int, KSamplerAdvanced, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RH_LLMAPI_NODE, RIFE VFI, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, Wan22PromptSelector, easy cleanGpuUsed, easy mathInt, easy promptConcat, easy seed, easy showAnything, wanBlock_Swap, 孤海图像组合批次]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2-native-LightX2V-I2V-多图首尾帧（5图）_1952027530180153346.json, 视频生成/文生视频/🈚️Wan2.2-native-Lightx-文生_图生视频_首中尾帧·多合一_1949884683304747009.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_791

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/WAN2.2-native-LightX2V-I2V-多图首尾帧（5图）_1952027530180153346.json、视频生成/文生视频/🈚️Wan2.2-native-Lightx-文生_图生视频_首中尾帧·多合一_1949884683304747009.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：43%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_QwenVL`
- `Any Switch (rgthree)`
- `Anything Everywhere`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CM_FloatToInt`
- `CM_IntToFloat`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `INTConstant`
- `ImageConcatFromBatch`
- `ImageResizeKJv2`
- `ImpactFloat`
- `ImpactSwitch`
- `Int`
- `KSamplerAdvanced`
- `LayerUtility: TextJoin`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RH_LLMAPI_NODE`
- `RIFE VFI`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `Wan22PromptSelector`
- `easy cleanGpuUsed`
- `easy mathInt`
- `easy promptConcat`
- `easy seed`
- `easy showAnything`
- `wanBlock_Swap`
- `孤海图像组合批次`

**可变部分**（部分 workflow 才有）：
- `ImageConcatMulti` —— 1/2 个有
- `WanFirstMiddleLastFrameToVideo` —— 1/2 个有
- `WanMultiFrameRefToVideo` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | normal | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 normal，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
