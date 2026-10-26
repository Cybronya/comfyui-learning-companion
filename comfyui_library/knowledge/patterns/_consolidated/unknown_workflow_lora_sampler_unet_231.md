---
name: unknown_workflow_lora_sampler_unet_231
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.819667
common_nodes: [Anything Everywhere3, CLIPLoader, EmptyLatentImage, Fast Groups Muter (rgthree), ImageScaleToTotalPixels, KSampler, LoadImage, LoraLoaderModelOnly, ProcessString, SaveImage, ShellAgentPluginInputText, Text Multiline, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAELoader, easy promptLine, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/千问人物_场景裂变+高清放大_1992069593663426561.json, 图片生成/文生图/千问人物_场景裂变_1988501930139934721.json, 数字人/数字人/千问姿势溶图_1987033447095054337.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_231

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/千问人物_场景裂变+高清放大_1992069593663426561.json、图片生成/文生图/千问人物_场景裂变_1988501930139934721.json、数字人/数字人/千问姿势溶图_1987033447095054337.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere3`
- `CLIPLoader`
- `EmptyLatentImage`
- `Fast Groups Muter (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ProcessString`
- `SaveImage`
- `ShellAgentPluginInputText`
- `Text Multiline`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy promptLine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 2/3 个有
- `SetNode` —— 2/3 个有
- `text_mul_Join` —— 2/3 个有
- `CR Prompt List` —— 1/3 个有
- `SeedVR2LoadDiTModel` —— 1/3 个有
- `SeedVR2LoadVAEModel` —— 1/3 个有
- `SeedVR2VideoUpscaler` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1920 | 1920 - 1920 | 3 | 100% |
| 高度 | 1080 | 1080 - 1080 | 3 | 100% |
| 采样步数 | 4 | 4 - 4 | 3 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 3 | 100% |
| 采样算法 | sa_solver | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 1920，观测区间 1920 - 1920，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1080，观测区间 1080 - 1080，3 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 sa_solver，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（10/3 个样本）：Steps较低可能导致细节不足
