---
name: text_to_image_sampler_clip_unet_139
type: Text To Image
frequency: 4
level: strong
coverage: 0.9615
common_nodes: [ApplyPulidFlux, CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptyLatentImage, KSampler, LoadImage, PulidFluxInsightFaceLoader, PulidFluxModelLoader, RH_Translator, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/Flux Krea 面部参考｜Pulid 技术_1951120433343082498.json, 图片生成/文生图/Flux+Krea 面部参考生图pulid_1951107074921050113.json, 图片生成/文生图/flux pulid 文生图 换脸 lora_1931578931458322433.json, 图片生成/文生图/批量文生图+换脸_1914135646209015810.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_139

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux Krea 面部参考｜Pulid 技术_1951120433343082498.json、图片生成/文生图/Flux+Krea 面部参考生图pulid_1951107074921050113.json、图片生成/文生图/flux pulid 文生图 换脸 lora_1931578931458322433.json、图片生成/文生图/批量文生图+换脸_1914135646209015810.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `ApplyPulidFlux`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `PulidFluxInsightFaceLoader`
- `PulidFluxModelLoader`
- `RH_Translator`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `PulidFluxEvaClipLoader` —— 3/4 个有
- `FluxGuidance` —— 2/4 个有
- `ImageScaleDownToSize` —— 2/4 个有
- `LoraLoaderModelOnly` —— 2/4 个有
- `VAEEncode` —— 2/4 个有
- `easy imageConcat` —— 2/4 个有
- `Bjornulf_ShowStringText` —— 1/4 个有
- `ImageResize+` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `PulidEvaClipLoader` —— 1/4 个有
- `RandomPrompt` —— 1/4 个有
- `SUPIR_Upscale` —— 1/4 个有
- `ShowText|pysssss` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 812 | 720 - 1024 | 4 | 85% |
| 高度 | 1240 | 1024 - 1280 | 4 | 91% |
| 采样步数 | 20 | 20 - 25 | 4 | 90% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 812，观测区间 720 - 1024，4 个样本，取值集中（一致性 85%）
- 高度 中位数 1240，观测区间 1024 - 1280，4 个样本，取值集中（一致性 91%）
- 采样步数 中位数 20，观测区间 20 - 25，4 个样本，取值集中（一致性 90%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
