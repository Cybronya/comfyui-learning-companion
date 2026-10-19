---
name: unknown_workflow_video_sampler_clip_231
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7145
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, GetNode, ImageResize+, Int, KSamplerAdvanced, LoadImage, MathExpression|pysssss, ModelSamplingSD3, PathchSageAttentionKJ, SetNode, SomethingToString, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2035997613283086338.json, 视频生成/图生视频/2027044559796047873.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_231

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2035997613283086338.json、视频生成/图生视频/2027044559796047873.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `GetNode`
- `ImageResize+`
- `Int`
- `KSamplerAdvanced`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SetNode`
- `SomethingToString`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 1/2 个有
- `LayerUtility: PurgeVRAM` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1` —— 1/2 个有
- `Qwen3_VQA` —— 1/2 个有
- `TextConcat` —— 1/2 个有
- `WanImageToVideo` —— 1/2 个有
- `llama_cpp_instruct_adv` —— 1/2 个有
- `llama_cpp_model_loader` —— 1/2 个有
- `llama_cpp_parameters` —— 1/2 个有
- `ttN concat` —— 1/2 个有
- `wanBlockSwap` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | increment | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4 | - | 2 | 100% |
| 采样算法 | 1 | - | 2 | 100% |
| 调度器 | euler | - | 2 | 100% |
| 重绘幅度 | normal | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 increment，2 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，2 个样本，一致性 100%
- 重绘幅度 最常用 normal，2 个样本，一致性 100%
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
