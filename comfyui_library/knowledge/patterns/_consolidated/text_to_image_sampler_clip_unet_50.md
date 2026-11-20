---
name: text_to_image_sampler_clip_unet_50
type: Text To Image
frequency: 12
level: moderate
coverage: 0.988083
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/QWEN千问古风美女_1976489433270755329.json, 图片生成/文生图/Qwen Image 2512 准确文字文生图_2027984052459937793.json, 图片生成/文生图/Qwen Image 2512文生图_2042508621921132546.json, 图片生成/文生图/Qwen2512巨无霸奶美女身材调节_2019041837285117953.json, 图片生成/文生图/Qwen2512文生图基础款_2024281731670482946.json, 图片生成/文生图/Qwen2512日系JK制服少女甜妹_2019053173494779906.json, 图片生成/文生图/Qwen2512日系少女甜妹美女_2019045029121101826.json, 图片生成/文生图/Qwen2512梨形完美身材美女_2018952499717218306.json, 图片生成/文生图/qwen2512大雷甜妹JK制服少女_2018569892831694850.json, 图片生成/文生图/qwenimg2512-文生图_2009674166802321409.json, "图片生成/文生图/全新VAE Z_image_turbo-VAE,加强细节，更高清_2003404331451912194.json", 图片生成/文生图/（贞贞版）Z-image-Kook真实幻想文生图V1_1995736528510922753.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_50

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/QWEN千问古风美女_1976489433270755329.json、图片生成/文生图/Qwen Image 2512 准确文字文生图_2027984052459937793.json、图片生成/文生图/Qwen Image 2512文生图_2042508621921132546.json、图片生成/文生图/Qwen2512巨无霸奶美女身材调节_2019041837285117953.json、图片生成/文生图/Qwen2512文生图基础款_2024281731670482946.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 11/12 个有
- `LatentFrequencyEnhancer_lrzjason` —— 6/12 个有
- `CFGNorm` —— 2/12 个有
- `VAEEncode` —— 2/12 个有
- `CompressImages` —— 1/12 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/12 个有
- `LoraLoader` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1536 | 12 | 77% |
| 高度 | 1360 | 1024 - 1920 | 12 | 74% |
| 采样步数 | 8.5 | 8 - 16 | 12 | 66% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 12 | 46% |
| 采样算法 | euler | - | 12 | 75% |
| 调度器 | simple | - | 12 | 50% |
| 重绘幅度 | 1 | 0.2 - 1 | 12 | 76% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 9/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1536，12 个样本
- 高度 中位数 1360，观测区间 1024 - 1920，12 个样本
- 采样步数 中位数 8.5，观测区间 8 - 16，12 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，12 个样本，取值分散，一致性仅 46%
- 采样算法 最常用 euler，12 个样本，一致性 75%
- 调度器 最常用 simple，12 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，12 个样本
- 高发问题（9/12 个样本）：Steps较低可能导致细节不足
