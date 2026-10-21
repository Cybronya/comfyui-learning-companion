---
name: text_to_image_lora_sampler_clip_143
type: Text To Image
frequency: 8
level: weak
coverage: 0.98
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2_反推生图_自动尺寸_2087151855494328321.json, 图片生成/文生图/Krea2动漫人物写实复古风工作流_2073834007481110529.json, 图片生成/文生图/Krea2图图工作流_2072525906350006273.json, 图片生成/文生图/Krea2图图文生图工作流_2095107374737616898.json, 图片生成/文生图/Krea2文生图工作流_2089571875075747842.json, 图片生成/文生图/Qwen Image 2512 文生图_2011450632992989185.json, 图片生成/文生图/Qwen-Image-2.1_文生图+4步加速_2103505307195502594.json, 图片生成/文生图/Z-image建筑文生图工作流_1993985159852654594.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_143

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/Krea2_反推生图_自动尺寸_2087151855494328321.json、图片生成/文生图/Krea2动漫人物写实复古风工作流_2073834007481110529.json、图片生成/文生图/Krea2图图工作流_2072525906350006273.json、图片生成/文生图/Krea2图图文生图工作流_2095107374737616898.json、图片生成/文生图/Krea2文生图工作流_2089571875075747842.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 7/8 个有
- `CR Text` —— 3/8 个有
- `AILab_QwenVL` —— 2/8 个有
- `LoadImage` —— 2/8 个有
- `PreviewImage` —— 2/8 个有
- `GetImageSize+` —— 1/8 个有
- `ImageScaleToTotalPixels` —— 1/8 个有
- `ModelAttentionBackend` —— 1/8 个有
- `SaveImageAdvanced` —— 1/8 个有
- `Text Concatenate` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 6 - 30 | 8 | 38% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 8 | 28% |
| 采样算法 | er_sde | - | 8 | 62% |
| 调度器 | simple | - | 8 | 88% |
| 重绘幅度 | 1 | 0.58 - 1 | 8 | 85% |
| 宽度 | 1080 | 512 - 2048 | 8 | 53% |
| 高度 | 1360 | 512 - 1920 | 8 | 59% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 6 - 30，8 个样本，取值分散，一致性仅 38%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，8 个样本，取值分散，一致性仅 28%
- 采样算法 最常用 er_sde，8 个样本，一致性 62%
- 调度器 最常用 simple，8 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 0.58 - 1，8 个样本，取值集中（一致性 85%）
- 宽度 中位数 1080，观测区间 512 - 2048，8 个样本
- 高度 中位数 1360，观测区间 512 - 1920，8 个样本
- 高发问题（4/8 个样本）：Steps较低可能导致细节不足
