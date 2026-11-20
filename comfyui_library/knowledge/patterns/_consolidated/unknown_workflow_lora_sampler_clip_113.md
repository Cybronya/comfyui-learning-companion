---
name: unknown_workflow_lora_sampler_clip_113
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.880833
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CropWithPadInfo_EditUtils, FluxKontextMultiReferenceLatentMethod, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, QwenEditConfigPreparer, QwenEditOutputExtractor_EditUtils, SaveImage, TextEncodeQwenImageEditPlusCustom_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/printing_extraction_api_2100774516120186882.json, 图片生成/图生图/印花提取——qwen2511_2096790576627802114.json, 图片生成/图生图/印花提取——qwen2511_2097136560390103041.json, 平台全量/动漫转3D——2511_2045352602170298370.json, 平台全量/印花提取——2511_2039733952587501570.json, 平台全量/图案迁移至T恤——2509版_2008309290020376578.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_113

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/printing_extraction_api_2100774516120186882.json、图片生成/图生图/印花提取——qwen2511_2096790576627802114.json、图片生成/图生图/印花提取——qwen2511_2097136560390103041.json、平台全量/动漫转3D——2511_2045352602170298370.json、平台全量/印花提取——2511_2039733952587501570.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CropWithPadInfo_EditUtils`
- `FluxKontextMultiReferenceLatentMethod`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `QwenEditConfigPreparer`
- `QwenEditOutputExtractor_EditUtils`
- `SaveImage`
- `TextEncodeQwenImageEditPlusCustom_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 5/6 个有
- `easy cleanGpuUsed` —— 5/6 个有
- `GetNode` —— 4/6 个有
- `SetNode` —— 4/6 个有
- `CR Overlay Transparent Image` —— 1/6 个有
- `Image Input Switch` —— 1/6 个有
- `ImageScale` —— 1/6 个有
- `ImageUpscaleWithModel` —— 1/6 个有
- `SimpleMath+` —— 1/6 个有
- `UpscaleModelLoader` —— 1/6 个有
- `ZML_ArithmeticComparison` —— 1/6 个有
- `easy imageSizeByLongerSide` —— 1/6 个有
- `easy int` —— 1/6 个有
- `easy mathInt` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | FlowMatchEulerDiscreteScheduler | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 FlowMatchEulerDiscreteScheduler，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
