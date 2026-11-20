---
name: image_to_image_lora_sampler_unet_51
type: Image To Image
frequency: 12
level: moderate
coverage: 0.97875
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen2511-儿童涂鸦风格转绘-小宣喧-RH_2007047125556797442.json, 图片生成/图生图/Qwen2511-阿凡达风格-小宣喧-RH_2008411628018081793.json, 图片生成/图生图/Qwen2511换装最新图像编辑_2072124811735822338.json, 图片生成/图生图/Qwen2511换装最新图像编辑_2072133881209384962.json, 图片生成/图生图/QwenEdit2511-Q版角色-小宣喧-RH_2006747284024860673.json, 图片生成/图生图/Qwen千问Image Edit 2511 多图编辑工作流_1953374181926817794.json, 图片生成/图生图/qwen2511一键换衣千问图像编辑换装_2060331107287134210.json, 图片生成/图生图/qwen_image_edit_2511_2004461710926901250.json, 图片生成/图生图/【AI小王子】86.Qwen+2511+图生图一致性之王！_2048651007839707137.json, 图片生成/图生图/剪辑必备-去水印qwen2511_2085741599010676737.json, 图片生成/图生图/图片去水印-Qwen2511-Lighting-速度快-效果好_2021029263138365441.json, 平台全量/图片去水印-Qwen2511-Lighting-速度快-效果好_2056354108122161154.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_51

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Qwen2511-儿童涂鸦风格转绘-小宣喧-RH_2007047125556797442.json、图片生成/图生图/Qwen2511-阿凡达风格-小宣喧-RH_2008411628018081793.json、图片生成/图生图/Qwen2511换装最新图像编辑_2072124811735822338.json、图片生成/图生图/Qwen2511换装最新图像编辑_2072133881209384962.json、图片生成/图生图/QwenEdit2511-Q版角色-小宣喧-RH_2006747284024860673.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `FluxKontextMultiReferenceLatentMethod` —— 11/12 个有
- `CR Text` —— 9/12 个有
- `ImageScaleToTotalPixels` —— 9/12 个有
- `SaveImage` —— 9/12 个有
- `ImageConcanate` —— 8/12 个有
- `ImageStitch` —— 4/12 个有
- `ImageResize+` —— 3/12 个有
- `KOOK_SaveJPGImage` —— 3/12 个有
- `Label (rgthree)` —— 3/12 个有
- `CustomAddLabel` —— 2/12 个有
- `Image Comparer (rgthree)` —— 2/12 个有
- `ImageConcatMulti` —— 2/12 个有
- `CR SDXL Aspect Ratio` —— 1/12 个有
- `EmptyLatentImage` —— 1/12 个有
- `ImpactSwitch` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 25 | 12 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | euler | - | 12 | 100% |
| 调度器 | simple | - | 12 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |
| 宽度 | 1024 | - | 1 | 100% |
| 高度 | 768 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 25，12 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，12 个样本，一致性 100%
- 调度器 最常用 simple，12 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 高发问题（11/12 个样本）：Steps较低可能导致细节不足
