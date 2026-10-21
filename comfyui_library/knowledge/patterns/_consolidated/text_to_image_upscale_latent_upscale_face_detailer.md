---
name: text_to_image_upscale_latent_upscale_face_detailer
type: Text To Image
frequency: 2
level: weak
coverage: 0.726
common_nodes: [CLIPTextEncode, CR Seed, CheckpointLoaderSimple, EmptyLatentImage, FaceDetailer, KSampler, LatentUpscaleBy, LoraLoader, ModelSamplingDiscrete, PreviewImage, SaveImage, UltralyticsDetectorProvider, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/2.5D半写实(CunnyFunky风格)+脸部修复+contorlnet_2094400913845866498.json, 图片生成/文生图/Illustrious半写实(NFFA风格)+CN控制_2094636000302682113.json]
source: knowledge_consolidation
---

# text_to_image_upscale_latent_upscale_face_detailer

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/2.5D半写实(CunnyFunky风格)+脸部修复+contorlnet_2094400913845866498.json、图片生成/文生图/Illustrious半写实(NFFA风格)+CN控制_2094636000302682113.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CR Seed`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `FaceDetailer`
- `KSampler`
- `LatentUpscaleBy`
- `LoraLoader`
- `ModelSamplingDiscrete`
- `PreviewImage`
- `SaveImage`
- `UltralyticsDetectorProvider`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `AV_ControlNetPreprocessor` —— 1/2 个有
- `ControlNetApplyAdvanced` —— 1/2 个有
- `ControlNetLoader` —— 1/2 个有
- `LoadImage` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 0.5 | - | 2 | 60% |
| LoRA 文本强度 | 1 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 1536 | - | 2 | 100% |
| 采样步数 | 20 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 5 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 0.45 | - | 2 | 89% |
| ControlNet 权重 | 0.6 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- LoRA 模型强度 中位数 0.5，样本不足，未给区间，2 个样本
- LoRA 文本强度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1536，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 20，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 0.45，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
