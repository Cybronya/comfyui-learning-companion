---
name: text_to_image_lora_sampler_clip_201
type: Text To Image
frequency: 9
level: moderate
coverage: 0.952889
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/中文直出一件多图中文直出一件多图_1919003517552361474.json, 图片生成/文生图/Anima 示例工作流_2055183971406884866.json, 图片生成/文生图/Lisa生成器1.0【含8step+基础】_1985898941021659137.json, 图片生成/文生图/Qwen Image 2512文生图_2016788115049947137.json, 图片生成/文生图/Qwen Image 2512文生图_2039178765472899073.json, 图片生成/文生图/Qwen Image 2512文生图_2047443732449988609.json, 图片生成/文生图/Qwen Image 2512文生图_2048284006793351169.json, 图片生成/文生图/Qwen Image 2512文生图_2048288138644164609.json, 图片生成/文生图/Qwen Image 2512文生图_2055456154658066434.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_201

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/中文直出一件多图中文直出一件多图_1919003517552361474.json、图片生成/文生图/Anima 示例工作流_2055183971406884866.json、图片生成/文生图/Lisa生成器1.0【含8step+基础】_1985898941021659137.json、图片生成/文生图/Qwen Image 2512文生图_2016788115049947137.json、图片生成/文生图/Qwen Image 2512文生图_2039178765472899073.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 8/9 个有
- `Int` —— 7/9 个有
- `ImpactSwitch` —— 6/9 个有
- `LoadImage` —— 3/9 个有
- `CompressImages` —— 1/9 个有
- `EmptySD3LatentImage` —— 1/9 个有
- `ImageResizeKJv2` —— 1/9 个有
- `Power Lora Loader (rgthree)` —— 1/9 个有
- `Text Multiline` —— 1/9 个有
- `TextEncodeQwenImageEdit` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 14 | 9 | 77% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 9 | 100% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 78% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 512 | 512 - 896 | 9 | 77% |
| 高度 | 512 | 512 - 1152 | 9 | 62% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 14，9 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 78%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 896，9 个样本
- 高度 中位数 512，观测区间 512 - 1152，9 个样本
- 高发问题（12/9 个样本）：Steps较低可能导致细节不足
