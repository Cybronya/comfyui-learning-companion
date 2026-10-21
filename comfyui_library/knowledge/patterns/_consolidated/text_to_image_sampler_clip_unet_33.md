---
name: text_to_image_sampler_clip_unet_33
type: Text To Image
frequency: 11
level: moderate
coverage: 0.981727
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Beyond Reality Super Z Image 文生图_2018143805811200001.json, 图片生成/文生图/Boogu-Image Base+Turbe双采文生图2606_2068416769479499777.json, 图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2069658196112920577.json, 图片生成/文生图/FLUX 2 文生图_1993572229503975426.json, 图片生成/文生图/KREA2-CC人像版_2095722389442224130.json, 图片生成/文生图/Krea2-turbo文生图3D国漫CG场景_2085325906326937602.json, 图片生成/文生图/Krea2-turbo文生图3D国漫CG风格_2089394677895221249.json, 图片生成/文生图/Krea2-turbo文生图超写实真人摄影风格_2089316645973086210.json, 图片生成/文生图/krea2 turbo 写实人像 超绝身材 MJ风格滤镜_2093335241376223233.json, 图片生成/文生图/krea2_写实人像_超绝身材_MJ风格滤镜_2093883637514194945.json, 图片生成/文生图/krea2_写实人像_超绝身材_MJ风格滤镜_2093905614782160897.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_33

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/Beyond Reality Super Z Image 文生图_2018143805811200001.json、图片生成/文生图/Boogu-Image Base+Turbe双采文生图2606_2068416769479499777.json、图片生成/文生图/ERNIE-Image  百度团队的文生图模型80亿参数_2069658196112920577.json、图片生成/文生图/FLUX 2 文生图_1993572229503975426.json、图片生成/文生图/KREA2-CC人像版_2095722389442224130.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：中等可信
- **平均知识覆盖**：98%

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
- `LoraLoaderModelOnly` —— 9/11 个有
- `Seed (rgthree)` —— 4/11 个有
- `CompressImages` —— 3/11 个有
- `ConditioningKrea2Rebalance` —— 2/11 个有
- `Text` —— 2/11 个有
- `FluxGuidance` —— 1/11 个有
- `Int` —— 1/11 个有
- `easy int` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 4 - 20 | 11 | 56% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 11 | 32% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | simple | - | 11 | 91% |
| 重绘幅度 | 1 | 0.35 - 1 | 11 | 80% |
| 宽度 | 1152 | 720 - 1920 | 11 | 76% |
| 高度 | 1536 | 1080 - 1984 | 11 | 83% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 4 - 20，11 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，11 个样本，取值分散，一致性仅 32%
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 0.35 - 1，11 个样本，取值集中（一致性 80%）
- 宽度 中位数 1152，观测区间 720 - 1920，11 个样本
- 高度 中位数 1536，观测区间 1080 - 1984，11 个样本，取值集中（一致性 83%）
