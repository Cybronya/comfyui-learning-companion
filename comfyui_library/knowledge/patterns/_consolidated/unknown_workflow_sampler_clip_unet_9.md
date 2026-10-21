---
name: unknown_workflow_sampler_clip_unet_9
type: Unknown Workflow
frequency: 26
level: moderate
coverage: 0.985923
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/API - Qwenimage文生图_2066885101774008321.json, 图片生成/文生图/LH-DMT版本-2.生图片类-022.Z_image_turbo文生图_2016484426032619521.json, 图片生成/文生图/LH-DMT版本-2.生图片类-044.Qwen-Image-10步蒸馏-Q版3D人物_2016524825891704833.json, 图片生成/文生图/Ovis文生图工作流_1997584970094952450.json, 图片生成/文生图/QWen2512基础文生图工作流+LoRA_2094427546531229697.json, 图片生成/文生图/Qwen 2512文生图_2007744253128089601.json, 图片生成/文生图/Qwen image 2512文生图，恐怖悬疑动漫二次元，千问文生图推文，_2009994751235334145.json, 图片生成/文生图/Qwen2512文生图工作流_2026224981025234945.json, 图片生成/文生图/qwen-image文生图-超写实风格电商图片文生图中文输入英文输入提示词_2067604904981647362.json, 图片生成/文生图/qwen-image文生图-超写实风格电商图片文生图中文输入英文输入提示词_2082433240765386754.json, 图片生成/文生图/千问image文生图真实感增强_1996838932895735809.json, 图片生成/文生图/千问文生图-超写实风格V4。_1996850075932532737.json, 图片生成/文生图/千问文生图-超写实风格V4。_2056933090823598081.json, 图片生成/文生图/千问文生图-超写实风格V4。_2058722964627083266.json, 图片生成/文生图/千问文生图-超写实风格V4。_2059928485799485442.json, 图片生成/文生图/千问文生图-超写实风格V4。_2059929962727174145.json, 图片生成/文生图/千问文生图-超写实风格V4。_2061999718896586753.json, 图片生成/文生图/千问文生图-超写实风格V4。_2064145427351556097.json, 图片生成/文生图/千问文生图-超写实风格V4。_2068933719162970113.json, 图片生成/文生图/千问文生图-超写实风格V4。_2072205725044133890.json, 图片生成/文生图/千问文生图-超写实风格V4。_2077559719371304962.json, 图片生成/文生图/千问文生图-超写实风格V4。_2078034646411071489.json, 图片生成/文生图/千问文生图-超写实风格V4。_2078825624730431490.json, 图片生成/文生图/千问文生图-超写实风格V4。_2079363498722816002.json, 图片生成/文生图/千问文生图-超写实风格V4。_2084453286693920770.json, 图片生成/文生图/千问文生图-超写实风格V4。_2088095437621391362.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_9

> 由 `engine/knowledge_consolidation` 从 26 个 workflow 归纳得出（图片生成/文生图/API - Qwenimage文生图_2066885101774008321.json、图片生成/文生图/LH-DMT版本-2.生图片类-022.Z_image_turbo文生图_2016484426032619521.json、图片生成/文生图/LH-DMT版本-2.生图片类-044.Qwen-Image-10步蒸馏-Q版3D人物_2016524825891704833.json、图片生成/文生图/Ovis文生图工作流_1997584970094952450.json、图片生成/文生图/QWen2512基础文生图工作流+LoRA_2094427546531229697.json…）

- **类型**：Unknown Workflow
- **样本数**：26
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 26 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 22/26 个有
- `CR Text` —— 20/26 个有
- `easy cleanGpuUsed` —— 20/26 个有
- `CR Text Concatenate` —— 18/26 个有
- `String` —— 18/26 个有
- `Int` —— 3/26 个有
- `Fast Groups Bypasser (rgthree)` —— 1/26 个有
- `LoadImage` —— 1/26 个有
- `LoraLoader` —— 1/26 个有
- `Text _O` —— 1/26 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 50 | 26 | 55% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 5 | 26 | 60% |
| 采样算法 | euler | - | 26 | 96% |
| 调度器 | beta57 | - | 26 | 69% |
| 重绘幅度 | 1 | 1 - 1 | 26 | 100% |
| LoRA 模型强度 | 1 | - | 1 | 100% |
| LoRA 文本强度 | 1 | - | 1 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/26 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 50，26 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 5，26 个样本
- 采样算法 最常用 euler，26 个样本，一致性 96%
- 调度器 最常用 beta57，26 个样本，一致性 69%
- 重绘幅度 中位数 1，观测区间 1 - 1，26 个样本，取值集中（一致性 100%）
