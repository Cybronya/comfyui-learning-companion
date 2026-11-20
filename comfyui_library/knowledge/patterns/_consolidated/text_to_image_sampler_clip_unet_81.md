---
name: text_to_image_sampler_clip_unet_81
type: Text To Image
frequency: 9
level: moderate
coverage: 0.900667
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/z_mage+古风_lora直出高清图_2001669410228170753.json, 图片生成/文生图/千问qwen-2512文生图（自定义尺寸）_2083196882171547649.json, 图片生成/文生图/千问文生图4步加速工作流_2011421425135001601.json, 图片生成/文生图/千问文生图工作流_1992469322945851393.json, 图片生成/文生图/千问文生图工作流_2003750459162673154.json, 图片生成/文生图/原神风格文生图场景设计_2100396348150472705.json, 图片生成/文生图/文生图_2110627225245671426.json, 图片生成/文生图/潦草线条铅笔画_2017271179677016065.json, 图片生成/文生图/绝区零风格文生图场景设计_2100441031195062274.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_81

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/文生图/z_mage+古风_lora直出高清图_2001669410228170753.json、图片生成/文生图/千问qwen-2512文生图（自定义尺寸）_2083196882171547649.json、图片生成/文生图/千问文生图4步加速工作流_2011421425135001601.json、图片生成/文生图/千问文生图工作流_1992469322945851393.json、图片生成/文生图/千问文生图工作流_2003750459162673154.json…）

- **类型**：Text To Image
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 8/9 个有
- `LoraLoaderModelOnly` —— 6/9 个有
- `PreviewImage` —— 5/9 个有
- `ModelSamplingAuraFlow` —— 3/9 个有
- `PrimitiveStringMultiline` —— 2/9 个有
- `TextEncodeQwenImageEditPlus` —— 2/9 个有
- `UpscaleModelLoader` —— 2/9 个有
- `DyPE_FLUX` —— 1/9 个有
- `JjkText` —— 1/9 个有
- `Text Concatenate` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 6 - 35 | 9 | 36% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 9 | 44% |
| 采样算法 | euler | - | 9 | 89% |
| 调度器 | simple | - | 9 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |
| 宽度 | 1280 | 720 - 1536 | 9 | 76% |
| 高度 | 1024 | 720 - 1472 | 9 | 75% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 6 - 35，9 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，9 个样本，取值分散，一致性仅 44%
- 采样算法 最常用 euler，9 个样本，一致性 89%
- 调度器 最常用 simple，9 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
- 宽度 中位数 1280，观测区间 720 - 1536，9 个样本
- 高度 中位数 1024，观测区间 720 - 1472，9 个样本
