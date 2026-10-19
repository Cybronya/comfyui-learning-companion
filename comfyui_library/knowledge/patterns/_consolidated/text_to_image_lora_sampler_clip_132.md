---
name: text_to_image_lora_sampler_clip_132
type: Text To Image
frequency: 7
level: weak
coverage: 0.921857
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Z-Image-瑶光版-适合人像创作_2102648327572647937.json, 图片生成/文生图/Z-Image瑶光版文生图｜人像创作质感出片首选_2104572471079952385.json, 图片生成/文生图/aigc-image-2.5文生图九图连出｜太平风格批量出图_2106953497185972225.json, 图片生成/文生图/千问2.1文生图官方原生架构｜一键出图带海报制作｜新手友好_2104813513557504002.json, 图片生成/文生图/千问2.1白底商品图｜商业摄影级纯白底｜电商主图批量生成_2104808797784072193.json, 图片生成/文生图/场景道具图批量文生图｜布景陈设素材一键出全套_2103107503109263362.json, 图片生成/文生图/文生图AIGC Image 2.5九图工作流，高质量文本到图像生成方案_2107237308658446338.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_132

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/文生图/Z-Image-瑶光版-适合人像创作_2102648327572647937.json、图片生成/文生图/Z-Image瑶光版文生图｜人像创作质感出片首选_2104572471079952385.json、图片生成/文生图/aigc-image-2.5文生图九图连出｜太平风格批量出图_2106953497185972225.json、图片生成/文生图/千问2.1文生图官方原生架构｜一键出图带海报制作｜新手友好_2104813513557504002.json、图片生成/文生图/千问2.1白底商品图｜商业摄影级纯白底｜电商主图批量生成_2104808797784072193.json…）

- **类型**：Text To Image
- **样本数**：7
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

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
- `CR Prompt Text` —— 3/7 个有
- `CR Text` —— 2/7 个有
- `FastFilmGrain` —— 2/7 个有
- `LayerColor: BrightnessContrastV2` —— 2/7 个有
- `RH_RhartImageG25SunburstTextToImage` —— 2/7 个有
- `TextEncodeQwenImage21` —— 2/7 个有
- `RH_RhartImageG2TextToImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1080 | 7 | 0% |
| 高度 | 80 | 80 - 1920 | 7 | 0% |
| 采样步数 | 4 | 4 - 8 | 7 | 69% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 7 | 69% |
| 采样算法 | er_sde | - | 7 | 86% |
| 调度器 | beta | - | 7 | 86% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1080，7 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，7 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 8，7 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，7 个样本
- 采样算法 最常用 er_sde，7 个样本，一致性 86%
- 调度器 最常用 beta，7 个样本，一致性 86%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（8/7 个样本）：Steps较低可能导致细节不足
