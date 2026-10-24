---
name: text_to_image_sampler_clip_unet_30
type: Text To Image
frequency: 14
level: weak
coverage: 0.800286
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, PreviewAny, PrimitiveStringMultiline, SaveImage, TextGenerate, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/文生图_krea2_2071423975636426754.json, 图片生成/图生图/（贞贞版-Raw Lora 11500）Krea2 Turbo文生图V1_2073803035968622594.json, 图片生成/文生图/5.Krea2 文生图_2083469098800996354.json, 图片生成/文生图/KREA2_LORA人像工作流_2078646318087630849.json, 图片生成/文生图/Krea-2_ 文生图_2095794360649601025.json, 图片生成/文生图/Krea-2文生图官方版｜高质量图像生成工作流_2095956990584512513.json, 图片生成/文生图/Krea-2文生图工作流｜写实质感出图效果稳定可靠_2107695970124386305.json, 图片生成/文生图/Krea2 Turbo极速文生图 API写实人像高质量生成_2099221894967947265.json, 图片生成/文生图/Moss-image Base 基础文生图｜轻量快速出图首选_2112407813287931906.json, 图片生成/文生图/Moss-image Base 文生图入门款｜极简参数秒上手_2112420853316153345.json, 图片生成/文生图/Moss-image+Base 文生图带反推｜提示词一键获取_2112453139499667458.json, 图片生成/文生图/Moss-image+Sft 文生图反推版｜反推提示词更准_2112461263623254018.json, 图片生成/文生图/QWen2.1文生图工作流｜千问模型文字生图轻松创作_2106996835603800065.json, 图片生成/文生图/Qwen 2.1文生图工作流，高质量文本到图像生成方案_2107183009446326274.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_30

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/图生图/文生图_krea2_2071423975636426754.json、图片生成/图生图/（贞贞版-Raw Lora 11500）Krea2 Turbo文生图V1_2073803035968622594.json、图片生成/文生图/5.Krea2 文生图_2083469098800996354.json、图片生成/文生图/KREA2_LORA人像工作流_2078646318087630849.json、图片生成/文生图/Krea-2_ 文生图_2095794360649601025.json…）

- **类型**：Text To Image
- **样本数**：14
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 14 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `SaveImage`
- `TextGenerate`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 13/14 个有
- `LoraLoaderModelOnly` —— 13/14 个有
- `PrimitiveBoolean` —— 13/14 个有
- `ResolutionSelector` —— 12/14 个有
- `JjkText` —— 9/14 个有
- `solarL_SaveImagesToZip` —— 9/14 个有
- `孤海注释` —— 9/14 个有
- `ConditioningZeroOut` —— 8/14 个有
- `StringConcatenate` —— 8/14 个有
- `EmptyFlux2LatentImage` —— 4/14 个有
- `CR Prompt Text` —— 3/14 个有
- `Int` —— 2/14 个有
- `PrimitiveInt` —— 2/14 个有
- `QwenImage21Cache` —— 2/14 个有
- `TextEncodeQwenImage21` —— 2/14 个有
- `PlaySound|pysssss` —— 1/14 个有
- `Power Lora Loader (rgthree)` —— 1/14 个有
- `TextConcat` —— 1/14 个有
- `easy positive` —— 1/14 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 10 | 14 | 61% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 14 | 48% |
| 采样算法 | er_sde | - | 14 | 64% |
| 调度器 | beta | - | 14 | 64% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |
| 宽度 | 80 | 80 - 1024 | 14 | 0% |
| 高度 | 80 | 80 - 1024 | 14 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 16/14 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 10，14 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，14 个样本，取值分散，一致性仅 48%
- 采样算法 最常用 er_sde，14 个样本，一致性 64%
- 调度器 最常用 beta，14 个样本，一致性 64%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1024，14 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1024，14 个样本，取值分散，一致性仅 0%
- 高发问题（16/14 个样本）：Steps较低可能导致细节不足
