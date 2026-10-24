---
name: unknown_workflow_sampler_clip_unet_38
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.822278
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/QWen-Image中文渲染-ComfyUI_1952892525439873025.json, 图片生成/文生图/QWen-Image模型lora训练测试工作流_1963484613191749634.json, 图片生成/文生图/QWen2512基础文生图工作流+LoRA_2094427546531229697.json, 图片生成/文生图/Qwen 2512文生图_2007744253128089601.json, 图片生成/文生图/Qwen Image 中文文生图_1952919451249348609.json, 图片生成/文生图/Qwen Image 官方版超级加速-StarAI_1960034364899930114.json, 图片生成/文生图/Qwen image 2512文生图，恐怖悬疑动漫二次元，千问文生图推文，_2009994751235334145.json, 图片生成/文生图/Qwen-image文生图优化工作流_1953624443421687810.json, 图片生成/文生图/Qwen_千问-时尚穿搭_1995326727742218242.json, 图片生成/文生图/qianwen文生图_2055105575016509442.json, 图片生成/文生图/qwen-串珠艺术_1983771974319153153.json, 图片生成/文生图/千问提示词文生图_2033382870437339137.json, "图片生成/文生图/千问文生图(小即梦,内有提示词) 可能是目前市面上最强、最好用的中文文生图大模型，没有之一_2052654740084936705.json", "图片生成/文生图/千问文生图(小即梦,内有提示词)_1957736066219606018.json", "图片生成/文生图/千问文生图(比即梦厉害,内有提示词)_2065148780411973633.json", 图片生成/文生图/千问文生图_2052192004871860226.json, 图片生成/文生图/千问文生图_2053677771662086145.json, 图片生成/文生图/视频封面_2102206325894770690.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_38

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/文生图/QWen-Image中文渲染-ComfyUI_1952892525439873025.json、图片生成/文生图/QWen-Image模型lora训练测试工作流_1963484613191749634.json、图片生成/文生图/QWen2512基础文生图工作流+LoRA_2094427546531229697.json、图片生成/文生图/Qwen 2512文生图_2007744253128089601.json、图片生成/文生图/Qwen Image 中文文生图_1952919451249348609.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `EmptySD3LatentImage` —— 16/18 个有
- `CR Text` —— 13/18 个有
- `Int` —— 12/18 个有
- `ImpactInt` —— 10/18 个有
- `Seed (rgthree)` —— 10/18 个有
- `GetNode` —— 8/18 个有
- `SetNode` —— 8/18 个有
- `LoraLoaderModelOnly` —— 7/18 个有
- `easy cleanGpuUsed` —— 4/18 个有
- `CR SDXL Aspect Ratio` —— 2/18 个有
- `LoadImage` —— 2/18 个有
- `ModelPatchTorchSettings` —— 1/18 个有
- `Note Plus (mtb)` —— 1/18 个有
- `PathchSageAttentionKJ` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 8 - 20 | 18 | 72% |
| Prompt 约束强度(CFG) | 4 | 1 - 4 | 18 | 57% |
| 采样算法 | euler | - | 18 | 100% |
| 调度器 | simple | - | 18 | 89% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 8 - 20，18 个样本
- Prompt 约束强度(CFG) 中位数 4，观测区间 1 - 4，18 个样本
- 采样算法 最常用 euler，18 个样本，一致性 100%
- 调度器 最常用 simple，18 个样本，一致性 89%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
