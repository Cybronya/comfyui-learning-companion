---
name: image_to_image_lora_sampler_clip_109
type: Image To Image
frequency: 4
level: strong
coverage: 0.9305
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FastCanvas, FastCanvasTool, FluxGuidance, FluxKontextImageScale, ImageConcanate, ImageConcatMulti, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/kontext图像融合图像编辑_1947080294626799618.json, 图片生成/图生图/▶Flux-kontext万物溶图流_1956309858435956737.json, 图片生成/图生图/产品融图工作流_1966999229111603201.json, 平台全量/Kontext稳定融合两张图片（调加商业级lora）_1946852128938684417.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_109

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/kontext图像融合图像编辑_1947080294626799618.json、图片生成/图生图/▶Flux-kontext万物溶图流_1956309858435956737.json、图片生成/图生图/产品融图工作流_1966999229111603201.json、平台全量/Kontext稳定融合两张图片（调加商业级lora）_1946852128938684417.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：93%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FastCanvas`
- `FastCanvasTool`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageConcanate`
- `ImageConcatMulti`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BiRefNetRMBG` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `DeepTranslatorTextNode` —— 2/4 个有
- `ImageScaleToMegapixels` —— 2/4 个有
- `Bjornulf_FreeVRAM` —— 1/4 个有
- `ConcatTextOfUtils` —— 1/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/4 个有
- `RH_LLMAPI_NODE` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有
- `TextInput_` —— 1/4 个有
- `easy imageRemBg` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
