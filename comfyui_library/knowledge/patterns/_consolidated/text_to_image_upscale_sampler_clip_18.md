---
name: text_to_image_upscale_sampler_clip_18
type: Text To Image
frequency: 4
level: strong
coverage: 0.87975
common_nodes: [CLIPTextEncode, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, UpscaleModelLoader, VAEDecode]
problems: []
missing: [easy imageRemBg, MaskPreview+]
members: [图片生成/文生图/1909573084695986178.json, 图片生成/文生图/SDXL文生图工作流_2101638559093575681.json, 图片生成/文生图/冰雕世界_1792766439749373954.json, 图片生成/文生图/基础CG图片高清放大工作流_2016839532573892610.json]
source: knowledge_consolidation
---

# text_to_image_upscale_sampler_clip_18

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/1909573084695986178.json、图片生成/文生图/SDXL文生图工作流_2101638559093575681.json、图片生成/文生图/冰雕世界_1792766439749373954.json、图片生成/文生图/基础CG图片高清放大工作流_2016839532573892610.json）

- **类型**：Text To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：88%

## 共有节点

全部 4 个 workflow 都包含：
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 3/4 个有
- `LoraLoader` —— 3/4 个有
- `UltimateSDUpscale` —— 2/4 个有
- `VAELoader` —— 2/4 个有
- `LatentPixelScale` —— 1/4 个有
- `MaskPreview+` —— 1/4 个有
- `PreviewImage` —— 1/4 个有
- `easy imageRemBg` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 768 | 4 | 84% |
| 高度 | 896 | 512 - 1024 | 4 | 74% |
| 采样步数 | 30 | 20 - 33 | 4 | 83% |
| Prompt 约束强度(CFG) | 7 | 6.5 - 8 | 4 | 92% |
| 采样算法 | dpmpp_2m_sde | - | 4 | 50% |
| 调度器 | normal | - | 4 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |
| LoRA 模型强度 | 1 | 0.56 - 1 | 3 | 76% |
| LoRA 文本强度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 768，4 个样本，取值集中（一致性 84%）
- 高度 中位数 896，观测区间 512 - 1024，4 个样本
- 采样步数 中位数 30，观测区间 20 - 33，4 个样本，取值集中（一致性 83%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 6.5 - 8，4 个样本，取值集中（一致性 92%）
- 采样算法 最常用 dpmpp_2m_sde，4 个样本，一致性 50%
- 调度器 最常用 normal，4 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- LoRA 模型强度 中位数 1，观测区间 0.56 - 1，3 个样本
- LoRA 文本强度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 这些节点还没有知识卡，系统对它们的理解有限：easy imageRemBg、MaskPreview+
