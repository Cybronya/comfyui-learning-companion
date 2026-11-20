---
name: text_to_image_lora_sampler_clip_344
type: Text To Image
frequency: 6
level: strong
coverage: 0.985167
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, FluxGuidance, FluxKontextImageScale, KSampler, LoadImage, LoraLoader, ReferenceLatent, SaveImage, VAEDecode, VAEEncode, VAELoader, easy cleanGpuUsed, easy clearCacheAll]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/一键提取服装白底图 Kontext_2103488451134967809.json, 图片生成/图生图/平铺服装_挂拍服装图转3D立体效果图_2104905928461086722.json, 图片生成/图生图/服装提取平铺图【电商必备】_2043953787542441986.json, 图片生成/图生图/服装提取平铺视图-直出4K-FLUX-Kontext_2097872977068126209.json, 图片生成/图生图/服装提取平铺视图-直出4K-FLUX-Kontext_2099409741830254594.json, 平台全量/服装提取平铺视图-直出4K-FLUX-Kontext_1990787812637224961.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_344

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/一键提取服装白底图 Kontext_2103488451134967809.json、图片生成/图生图/平铺服装_挂拍服装图转3D立体效果图_2104905928461086722.json、图片生成/图生图/服装提取平铺图【电商必备】_2043953787542441986.json、图片生成/图生图/服装提取平铺视图-直出4K-FLUX-Kontext_2097872977068126209.json、图片生成/图生图/服装提取平铺视图-直出4K-FLUX-Kontext_2099409741830254594.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `FluxGuidance`
- `FluxKontextImageScale`
- `KSampler`
- `LoadImage`
- `LoraLoader`
- `ReferenceLatent`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy clearCacheAll`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 5/6 个有
- `SeedVR2LoadDiTModel` —— 5/6 个有
- `SeedVR2LoadVAEModel` —— 5/6 个有
- `SeedVR2VideoUpscaler` —— 5/6 个有
- `easy int` —— 5/6 个有
- `easy imageSize` —— 4/6 个有
- `Int` —— 2/6 个有
- `PreviewImage` —— 2/6 个有
- `CLIPLoader` —— 1/6 个有
- `EmptyFlux2LatentImage` —— 1/6 个有
- `LayerUtility: FluxKontextImageScale` —— 1/6 个有
- `LoraLoaderModelOnly` —— 1/6 个有
- `MemoryCleaner` —— 1/6 个有
- `UNETLoader` —— 1/6 个有
- `YuanColorMatch` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | 1 - 1 | 6 | 100% |
| LoRA 文本强度 | 1 | 1 - 1 | 6 | 100% |
| 采样步数 | 20 | 20 - 20 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | er_sde | - | 6 | 100% |
| 调度器 | beta57 | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 6 | 100% |
| 高度 | 1536 | 1536 - 1536 | 6 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- LoRA 模型强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- LoRA 文本强度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，观测区间 20 - 20，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，6 个样本，一致性 100%
- 调度器 最常用 beta57，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，6 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，观测区间 1536 - 1536，6 个样本，取值集中（一致性 100%）
