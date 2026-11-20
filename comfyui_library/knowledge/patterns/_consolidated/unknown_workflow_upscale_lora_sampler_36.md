---
name: unknown_workflow_upscale_lora_sampler_36
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.738429
common_nodes: [AdaptiveLongestEdge_EditUtils, CLIPLoader, CR Text Concatenate, ConditioningZeroOut, CropWithPadInfo_EditUtils, EditTextEncode_EditUtils, Flux2KleinModelConfig_EditUtils, Flux2KleinOutputExtractor_EditUtils, GetNode, Image Comparer (rgthree), ImageScaleToTotalPixels, ImageStitch, KSampler, LoraLoaderModelOnly, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, StringFunction|pysssss, Text Multiline, UNETLoader, VAEDecode, VAELoader, easy textIndexSwitch]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/最强开源flux2kelin一键透视渲染_2026582049326370817.json, 平台全量/FLUX2宋氏美学_2113502717699252225.json, 平台全量/Flux2Kelly室内外效果图洗图一键操作_2105107185557659650.json, 平台全量/Flux2Kelly室内外透视渲染+洗图_2104747465764331521.json, 平台全量/Flux2Kelly室内外透视渲染_2106312162489753601.json, 平台全量/Flux2Kelly室内极简或现代_2110636347785568258.json, 平台全量/透视渲染_2039985035759063041.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_lora_sampler_36

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/最强开源flux2kelin一键透视渲染_2026582049326370817.json、平台全量/FLUX2宋氏美学_2113502717699252225.json、平台全量/Flux2Kelly室内外效果图洗图一键操作_2105107185557659650.json、平台全量/Flux2Kelly室内外透视渲染+洗图_2104747465764331521.json、平台全量/Flux2Kelly室内外透视渲染_2106312162489753601.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 7 个 workflow 都包含：
- `AdaptiveLongestEdge_EditUtils`
- `CLIPLoader`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `CropWithPadInfo_EditUtils`
- `EditTextEncode_EditUtils`
- `Flux2KleinModelConfig_EditUtils`
- `Flux2KleinOutputExtractor_EditUtils`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageStitch`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `StringFunction|pysssss`
- `Text Multiline`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy textIndexSwitch`

**可变部分**（部分 workflow 才有）：
- `Flux2KleinConfigPreparer_EditUtils` —— 6/7 个有
- `StringConcatenate` —— 6/7 个有
- `LoadImage` —— 5/7 个有
- `ImageLoader` —— 2/7 个有
- `Flux3KleinConfigPreparer_EditUtils` —— 1/7 个有
- `RepeatLatentBatch` —— 1/7 个有
- `easy cleanGpuUsed` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
