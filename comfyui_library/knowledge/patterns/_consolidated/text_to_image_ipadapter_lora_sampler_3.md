---
name: text_to_image_ipadapter_lora_sampler_3
type: Text To Image
frequency: 3
level: moderate
coverage: 0.953
common_nodes: [CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, EmptyLatentImage, IPAdapterFaceID, IPAdapterInsightFaceLoader, IPAdapterModelLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/【遇见AI】ipadapter风格迁移功能全讲解_2018229864947523585.json, 图片生成/文生图/WH-AI-Studio-IPAdapter文生图-换脸-根据人脸文生图_2020112202174308353.json, 平台全量/IPAdapter换脸_1978028146278674434.json]
source: knowledge_consolidation
---

# text_to_image_ipadapter_lora_sampler_3

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/【遇见AI】ipadapter风格迁移功能全讲解_2018229864947523585.json、图片生成/文生图/WH-AI-Studio-IPAdapter文生图-换脸-根据人脸文生图_2020112202174308353.json、平台全量/IPAdapter换脸_1978028146278674434.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncode`
- `CLIPVisionLoader`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `IPAdapterFaceID`
- `IPAdapterInsightFaceLoader`
- `IPAdapterModelLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `IPAdapterAdvanced` —— 1/3 个有
- `IPAdapterCombineEmbeds` —— 1/3 个有
- `IPAdapterEmbeds` —— 1/3 个有
- `IPAdapterEncoder` —— 1/3 个有
- `IPAdapterUnifiedLoader` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有
- `ImageScale` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 720 | 512 - 768 | 3 | 83% |
| 高度 | 768 | 512 - 1280 | 3 | 63% |
| 采样步数 | 30 | 20 - 30 | 3 | 82% |
| Prompt 约束强度(CFG) | 6 | 6 - 8 | 3 | 86% |
| 采样算法 | dpmpp_2m_sde | - | 3 | 67% |
| 调度器 | karras | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 720，观测区间 512 - 768，3 个样本，取值集中（一致性 83%）
- 高度 中位数 768，观测区间 512 - 1280，3 个样本
- 采样步数 中位数 30，观测区间 20 - 30，3 个样本，取值集中（一致性 82%）
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 8，3 个样本，取值集中（一致性 86%）
- 采样算法 最常用 dpmpp_2m_sde，3 个样本，一致性 67%
- 调度器 最常用 karras，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
