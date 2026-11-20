---
name: unknown_workflow_video_lora_sampler_455
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.776857
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DapaoSmartMemoryOptimizerNode, Fast Bypasser (rgthree), GetNode, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, RIFE VFI, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMoeKSampler, easy setNode]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2-REMIX V3-PromptRelay-无审查-图生视频_2061793928344588289.json, 视频生成/图生视频/Wan2.2-REMIX V3-无审查-首尾帧视频_2061751615295680514.json, 视频生成/图生视频/Wan2.2工作流-REMIX V3-图生视频_2061718724150906881.json, 视频生成/图生视频/最好用的Wan2.2工作流-REMIX V3-图生视频_2035281651009327105.json, 视频生成/图生视频/极致进化！REMIX V3 图生视频【自动优化+Qwen3.5】_2038957915788283906.json, 视频生成/图生视频/极致进化！REMIX V3 图生视频【自动优化+Qwen3.5】_2089713058884177921.json, 视频生成/图生视频/🕵🏻极致进化！REMIX V3 图生视频【自动优化+Qwen3.5】_2034912808818712577.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_455

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/Wan2.2-REMIX V3-PromptRelay-无审查-图生视频_2061793928344588289.json、视频生成/图生视频/Wan2.2-REMIX V3-无审查-首尾帧视频_2061751615295680514.json、视频生成/图生视频/Wan2.2工作流-REMIX V3-图生视频_2061718724150906881.json、视频生成/图生视频/最好用的Wan2.2工作流-REMIX V3-图生视频_2035281651009327105.json、视频生成/图生视频/极致进化！REMIX V3 图生视频【自动优化+Qwen3.5】_2038957915788283906.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DapaoSmartMemoryOptimizerNode`
- `Fast Bypasser (rgthree)`
- `GetNode`
- `ImpactInt`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MathExpression|pysssss`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `Mute / Bypass Repeater (rgthree)`
- `PathchSageAttentionKJ`
- `RIFE VFI`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanMoeKSampler`
- `easy setNode`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 6/7 个有
- `PainterI2V` —— 6/7 个有
- `easy ifElse` —— 6/7 个有
- `easy isNone` —— 6/7 个有
- `easy showAnything` —— 6/7 个有
- `llama_cpp_instruct_adv` —— 6/7 个有
- `llama_cpp_model_loader` —— 6/7 个有
- `llama_cpp_parameters` —— 6/7 个有
- `easy getNode` —— 4/7 个有
- `CustomAddLabel` —— 3/7 个有
- `FlashVSRNode` —— 3/7 个有
- `ImageConcanate` —— 3/7 个有
- `PrimitiveInt` —— 3/7 个有
- `EmptyLTXVLatentVideo` —— 1/7 个有
- `ImageResizeKJ` —— 1/7 个有
- `Note Plus (mtb)` —— 1/7 个有
- `PainterFLF2V` —— 1/7 个有
- `PromptRelayEncodeTimeline` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 7 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 7 | 100% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | 1 | 1 - 1 | 7 | 100% |
| 重绘幅度 | euler_ancestral | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，7 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，7 个样本，一致性 100%
