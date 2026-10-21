---
name: text_to_image_lora_sampler_clip_173
type: Text To Image
frequency: 7
level: weak
coverage: 0.898429
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/anima base v1.0 turbo 极速文生图｜动漫角色热门IP出图_2096834722365263874.json, 图片生成/文生图/anima_basev1.0_turbo_t2i_2057191803308298242.json, 图片生成/文生图/anima_basev1.0_turbo_t2i动漫角色生成｜热门IP文生图_2096656041508425730.json, 视频生成/文生视频/Qwen2512领军模型｜完美中文文生图图生图生成_2090530166060707841.json, 视频生成/文生视频/Qwen2512领军模型｜完美中文文生图图生图生成_2094308048687951873.json, 视频生成/文生视频/千问Qwen2512文生图 中文理解领军模型高质量出图_2098113334959759362.json, 视频生成/文生视频/完美中文理解领军模型｜Qwen2512文生图千问旗舰_2090825263516045313.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_173

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/anima base v1.0 turbo 极速文生图｜动漫角色热门IP出图_2096834722365263874.json、图片生成/文生图/anima_basev1.0_turbo_t2i_2057191803308298242.json、图片生成/文生图/anima_basev1.0_turbo_t2i动漫角色生成｜热门IP文生图_2096656041508425730.json、视频生成/文生视频/Qwen2512领军模型｜完美中文文生图图生图生成_2090530166060707841.json、视频生成/文生视频/Qwen2512领军模型｜完美中文文生图图生图生成_2094308048687951873.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 7 个 workflow 都包含：
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
- `JjkText` —— 6/7 个有
- `solarL_SaveImagesToZip` —— 6/7 个有
- `孤海注释` —— 6/7 个有
- `FluxKontextImageScale` —— 3/7 个有
- `LatentUpscaleBy` —— 3/7 个有
- `SDVN Translate` —— 3/7 个有
- `SeedGenerator` —— 3/7 个有
- `ShowText|pysssss` —— 3/7 个有
- `StringMergeNode` —— 3/7 个有
- `Text Multiline` —— 3/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 7 | 57% |
| Prompt 约束强度(CFG) | 4.5 | 1.5 - 4.5 | 7 | 74% |
| 采样算法 | er_sde | - | 7 | 100% |
| 调度器 | beta | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |
| 宽度 | 80 | 80 - 768 | 7 | 0% |
| 高度 | 80 | 80 - 1152 | 7 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，7 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1.5 - 4.5，7 个样本
- 采样算法 最常用 er_sde，7 个样本，一致性 100%
- 调度器 最常用 beta，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 768，7 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1152，7 个样本，取值分散，一致性仅 0%
- 高发问题（6/7 个样本）：Steps较低可能导致细节不足
