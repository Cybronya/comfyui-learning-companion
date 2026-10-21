---
name: text_to_image_lora_sampler_clip_169
type: Text To Image
frequency: 7
level: weak
coverage: 0.789286
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, ConditioningZeroOut, EmptyLatentImage, ImpactSwitch, Int, KSampler, LoraLoaderModelOnly, PlaySound|pysssss, PreviewImage, ResolutionSelector, SaveImage, Seed (rgthree), ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2+多风格插画人像Lora文生图_2084477652022415361.json, 图片生成/文生图/Krea2+多风格插画场景Lora文生图_2085291737651703809.json, 图片生成/文生图/Krea2+官方LORA文生图_2081387893163126786.json, 图片生成/文生图/Krea2多风格插画场景Lora｜文生图经典绘画风10选_2089435469040939010.json, 图片生成/文生图/多风格插画人像Lora文生图｜Krea2现代创意经典绘画风工作流_2087158817585983490.json, 图片生成/文生图/多风格插画人像Lora｜Krea2文生图经典绘画风_2092756714033598465.json, 图片生成/文生图/官方LORA文生图｜Krea2宠物摄影人像写真生成_2092755228268519425.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_169

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Krea2+多风格插画人像Lora文生图_2084477652022415361.json、图片生成/文生图/Krea2+多风格插画场景Lora文生图_2085291737651703809.json、图片生成/文生图/Krea2+官方LORA文生图_2081387893163126786.json、图片生成/文生图/Krea2多风格插画场景Lora｜文生图经典绘画风10选_2089435469040939010.json、图片生成/文生图/多风格插画人像Lora文生图｜Krea2现代创意经典绘画风工作流_2087158817585983490.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `ImpactSwitch`
- `Int`
- `KSampler`
- `LoraLoaderModelOnly`
- `PlaySound|pysssss`
- `PreviewImage`
- `ResolutionSelector`
- `SaveImage`
- `Seed (rgthree)`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 6/7 个有
- `easy promptLine` —— 5/7 个有
- `JjkText` —— 4/7 个有
- `MuyeTextEditOutput` —— 4/7 个有
- `solarL_SaveImagesToZip` —— 4/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 768 | 7 | 9% |
| 高度 | 80 | 80 - 1024 | 7 | 4% |
| 采样步数 | 4 | 4 - 10 | 7 | 55% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 7 | 42% |
| 采样算法 | er_sde | - | 7 | 57% |
| 调度器 | beta | - | 7 | 57% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 768，7 个样本，取值分散，一致性仅 9%
- 高度 中位数 80，观测区间 80 - 1024，7 个样本，取值分散，一致性仅 4%
- 采样步数 中位数 4，观测区间 4 - 10，7 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，7 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 er_sde，7 个样本，一致性 57%
- 调度器 最常用 beta，7 个样本，一致性 57%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（4/7 个样本）：Steps较低可能导致细节不足
