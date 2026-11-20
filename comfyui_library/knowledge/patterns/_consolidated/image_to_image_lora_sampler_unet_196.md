---
name: image_to_image_lora_sampler_unet_196
type: Image To Image
frequency: 4
level: strong
coverage: 0.8725
common_nodes: [ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageStitch, KSampler, LoadImage, LoadImageOutput, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Kontext-LORA效果测试工作流_1942450419496857602.json, 图片生成/文生图/kontext-lora 一键转换手绘风格三视图_1940252363783360514.json, 图片生成/文生图/服装提取_1956530025573044225.json, 平台全量/去水印_2000483507875049473.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_196

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/Kontext-LORA效果测试工作流_1942450419496857602.json、图片生成/文生图/kontext-lora 一键转换手绘风格三视图_1940252363783360514.json、图片生成/文生图/服装提取_1956530025573044225.json、平台全量/去水印_2000483507875049473.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `LoadImageOutput`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncode` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `CR Simple Image Compare` —— 1/4 个有
- `DeepTranslatorCLIPTextEncodeNode` —— 1/4 个有
- `EmptySD3LatentImage` —— 1/4 个有
- `Fast Groups Bypasser (rgthree)` —— 1/4 个有
- `GoogleTranslateTextNode` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `PreviewTextNode` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有
- `TeaCache` —— 1/4 个有
- `Text` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 10 - 20 | 4 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 10 - 20，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
