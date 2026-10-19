---
name: unknown_workflow_video_sampler_clip_108
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9074
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Text, ImageResizeKJv2, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MathExpression|pysssss, ModelSamplingSD3, PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy cleanGpuUsed, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/2039893692558876673.json, 视频生成/图生视频/2036675075717472258.json, 视频生成/图生视频/2035931554823806977.json, 视频生成/图生视频/2036102577590374402.json, 视频生成/图生视频/2036614477726097410.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_108

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/2039893692558876673.json、视频生成/图生视频/2036675075717472258.json、视频生成/图生视频/2035931554823806977.json、视频生成/图生视频/2036102577590374402.json、视频生成/图生视频/2036614477726097410.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：91%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Text`
- `ImageResizeKJv2`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MathExpression|pysssss`
- `ModelSamplingSD3`
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 4/5 个有
- `Float` —— 4/5 个有
- `LayerUtility: PurgeVRAM` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `FL_RIFE` —— 3/5 个有
- `RTXVideoSuperResolution` —— 3/5 个有
- `ImageFromBatch+` —— 2/5 个有
- `Load Image From Url (mtb)` —— 1/5 个有
- `PrimitiveFloat` —— 1/5 个有
- `RunningHub Deepcleaner` —— 1/5 个有
- `Seed (rgthree)` —— 1/5 个有
- `ShellAgentPluginOutputText` —— 1/5 个有
- `String` —— 1/5 个有
- `easy anythingIndexSwitch` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler_ancestral | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler_ancestral，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
