---
name: image_to_image_lora_sampler_clip_76
type: Image To Image
frequency: 4
level: weak
coverage: 0.992
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/WAN2.2低噪模型重绘极速洗图工作流_1969774653545848833.json, 图片生成/图生图/Wan2.1 图生图洗图+修复工作流_1945503532646637569.json, 图片生成/图生图/Wan2.2写实洗图工作流_1957018598755721218.json, 图片生成/图生图/Wan2.2真实图生图洗图工作流lora去除AI油腻味，_1958429494354853889.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_76

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/WAN2.2低噪模型重绘极速洗图工作流_1969774653545848833.json、图片生成/图生图/Wan2.1 图生图洗图+修复工作流_1945503532646637569.json、图片生成/图生图/Wan2.2写实洗图工作流_1957018598755721218.json、图片生成/图生图/Wan2.2真实图生图洗图工作流lora去除AI油腻味，_1958429494354853889.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：99%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LayerUtility: PurgeVRAM` —— 2/4 个有
- `ApplySageAttention` —— 1/4 个有
- `DeepTranslatorTextNode` —— 1/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `ImageConcanate` —— 1/4 个有
- `ImageConcatMulti` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `easy float` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 10 | 4 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 3.5 | 4 | 33% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 50% |
| 重绘幅度 | 0.225 | 0.1 - 0.5 | 4 | 44% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 10，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3.5，4 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 50%
- 重绘幅度 中位数 0.225，观测区间 0.1 - 0.5，4 个样本，取值分散，一致性仅 44%
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
