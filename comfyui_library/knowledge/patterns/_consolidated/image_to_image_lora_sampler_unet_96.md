---
name: image_to_image_lora_sampler_unet_96
type: Image To Image
frequency: 7
level: strong
coverage: 0.940143
common_nodes: [CFGNorm, CLIPLoader, CR Prompt Text, KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/多景镜头人物一致性-Qwen-Edit-2511_2012351159188594690.json, 图片生成/图生图/小红书FireRed-Image-edit1.1 双图编辑_2031635950748569602.json, 图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑_2033152678896869378.json, 图片生成/图生图/小红书FireRed1.1 (单图编辑)_2031636180478992385.json, 图片生成/图生图/小红书双图编辑器_2034535893565968385.json, 图片生成/图生图/老照片修复_2009751417199796225.json, 图片生成/图生图/（自用）小红书FireRed-Image-edit 双图编辑（换装）_2029612197713813506.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_96

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/多景镜头人物一致性-Qwen-Edit-2511_2012351159188594690.json、图片生成/图生图/小红书FireRed-Image-edit1.1 双图编辑_2031635950748569602.json、图片生成/图生图/小红书FireRed-Image-edit1.1单图编辑_2033152678896869378.json、图片生成/图生图/小红书FireRed1.1 (单图编辑)_2031636180478992385.json、图片生成/图生图/小红书双图编辑器_2034535893565968385.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Prompt Text`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 5/7 个有
- `easy cleanGpuUsed` —— 5/7 个有
- `easy int` —— 4/7 个有
- `INTConstant` —— 2/7 个有
- `ReferenceLatent` —— 2/7 个有
- `ConditioningZeroOut` —— 1/7 个有
- `DyPE_FLUX` —— 1/7 个有
- `Image Comparer (rgthree)` —— 1/7 个有
- `MemoryCleaner` —— 1/7 个有
- `easy promptLine` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 7 | 74% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 86% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 86%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
