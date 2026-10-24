---
name: unknown_workflow_lora_sampler_clip_27
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.980455
common_nodes: [CLIPLoader, CLIPTextEncode, EG_ZZ_TMTX, EmptySD3LatentImage, GrowMaskWithBlur, Int, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, RMBG, Sa2VANodeTpl, SaveImage, SimpleMath+, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageCropFromMask]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/透明素材生成仓库_2099410851257208833.json, 图片生成/文生图/Qwen 生成带透明通道的素材_2021953318397943810.json, 图片生成/文生图/z-image 透明素材生成_2018871198733574146.json, 图片生成/文生图/一键生成透明素材_2038882407293657089.json, 图片生成/文生图/根据提示词生成素材或透明素材或实物物体 万物可生_1993132200847671298.json, 图片生成/文生图/透明素材生成_2037333902938873858.json, 图片生成/文生图/透明素材生成仓库_1991047114425868289.json, 图片生成/文生图/透明素材生成仓库_2097876593392836610.json, 图片生成/文生图/透明素材生成器_2072535866597273602.json, 图片生成/文生图/透明素材生成器_2072536930167910402.json, 图片生成/文生图/透明素材生成器_2072537785935945730.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_27

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/透明素材生成仓库_2099410851257208833.json、图片生成/文生图/Qwen 生成带透明通道的素材_2021953318397943810.json、图片生成/文生图/z-image 透明素材生成_2018871198733574146.json、图片生成/文生图/一键生成透明素材_2038882407293657089.json、图片生成/文生图/根据提示词生成素材或透明素材或实物物体 万物可生_1993132200847671298.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：98%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EG_ZZ_TMTX`
- `EmptySD3LatentImage`
- `GrowMaskWithBlur`
- `Int`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `RMBG`
- `Sa2VANodeTpl`
- `SaveImage`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`
- `easy imageCropFromMask`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 10/11 个有
- `Text` —— 1/11 个有
- `TextConcatenate` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | euler | - | 11 | 100% |
| 调度器 | beta57 | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，11 个样本，一致性 100%
- 调度器 最常用 beta57，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
