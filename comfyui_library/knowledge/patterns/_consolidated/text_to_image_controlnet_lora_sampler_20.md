---
name: text_to_image_controlnet_lora_sampler_20
type: Text To Image
frequency: 2
level: weak
coverage: 0.934
common_nodes: [AIO_Preprocessor, CLIPTextEncode, CannyEdgePreprocessor, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, ImageScaleBy, KSampler, LineArtPreprocessor, LoadImage, LoraLoaderModelOnly, OpenposePreprocessor, PreviewImage, SaveImage, ScribblePreprocessor, VAEDecode, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/Controlnet控制_2006929757698527233.json, 图片生成/图生图/Controlnet控制_2018183964711718914.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_lora_sampler_20

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Controlnet控制_2006929757698527233.json、图片生成/图生图/Controlnet控制_2018183964711718914.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `AIO_Preprocessor`
- `CLIPTextEncode`
- `CannyEdgePreprocessor`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `ImageScaleBy`
- `KSampler`
- `LineArtPreprocessor`
- `LoadImage`
- `LoraLoaderModelOnly`
- `OpenposePreprocessor`
- `PreviewImage`
- `SaveImage`
- `ScribblePreprocessor`
- `VAEDecode`
- `easy imageSize`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.85 | - | 2 | 100% |
| 宽度 | 1024 | - | 2 | 100% |
| 高度 | 768 | - | 2 | 100% |
| 采样步数 | 25 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 100% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.85，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 768，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
