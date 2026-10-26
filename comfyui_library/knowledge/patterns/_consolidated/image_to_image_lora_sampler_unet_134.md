---
name: image_to_image_lora_sampler_unet_134
type: Image To Image
frequency: 5
level: strong
coverage: 0.9464
common_nodes: [CFGNorm, CLIPLoader, ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问edit2509参考风格洗图_1991378978059452418.json, 图片生成/图生图/材质修改Q2511_2008020062157934594.json, 图片生成/图生图/自动加模特，换背景_2053030897783459841.json, 图片生成/图生图/角色多视角生成_1987538986363195394.json, 图片生成/文生图/Qwen Image Edit 2511-三图编辑-圣诞节快乐_2003966404120461313.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_134

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/千问edit2509参考风格洗图_1991378978059452418.json、图片生成/图生图/材质修改Q2511_2008020062157934594.json、图片生成/图生图/自动加模特，换背景_2053030897783459841.json、图片生成/图生图/角色多视角生成_1987538986363195394.json、图片生成/文生图/Qwen Image Edit 2511-三图编辑-圣诞节快乐_2003966404120461313.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 2/5 个有
- `AIO_Preprocessor` —— 1/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `RH_LLMAPI_NODE` —— 1/5 个有
- `String` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 5 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，5 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（8/5 个样本）：Steps较低可能导致细节不足
