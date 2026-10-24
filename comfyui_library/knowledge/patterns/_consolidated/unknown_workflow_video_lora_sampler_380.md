---
name: unknown_workflow_video_lora_sampler_380
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7862
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, GetNode, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PainterI2V, PathchSageAttentionKJ, RIFE VFI, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMoeKSampler, easy getNode, easy setNode]
problems: []
missing: []
members: [图片生成/图生图/REMIX V3 图生视频-批量_2035929397282217985.json, 视频生成/图生视频/REMIX V2 在线批量-图生视频_2004740865878884354.json, 视频生成/图生视频/图生视频_1999866584787189761.json, 视频生成/图生视频/图生视频修改_2009703059848433666.json, 视频生成/图生视频/🕵🏻极致进化！REMIX V3 图生视频【自动优化+Qwen3.5】_2034912808818712577.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_380

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/REMIX V3 图生视频-批量_2035929397282217985.json、视频生成/图生视频/REMIX V2 在线批量-图生视频_2004740865878884354.json、视频生成/图生视频/图生视频_1999866584787189761.json、视频生成/图生视频/图生视频修改_2009703059848433666.json、视频生成/图生视频/🕵🏻极致进化！REMIX V3 图生视频【自动优化+Qwen3.5】_2034912808818712577.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：79%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `ImpactInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `Mute / Bypass Repeater (rgthree)`
- `PainterI2V`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanMoeKSampler`
- `easy getNode`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 4/5 个有
- `Fast Bypasser (rgthree)` —— 4/5 个有
- `LoadImage` —— 4/5 个有
- `easy showAnything` —— 3/5 个有
- `wanBlockSwap` —— 3/5 个有
- `RHBatchImages:` —— 2/5 个有
- `RHExtractImage` —— 2/5 个有
- `RHUploadZip` —— 2/5 个有
- `easy forLoopEnd` —— 2/5 个有
- `easy forLoopStart` —— 2/5 个有
- `easy ifElse` —— 2/5 个有
- `easy imageCount` —— 2/5 个有
- `easy isNone` —— 2/5 个有
- `llama_cpp_instruct_adv` —— 2/5 个有
- `llama_cpp_model_loader` —— 2/5 个有
- `llama_cpp_parameters` —— 2/5 个有
- `DapaoSmartMemoryOptimizerNode` —— 1/5 个有
- `Fast Muter (rgthree)` —— 1/5 个有
- `LayerUtility: PurgeVRAM` —— 1/5 个有
- `Note Plus (mtb)` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 5 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | 1 | 1 - 1 | 5 | 100% |
| 重绘幅度 | euler_ancestral | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，5 个样本，一致性 100%
