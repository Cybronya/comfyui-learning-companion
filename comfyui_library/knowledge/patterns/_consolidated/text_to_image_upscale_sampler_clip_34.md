---
name: text_to_image_upscale_sampler_clip_34
type: Text To Image
frequency: 3
level: moderate
coverage: 0.889
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, UpscaleModelLoader, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/【遇见AI】放大的5种高级方法-SD放大_2032750596230483969.json, 图片生成/文生图/三重放大细致到毛孔_1934989569676746753.json, 图片生成/文生图/动漫文生图学习duck版_2040649378280513537.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_34

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/【遇见AI】放大的5种高级方法-SD放大_2032750596230483969.json、图片生成/文生图/三重放大细致到毛孔_1934989569676746753.json、图片生成/文生图/动漫文生图学习duck版_2040649378280513537.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `LatentUpscaleBy` —— 2/3 个有
- `UltimateSDUpscale` —— 2/3 个有
- `DuckHideNode` —— 1/3 个有
- `HD UltimateSDUpscale` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `ImageUpscaleWithModel` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 768 | 3 | 80% |
| 高度 | 512 | 432 - 768 | 3 | 75% |
| 采样步数 | 20 | 20 - 25 | 3 | 89% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 3 | 100% |
| 采样算法 | euler | - | 3 | 33% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 1 | 0.5 - 1 | 3 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 768，3 个样本
- 高度 中位数 512，观测区间 432 - 768，3 个样本
- 采样步数 中位数 20，观测区间 20 - 25，3 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 33%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，3 个样本
