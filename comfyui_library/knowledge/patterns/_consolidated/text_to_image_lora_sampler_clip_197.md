---
name: text_to_image_lora_sampler_clip_197
type: Text To Image
frequency: 6
level: weak
coverage: 0.933333
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: [easy cleanGpuUsed]
members: [图片生成/文生图/1950437362914516993.json, 图片生成/文生图/1988883409260916737.json, 图片生成/文生图/1989381394365378562.json, 图片生成/文生图/Qwen Image 2512文生图_2016788115049947137.json, 图片生成/文生图/Qwen Image 2512文生图_2055456154658066434.json, 图片生成/文生图/Qwen文生图基础工作流_1989984703535083522.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_197

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/文生图/1950437362914516993.json、图片生成/文生图/1988883409260916737.json、图片生成/文生图/1989381394365378562.json、图片生成/文生图/Qwen Image 2512文生图_2016788115049947137.json、图片生成/文生图/Qwen Image 2512文生图_2055456154658066434.json…）

- **类型**：Text To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 6 个 workflow 都包含：
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
- `ModelSamplingAuraFlow` —— 5/6 个有
- `Int` —— 4/6 个有
- `easy cleanGpuUsed` —— 3/6 个有
- `CFGNorm` —— 2/6 个有
- `ImpactSwitch` —— 2/6 个有
- `PathchSageAttentionKJ` —— 2/6 个有
- `ModelSamplingSD3` —— 1/6 个有
- `RH_Translator` —— 1/6 个有
- `ShowText|pysssss` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 30 | 6 | 37% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 6 | 25% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 512 | 512 - 1080 | 6 | 63% |
| 高度 | 512 | 512 - 1920 | 6 | 37% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 30，6 个样本，取值分散，一致性仅 37%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，6 个样本，取值分散，一致性仅 25%
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 1080，6 个样本
- 高度 中位数 512，观测区间 512 - 1920，6 个样本，取值分散，一致性仅 37%
- 高发问题（4/6 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：easy cleanGpuUsed
