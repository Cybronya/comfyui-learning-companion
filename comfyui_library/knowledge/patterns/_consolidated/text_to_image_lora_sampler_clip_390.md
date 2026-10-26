---
name: text_to_image_lora_sampler_clip_390
type: Text To Image
frequency: 5
level: strong
coverage: 0.935
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, RH_Captioner, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Wan2.2 +lora宠物+文生图_1986964422252015617.json, 图片生成/图生图/krea2图生图工作流_2071600191748272129.json, 图片生成/图生图/krea2基础图生图_2071358346015371266.json, 图片生成/图生图/krea2基础图生图_2095763877953884162.json, 图片生成/图生图/pipi提示词反推+Z-Image图生图（洗图）_1998176083553976322.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_390

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Wan2.2 +lora宠物+文生图_1986964422252015617.json、图片生成/图生图/krea2图生图工作流_2071600191748272129.json、图片生成/图生图/krea2基础图生图_2071358346015371266.json、图片生成/图生图/krea2基础图生图_2095763877953884162.json、图片生成/图生图/pipi提示词反推+Z-Image图生图（洗图）_1998176083553976322.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：94%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `RH_Captioner`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 4/5 个有
- `ShowText|pysssss` —— 4/5 个有
- `MultiTextConcatenate` —— 2/5 个有
- `String Literal` —— 2/5 个有
- `Anything Everywhere` —— 1/5 个有
- `ImageScale` —— 1/5 个有
- `ModelSamplingSD3` —— 1/5 个有
- `PathchSageAttentionKJ` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 10 | 8 - 10 | 5 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 60% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |
| 宽度 | 1024 | 864 - 1504 | 5 | 78% |
| 高度 | 1536 | 1504 - 1920 | 5 | 90% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 10，观测区间 8 - 10，5 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 864 - 1504，5 个样本
- 高度 中位数 1536，观测区间 1504 - 1920，5 个样本，取值集中（一致性 90%）
