---
name: image_to_image_lora_sampler_clip_53
type: Image To Image
frequency: 5
level: strong
coverage: 0.977
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FluxGuidance, KSampler, LoadImage, LoraLoaderModelOnly, ReferenceLatent, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/KONTEXT单图可更换lora工作流_1950619095806971905.json, 图片生成/图生图/Kontext  模特服装展示｜试穿_1942401666282893314.json, 图片生成/图生图/Kontext [dev] 多图融合｜多物体融合_1939513365821833217.json, 图片生成/图生图/Kontext dev 人物衣服试穿｜虚拟试穿_1939656115514679298.json, 图片生成/图生图/Kontext-Relighting-重新打光-实现艺术照打光自由V1_2029902628368420865.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_53

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/KONTEXT单图可更换lora工作流_1950619095806971905.json、图片生成/图生图/Kontext  模特服装展示｜试穿_1942401666282893314.json、图片生成/图生图/Kontext [dev] 多图融合｜多物体融合_1939513365821833217.json、图片生成/图生图/Kontext dev 人物衣服试穿｜虚拟试穿_1939656115514679298.json、图片生成/图生图/Kontext-Relighting-重新打光-实现艺术照打光自由V1_2029902628368420865.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FluxGuidance`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ReferenceLatent`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 3/5 个有
- `ImageConcatMulti` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 3/5 个有
- `easy imageSize` —— 3/5 个有
- `ConstrainImage|pysssss` —— 2/5 个有
- `Image Comparer (rgthree)` —— 2/5 个有
- `FluxKontextImageScale` —— 1/5 个有
- `GLM_Translation_Text` —— 1/5 个有
- `Text _O` —— 1/5 个有
- `UltimateSDUpscale` —— 1/5 个有
- `UpscaleModelLoader` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 25 | 5 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 25，5 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
