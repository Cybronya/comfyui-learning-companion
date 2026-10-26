---
name: unknown_workflow_video_sampler_clip_190
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.879333
common_nodes: [CLIPTextEncode, CR Text, JWInteger, KSamplerAdvanced, LoadImage, MathExpression|pysssss, RIFE VFI, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, VAEDecode, VHS_VideoCombine, WanImageToVideo, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Smooth Mix+Wan2.2 图生视频（自动提示词）_1982274042864517122.json, 视频生成/图生视频/Wan2.2 Smooth Mix图生视频_1979813439872864257.json, 视频生成/图生视频/图生视频，Wan2.2高动态，超强语义遵循_1981008328186806273.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_190

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/Smooth Mix+Wan2.2 图生视频（自动提示词）_1982274042864517122.json、视频生成/图生视频/Wan2.2 Smooth Mix图生视频_1979813439872864257.json、视频生成/图生视频/图生视频，Wan2.2高动态，超强语义遵循_1981008328186806273.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Text`
- `JWInteger`
- `KSamplerAdvanced`
- `LoadImage`
- `MathExpression|pysssss`
- `RIFE VFI`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `SeedVR2GGUF`
- `VAEDecode`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `AILab_QwenVL` —— 2/3 个有
- `CLIPLoader` —— 2/3 个有
- `CLIPVisionEncode` —— 2/3 个有
- `CLIPVisionLoader` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `ImageScale` —— 2/3 个有
- `ImpactSwitch` —— 2/3 个有
- `LayerUtility: BooleanOperatorV2` —— 2/3 个有
- `LayerUtility: If ` —— 2/3 个有
- `ModelPatchTorchSettings` —— 2/3 个有
- `ModelSamplingSD3` —— 2/3 个有
- `PathchSageAttentionKJ` —— 2/3 个有
- `PreviewAny` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `UNETLoader` —— 2/3 个有
- `VAELoader` —— 2/3 个有
- `easy imageScaleDownToSize` —— 2/3 个有
- `easy int` —— 2/3 个有
- `wanBlockSwap` —— 2/3 个有
- `CR Text Input Switch` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `RH_Translator` —— 1/3 个有
- `workflow>SMOOTH MIX-WAN2.2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler_ancestral | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
