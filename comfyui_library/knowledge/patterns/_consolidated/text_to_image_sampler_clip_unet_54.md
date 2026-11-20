---
name: text_to_image_sampler_clip_unet_54
type: Text To Image
frequency: 12
level: moderate
coverage: 0.841083
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/AI漫剧文生四视图工作流_2097319620981125121.json, 图片生成/文生图/Anima Aesthetic 1.0b｜纯审美微调文生图_2075555639908196353.json, 图片生成/文生图/Anima Aesthetic 1.0｜开箱即用高质量文生图_2075555648682684418.json, 图片生成/文生图/Anima Base 复古动漫文生图_2078659623917277185.json, 图片生成/文生图/Anima Turbo 10-Step｜10步极速文生图_2075555632480079873.json, 图片生成/文生图/Anima V10 二次元动漫模型_2059087045875822593.json, 图片生成/文生图/Anima V10 二次元动漫模型_2061626870118047746.json, 图片生成/文生图/Anima 最强二次元动漫模型_2056935315700543489.json, 图片生成/文生图/Anima二次元_2061726328621191169.json, 图片生成/文生图/Boogu 文生图_2085097416587563010.json, 图片生成/文生图/开源图像悍将boogu 急速文生图 提示词自动优化版_2069366240002535425.json, 图片生成/文生图/开源图像悍将boogu 急速文生图 提示词自动优化版_2083610947033321474.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_54

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/文生图/AI漫剧文生四视图工作流_2097319620981125121.json、图片生成/文生图/Anima Aesthetic 1.0b｜纯审美微调文生图_2075555639908196353.json、图片生成/文生图/Anima Aesthetic 1.0｜开箱即用高质量文生图_2075555648682684418.json、图片生成/文生图/Anima Base 复古动漫文生图_2078659623917277185.json、图片生成/文生图/Anima Turbo 10-Step｜10步极速文生图_2075555632480079873.json…）

- **类型**：Text To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：84%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 8/12 个有
- `DapaoImageRatioLimitNode` —— 8/12 个有
- `孤海注释` —— 8/12 个有
- `Dapao_LlamaChat` —— 7/12 个有
- `Seed (rgthree)` —— 7/12 个有
- `easy showAnything` —— 7/12 个有
- `ConditioningZeroOut` —— 4/12 个有
- `PreviewImage` —— 4/12 个有
- `Note Plus (mtb)` —— 3/12 个有
- `Lora Loader Stack (rgthree)` —— 1/12 个有
- `LoraLoaderModelOnly` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 512 - 1080 | 12 | 71% |
| 高度 | 1024 | 512 - 1920 | 12 | 56% |
| 采样步数 | 32.5 | 4 - 40 | 12 | 37% |
| Prompt 约束强度(CFG) | 4 | 1 - 5 | 12 | 42% |
| 采样算法 | euler | - | 12 | 33% |
| 调度器 | simple | - | 12 | 42% |
| 重绘幅度 | 1 | 1 - 1 | 12 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/12 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1024，观测区间 512 - 1080，12 个样本
- 高度 中位数 1024，观测区间 512 - 1920，12 个样本
- 采样步数 中位数 32.5，观测区间 4 - 40，12 个样本，取值分散，一致性仅 37%
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 5，12 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 euler，12 个样本，一致性 33%
- 调度器 最常用 simple，12 个样本，一致性 42%
- 重绘幅度 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
