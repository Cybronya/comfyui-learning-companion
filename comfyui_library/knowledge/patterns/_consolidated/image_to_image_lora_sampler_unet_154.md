---
name: image_to_image_lora_sampler_unet_154
type: Image To Image
frequency: 4
level: weak
coverage: 0.91975
common_nodes: [CFGNorm, CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-image-edit线图或插图直接转换3D真实图_1981531839686942721.json, 图片生成/图生图/QwenEdit图片编辑+1个流的多玩法_1959226835055882241.json, 图片生成/图生图/qwen_edit_一键Chibi角色风格转换 Q版风格化_1980449032965435394.json, 图片生成/文生图/Qwen-Image-Edit-一键转宫崎骏风_2095060097503420418.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_154

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Qwen-image-edit线图或插图直接转换3D真实图_1981531839686942721.json、图片生成/图生图/QwenEdit图片编辑+1个流的多玩法_1959226835055882241.json、图片生成/图生图/qwen_edit_一键Chibi角色风格转换 Q版风格化_1980449032965435394.json、图片生成/文生图/Qwen-Image-Edit-一键转宫崎骏风_2095060097503420418.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 3/4 个有
- `TextEncodeQwenImageEdit` —— 3/4 个有
- `CR Simple Image Compare` —— 2/4 个有
- `Image Comparer (rgthree)` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `JjkText` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `AILab_ImageStitch` —— 1/4 个有
- `TextEncodeQwenImageEditEnhanced` —— 1/4 个有
- `easy cleanGpuUsed` —— 1/4 个有
- `easy imageSave` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 20 | 4 | 27% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 4 | 0% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 20，4 个样本，取值分散，一致性仅 27%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，4 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（3/4 个样本）：Steps较低可能导致细节不足
