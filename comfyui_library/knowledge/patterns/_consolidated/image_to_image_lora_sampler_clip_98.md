---
name: image_to_image_lora_sampler_clip_98
type: Image To Image
frequency: 3
level: strong
coverage: 0.801333
common_nodes: [CLIPLoader, CLIPTextEncode, ColorMatch, ConditioningZeroOut, EmptyFlux2LatentImage, Image Comparer (rgthree), KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, 图像缩放V2_孤海]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/flux-2-klein全家桶系列-2（编辑式-局部重绘）_2039512266135052289.json, 图片生成/图生图/flux-2-klein全家桶系列-4（ 多角度转换流）_2044609507912851458.json, 图片生成/图生图/flux-2-klein全家桶系列6（图像扩展流）_2045850796675305474.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_98

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/flux-2-klein全家桶系列-2（编辑式-局部重绘）_2039512266135052289.json、图片生成/图生图/flux-2-klein全家桶系列-4（ 多角度转换流）_2044609507912851458.json、图片生成/图生图/flux-2-klein全家桶系列6（图像扩展流）_2045850796675305474.json）

- **类型**：Image To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：80%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ColorMatch`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `图像缩放V2_孤海`

**可变部分**（部分 workflow 才有）：
- `DrawMaskOnImage` —— 2/3 个有
- `GetNode` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `CR Prompt Text` —— 1/3 个有
- `CR Text Concatenate` —— 1/3 个有
- `ImagePadForOutpaint` —— 1/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `PlaySound|pysssss` —— 1/3 个有
- `QwenMultiangleCameraNode` —— 1/3 个有
- `Text` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（3/3 个样本）：Steps较低可能导致细节不足
