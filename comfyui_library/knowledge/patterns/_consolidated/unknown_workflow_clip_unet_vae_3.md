---
name: unknown_workflow_clip_unet_vae_3
type: Unknown Workflow
frequency: 15
level: weak
coverage: 0.918867
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [平台全量/AI古风人像·Qwen写实·一句话出图工作流_2099719627638140930.json, 平台全量/AI数字人工作流云端口播V1_2118227072048001026.json, 平台全量/AI电商主图·Qwen写实·一句话出图工作流_2099719419659378690.json, 平台全量/Qwen-Image Lightning8步加速lora 8steps-V1.0_1954344869051428866.json, 平台全量/Qwen2512版CG插画创作_2054037288224600066.json, 平台全量/Qwen中式插画_2011454376958763010.json, 平台全量/Z-image-Turbo文生图_2120118502882365442.json, 平台全量/ZIB国风CG精细人像专用_2061802698525200385.json, 平台全量/ZIB国风人像摄影专用_2020329970081468417.json, 平台全量/z-image测试_1998677341066907650.json, 平台全量/文生图-Q版_2117179326247559169.json, 平台全量/电商定制中文营销海报_1953454579499368449.json, 平台全量/电商生成文字海报 ZImage_2019941449403473922.json, 平台全量/电商生成真实模特_1954801511316504577.json, 数字人/数字人/电商模特IP Lora_1985545576563548161.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_unet_vae_3

> 由 `engine/knowledge_consolidation` 从 15 个 workflow 归纳得出（平台全量/AI古风人像·Qwen写实·一句话出图工作流_2099719627638140930.json、平台全量/AI数字人工作流云端口播V1_2118227072048001026.json、平台全量/AI电商主图·Qwen写实·一句话出图工作流_2099719419659378690.json、平台全量/Qwen-Image Lightning8步加速lora 8steps-V1.0_1954344869051428866.json、平台全量/Qwen2512版CG插画创作_2054037288224600066.json…）

- **类型**：Unknown Workflow
- **样本数**：15
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 15 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `KSampler` —— 14/15 个有
- `LoraLoaderModelOnly` —— 11/15 个有
- `ModelSamplingAuraFlow` —— 11/15 个有
- `ConditioningZeroOut` —— 4/15 个有
- `JjkText` —— 4/15 个有
- `CR Prompt Text` —— 2/15 个有
- `TextGenerate` —— 2/15 个有
- `KSamplerAdvanced` —— 1/15 个有
- `PathchSageAttentionKJ` —— 1/15 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8.5 | 4 - 20 | 14 | 52% |
| Prompt 约束强度(CFG) | 1.52 | 1 - 8 | 15 | 19% |
| 采样算法 | euler | - | 15 | 80% |
| 调度器 | simple | - | 15 | 47% |
| 重绘幅度 | 1 | 1 - 1 | 14 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 8/15 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8.5，观测区间 4 - 20，14 个样本
- Prompt 约束强度(CFG) 中位数 1.52，观测区间 1 - 8，15 个样本，取值分散，一致性仅 19%
- 采样算法 最常用 euler，15 个样本，一致性 80%
- 调度器 最常用 simple，15 个样本，一致性 47%
- 重绘幅度 中位数 1，观测区间 1 - 1，14 个样本，取值集中（一致性 100%）
- 高发问题（8/15 个样本）：Steps较低可能导致细节不足
