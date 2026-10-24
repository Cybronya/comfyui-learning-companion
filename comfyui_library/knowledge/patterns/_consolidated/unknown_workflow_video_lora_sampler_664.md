---
name: unknown_workflow_video_lora_sampler_664
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.878333
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, CR Prompt Text, CompressImages, DF_Float, DiffusionModelLoaderKJ, DuckHideNode, Float, ImageResizeKJv2, Int, JWInteger, JjkText, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PainterI2V, PathchSageAttentionKJ, PrimitiveInt, RIFE VFI, RunningHub Deepcleaner, SaveImage, SaveMP4, Seed (rgthree), SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/做鬼脸_2050235344452374529.json, 视频生成/图生视频/自用_丝足_2049135823223787522.json, 视频生成/图生视频/造梦喷泉_2049148615460917249.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_664

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/做鬼脸_2050235344452374529.json、视频生成/图生视频/自用_丝足_2049135823223787522.json、视频生成/图生视频/造梦喷泉_2049148615460917249.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `CR Prompt Text`
- `CompressImages`
- `DF_Float`
- `DiffusionModelLoaderKJ`
- `DuckHideNode`
- `Float`
- `ImageResizeKJv2`
- `Int`
- `JWInteger`
- `JjkText`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PainterI2V`
- `PathchSageAttentionKJ`
- `PrimitiveInt`
- `RIFE VFI`
- `RunningHub Deepcleaner`
- `SaveImage`
- `SaveMP4`
- `Seed (rgthree)`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `JWString` —— 2/3 个有
- `AILab_QwenVL` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `PainterI2V-up WAN2.2 LatentMotion Enhancer by paicat1` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `YCSwitch` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 3 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | 1 | 1 - 1 | 3 | 100% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
