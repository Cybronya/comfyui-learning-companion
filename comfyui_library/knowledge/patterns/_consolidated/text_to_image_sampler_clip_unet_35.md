---
name: text_to_image_sampler_clip_unet_35
type: Text To Image
frequency: 13
level: weak
coverage: 0.844077
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Anima-Base 动漫艺术_2057379324319326210.json, 图片生成/文生图/Anima-aesthetic-v1.1 高质量文生图_2092915857054855170.json, 图片生成/文生图/Anima-base-v1.0 文生图_2092909550499352577.json, 图片生成/文生图/Anima-turbo-v1.0 文生图_2092898755967279105.json, 图片生成/文生图/Anima动漫文生图_2057367708785790977.json, 图片生成/文生图/Krea 2 甜美人像_2082369312555356161.json, 图片生成/文生图/Krea-2 全官方 LoRA 风格集成_2069797124136595458.json, 图片生成/文生图/ZIMAGE-杰洛特文生图_2044311451736739841.json, 图片生成/文生图/anima 动漫王者文生图_2057038503191605250.json, 图片生成/文生图/krea2-trubo-青绿水彩风格+水墨风格+光影效果彩色极简素描风格_2069757903887753218.json, 图片生成/文生图/电商文生图 krea2_2079494663781834754.json, 图片生成/文生图/百度大模型 文生图ERNIE-image-turbo 人物一致性 自然真实_2044640662099857410.json, 图片生成/文生图/百度大模型ERNIE-image-turbo-文生图  人物一致性 自然真实_2044656791585296386.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_35

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/文生图/Anima-Base 动漫艺术_2057379324319326210.json、图片生成/文生图/Anima-aesthetic-v1.1 高质量文生图_2092915857054855170.json、图片生成/文生图/Anima-base-v1.0 文生图_2092909550499352577.json、图片生成/文生图/Anima-turbo-v1.0 文生图_2092898755967279105.json、图片生成/文生图/Anima动漫文生图_2057367708785790977.json…）

- **类型**：Text To Image
- **样本数**：13
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 13 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 6/13 个有
- `RH_Translator` —— 6/13 个有
- `Fast Groups Bypasser (rgthree)` —— 4/13 个有
- `JjkText` —— 4/13 个有
- `PreviewImage` —— 4/13 个有
- `CompressImages` —— 3/13 个有
- `ConditioningZeroOut` —— 3/13 个有
- `PrimitiveInt` —— 3/13 个有
- `ShowText|pysssss` —— 2/13 个有
- `Anything Everywhere` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1152 | 720 - 1920 | 13 | 65% |
| 高度 | 1280 | 1080 - 2160 | 13 | 78% |
| 采样步数 | 8 | 2 - 40 | 13 | 23% |
| Prompt 约束强度(CFG) | 1 | 1 - 5 | 13 | 26% |
| 采样算法 | euler | - | 13 | 69% |
| 调度器 | simple | - | 13 | 54% |
| 重绘幅度 | 1 | 0.2 - 1 | 13 | 77% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 23/13 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1152，观测区间 720 - 1920，13 个样本
- 高度 中位数 1280，观测区间 1080 - 2160，13 个样本
- 采样步数 中位数 8，观测区间 2 - 40，13 个样本，取值分散，一致性仅 23%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 5，13 个样本，取值分散，一致性仅 26%
- 采样算法 最常用 euler，13 个样本，一致性 69%
- 调度器 最常用 simple，13 个样本，一致性 54%
- 重绘幅度 中位数 1，观测区间 0.2 - 1，13 个样本
- 高发问题（23/13 个样本）：Steps较低可能导致细节不足
