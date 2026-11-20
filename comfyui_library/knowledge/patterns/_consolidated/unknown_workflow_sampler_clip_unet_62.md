---
name: unknown_workflow_sampler_clip_unet_62
type: Unknown Workflow
frequency: 15
level: moderate
coverage: 0.7754
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 官方版超级加速-StarAI_1960034364899930114.json, 图片生成/文生图/Qwen image 2512文生图，恐怖悬疑动漫二次元，千问文生图推文，_2009994751235334145.json, 图片生成/文生图/Qwen 千问文生图工作流_1966311321211985921.json, 图片生成/文生图/Qwen_千问-时尚穿搭_1995326727742218242.json, 图片生成/文生图/qianwen文生图_2055105575016509442.json, 图片生成/文生图/qwen-串珠艺术_1983771974319153153.json, 图片生成/文生图/千问提示词文生图_2033382870437339137.json, "图片生成/文生图/千问文生图(小即梦,内有提示词) 可能是目前市面上最强、最好用的中文文生图大模型，没有之一_2052654740084936705.json", "图片生成/文生图/千问文生图(小即梦,内有提示词)_1957736066219606018.json", "图片生成/文生图/千问文生图(比即梦厉害,内有提示词)_2065148780411973633.json", 图片生成/文生图/千问文生图_2052192004871860226.json, 图片生成/文生图/千问文生图_2053677771662086145.json, 图片生成/文生图/视频封面_2102206325894770690.json, 图片生成/文生图/🥨Qwen 千问开源文生图【官方流 更快更稳更可控】🥨_1952916801829146626.json, 视频生成/图生视频/视频封面_2104049803217952770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_62

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（图片生成/文生图/Qwen Image 官方版超级加速-StarAI_1960034364899930114.json、图片生成/文生图/Qwen image 2512文生图，恐怖悬疑动漫二次元，千问文生图推文，_2009994751235334145.json、图片生成/文生图/Qwen 千问文生图工作流_1966311321211985921.json、图片生成/文生图/Qwen_千问-时尚穿搭_1995326727742218242.json、图片生成/文生图/qianwen文生图_2055105575016509442.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 14/15 个有
- `ImpactInt` —— 13/15 个有
- `Int` —— 13/15 个有
- `Seed (rgthree)` —— 13/15 个有
- `GetNode` —— 9/15 个有
- `SetNode` —— 9/15 个有
- `LoraLoaderModelOnly` —— 4/15 个有
- `LoadImage` —— 3/15 个有
- `Note Plus (mtb)` —— 2/15 个有
- `easy cleanGpuUsed` —— 2/15 个有
- `EmptyImage` —— 1/15 个有
- `ModelPatchTorchSettings` —— 1/15 个有
- `PathchSageAttentionKJ` —— 1/15 个有
- `PreviewImage` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 15 | 81% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 15 | 72% |
| 采样算法 | euler | - | 15 | 100% |
| 调度器 | simple | - | 15 | 93% |
| 重绘幅度 | 1 | 1 - 1 | 15 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，15 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，15 个样本
- 采样算法 最常用 euler，15 个样本，一致性 100%
- 调度器 最常用 simple，15 个样本，一致性 93%
- 重绘幅度 中位数 1，观测区间 1 - 1，15 个样本，取值集中（一致性 100%）
