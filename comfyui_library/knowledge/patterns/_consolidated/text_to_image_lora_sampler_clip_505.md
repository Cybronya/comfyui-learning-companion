---
name: text_to_image_lora_sampler_clip_505
type: Text To Image
frequency: 3
level: weak
coverage: 0.78
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, PrimitiveStringMultiline, SaveImage, StringConcatenate, TextEncodeQwenImage21, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/CHIEFAI-千问IMAGE2.1电商换身换头工作流_2108359942859218946.json, 图片生成/图生图/千问IMAGE2.1电商换身换头，图生图模特一键替换_2110824556486287361.json, 视频生成/图生视频/Qwen Image 2.1 Fix 1.0_2.0画质修复 去全能图片G味高频伪细节_2110352689484886017.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_505

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/CHIEFAI-千问IMAGE2.1电商换身换头工作流_2108359942859218946.json、图片生成/图生图/千问IMAGE2.1电商换身换头，图生图模特一键替换_2110824556486287361.json、视频生成/图生视频/Qwen Image 2.1 Fix 1.0_2.0画质修复 去全能图片G味高频伪细节_2110352689484886017.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveStringMultiline`
- `SaveImage`
- `StringConcatenate`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Anything Everywhere` —— 2/3 个有
- `ConditioningZeroOut` —— 2/3 个有
- `Get resolution [Crystools]` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `ReferenceLatent` —— 2/3 个有
- `RegexReplace` —— 2/3 个有
- `VAEEncode` —— 2/3 个有
- `solarL_SaveImagesToZip` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `ComfySwitchNode` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `RegexExtract` —— 1/3 个有
- `SeedNode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 3 | 0% |
| 高度 | 80 | 80 - 1024 | 3 | 0% |
| 采样步数 | 4 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4 - 4.5 | 3 | 95% |
| 采样算法 | er_sde | - | 3 | 67% |
| 调度器 | beta | - | 3 | 67% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4 - 4.5，3 个样本，取值集中（一致性 95%）
- 采样算法 最常用 er_sde，3 个样本，一致性 67%
- 调度器 最常用 beta，3 个样本，一致性 67%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
