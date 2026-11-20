---
name: text_to_image_sampler_clip_unet_8
type: Text To Image
frequency: 26
level: moderate
coverage: 0.883308
common_nodes: [CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, EmptySD3LatentImage, ImpactSwitch, Int, KSampler, ModelSamplingAuraFlow, RHHiddenNodes, SaveImage, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: ["图片生成/图生图/人物模特生成-智能提示词版,+反推_1986598255008088066.json", 图片生成/文生图/人物模特生成-智能提示词版_1982988891378581505.json, 图片生成/文生图/人物模特生成-智能提示词版_1995026660728692737.json, 图片生成/文生图/人物模特生成-智能提示词版_2076466004066127873.json, 图片生成/文生图/人物模特生成-智能提示词版_2080539428451344386.json, 图片生成/文生图/人物模特生成-智能提示词版_2080543119690518530.json, 图片生成/文生图/人物模特生成-智能提示词版_2103298288773591042.json, 图片生成/文生图/人物模特生成-智能提示词版_2103666446302797825.json, 图片生成/文生图/人物模特生成-智能提示词版_2104489691142774785.json, 图片生成/文生图/人物模特生成-智能提示词版_2104848974585876481.json, 图片生成/文生图/人物模特生成-智能提示词版一键生成_1990789159143022593.json, 图片生成/文生图/人物模特生成-智能提示词版一键生成_2010607632972783618.json, 图片生成/文生图/人物模特生成-智能提示词版一键生成_2032748621736710145.json, 图片生成/文生图/人物模特生成-智能提示词版一键生成_2073095542183391234.json, 图片生成/文生图/人物模特生成智能提示词版文生图处理工作流_2101371503924305921.json, 图片生成/文生图/人物生成_2048068835172945922.json, 图片生成/文生图/文生图-智能提示词版_2055097130783649794.json, 图片生成/文生图/文生图-智能提示词版_2055208829247336449.json, 图片生成/文生图/文生图-智能提示词版_2058810512481275906.json, 图片生成/文生图/文生图-角色卡-qwen-智能提示词版_2059759473899687938.json, 图片生成/文生图/文生图智能提示词版_2060919208803917825.json, 图片生成/文生图/智能提示词 极致写实文生图 直生4K_2043502777824976897.json, 图片生成/文生图/智能提示词模特生成｜人物文生图人像写真美少女_2092168856931487746.json, 图片生成/文生图/智能提示词版人物模特生成文生图人像写真美少女_2088514274841944065.json, 图片生成/文生图/模特生成_2038509746478653442.json, 图片生成/文生图/模特生成_2057659291838017538.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_8

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（图片生成/图生图/人物模特生成-智能提示词版,+反推_1986598255008088066.json、图片生成/文生图/人物模特生成-智能提示词版_1982988891378581505.json、图片生成/文生图/人物模特生成-智能提示词版_1995026660728692737.json、图片生成/文生图/人物模特生成-智能提示词版_2076466004066127873.json、图片生成/文生图/人物模特生成-智能提示词版_2080539428451344386.json…）

- **类型**：Text To Image
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 26 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `ImpactSwitch`
- `Int`
- `KSampler`
- `ModelSamplingAuraFlow`
- `RHHiddenNodes`
- `SaveImage`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `PrimitiveString` —— 25/26 个有
- `TextInput_` —— 25/26 个有
- `easy anythingIndexSwitch` —— 25/26 个有
- `LoadImage` —— 6/26 个有
- `JjkText` —— 3/26 个有
- `LoraLoaderModelOnly` —— 3/26 个有
- `solarL_SaveImagesToZip` —— 3/26 个有
- `孤海注释` —— 3/26 个有
- `CR Text` —— 1/26 个有
- `MuyeTextEditOutput` —— 1/26 个有
- `RH_LLMAPI_Pro_Node` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 80 - 512 | 26 | 70% |
| 高度 | 512 | 80 - 512 | 26 | 70% |
| 采样步数 | 20 | 4 - 20 | 26 | 72% |
| Prompt 约束强度(CFG) | 2.5 | 2.5 - 4.5 | 26 | 77% |
| 采样算法 | res_2m | - | 26 | 88% |
| 调度器 | sgm_uniform | - | 26 | 88% |
| 重绘幅度 | 1 | 1 - 1 | 26 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 3/26 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 512，观测区间 80 - 512，26 个样本
- 高度 中位数 512，观测区间 80 - 512，26 个样本
- 采样步数 中位数 20，观测区间 4 - 20，26 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 2.5 - 4.5，26 个样本
- 采样算法 最常用 res_2m，26 个样本，一致性 88%
- 调度器 最常用 sgm_uniform，26 个样本，一致性 88%
- 重绘幅度 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
