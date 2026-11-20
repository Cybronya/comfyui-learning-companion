---
name: image_to_image_sampler_clip_unet_139
type: Image To Image
frequency: 3
level: weak
coverage: 0.905333
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/QWen-Image图生图中文渲染-ComfyUI_1953102878534791169.json, 图片生成/图生图/ZImage+LoRA图生图_1995169009526038529.json, 图片生成/图生图/Z_image_turbo图洗图_2056328304931725313.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_139

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/QWen-Image图生图中文渲染-ComfyUI_1953102878534791169.json、图片生成/图生图/ZImage+LoRA图生图_1995169009526038529.json、图片生成/图生图/Z_image_turbo图洗图_2056328304931725313.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 2/3 个有
- `RH_Captioner` —— 2/3 个有
- `Text Concatenate` —— 2/3 个有
- `Image Compare (mtb)` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有
- `Text Multiline` —— 1/3 个有
- `easy showAnything` —— 1/3 个有
- `easy stylesSelector` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | 4 - 20 | 3 | 39% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 0.5 - 1 | 3 | 72% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，观测区间 4 - 20，3 个样本，取值分散，一致性仅 39%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，3 个样本
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
