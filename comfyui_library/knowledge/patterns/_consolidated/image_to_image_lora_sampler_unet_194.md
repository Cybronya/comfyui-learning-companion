---
name: image_to_image_lora_sampler_unet_194
type: Image To Image
frequency: 3
level: strong
coverage: 0.760333
common_nodes: [CFGNorm, CLIPLoader, CR Prompt Text, JDCN_StringToList, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, ProcessString, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一张图生成多模特姿势电商小红书抖音_2067435931765927938.json, 图片生成/图生图/手动改变图片角度和镜头2511_2109842555734151170.json, 图片生成/图生图/用一张图生成16张写真姿势图片_1995057637274345474.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_194

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/一张图生成多模特姿势电商小红书抖音_2067435931765927938.json、图片生成/图生图/手动改变图片角度和镜头2511_2109842555734151170.json、图片生成/图生图/用一张图生成16张写真姿势图片_1995057637274345474.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Prompt Text`
- `JDCN_StringToList`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `ProcessString`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `Text Concatenate` —— 2/3 个有
- `FluxKontextMultiReferenceLatentMethod` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 3 | 72% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | res_2m | - | 3 | 67% |
| 调度器 | sgm_uniform | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_2m，3 个样本，一致性 67%
- 调度器 最常用 sgm_uniform，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
