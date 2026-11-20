---
name: text_to_image_ipadapter_sampler_clip_3
type: Text To Image
frequency: 2
level: weak
coverage: 0.9285
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, IPAdapter, IPAdapterUnifiedLoader, KSampler, LoadImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/comfyui_career_autodress_img2img222_1994612041421819905.json, 平台全量/彩瓷仙子_1788477050340831233.json]
source: knowledge_consolidation
---

# text_to_image_ipadapter_sampler_clip_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/comfyui_career_autodress_img2img222_1994612041421819905.json、平台全量/彩瓷仙子_1788477050340831233.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `IPAdapter`
- `IPAdapterUnifiedLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageBatch` —— 1/2 个有
- `LmcqDeepGen` —— 1/2 个有
- `LmcqDeepLoader` —— 1/2 个有
- `LoraLoader` —— 1/2 个有
- `ShowText|pysssss` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 34 | - | 2 | 88% |
| Prompt 约束强度(CFG) | 5.4 | - | 2 | 70% |
| 采样算法 | dpmpp_2m | - | 2 | 100% |
| 调度器 | karras | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 992 | - | 2 | 97% |
| 高度 | 1088 | - | 2 | 94% |
| LoRA 模型强度 | 0.7 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 34，样本不足，未给区间，2 个样本，取值集中（一致性 88%）
- Prompt 约束强度(CFG) 中位数 5.4，样本不足，未给区间，2 个样本
- 采样算法 最常用 dpmpp_2m，2 个样本，一致性 100%
- 调度器 最常用 karras，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 992，样本不足，未给区间，2 个样本，取值集中（一致性 97%）
- 高度 中位数 1088，样本不足，未给区间，2 个样本，取值集中（一致性 94%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
