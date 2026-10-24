---
name: image_to_image_lora_sampler_clip_56
type: Image To Image
frequency: 5
level: strong
coverage: 0.9214
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, FluxKontextImageScale, ImageStitch, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Kontext 老年的你_1947231811882655745.json, 图片生成/图生图/Kontext 老年的你_1976488006263640065.json, 图片生成/图生图/图像高清去模糊deblur(Kontext-LORA版)_1943499477413994497.json, 图片生成/图生图/提取服装平铺图_1942986904318984194.json, 图片生成/图生图/老照片修复_Kontext-LORA版_1943506433671372802.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_56

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Kontext 老年的你_1947231811882655745.json、图片生成/图生图/Kontext 老年的你_1976488006263640065.json、图片生成/图生图/图像高清去模糊deblur(Kontext-LORA版)_1943499477413994497.json、图片生成/图生图/提取服装平铺图_1942986904318984194.json、图片生成/图生图/老照片修复_Kontext-LORA版_1943506433671372802.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `FluxKontextImageScale`
- `ImageStitch`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 3/5 个有
- `UNETLoader` —— 3/5 个有
- `DF_Integer` —— 2/5 个有
- `Int2String` —— 2/5 个有
- `StringReplace` —— 2/5 个有
- `UnetLoaderGGUF` —— 2/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `TextInputBasic` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 28 | 5 | 85% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 60% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 28，5 个样本，取值集中（一致性 85%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 60%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
