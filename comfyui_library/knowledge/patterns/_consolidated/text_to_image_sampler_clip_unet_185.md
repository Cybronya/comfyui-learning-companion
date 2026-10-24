---
name: text_to_image_sampler_clip_unet_185
type: Text To Image
frequency: 3
level: strong
coverage: 0.87
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyLatentImage, KSampler, SaveImage, Seed (rgthree), UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/Z-Image 美女自动扩写文生图_1996110278268010498.json, 图片生成/文生图/Z-Image_Art批量文生图工作流_2018158285647519745.json, 图片生成/文生图/Z-image DetailedEyes Lora权重对比工作流_1994403733771591682.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_185

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Z-Image 美女自动扩写文生图_1996110278268010498.json、图片生成/文生图/Z-Image_Art批量文生图工作流_2018158285647519745.json、图片生成/文生图/Z-image DetailedEyes Lora权重对比工作流_1994403733771591682.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `Seed (rgthree)`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `LayerUtility: PurgeVRAM` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `Text Concatenate` —— 2/3 个有
- `easy promptLine` —— 2/3 个有
- `CR Text Replace` —— 1/3 个有
- `Image Compare (mtb)` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `Qwen3_VQA` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `RH_LLMAPI_Pro_Node` —— 1/3 个有
- `TextListSplit` —— 1/3 个有
- `easy promptConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 10 - 10 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |
| 宽度 | 1080 | 1080 - 1080 | 3 | 100% |
| 高度 | 1920 | 1920 - 1920 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 10，观测区间 10 - 10，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 宽度 中位数 1080，观测区间 1080 - 1080，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1920，观测区间 1920 - 1920，3 个样本，取值集中（一致性 100%）
