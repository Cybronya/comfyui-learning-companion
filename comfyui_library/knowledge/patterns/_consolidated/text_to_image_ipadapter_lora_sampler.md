---
name: text_to_image_ipadapter_lora_sampler
type: Text To Image
frequency: 2
level: weak
coverage: 0.963
common_nodes: [CLIPTextEncode, CLIPVisionLoader, CheckpointLoaderSimple, EmptyLatentImage, IPAdapterFaceID, IPAdapterInsightFaceLoader, IPAdapterModelLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/图生图/【遇见AI】ipadapter风格迁移功能全讲解_2018229864947523585.json, 图片生成/文生图/WH-AI-Studio-IPAdapter文生图-换脸-根据人脸文生图_2020112202174308353.json]
source: knowledge_consolidation
---

# text_to_image_ipadapter_lora_sampler

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【遇见AI】ipadapter风格迁移功能全讲解_2018229864947523585.json、图片生成/文生图/WH-AI-Studio-IPAdapter文生图-换脸-根据人脸文生图_2020112202174308353.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
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
- `IPAdapterAdvanced` —— 1/2 个有
- `IPAdapterCombineEmbeds` —— 1/2 个有
- `IPAdapterEmbeds` —— 1/2 个有
- `IPAdapterEncoder` —— 1/2 个有
- `IPAdapterUnifiedLoader` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 616 | - | 2 | 83% |
| 高度 | 896 | - | 2 | 57% |
| 采样步数 | 25 | - | 2 | 80% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 86% |
| 采样算法 | euler | - | 2 | 50% |
| 调度器 | normal | - | 2 | 50% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 616，样本不足，未给区间，2 个样本，取值集中（一致性 83%）
- 高度 中位数 896，样本不足，未给区间，2 个样本
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 80%）
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 86%）
- 采样算法 最常用 euler，2 个样本，一致性 50%
- 调度器 最常用 normal，2 个样本，一致性 50%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
