---
name: text_to_image_controlnet_sampler_clip
type: Text To Image
frequency: 7
level: strong
coverage: 0.959857
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, EmptyLatentImage, KSampler, LoadImage, SaveImage, VAEDecode]
problems: []
missing: []
members: [图片生成/文生图/1920050306917535746.json, 图片生成/文生图/1932442202058715137.json, 图片生成/文生图/1932443425478471681.json, 图片生成/文生图/1932448769386672129.json, 图片生成/文生图/1935504433507651585.json, 图片生成/文生图/1935513540252073985.json, 视频生成/文生视频/ControlNet预处理器_2016518079005593601.json]
source: knowledge_consolidation
---

# text_to_image_controlnet_sampler_clip

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/1920050306917535746.json、图片生成/文生图/1932442202058715137.json、图片生成/文生图/1932443425478471681.json、图片生成/文生图/1932448769386672129.json、图片生成/文生图/1935504433507651585.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
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
- `PreviewImage` —— 4/7 个有
- `VAELoader` —— 4/7 个有
- `AIO_Preprocessor` —— 2/7 个有
- `CLIPSetLastLayer` —— 2/7 个有
- `GetImageSize` —— 1/7 个有
- `LatentUpscale` —— 1/7 个有
- `SetUnionControlNetType` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1024 | 7 | 80% |
| 高度 | 1024 | 512 - 1024 | 7 | 81% |
| ControlNet 权重 | 1 | 0.55 - 1 | 7 | 83% |
| 采样步数 | 20 | 20 - 20 | 7 | 100% |
| Prompt 约束强度(CFG) | 7 | 5 - 8 | 7 | 86% |
| 采样算法 | dpmpp_2m | - | 7 | 29% |
| 调度器 | karras | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1024，7 个样本
- 高度 中位数 1024，观测区间 512 - 1024，7 个样本，取值集中（一致性 81%）
- ControlNet 权重 中位数 1，观测区间 0.55 - 1，7 个样本，取值集中（一致性 83%）
- 采样步数 中位数 20，观测区间 20 - 20，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 5 - 8，7 个样本，取值集中（一致性 86%）
- 采样算法 最常用 dpmpp_2m，7 个样本，一致性 29%
- 调度器 最常用 karras，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
