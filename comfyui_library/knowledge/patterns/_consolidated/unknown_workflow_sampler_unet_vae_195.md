---
name: unknown_workflow_sampler_unet_vae_195
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.885286
common_nodes: [BasicScheduler, CLIPLoader, CR Text, EmptyLatentImage, KSamplerSelect, LoadImage, ModelSamplingAuraFlow, SamplerCustom, SaveImage, TextEncodeBooguEdit, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/boogu edit图像编辑_2069677788981981186.json, 图片生成/图生图/boogu edit图像编辑_2070346438869086209.json, 图片生成/图生图/boogu edit图像编辑_2070347722284158977.json, 图片生成/图生图/boogu 图像编辑模式 提示词自动优化版_2083613193791959042.json, 图片生成/图生图/开源图像boogu 图像编辑 提示词自动优化版_2069584129343184898.json, 图片生成/图生图/开源图像悍将boogu 图像编辑模式 提示词自动优化版_2069366511243980802.json, 视频生成/图生视频/开源图像boogu_图像编辑_提示词自动优化版_2116348585221640193.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_195

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/boogu edit图像编辑_2069677788981981186.json、图片生成/图生图/boogu edit图像编辑_2070346438869086209.json、图片生成/图生图/boogu edit图像编辑_2070347722284158977.json、图片生成/图生图/boogu 图像编辑模式 提示词自动优化版_2083613193791959042.json、图片生成/图生图/开源图像boogu 图像编辑 提示词自动优化版_2069584129343184898.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 7 个 workflow 都包含：
- `BasicScheduler`
- `CLIPLoader`
- `CR Text`
- `EmptyLatentImage`
- `KSamplerSelect`
- `LoadImage`
- `ModelSamplingAuraFlow`
- `SamplerCustom`
- `SaveImage`
- `TextEncodeBooguEdit`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `DapaoImageAspectRatioResizeNode` —— 4/7 个有
- `Dapao_LlamaChat` —— 4/7 个有
- `Seed (rgthree)` —— 4/7 个有
- `easy showAnything` —— 4/7 个有
- `孤海注释` —— 4/7 个有
- `GetImageSize` —— 3/7 个有
- `ResizeImageMaskNode` —— 3/7 个有
- `Note Plus (mtb)` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 1024 | 7 | 65% |
| 高度 | 512 | 512 - 1024 | 7 | 65% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 1024，7 个样本
- 高度 中位数 512，观测区间 512 - 1024，7 个样本
