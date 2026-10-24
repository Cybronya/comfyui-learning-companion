---
name: text_to_image_sampler_clip_unet_78
type: Text To Image
frequency: 8
level: strong
coverage: 0.90025
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Text to Image _ Z-IMAGE_1993955627510726657.json, "图片生成/文生图/Tutu's Aurora 8D HiSilk Z Image workflow_2070527638774566913.json", "图片生成/文生图/Tutu's HiSilk Fishnet Z Image workflow_2070527636975210497.json", 图片生成/文生图/VividMuse Z-Image-Turbo Dark Dreamcore Style_2060957933088890881.json, 图片生成/文生图/Z-Image 超强文生图_1993850615438704641.json, 图片生成/文生图/Z-image 提示词列表1次生成5张图_2022135215480639489.json, 图片生成/文生图/Z-image-turbo 极速文生图_1993943881752444930.json, 图片生成/文生图/▶▷Krea2文生图_2107457543818801153.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_78

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Text to Image _ Z-IMAGE_1993955627510726657.json、图片生成/文生图/Tutu's Aurora 8D HiSilk Z Image workflow_2070527638774566913.json、图片生成/文生图/Tutu's HiSilk Fishnet Z Image workflow_2070527636975210497.json、图片生成/文生图/VividMuse Z-Image-Turbo Dark Dreamcore Style_2060957933088890881.json、图片生成/文生图/Z-Image 超强文生图_1993850615438704641.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/8 个有
- `PrimitiveStringMultiline` —— 3/8 个有
- `easy promptList` —— 3/8 个有
- `CR SDXL Aspect Ratio` —— 2/8 个有
- `Seed (rgthree)` —— 2/8 个有
- `Textbox` —— 2/8 个有
- `Anything Everywhere3` —— 1/8 个有
- `HAIGC_SaveImagesToZip` —— 1/8 个有
- `ResolutionSelector` —— 1/8 个有
- `easy anythingIndexSwitch` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 6 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 83% |
| 调度器 | simple | - | 6 | 83% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1052 | 720 - 1536 | 8 | 78% |
| 高度 | 1376 | 1024 - 2048 | 8 | 74% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，6 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 83%
- 调度器 最常用 simple，6 个样本，一致性 83%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1052，观测区间 720 - 1536，8 个样本
- 高度 中位数 1376，观测区间 1024 - 2048，8 个样本
