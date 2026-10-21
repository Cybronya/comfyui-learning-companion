---
name: text_to_image_controlnet_sampler_clip
type: Text To Image
frequency: 8
level: strong
coverage: 0.957875
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/1920050306917535746.json, 图片生成/文生图/1932442202058715137.json, 图片生成/文生图/1932443425478471681.json, 图片生成/文生图/1932448769386672129.json, 图片生成/文生图/1935504433507651585.json, 图片生成/文生图/1935513540252073985.json, 图片生成/文生图/Controlnet控制_2008470287586693121.json, 图片生成/文生图/SDXL文生图基础工作流_2000486653930110978.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1920050306917535746.json、图片生成/文生图/1932442202058715137.json、图片生成/文生图/1932443425478471681.json、图片生成/文生图/1932448769386672129.json、图片生成/文生图/1935504433507651585.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `VAELoader` —— 5/8 个有
- `PreviewImage` —— 4/8 个有
- `AIO_Preprocessor` —— 3/8 个有
- `CLIPSetLastLayer` —— 2/8 个有
- `SetUnionControlNetType` —— 2/8 个有
- `DualCLIPLoader` —— 1/8 个有
- `Image Comparer (rgthree)` —— 1/8 个有
- `LatentUpscale` —— 1/8 个有
- `Lora Loader Stack (rgthree)` —— 1/8 个有
- `RH_Translator` —— 1/8 个有
- `UNETLoader` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1280 | 8 | 85% |
| 高度 | 1024 | 1024 - 1280 | 8 | 92% |
| ControlNet 权重 | 1 | 0.55 - 1 | 8 | 83% |
| 采样步数 | 20 | 20 - 30 | 8 | 84% |
| Prompt 约束强度(CFG) | 6.5 | 1 - 7 | 8 | 67% |
| 采样算法 | dpmpp_2m | - | 8 | 50% |
| 调度器 | karras | - | 8 | 62% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1280，8 个样本，取值集中（一致性 85%）
- 高度 中位数 1024，观测区间 1024 - 1280，8 个样本，取值集中（一致性 92%）
- ControlNet 权重 中位数 1，观测区间 0.55 - 1，8 个样本，取值集中（一致性 83%）
- 采样步数 中位数 20，观测区间 20 - 30，8 个样本，取值集中（一致性 84%）
- Prompt 约束强度(CFG) 中位数 6.5，观测区间 1 - 7，8 个样本
- 采样算法 最常用 dpmpp_2m，8 个样本，一致性 50%
- 调度器 最常用 karras，8 个样本，一致性 62%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
