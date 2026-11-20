---
name: text_to_image_sampler_clip_unet_21
type: Text To Image
frequency: 18
level: weak
coverage: 0.867556
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima-Base 动漫艺术_2057379324319326210.json, 图片生成/文生图/Anima-aesthetic-v1.1 高质量文生图_2092915857054855170.json, 图片生成/文生图/Anima-base-v1.0 文生图_2092909550499352577.json, 图片生成/文生图/Anima-turbo-v1.0 文生图_2092898755967279105.json, 图片生成/文生图/Anima动漫文生图_2057367708785790977.json, 图片生成/文生图/Image2.5文生图 顶级_2101616440351748097.json, 图片生成/文生图/Image2.5文生图 高质量图片生成工具_2100292745112936450.json, 图片生成/文生图/Image2.5文生图 高质量图片生成工具_2101592299229761537.json, 图片生成/文生图/Image2.5文生图顶级处理生成工作流工具_2102116515188400130.json, 图片生成/文生图/Image2.5文生图顶级处理生成工作流工具_2112897925230714881.json, 图片生成/文生图/Image2.5文生图顶级工作流｜高质量图片生成｜文案配图一步到位_2101886755678015490.json, 图片生成/文生图/Image2.5文生图高质量图片生成工具｜高级感图像一键生成_2101936480737382401.json, 图片生成/文生图/Krea2-turbo超写实真人摄影｜文生图人像写真写实风格_2089715224533360641.json, 图片生成/文生图/Krea2写实4K直出｜文生图去ai感真实人像生成_2093105565953249281.json, 图片生成/文生图/低价渠道版｜全能图片G-2.0图生图商品替换_2094033849197096961.json, 图片生成/文生图/图生图官方稳定版｜全能图片G2.0超强一致性_2093819752287399937.json, 图片生成/文生图/官方稳定版超强一致性｜全能图片G-2.0图生图直出_2093812472296853505.json, 图片生成/文生图/超强一致性官方稳定版｜全能图片G-2.0图生图替换_2094031047418802178.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_21

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/Anima-Base 动漫艺术_2057379324319326210.json、图片生成/文生图/Anima-aesthetic-v1.1 高质量文生图_2092915857054855170.json、图片生成/文生图/Anima-base-v1.0 文生图_2092909550499352577.json、图片生成/文生图/Anima-turbo-v1.0 文生图_2092898755967279105.json、图片生成/文生图/Anima动漫文生图_2057367708785790977.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 15/18 个有
- `LoraLoaderModelOnly` —— 14/18 个有
- `solarL_SaveImagesToZip` —— 13/18 个有
- `孤海注释` —— 10/18 个有
- `RH_RhartImageG25SunburstTextToImage` —— 7/18 个有
- `LoadImage` —— 6/18 个有
- `PreviewImage` —— 6/18 个有
- `Fast Groups Bypasser (rgthree)` —— 4/18 个有
- `CompressImages` —— 3/18 个有
- `RH_RhartImageG2ImageToImage` —— 3/18 个有
- `PrimitiveInt` —— 2/18 个有
- `RH_RhartImageG2OfficialImageToImage` —— 2/18 个有
- `RH_Translator` —— 2/18 个有
- `ConditioningKrea2Rebalance` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 1920 | 18 | 0% |
| 高度 | 80 | 80 - 1536 | 18 | 0% |
| 采样步数 | 4 | 4 - 40 | 18 | 0% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 5 | 18 | 81% |
| 采样算法 | er_sde | - | 18 | 78% |
| 调度器 | beta | - | 18 | 72% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 1920，18 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1536，18 个样本，取值分散，一致性仅 0%
- 采样步数 中位数 4，观测区间 4 - 40，18 个样本，取值分散，一致性仅 0%
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 5，18 个样本，取值集中（一致性 81%）
- 采样算法 最常用 er_sde，18 个样本，一致性 78%
- 调度器 最常用 beta，18 个样本，一致性 72%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（19/18 个样本）：Steps较低可能导致细节不足
