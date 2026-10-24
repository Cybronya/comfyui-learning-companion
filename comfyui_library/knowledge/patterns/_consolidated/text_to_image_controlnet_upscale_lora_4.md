---
name: text_to_image_controlnet_upscale_lora_4
type: Text To Image
frequency: 4
level: strong
coverage: 0.905
common_nodes: [CLIPTextEncode, CannyEdgePreprocessor, ControlNetApplyAdvanced, ControlNetLoader, DualCLIPLoader, EmptyLatentImage, GetImageSize_, ImageResize+, KSampler, LoadImage, LoraLoaderModelOnly, PreviewImage, SaveImage, SetUnionControlNetType, UNETLoader, UltimateSDUpscale, UpscaleModelLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX线稿上色 逼真细节 减少AI感_1921726181299912706.json, 图片生成/图生图/FLUX线稿上色｜真细节 减少AI感_1921800485895077889.json, 图片生成/图生图/kontext dev 线稿上色_1948257307990863873.json, 图片生成/图生图/连环画线稿上色_1970615580032200706.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_upscale_lora_4

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/FLUX线稿上色 逼真细节 减少AI感_1921726181299912706.json、图片生成/图生图/FLUX线稿上色｜真细节 减少AI感_1921800485895077889.json、图片生成/图生图/kontext dev 线稿上色_1948257307990863873.json、图片生成/图生图/连环画线稿上色_1970615580032200706.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CannyEdgePreprocessor`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `DualCLIPLoader`
- `EmptyLatentImage`
- `GetImageSize_`
- `ImageResize+`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `SaveImage`
- `SetUnionControlNetType`
- `UNETLoader`
- `UltimateSDUpscale`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAELoader`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.6 | 0.6 - 0.9 | 4 | 81% |
| 宽度 | 768 | 768 - 768 | 4 | 100% |
| 高度 | 1024 | 1024 - 1024 | 4 | 100% |
| 采样步数 | 25 | 25 - 25 | 4 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | normal | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.6，观测区间 0.6 - 0.9，4 个样本，取值集中（一致性 81%）
- 宽度 中位数 768，观测区间 768 - 768，4 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，4 个样本，取值集中（一致性 100%）
- 采样步数 中位数 25，观测区间 25 - 25，4 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 normal，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
