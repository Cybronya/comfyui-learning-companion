---
name: unknown_workflow_lora_sampler_clip_7
type: Unknown Workflow
frequency: 34
level: moderate
coverage: 0.981971
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问文生图-超写实风格V4。_2066441527123070977.json, 图片生成/图生图/千问文生图-超写实风格V4。_2070041358575947777.json, 图片生成/文生图/12月最新文生图 Qwen 2512 标准模型非FP8_2007791461693136897.json, 图片生成/文生图/AI模特文生图_2005619684131172353.json, 图片生成/文生图/DreamCore-梦核_2073300420767862785.json, 图片生成/文生图/Qwen-Image文生图（亚洲复古胶片摄影）_2063953908111859714.json, 图片生成/文生图/Qwen-image Lora 文生图_1981766660744986626.json, 图片生成/文生图/Qwen-image Lora_2007472820174987265.json, 图片生成/文生图/Y-Z-Image-turbo+lenovo lora-workflow_1995640202892861441.json, 图片生成/文生图/Y-Z-Image-turbo+zit-flow-dpo-lora-workflow_2029147456390303745.json, 图片生成/文生图/qwen-image文生图-超写实风格V4。_2054466280689807362.json, 图片生成/文生图/qwen-image文生图-超写实风格电商图片文生图中文输入英文输入提示词_2067604904981647362.json, 图片生成/文生图/qwen-image文生图-超写实风格电商图片文生图中文输入英文输入提示词_2082433240765386754.json, 图片生成/文生图/qwen文生图-超写实风格V4。_2054841790506782721.json, 图片生成/文生图/千问文生图-超写实风格V4_2032033177165897730.json, 图片生成/文生图/千问文生图-超写实风格V4。_1996850075932532737.json, 图片生成/文生图/千问文生图-超写实风格V4。_2038886359821197313.json, 图片生成/文生图/千问文生图-超写实风格V4。_2049682901758951426.json, 图片生成/文生图/千问文生图-超写实风格V4。_2054112333609357313.json, 图片生成/文生图/千问文生图-超写实风格V4。_2054120989398708226.json, 图片生成/文生图/千问文生图-超写实风格V4。_2056933090823598081.json, 图片生成/文生图/千问文生图-超写实风格V4。_2058722964627083266.json, 图片生成/文生图/千问文生图-超写实风格V4。_2059928485799485442.json, 图片生成/文生图/千问文生图-超写实风格V4。_2059929962727174145.json, 图片生成/文生图/千问文生图-超写实风格V4。_2061999718896586753.json, 图片生成/文生图/千问文生图-超写实风格V4。_2064145427351556097.json, 图片生成/文生图/千问文生图-超写实风格V4。_2068933719162970113.json, 图片生成/文生图/千问文生图-超写实风格V4。_2072205725044133890.json, 图片生成/文生图/千问文生图-超写实风格V4。_2077559719371304962.json, 图片生成/文生图/千问文生图-超写实风格V4。_2078034646411071489.json, 图片生成/文生图/千问文生图-超写实风格V4。_2078825624730431490.json, 图片生成/文生图/千问文生图-超写实风格V4。_2079363498722816002.json, 图片生成/文生图/千问文生图-超写实风格V4。_2084453286693920770.json, 图片生成/文生图/千问文生图-超写实风格V4。_2088095437621391362.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_7

> 由 `engine/knowledge_consolidation` 从 34 个 workflow 归纳得出（图片生成/图生图/千问文生图-超写实风格V4。_2066441527123070977.json、图片生成/图生图/千问文生图-超写实风格V4。_2070041358575947777.json、图片生成/文生图/12月最新文生图 Qwen 2512 标准模型非FP8_2007791461693136897.json、图片生成/文生图/AI模特文生图_2005619684131172353.json、图片生成/文生图/DreamCore-梦核_2073300420767862785.json…）

- **类型**：Unknown Workflow
- **样本数**：34
- **可信度**：中等可信
- **平均知识覆盖**：98%

## 共有节点

全部 34 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 31/34 个有
- `CR Text` —— 27/34 个有
- `CR Text Concatenate` —— 26/34 个有
- `String` —— 26/34 个有
- `ConditioningZeroOut` —— 5/34 个有
- `PrimitiveStringMultiline` —— 4/34 个有
- `FluxResolutionNode` —— 2/34 个有
- `SDXLAspectRatio` —— 2/34 个有
- `JWInteger` —— 1/34 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 50 | 34 | 61% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 34 | 72% |
| 采样算法 | euler | - | 34 | 88% |
| 调度器 | beta57 | - | 34 | 82% |
| 重绘幅度 | 1 | 1 - 1 | 34 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/34 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 50，34 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，34 个样本
- 采样算法 最常用 euler，34 个样本，一致性 88%
- 调度器 最常用 beta57，34 个样本，一致性 82%
- 重绘幅度 中位数 1，观测区间 1 - 1，34 个样本，取值集中（一致性 100%）
