---
name: text_to_image_sampler_clip_unet_153
type: Text To Image
frequency: 5
level: moderate
coverage: 0.847
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/光影溶图合成-千问模型PLUS_1972274586048000001.json, 平台全量/图片多角度、多视角编辑工作流_2036688999208718338.json, 平台全量/多角度分镜生成(产品_摄影_物体)_2010339460604497922.json, 平台全量/多角度分镜生成_2012122697576226818.json, 平台全量/手动调整场景视角_2010530646023741442.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_153

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/光影溶图合成-千问模型PLUS_1972274586048000001.json、平台全量/图片多角度、多视角编辑工作流_2036688999208718338.json、平台全量/多角度分镜生成(产品_摄影_物体)_2010339460604497922.json、平台全量/多角度分镜生成_2012122697576226818.json、平台全量/手动调整场景视角_2010530646023741442.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `QwenMultiangleCameraNode` —— 4/5 个有
- `GetNode` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `easy imageSize` —— 3/5 个有
- `GetImageSize` —— 1/5 个有
- `Int` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有
- `LoraLoader` —— 1/5 个有
- `PreviewImage` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1280 | 1024 - 1280 | 5 | 92% |
| 高度 | 720 | 720 - 1024 | 5 | 84% |
| 采样步数 | 8 | 4 - 20 | 5 | 43% |
| Prompt 约束强度(CFG) | 1 | 1 - 1.5 | 5 | 82% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1280，观测区间 1024 - 1280，5 个样本，取值集中（一致性 92%）
- 高度 中位数 720，观测区间 720 - 1024，5 个样本，取值集中（一致性 84%）
- 采样步数 中位数 8，观测区间 4 - 20，5 个样本，取值分散，一致性仅 43%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1.5，5 个样本，取值集中（一致性 82%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（4/5 个样本）：Steps较低可能导致细节不足
