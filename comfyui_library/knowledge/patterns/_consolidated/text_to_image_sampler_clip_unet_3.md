---
name: text_to_image_sampler_clip_unet_3
type: Text To Image
frequency: 11
level: weak
coverage: 0.814727
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/1903742090277195777.json, 图片生成/文生图/1911034174755799042.json, 图片生成/文生图/1988965178039480322.json, 图片生成/文生图/Krea-2_ 文生图_2095794360649601025.json, 图片生成/文生图/QWen2.1文生图工作流｜千问模型文字生图轻松创作_2106996835603800065.json, 图片生成/文生图/Qwen 2.1文生图4步加速版｜快节奏出图不影响质量_2103063918653558786.json, 图片生成/文生图/Qwen 2.1文生图工作流，高质量文本到图像生成方案_2107183009446326274.json, 图片生成/文生图/Qwen Image 2.1 PE多宫格生图｜一张出九宫排版素材_2103032143940243457.json, 图片生成/文生图/Qwen Image 2.1 PE文生图，提示词增强高质量文本到图像生成工作流_2103222827108364290.json, 图片生成/文生图/Qwen Image 2.1 V2文生图，文本到图像生成升级版本工作流_2103243206614937601.json, 图片生成/文生图/image_krea2_turbo_t2i_2099207878002429953.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_3

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/1903742090277195777.json、图片生成/文生图/1911034174755799042.json、图片生成/文生图/1988965178039480322.json、图片生成/文生图/Krea-2_ 文生图_2095794360649601025.json、图片生成/文生图/QWen2.1文生图工作流｜千问模型文字生图轻松创作_2106996835603800065.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ResolutionSelector` —— 9/11 个有
- `LoraLoaderModelOnly` —— 8/11 个有
- `ComfySwitchNode` —— 7/11 个有
- `PrimitiveStringMultiline` —— 7/11 个有
- `JjkText` —— 6/11 个有
- `PreviewAny` —— 6/11 个有
- `TextEncodeQwenImage21` —— 6/11 个有
- `TextGenerate` —— 6/11 个有
- `solarL_SaveImagesToZip` —— 6/11 个有
- `孤海注释` —— 6/11 个有
- `CR Prompt Text` —— 5/11 个有
- `ConditioningZeroOut` —— 5/11 个有
- `QwenImage21Cache` —— 5/11 个有
- `PrimitiveBoolean` —— 4/11 个有
- `PrimitiveInt` —— 4/11 个有
- `StringConcatenate` —— 4/11 个有
- `QwenPERewriteT8` —— 3/11 个有
- `easy cleanGpuUsed` —— 3/11 个有
- `easy showAnything` —— 3/11 个有
- `RegexExtract` —— 1/11 个有
- `SaveImageAdvanced` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1024 | 11 | 5% |
| 高度 | 80 | 80 - 1536 | 11 | 0% |
| 采样步数 | 4 | 4 - 9 | 11 | 61% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 11 | 40% |
| 采样算法 | er_sde | - | 11 | 55% |
| 调度器 | beta | - | 11 | 55% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 12/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1024，11 个样本，取值分散，一致性仅 5%
- 高度 中位数 80，观测区间 80 - 1536，11 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 9，11 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，11 个样本，取值分散，一致性仅 40%
- 采样算法 最常用 er_sde，11 个样本，一致性 55%
- 调度器 最常用 beta，11 个样本，一致性 55%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（12/11 个样本）：Steps较低可能导致细节不足
