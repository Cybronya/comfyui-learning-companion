---
name: unknown_workflow_sampler_clip_unet_34
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.81485
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen Image 官方版超级加速-StarAI_1960034364899930114.json, 图片生成/文生图/Qwen Image文生图V1（QQ动漫版风格）_1954798087374987266.json, 图片生成/文生图/Qwen Image文生图V1（贞贞LORA版2500步）_1953815517956112386.json, 图片生成/文生图/Qwen Image，文生图 + Lora（人物写实）_1987158769756999681.json, 图片生成/文生图/Qwen image 2512文生图，恐怖悬疑动漫二次元，千问文生图推文，_2009994751235334145.json, 图片生成/文生图/Qwen 千问文生图工作流_1966311321211985921.json, 图片生成/文生图/Qwen-image文生图优化工作流_1953624443421687810.json, 图片生成/文生图/Qwen_千问-时尚穿搭_1995326727742218242.json, 图片生成/文生图/qianwen文生图_2055105575016509442.json, 图片生成/文生图/qwen-串珠艺术_1983771974319153153.json, 图片生成/文生图/千问提示词文生图_2033382870437339137.json, "图片生成/文生图/千问文生图(小即梦,内有提示词) 可能是目前市面上最强、最好用的中文文生图大模型，没有之一_2052654740084936705.json", "图片生成/文生图/千问文生图(小即梦,内有提示词)_1957736066219606018.json", "图片生成/文生图/千问文生图(比即梦厉害,内有提示词)_2065148780411973633.json", 图片生成/文生图/千问文生图_2052192004871860226.json, 图片生成/文生图/千问文生图_2053677771662086145.json, 图片生成/文生图/视频封面_2102206325894770690.json, 图片生成/文生图/🥨Qwen 千问开源文生图【官方流 更快更稳更可控】🥨_1952916801829146626.json, 图片生成/文生图/🦖qwen文生图_1960272130506174465.json, 视频生成/图生视频/视频封面_2104049803217952770.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_34

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/文生图/Qwen Image 官方版超级加速-StarAI_1960034364899930114.json、图片生成/文生图/Qwen Image文生图V1（QQ动漫版风格）_1954798087374987266.json、图片生成/文生图/Qwen Image文生图V1（贞贞LORA版2500步）_1953815517956112386.json、图片生成/文生图/Qwen Image，文生图 + Lora（人物写实）_1987158769756999681.json、图片生成/文生图/Qwen image 2512文生图，恐怖悬疑动漫二次元，千问文生图推文，_2009994751235334145.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 20 个 workflow 都包含：
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
- `CR Text` —— 16/20 个有
- `Int` —— 15/20 个有
- `ImpactInt` —— 14/20 个有
- `Seed (rgthree)` —— 13/20 个有
- `GetNode` —— 10/20 个有
- `SetNode` —— 9/20 个有
- `LoraLoaderModelOnly` —— 7/20 个有
- `LoadImage` —— 3/20 个有
- `Note Plus (mtb)` —— 2/20 个有
- `easy cleanGpuUsed` —— 2/20 个有
- `EmptyImage` —— 1/20 个有
- `ModelPatchTorchSettings` —— 1/20 个有
- `PathchSageAttentionKJ` —— 1/20 个有
- `PreviewImage` —— 1/20 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 6 - 20 | 20 | 77% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 20 | 70% |
| 采样算法 | euler | - | 20 | 100% |
| 调度器 | simple | - | 20 | 85% |
| 重绘幅度 | 1 | 1 - 1 | 20 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/20 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 6 - 20，20 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，20 个样本
- 采样算法 最常用 euler，20 个样本，一致性 100%
- 调度器 最常用 simple，20 个样本，一致性 85%
- 重绘幅度 中位数 1，观测区间 1 - 1，20 个样本，取值集中（一致性 100%）
