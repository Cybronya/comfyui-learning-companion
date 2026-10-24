---
name: unknown_workflow_video_sampler_clip_152
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.87225
common_nodes: [CLIPTextEncode, CR Text, JWInteger, KSamplerAdvanced, LoadImage, MathExpression|pysssss, RIFE VFI, SeedVR2BlockSwap, SeedVR2ExtraArgs, SeedVR2GGUF, VAEDecode, VHS_VideoCombine, WanImageToVideo, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Smooth Mix+Wan2.2 图生视频（自动提示词）_1982274042864517122.json, 视频生成/图生视频/Wan2.2 Smooth Mix图生视频_1979813439872864257.json, 视频生成/图生视频/图生视频，Wan2.2高动态，超强语义遵循_1981008328186806273.json, 视频生成/图生视频/高动态，超强理解，Wan2.2 图生视频_1981000332023042050.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_152

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/Smooth Mix+Wan2.2 图生视频（自动提示词）_1982274042864517122.json、视频生成/图生视频/Wan2.2 Smooth Mix图生视频_1979813439872864257.json、视频生成/图生视频/图生视频，Wan2.2高动态，超强语义遵循_1981008328186806273.json、视频生成/图生视频/高动态，超强理解，Wan2.2 图生视频_1981000332023042050.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
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
- `CLIPLoader` —— 3/4 个有
- `CLIPVisionEncode` —— 3/4 个有
- `CLIPVisionLoader` —— 3/4 个有
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `ModelPatchTorchSettings` —— 3/4 个有
- `ModelSamplingSD3` —— 3/4 个有
- `PathchSageAttentionKJ` —— 3/4 个有
- `UNETLoader` —— 3/4 个有
- `VAELoader` —— 3/4 个有
- `wanBlockSwap` —— 3/4 个有
- `AILab_QwenVL` —— 2/4 个有
- `CR Text Input Switch` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `ImageScale` —— 2/4 个有
- `ImpactSwitch` —— 2/4 个有
- `LayerUtility: BooleanOperatorV2` —— 2/4 个有
- `LayerUtility: If ` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `PreviewAny` —— 2/4 个有
- `PreviewImage` —— 2/4 个有
- `RH_LLMAPI_NODE` —— 2/4 个有
- `easy imageScaleDownToSize` —— 2/4 个有
- `easy int` —— 2/4 个有
- `GetNode` —— 1/4 个有
- `RH_Translator` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `workflow>SMOOTH MIX-WAN2.2` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 4 | 75% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 4 | 100% |
| 采样算法 | 1 | 1 - 1 | 4 | 100% |
| 调度器 | euler_ancestral | - | 4 | 100% |
| 重绘幅度 | simple | - | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，4 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，4 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，4 个样本，一致性 100%
- 重绘幅度 最常用 simple，4 个样本，一致性 100%
