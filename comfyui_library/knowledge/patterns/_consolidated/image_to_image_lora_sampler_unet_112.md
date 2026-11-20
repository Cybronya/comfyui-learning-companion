---
name: image_to_image_lora_sampler_unet_112
type: Image To Image
frequency: 7
level: moderate
coverage: 0.85
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen光影_2002990949435338754.json, 图片生成/图生图/laoA 单姿态控制_2083568675835174913.json, 图片生成/图生图/qwen-edit胸部增强模型-丰胸自动流程_1984437814957850626.json, 图片生成/图生图/丰胸神器_2040754896382726145.json, 图片生成/图生图/局部编辑+🐻变大+自定义强度+全节点注释_2057684290074398722.json, 图片生成/图生图/胸部增强_2085270174135046146.json, 图片生成/图生图/胸部增强，一键运行，即刻变美！_2005667509246324737.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_112

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Qwen光影_2002990949435338754.json、图片生成/图生图/laoA 单姿态控制_2083568675835174913.json、图片生成/图生图/qwen-edit胸部增强模型-丰胸自动流程_1984437814957850626.json、图片生成/图生图/丰胸神器_2040754896382726145.json、图片生成/图生图/局部编辑+🐻变大+自定义强度+全节点注释_2057684290074398722.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 7 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
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
- `SeedVR2` —— 6/7 个有
- `SeedVR2BlockSwap` —— 6/7 个有
- `Text` —— 6/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `ImageScaleToTotalPixels` —— 5/7 个有
- `Int` —— 5/7 个有
- `PrimitiveFloat` —— 5/7 个有
- `easy cleanGpuUsed` —— 5/7 个有
- `PreviewImage` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `CR Text` —— 1/7 个有
- `ColorMatchPro` —— 1/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `RHHiddenNodes` —— 1/7 个有
- `TT_img_enc_v2` —— 1/7 个有
- `Text Concatenate` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 30 | 7 | 0% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 30，7 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
