---
name: text_to_image_controlnet_sampler_clip_19
type: Text To Image
frequency: 3
level: moderate
coverage: 0.644667
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, EmptyLatentImage, GetNode, KSampler, LoadImage, ModelPatchLoader, ModelSamplingAuraFlow, PreviewImage, QwenImageDiffsynthControlnet, SaveImage, SetNode, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/千问图生图 【小即梦你懂的~】_1959580226474946562.json, 图片生成/文生图/Controlnet 控制 Z-image_2018207991035596801.json, 图片生成/文生图/Z-IMAGE_ControlNet控制_1996388619596210177.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/千问图生图 【小即梦你懂的~】_1959580226474946562.json、图片生成/文生图/Controlnet 控制 Z-image_2018207991035596801.json、图片生成/文生图/Z-IMAGE_ControlNet控制_1996388619596210177.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `EmptyLatentImage`
- `GetNode`
- `KSampler`
- `LoadImage`
- `ModelPatchLoader`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `QwenImageDiffsynthControlnet`
- `SaveImage`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 2/3 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/3 个有
- `Anything Everywhere` —— 1/3 个有
- `Anything Everywhere3` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `LoraLoaderModelOnly` —— 1/3 个有
- `easy imageConcat` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1536 | 512 - 1536 | 3 | 60% |
| 高度 | 1024 | 512 - 1024 | 3 | 72% |
| 采样步数 | 10 | 10 - 20 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | euler_ancestral | - | 3 | 67% |
| 调度器 | bong_tangent | - | 3 | 33% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1536，观测区间 512 - 1536，3 个样本
- 高度 中位数 1024，观测区间 512 - 1024，3 个样本
- 采样步数 中位数 10，观测区间 10 - 20，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 euler_ancestral，3 个样本，一致性 67%
- 调度器 最常用 bong_tangent，3 个样本，一致性 33%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
