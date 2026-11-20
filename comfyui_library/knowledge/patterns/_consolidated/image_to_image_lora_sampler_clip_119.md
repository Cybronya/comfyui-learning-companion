---
name: image_to_image_lora_sampler_clip_119
type: Image To Image
frequency: 3
level: strong
coverage: 0.938
common_nodes: [CLIPLoader, CLIPTextEncode, CannyEdgePreprocessor, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/草扎草编工艺_灯具设计_斗笠型_2098035544990244865.json, 图片生成/文生图/草扎草编工艺_灯具设计_灯笼型_2098035451851530241.json, 图片生成/文生图/草扎草编工艺_灯具设计_鱼篓型_2098023963254419458.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_119

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/草扎草编工艺_灯具设计_斗笠型_2098035544990244865.json、图片生成/文生图/草扎草编工艺_灯具设计_灯笼型_2098035451851530241.json、图片生成/文生图/草扎草编工艺_灯具设计_鱼篓型_2098023963254419458.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CannyEdgePreprocessor`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 24 | 3 | 91% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 0.95 | 0.95 - 0.95 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 24，3 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 0.95，观测区间 0.95 - 0.95，3 个样本，取值集中（一致性 100%）
