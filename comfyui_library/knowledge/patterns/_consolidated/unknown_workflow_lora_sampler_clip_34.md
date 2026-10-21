---
name: unknown_workflow_lora_sampler_clip_34
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.945875
common_nodes: [CLIPLoader, CLIPTextEncode, EG_ZZ_TMTX, EmptySD3LatentImage, GrowMaskWithBlur, Int, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, RMBG, Sa2VANodeTpl, SaveImage, SimpleMath+, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed, easy imageCropFromMask]
problems: [Steps较低可能导致细节不足]
missing: [CR Text, SimpleMath+, easy cleanGpuUsed, easy imageCropFromMask]
members: [图片生成/文生图/1991047114425868289.json, 图片生成/文生图/Qwen 生成带透明通道的素材_2021953318397943810.json, 图片生成/文生图/z-image 透明素材生成_2018871198733574146.json, 图片生成/文生图/根据提示词生成素材或透明素材或实物物体 万物可生_1993132200847671298.json, 图片生成/文生图/透明素材生成仓库_2097876593392836610.json, 图片生成/文生图/透明素材生成器_2072535866597273602.json, 图片生成/文生图/透明素材生成器_2072536930167910402.json, 图片生成/文生图/透明素材生成器_2072537785935945730.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_34

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/文生图/1991047114425868289.json、图片生成/文生图/Qwen 生成带透明通道的素材_2021953318397943810.json、图片生成/文生图/z-image 透明素材生成_2018871198733574146.json、图片生成/文生图/根据提示词生成素材或透明素材或实物物体 万物可生_1993132200847671298.json、图片生成/文生图/透明素材生成仓库_2097876593392836610.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：95%

## 共有节点

全部 8 个 workflow 都包含：
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
- `CR Text` —— 7/8 个有
- `Text` —— 1/8 个有
- `TextConcatenate` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 8 - 8 | 8 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 8 | 100% |
| 采样算法 | euler | - | 8 | 100% |
| 调度器 | beta57 | - | 8 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 8 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/8 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，8 个样本，一致性 100%
- 调度器 最常用 beta57，8 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 高发问题（8/8 个样本）：Steps较低可能导致细节不足
- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、SimpleMath+、easy cleanGpuUsed、easy imageCropFromMask
