---
name: unknown_workflow_lora_clip_unet_4
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.981
common_nodes: [CLIPLoader, CLIPTextEncode, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-2511+Zimage人像转夸张画风_2069970171485315074.json, 图片生成/图生图/Qwen-2511+Zimage人像转抽象画风_2067163925694734338.json, 图片生成/图生图/Qwen-2511+Zimage人像转抽象画风_2069224963105714177.json, 图片生成/图生图/Qwen-2511+Zimage人像转抽象画风_2069701534362980354.json, 图片生成/图生图/Qwen-2511+Zimage人像转抽象画风图生图_2069734160117362689.json, 图片生成/图生图/Qwen-2511+Zimage抽象画风_2041336947678908417.json, 图片生成/图生图/Qwen-2511+Zimage抽象画风_2064238909428682753.json, 图片生成/图生图/Qwen-Image-Edit-2511 放大2k_2005875871875563521.json, 图片生成/图生图/Qwen-Image-Edit-2511-Upscale2K_2005851095861788673.json, 图片生成/图生图/Qwen2509 人物姿态精准模仿_2015989123600883713.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_clip_unet_4

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/Qwen-2511+Zimage人像转夸张画风_2069970171485315074.json、图片生成/图生图/Qwen-2511+Zimage人像转抽象画风_2067163925694734338.json、图片生成/图生图/Qwen-2511+Zimage人像转抽象画风_2069224963105714177.json、图片生成/图生图/Qwen-2511+Zimage人像转抽象画风_2069701534362980354.json、图片生成/图生图/Qwen-2511+Zimage人像转抽象画风图生图_2069734160117362689.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSamplerAdvanced` —— 7/10 个有
- `VAEEncode` —— 7/10 个有
- `KSampler` —— 3/10 个有
- `CR SDXL Aspect Ratio` —— 2/10 个有
- `ImageConcanate` —— 2/10 个有
- `Seed (rgthree)` —— 2/10 个有
- `AIO_Preprocessor` —— 1/10 个有
- `EmptySD3LatentImage` —— 1/10 个有
- `GetImageSize` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 10 | 70% |
| Prompt 约束强度(CFG) | 5 | 1 - 8 | 10 | 46% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 10 | 70% |
| 重绘幅度 | simple | - | 10 | 70% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 最常用 randomize，10 个样本，一致性 70%
- Prompt 约束强度(CFG) 中位数 5，观测区间 1 - 8，10 个样本，取值分散，一致性仅 46%
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，10 个样本，一致性 70%
- 重绘幅度 最常用 simple，10 个样本，一致性 70%
