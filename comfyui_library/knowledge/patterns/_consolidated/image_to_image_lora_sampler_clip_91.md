---
name: image_to_image_lora_sampler_clip_91
type: Image To Image
frequency: 5
level: strong
coverage: 0.7204
common_nodes: [AutoCropFaces, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, FaceAlign, FaceAnalysisModels, FluxGuidance, FluxKontextImageScale, Image Paste Crop, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, ReferenceLatent, SaveImage, TeaCache, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [平台全量/flux-kontext-新一代换脸技术-高精度换脸_1953407816914665473.json, 平台全量/换脸升级版100%相同脸型电商换脸工作流_1957403965182898177.json, 数字人/数字人/flux-kontext 高精度换脸工作流-许老师版_1974147774952378370.json, 数字人/数字人/flux-kontext 高精度换脸工作流_1948653600412184578.json, 数字人/数字人/高精度换脸工作流_1973604036207316994.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_91

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/flux-kontext-新一代换脸技术-高精度换脸_1953407816914665473.json、平台全量/换脸升级版100%相同脸型电商换脸工作流_1957403965182898177.json、数字人/数字人/flux-kontext 高精度换脸工作流-许老师版_1974147774952378370.json、数字人/数字人/flux-kontext 高精度换脸工作流_1948653600412184578.json、数字人/数字人/高精度换脸工作流_1973604036207316994.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：72%

## 共有节点

全部 5 个 workflow 都包含：
- `AutoCropFaces`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `FaceAlign`
- `FaceAnalysisModels`
- `FluxGuidance`
- `FluxKontextImageScale`
- `Image Paste Crop`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `ReferenceLatent`
- `SaveImage`
- `TeaCache`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageStitch` —— 4/5 个有
- `GetNode` —— 3/5 个有
- `SetNode` —— 3/5 个有
- `CR Text` —— 1/5 个有
- `ImageSmartSharpen+` —— 1/5 个有
- `Int` —— 1/5 个有
- `easy convertAnything` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 5 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
