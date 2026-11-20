---
name: unknown_workflow_lora_sampler_clip_341
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.793
common_nodes: [Anything Everywhere3, BatchCount+, Bjornulf_AnythingToText, CLIPLoader, CLIPTextEncode, CLIPVisionLoader, CreateVideo, EmptySD3LatentImage, Float, FluxResolutionNode, GetNode, Int, InversionDemoLazySwitch, JjkText, KSampler, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, PathchSageAttentionKJ, PrimitiveBoolean, ProcessString, RH_LLMAPI_NODE, RH_Translator, SaveVideo, SetNode, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, WanMultiFrameRefToVideo, easy cleanGpuUsed, easy promptConcat, easy promptLine, easy showAnything, wanBlockSwap]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/文生视频/Qwen Next Scene【吉海铁路beta1.1专版多图参考文生分镜成片】_1999964546368405506.json, 视频生成/文生视频/Qwen Next Scene【吉海铁路beta专版多图参考文生分镜成片】_1998520625754963969.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_341

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/Qwen Next Scene【吉海铁路beta1.1专版多图参考文生分镜成片】_1999964546368405506.json、视频生成/文生视频/Qwen Next Scene【吉海铁路beta专版多图参考文生分镜成片】_1998520625754963969.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `Anything Everywhere3`
- `BatchCount+`
- `Bjornulf_AnythingToText`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CreateVideo`
- `EmptySD3LatentImage`
- `Float`
- `FluxResolutionNode`
- `GetNode`
- `Int`
- `InversionDemoLazySwitch`
- `JjkText`
- `KSampler`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `PrimitiveBoolean`
- `ProcessString`
- `RH_LLMAPI_NODE`
- `RH_Translator`
- `SaveVideo`
- `SetNode`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `WanMultiFrameRefToVideo`
- `easy cleanGpuUsed`
- `easy promptConcat`
- `easy promptLine`
- `easy showAnything`
- `wanBlockSwap`

**可变部分**（部分 workflow 才有）：
- `FlashVSRNode` —— 1/2 个有
- `FlashVSR_SM_KSampler` —— 1/2 个有
- `FlashVSR_SM_Model` —— 1/2 个有
- `GetImageSize` —— 1/2 个有
- `RebatchImages` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 5.00797e+08 | - | 2 | 0% |
| Prompt 约束强度(CFG) | 1 | - | 1 | 100% |
| 采样算法 | 2 | - | 1 | 100% |
| 调度器 | 3.5 | - | 1 | 100% |
| 重绘幅度 | 6 | - | 2 | 17% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 5.00797e+08，样本不足，未给区间，2 个样本，取值分散，一致性仅 0%
- 重绘幅度 中位数 6，样本不足，未给区间，2 个样本，取值分散，一致性仅 17%
- 风险：采样步数 观测到 1.00159e+09，超出安全上限 60（steps 偏高收益递减且显著增加耗时）
- 风险：重绘幅度 观测到 11，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
