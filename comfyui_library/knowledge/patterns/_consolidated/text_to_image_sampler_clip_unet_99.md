---
name: text_to_image_sampler_clip_unet_99
type: Text To Image
frequency: 7
level: moderate
coverage: 0.968571
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/QWEN千问古风美女_1976489433270755329.json, 图片生成/文生图/Qwen Image 2512 准确文字文生图_2027984052459937793.json, 图片生成/文生图/Qwen Image 2512文生图_2042508621921132546.json, 图片生成/文生图/Qwen2512巨无霸奶美女身材调节_2019041837285117953.json, 图片生成/文生图/Qwen2512日系JK制服少女甜妹_2019053173494779906.json, 图片生成/文生图/Qwen2512梨形完美身材美女_2018952499717218306.json, 图片生成/文生图/Universal text to image_2057220020123561985.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_99

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/QWEN千问古风美女_1976489433270755329.json、图片生成/文生图/Qwen Image 2512 准确文字文生图_2027984052459937793.json、图片生成/文生图/Qwen Image 2512文生图_2042508621921132546.json、图片生成/文生图/Qwen2512巨无霸奶美女身材调节_2019041837285117953.json、图片生成/文生图/Qwen2512日系JK制服少女甜妹_2019053173494779906.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 6/7 个有
- `LatentFrequencyEnhancer_lrzjason` —— 4/7 个有
- `CFGNorm` —— 2/7 个有
- `CompressImages` —— 1/7 个有
- `JjkText` —— 1/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `LoraLoader` —— 1/7 个有
- `TextEncodeQwenImageEditPlus` —— 1/7 个有
- `VAEEncode` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 768 - 1280 | 7 | 81% |
| 高度 | 1024 | 1024 - 1920 | 7 | 75% |
| 采样步数 | 8 | 4 - 16 | 7 | 57% |
| Prompt 约束强度(CFG) | 2 | 1 - 3 | 7 | 54% |
| 采样算法 | euler | - | 7 | 71% |
| 调度器 | simple | - | 7 | 71% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 768 - 1280，7 个样本，取值集中（一致性 81%）
- 高度 中位数 1024，观测区间 1024 - 1920，7 个样本
- 采样步数 中位数 8，观测区间 4 - 16，7 个样本
- Prompt 约束强度(CFG) 中位数 2，观测区间 1 - 3，7 个样本
- 采样算法 最常用 euler，7 个样本，一致性 71%
- 调度器 最常用 simple，7 个样本，一致性 71%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（5/7 个样本）：Steps较低可能导致细节不足
