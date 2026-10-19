---
name: unknown_workflow_video_lora_sampler_280
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.778125
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, Fast Bypasser (rgthree), GetNode, ImpactInt, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, MathExpression|pysssss, ModelPatchTorchSettings, ModelSamplingSD3, Mute / Bypass Repeater (rgthree), PathchSageAttentionKJ, RIFE VFI, SetNode, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanMoeKSampler, easy setNode]
problems: []
missing: []
members: [视频生成/图生视频/2061793928344588289.json, 视频生成/图生视频/2061751615295680514.json, 视频生成/图生视频/2061718724150906881.json, 视频生成/图生视频/2035281651009327105.json, 视频生成/图生视频/2038957915788283906.json, 视频生成/图生视频/极致进化！REMIX V3 图生视频【自动优化+Qwen3.5】_2089713058884177921.json, 视频生成/图生视频/2052999624771813378.json, 视频生成/图生视频/2034912808818712577.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_280

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/2061793928344588289.json、视频生成/图生视频/2061751615295680514.json、视频生成/图生视频/2061718724150906881.json、视频生成/图生视频/2035281651009327105.json、视频生成/图生视频/2038957915788283906.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：78%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
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
- `DapaoSmartMemoryOptimizerNode` —— 7/8 个有
- `PainterI2V` —— 7/8 个有
- `easy showAnything` —— 7/8 个有
- `llama_cpp_instruct_adv` —— 7/8 个有
- `llama_cpp_model_loader` —— 7/8 个有
- `llama_cpp_parameters` —— 7/8 个有
- `CR Text` —— 6/8 个有
- `easy ifElse` —— 6/8 个有
- `easy isNone` —— 6/8 个有
- `easy getNode` —— 5/8 个有
- `CustomAddLabel` —— 4/8 个有
- `FlashVSRNode` —— 3/8 个有
- `ImageConcanate` —— 3/8 个有
- `PrimitiveInt` —— 3/8 个有
- `EmptyLTXVLatentVideo` —— 1/8 个有
- `ImageResizeKJ` —— 1/8 个有
- `Int` —— 1/8 个有
- `MultiTextConcatenate` —— 1/8 个有
- `Note Plus (mtb)` —— 1/8 个有
- `PainterFLF2V` —— 1/8 个有
- `PromptRelayEncodeTimeline` —— 1/8 个有
- `RH_Utils` —— 1/8 个有
- `SeedGeneratorMira` —— 1/8 个有
- `ShowText|pysssss` —— 1/8 个有
- `Text` —— 1/8 个有
- `easy cleanGpuUsed` —— 1/8 个有
- `easy positive` —— 1/8 个有
- `ttN concat` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | 1 | 1 - 1 | 8 | 100% |
| 重绘幅度 | euler_ancestral | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 重绘幅度 最常用 euler_ancestral，8 个样本，一致性 100%
