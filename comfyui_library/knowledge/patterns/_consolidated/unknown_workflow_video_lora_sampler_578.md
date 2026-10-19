---
name: unknown_workflow_video_lora_sampler_578
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.407333
common_nodes: [AILab_QwenVL, Any Switch (rgthree), Anything Everywhere, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CM_FloatToInt, CM_IntToFloat, CR Prompt Text, Fast Groups Bypasser (rgthree), GetNode, INTConstant, ImageConcatFromBatch, ImageResizeKJv2, ImpactFloat, ImpactSwitch, Int, KSamplerAdvanced, LayerUtility: TextJoin, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PreviewImage, RH_LLMAPI_NODE, RIFE VFI, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, Wan22PromptSelector, easy cleanGpuUsed, easy mathInt, easy promptConcat, easy seed, easy showAnything, wanBlock_Swap, 孤海图像组合批次]
problems: []
missing: [LayerUtility: TextJoin, RIFE VFI, easy cleanGpuUsed, easy mathInt, 孤海图像组合批次, CR Prompt Text, easy promptConcat, easy seed]
members: [视频生成/图生视频/1949884683304747009.json, 视频生成/图生视频/1952027530180153346.json, 视频生成/文生视频/1949884683304747009.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_578

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/1949884683304747009.json、视频生成/图生视频/1952027530180153346.json、视频生成/文生视频/1949884683304747009.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：41%

## 共有节点

全部 3 个 workflow 都包含：
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
- `WanFirstMiddleLastFrameToVideo` —— 2/3 个有
- `ImageConcatMulti` —— 1/3 个有
- `WanMultiFrameRefToVideo` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | normal | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 normal，3 个样本，一致性 100%
- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: TextJoin、RIFE VFI、easy cleanGpuUsed、easy mathInt、孤海图像组合批次
