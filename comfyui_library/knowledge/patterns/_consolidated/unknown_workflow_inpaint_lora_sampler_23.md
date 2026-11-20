---
name: unknown_workflow_inpaint_lora_sampler_23
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.7046
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DifferentialDiffusion, DualCLIPLoader, FluxGuidance, ImpactImageBatchToImageList, InpaintModelConditioning, Int, InvertMask, JWStringConcat, KSampler, LayerMask: MaskGrow, LayerMask: SegformerB2ClothesUltra, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LoadImage, LoraLoaderModelOnly, ModelSamplingFlux, PrimitiveString, RepeatLatentBatch, SaveImage, UNETLoader, VAEDecode, VAELoader, easy anythingIndexSwitch, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/CHAOS 照相馆 - 智能构图全身_半身_肖像照生成系统_2090293559198052354.json, 图片生成/图生图/CHAOS_照相馆_-_智能构图全身_半身_肖像照生成系统_2091723972449755138.json, 图片生成/图生图/CHAOS_照相馆_-_智能构图全身_半身_肖像照生成系统_2092060769549635585.json, 平台全量/CHAOS 照相馆 - 智能构图全身_半身_肖像照生成系统_1905427890211852289.json, 平台全量/CHAOS 照相馆 双人版 - 智能构图全身_半身_肖像照生成系统_1905428925693235202.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_lora_sampler_23

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/CHAOS 照相馆 - 智能构图全身_半身_肖像照生成系统_2090293559198052354.json、图片生成/图生图/CHAOS_照相馆_-_智能构图全身_半身_肖像照生成系统_2091723972449755138.json、图片生成/图生图/CHAOS_照相馆_-_智能构图全身_半身_肖像照生成系统_2092060769549635585.json、平台全量/CHAOS 照相馆 - 智能构图全身_半身_肖像照生成系统_1905427890211852289.json、平台全量/CHAOS 照相馆 双人版 - 智能构图全身_半身_肖像照生成系统_1905428925693235202.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DifferentialDiffusion`
- `DualCLIPLoader`
- `FluxGuidance`
- `ImpactImageBatchToImageList`
- `InpaintModelConditioning`
- `Int`
- `InvertMask`
- `JWStringConcat`
- `KSampler`
- `LayerMask: MaskGrow`
- `LayerMask: SegformerB2ClothesUltra`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingFlux`
- `PrimitiveString`
- `RepeatLatentBatch`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy anythingIndexSwitch`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `FaceAutoFitSingle` —— 4/5 个有
- `LayerUtility: PurgeVRAM` —— 4/5 个有
- `PromptSelectorSingleCHAOS` —— 4/5 个有
- `easy cleanGpuUsed` —— 4/5 个有
- `preview_mask` —— 4/5 个有
- `FaceAutoFitDouble` —— 1/5 个有
- `Label (rgthree)` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `PromptSelectorDoubleCHAOS` —— 1/5 个有
- `easy imageSize` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 12 | 12 - 12 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | sgm_uniform | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 12，观测区间 12 - 12，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 sgm_uniform，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
