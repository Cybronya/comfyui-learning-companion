---
name: text_to_image_sampler_clip_unet_52
type: Text To Image
frequency: 8
level: weak
coverage: 0.811625
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, DapaoImageRatioLimitNode, EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/AI漫剧文生四视图工作流_2097319620981125121.json, 图片生成/文生图/Anima V10 二次元动漫模型_2059087045875822593.json, 图片生成/文生图/Anima V10 二次元动漫模型_2061626870118047746.json, 图片生成/文生图/Anima 最强二次元动漫模型_2056935315700543489.json, 图片生成/文生图/Anima二次元_2061726328621191169.json, 图片生成/文生图/Boogu 文生图_2085097416587563010.json, 图片生成/文生图/开源图像悍将boogu 急速文生图 提示词自动优化版_2069366240002535425.json, 图片生成/文生图/开源图像悍将boogu 急速文生图 提示词自动优化版_2083610947033321474.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_52

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/AI漫剧文生四视图工作流_2097319620981125121.json、图片生成/文生图/Anima V10 二次元动漫模型_2059087045875822593.json、图片生成/文生图/Anima V10 二次元动漫模型_2061626870118047746.json、图片生成/文生图/Anima 最强二次元动漫模型_2056935315700543489.json、图片生成/文生图/Anima二次元_2061726328621191169.json…）

- **类型**：Text To Image
- **样本数**：8
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `DapaoImageRatioLimitNode`
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `Dapao_LlamaChat` —— 7/8 个有
- `Seed (rgthree)` —— 7/8 个有
- `easy showAnything` —— 7/8 个有
- `ConditioningZeroOut` —— 4/8 个有
- `PreviewImage` —— 4/8 个有
- `Note Plus (mtb)` —— 3/8 个有
- `Lora Loader Stack (rgthree)` —— 1/8 个有
- `LoraLoaderModelOnly` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 768 | 512 - 1024 | 8 | 67% |
| 高度 | 768 | 512 - 1536 | 8 | 51% |
| 采样步数 | 22.5 | 4 - 35 | 8 | 27% |
| Prompt 约束强度(CFG) | 3 | 1 - 5 | 8 | 33% |
| 采样算法 | res_2s | - | 8 | 50% |
| 调度器 | beta57 | - | 8 | 50% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 768，观测区间 512 - 1024，8 个样本
- 高度 中位数 768，观测区间 512 - 1536，8 个样本
- 采样步数 中位数 22.5，观测区间 4 - 35，8 个样本，取值分散，一致性仅 27%
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 5，8 个样本，取值分散，一致性仅 33%
- 采样算法 最常用 res_2s，8 个样本，一致性 50%
- 调度器 最常用 beta57，8 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
