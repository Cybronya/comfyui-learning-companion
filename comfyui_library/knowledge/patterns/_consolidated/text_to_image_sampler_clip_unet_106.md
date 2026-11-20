---
name: text_to_image_sampler_clip_unet_106
type: Text To Image
frequency: 7
level: moderate
coverage: 0.961714
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Magic-Wan-Image 现实生图_1990458117420978177.json, 图片生成/文生图/Magic-Wan-V2加速文生图_1991141173844639745.json, 图片生成/文生图/Magic-Wan-V2文生图_1990870633426919425.json, 图片生成/文生图/krea2 turbo 写实人像 超绝身材 MJ风格滤镜_2093335241376223233.json, 图片生成/文生图/krea2_写实人像_超绝身材_MJ风格滤镜_2093883637514194945.json, 图片生成/文生图/krea2_写实人像_超绝身材_MJ风格滤镜_2093905614782160897.json, 图片生成/文生图/wan2.2高阶文生图_1950437362914516993.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_106

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Magic-Wan-Image 现实生图_1990458117420978177.json、图片生成/文生图/Magic-Wan-V2加速文生图_1991141173844639745.json、图片生成/文生图/Magic-Wan-V2文生图_1990870633426919425.json、图片生成/文生图/krea2 turbo 写实人像 超绝身材 MJ风格滤镜_2093335241376223233.json、图片生成/文生图/krea2_写实人像_超绝身材_MJ风格滤镜_2093883637514194945.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 5/7 个有
- `Seed (rgthree)` —— 5/7 个有
- `ModelSamplingSD3` —— 4/7 个有
- `CompressImages` —— 3/7 个有
- `easy cleanGpuUsed` —— 2/7 个有
- `easy promptLine` —— 2/7 个有
- `LoraLoader` —— 1/7 个有
- `RH_Translator` —— 1/7 个有
- `ShowText|pysssss` —— 1/7 个有
- `UnetLoaderGGUF` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |
| 宽度 | 1080 | 768 - 1152 | 7 | 81% |
| 高度 | 1536 | 1376 - 1920 | 7 | 88% |
| 采样步数 | 10 | 4 - 25 | 7 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 57% |
| 调度器 | simple | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1080，观测区间 768 - 1152，7 个样本，取值集中（一致性 81%）
- 高度 中位数 1536，观测区间 1376 - 1920，7 个样本，取值集中（一致性 88%）
- 采样步数 中位数 10，观测区间 4 - 25，7 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 57%
- 调度器 最常用 simple，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
