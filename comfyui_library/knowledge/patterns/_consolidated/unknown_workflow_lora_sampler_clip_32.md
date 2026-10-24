---
name: unknown_workflow_lora_sampler_clip_32
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8657
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/EDGE OF QWEN BF16满血版洗图工作流_1957312732787830786.json, 图片生成/图生图/LYF千问-QWen-Image_1972278459286417410.json, 图片生成/图生图/千问写实_参考图-QWen-Image_1959667015088812033.json, 图片生成/图生图/麦橘千问美人图QWen-Image洗图123_2002778837123514370.json, 图片生成/文生图/AWP亚洲面孔千问LORA-QWen-Image【自动反推提示词】_1961577874413260802.json, 图片生成/文生图/AWP千问LORA-QWen-Image_1961096208251076609.json, 图片生成/文生图/EDGE OF QWEN BF16满血版文生图工作流_1957313561636827138.json, 图片生成/文生图/QWEN真实场景人物去油腻感_1959992517599113217.json, 图片生成/文生图/Qwen-Image-PruningQ文生图模型_1969006640156581890.json, 图片生成/文生图/Reality-Simulator真实摄影-QWen-Image_1959596933876756481.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_32

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/EDGE OF QWEN BF16满血版洗图工作流_1957312732787830786.json、图片生成/图生图/LYF千问-QWen-Image_1972278459286417410.json、图片生成/图生图/千问写实_参考图-QWen-Image_1959667015088812033.json、图片生成/图生图/麦橘千问美人图QWen-Image洗图123_2002778837123514370.json、图片生成/文生图/AWP亚洲面孔千问LORA-QWen-Image【自动反推提示词】_1961577874413260802.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 9/10 个有
- `RH_Captioner` —— 9/10 个有
- `CR SDXL Aspect Ratio` —— 8/10 个有
- `PrimitiveString` —— 8/10 个有
- `Text Concatenate` —— 8/10 个有
- `easy showAnything` —— 8/10 个有
- `PreviewImage` —— 3/10 个有
- `CFGNorm` —— 2/10 个有
- `EmptySD3LatentImage` —— 2/10 个有
- `SeedVR2` —— 2/10 个有
- `SeedVR2BlockSwap` —— 2/10 个有
- `TextConcatenator` —— 2/10 个有
- `CR Prompt Text` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 8 - 30 | 10 | 70% |
| Prompt 约束强度(CFG) | 3.75 | 1 - 4 | 10 | 71% |
| 采样算法 | euler | - | 10 | 80% |
| 调度器 | simple | - | 10 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 25，观测区间 8 - 30，10 个样本
- Prompt 约束强度(CFG) 中位数 3.75，观测区间 1 - 4，10 个样本
- 采样算法 最常用 euler，10 个样本，一致性 80%
- 调度器 最常用 simple，10 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
